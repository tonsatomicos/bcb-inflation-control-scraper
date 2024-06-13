from sqlalchemy import create_engine

db_url = "mssql+pyodbc://sa:Teste!1234@localhost:5434/BACEN?driver=SQL Server"

engine = create_engine(db_url, echo=True)

try:
    connection = engine.connect()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro na conexão: {e}")
finally:
    connection.close()