from config.webdriver import WebDriverConfig
from config.db_engine import DBEngine
from pipeline.etl.etl_processor import ETLProcessor
from pipeline.extract.data_extractor import DataExtractor
from pipeline.transform.data_transform import DataTransform
from pipeline.load.data_loader import DataLoader


webdriver_config = WebDriverConfig()
db_engine = DBEngine("postgresql", "localhost:5437", "admin", "admin", "bcb")

obj_data_extractor = DataExtractor(webdriver_config=webdriver_config)
obj_data_transform = DataTransform()
obj_data_loader = DataLoader(db_engine=db_engine)

url_extract = "https://www.bcb.gov.br/controleinflacao/historicotaxasjuros"
table_xpath = "/html/body/app-root/app-root/div/div/main/dynamic-comp/div/div/bcb-histtaxajuros/div[1]/table"

etl_batch = ETLProcessor(
    obj_data_extractor=obj_data_extractor,
    obj_data_transform=obj_data_transform,
    obj_data_loader=obj_data_loader,
)
etl_batch.extract_data(
    url_extract=url_extract, table_xpath=table_xpath
)
etl_batch.transform_data()
etl_batch.load_data()

etl_batch.get_status()
