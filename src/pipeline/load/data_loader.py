from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from models.models_historico_taxas_juros import HistoricoTaxasJuros
from .interface_data_loader import InterfaceDataLoader


class DataLoader(InterfaceDataLoader):
    def __init__(self, db_engine):
        self.db_engine = db_engine

    def load_data(self, df):
        session = self.db_engine.get_session()
        if session:
            try:
                for _, row in df.iterrows():
                    num_reuniao = row["num_reuniao"]
                    existing_reuniao = (
                        session.query(HistoricoTaxasJuros)
                        .filter_by(num_reuniao=num_reuniao)
                        .first()
                    )

                    if existing_reuniao:
                        changes = {
                            key: value
                            for key, value in row.items()
                            if getattr(existing_reuniao, key) != value
                        }
                        if changes:
                            session.execute(
                                update(HistoricoTaxasJuros)
                                .where(HistoricoTaxasJuros.num_reuniao == num_reuniao)
                                .values(**changes)
                            )
                    else:
                        new_reuniao = HistoricoTaxasJuros(**row)
                        session.add(new_reuniao)

                session.commit()

            except Exception as e:
                print(f"Erro na persistência dos dados: {e}")

            finally:
                if session:
                    session.close()
