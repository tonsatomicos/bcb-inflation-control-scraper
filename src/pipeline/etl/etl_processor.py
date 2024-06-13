from utils.log_decoretor import log_decorator
from pipeline.etl.interface_etl_processor import InterfaceETLProcessor
from pipeline.extract.interface_data_extractor import InterfaceDataExtractor
from pipeline.transform.interface_data_transform import InterfaceDataTransform
from pipeline.load.interface_data_loader import InterfaceDataLoader


class ETLProcessor(InterfaceETLProcessor):
    def __init__(
        self,
        obj_data_extractor: InterfaceDataExtractor,
        obj_data_transform: InterfaceDataTransform,
        obj_data_loader: InterfaceDataLoader,
    ):     
        self.data_extracted = None
        self.obj_data_extractor = obj_data_extractor
        self.obj_data_transform = obj_data_transform
        self.obj_data_loader = obj_data_loader

    @log_decorator
    def extract_data(self, url_extract: str, table_xpath: str):
        self.data_extracted = self.obj_data_extractor.extract_data(
            url_extract, table_xpath
        )
        return self.data_extracted

    @log_decorator
    def transform_data(self):
        self.data_extracted = self.obj_data_transform.transform_data(
            self.data_extracted
        )
        return self.data_extracted
    
    @log_decorator
    def load_data(self):
        self.obj_data_loader.load_data(self.data_extracted)

    def get_status(self):
        if self.status == True:
            print("Dados extraídos com sucesso.")
        else:
            print(f"Falha ao extrair dados: {self.status_message}")

