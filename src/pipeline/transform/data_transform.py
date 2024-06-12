import numpy as np
import pandas as pd
from .interface_data_transform import InterfaceDataTransform


class DataTransform(InterfaceDataTransform):
    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df.columns = df.columns.get_level_values(1)
            rename_columns = [
                "num_reuniao",
                "data_reuniao",
                "vies_reuniao",
                "periodo",
                "meta_selic",
                "tban",
                "taxa_selic_porcentagem",
                "taxa_selic_a_a",
            ]
            df.columns = rename_columns

            df["num_reuniao"] = df["num_reuniao"].str.replace(r"\D+", "", regex=True)
            df[["inicio_vigencia", "fim_vigencia"]] = df["periodo"].str.extract(
                r"([\d/]+)\s*-\s*(\s*[\d/]*)"
            )
            df.drop("periodo", axis=1, inplace=True)

            df["num_reuniao"] = df["num_reuniao"].astype(int)

            df["meta_selic"] = df["meta_selic"].astype(float) / 100
            df["tban"] = df["tban"].astype(float) / 100
            df["taxa_selic_porcentagem"] = df["taxa_selic_porcentagem"].astype(float) / 100
            df["taxa_selic_a_a"] = df["taxa_selic_a_a"].astype(float) / 100

            df["data_reuniao"] = (
                pd.to_datetime(df["data_reuniao"], format="%d/%m/%Y")
                .dt.strftime("%d%m%Y")
                .fillna("01011900")
            )
            df["inicio_vigencia"] = (
                pd.to_datetime(df["inicio_vigencia"], format="%d/%m/%Y")
                .dt.strftime("%d%m%Y")
                .fillna("01011900")
            )
            df["fim_vigencia"] = (
                pd.to_datetime(df["fim_vigencia"], format="%d/%m/%Y")
                .dt.strftime("%d%m%Y")
                .fillna("01011900")
            )

            df.replace(np.nan, None, inplace=True)

            return df
        
        except Exception as e:
                print(f"Erro na transformação dos dados: {e}")

