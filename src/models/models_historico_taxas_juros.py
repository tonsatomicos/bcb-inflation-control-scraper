from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DECIMAL

Base = declarative_base()

class HistoricoTaxasJuros(Base):
    __tablename__ = 'historico_taxas_juros'

    num_reuniao = Column(Integer, primary_key=True, autoincrement=False)
    data_reuniao = Column(String(15), nullable=False)
    vies_reuniao = Column(String(50),nullable=True)
    meta_selic = Column(DECIMAL(10, 1), nullable=True)
    tban = Column(DECIMAL(10, 1), nullable=True)
    taxa_selic_porcentagem = Column(DECIMAL(10, 1), nullable=True)
    taxa_selic_a_a = Column(DECIMAL(10, 1), nullable=True)
    inicio_vigencia = Column(String(15))
    fim_vigencia = Column(String(15), nullable=True)
