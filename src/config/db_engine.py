from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBEngine:
    def __init__(self, db_type, db_local, db_user, db_pass, db_name):
        self.db_type = db_type
        self.db_local = db_local
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.engine = self.create_engine()
        self.session_factory = sessionmaker(bind=self.engine)
        self.session = None

    def create_engine(self):
        if self.db_type == "postgresql":
            db_url = f"postgresql+psycopg2://{self.db_user}:{self.db_pass}@{self.db_local}/{self.db_name}"
        elif self.db_type == "sqlserver":
            db_url = f"mssql+pyodbc://{self.db_user}:{self.db_pass}@{self.db_local}/{self.db_name}?DRIVER={{ODBC Driver 17 for SQL Server}}"
        else:
            raise ValueError("Tipo de banco de dados não suportado")

        engine = create_engine(db_url)
        return engine

    def get_session(self):
        self.session = self.session_factory()
        return self.session
    
    def close_session(self):
        if self.session:
            self.session.close()

