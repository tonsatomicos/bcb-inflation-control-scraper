IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'bcb')
BEGIN
    CREATE DATABASE bcb;
END
GO

USE bcb;
GO

CREATE TABLE historico_taxas_juros (
    num_reuniao INT PRIMARY KEY,
    data_reuniao VARCHAR(8) NULL,
    vies_reuniao VARCHAR(50) NULL,
    meta_selic DECIMAL(10, 2) NULL,
    tban DECIMAL(10, 2) NULL,
    taxa_selic_porcentagem DECIMAL(10, 2) NULL,
    taxa_selic_a_a DECIMAL(10, 2) NULL,
    inicio_vigencia VARCHAR(8) NULL,
    fim_vigencia VARCHAR(8) NULL
);