import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "host": os.getenv("MYSQL_HOST"),
    "database": os.getenv("MYSQL_DATABASE"),
}

def connect_to_mysql():
    try:
        return mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def create_database(cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']};")
    print(f'Banco de dados "{DB_CONFIG["database"]}" criado/verificado com sucesso!')

def create_tables(cursor):
    """Cria as tabelas no banco de dados."""
    tabelas = {
        "atracacao": """
            CREATE TABLE IF NOT EXISTS atracacao (
                idatracacao INT PRIMARY KEY,
                cdtup TEXT,
                idberco TEXT,
                berco TEXT,
                porto_atracacao TEXT,
                coordenadas TEXT,
                apelido_instalacao_portuaria TEXT,
                complexo_portuario TEXT,
                tipo_da_autoridade_portuaria TEXT,
                data_atracacao DATETIME,
                data_chegada DATETIME,
                data_desatracacao DATETIME,
                data_inicio_operacao DATETIME,
                data_termino_operacao DATETIME,
                ano INT,
                mes TEXT,
                tipo_de_operacao TEXT,
                tipo_de_navegacao_da_atracacao TEXT,
                nacionalidade_do_armador FLOAT,
                flagmcoperacaoatracacao INT,
                terminal TEXT,
                municipio TEXT,
                uf TEXT,
                sguf VARCHAR(2),
                regiao_geografica TEXT,
                regiao_hidrografica TEXT,
                instalacao_portuaria_em_rio TEXT,
                no_da_capitania TEXT,
                no_do_imo TEXT,
                longitude FLOAT,
                latitude FLOAT
            );
        """,
        "carga": """
            CREATE TABLE IF NOT EXISTS carga (
                idcarga INT PRIMARY KEY,
                idatracacao INT,
                origem TEXT,
                destino TEXT,
                cdmercadoria TEXT,
                tipo_operacao_da_carga TEXT,
                carga_geral_acondicionamento TEXT,
                conteinerestado TEXT,
                tipo_navegacao TEXT,
                flagautorizacao TEXT,
                flagcabotagem FLOAT,
                flagcabotagemmovimentacao FLOAT,
                flagconteinertamanho TEXT,
                flaglongocurso FLOAT,
                flagmcoperacaocarga INT,
                flagoffshore FLOAT,
                flagtransporteviainterioir INT,
                percurso_transporte_em_vias_interiores TEXT,
                percurso_transporte_interiores TEXT,
                stnaturezacarga TEXT,
                stsh2 TEXT,
                stsh4 TEXT,
                natureza_da_carga TEXT,
                sentido TEXT,
                teu FLOAT,
                qtcarga FLOAT,
                vlpesocargabruta FLOAT,
                FOREIGN KEY (idatracacao) REFERENCES atracacao(idatracacao)
            );
        """,
        "carga_conteineirizada": """
            CREATE TABLE IF NOT EXISTS carga_conteinerizada (
                idcarga INT PRIMARY KEY,
                cdmercadoriaconteinerizada VARCHAR(10),
                vlpesocargaconteinerizada FLOAT,
                FOREIGN KEY (idcarga) REFERENCES carga(idcarga)
            );
        """
    }
    
    for nome, sql in tabelas.items():
        cursor.execute(sql)
        print(f"Tabela '{nome}' criada/verificada com sucesso!")

def main():
    connection = connect_to_mysql()
    if connection:
        try:
            cursor = connection.cursor()
            create_database(cursor)
            connection.database = DB_CONFIG["database"]
            create_tables(cursor)
        except Error as e:
            print(f"Erro ao criar banco de dados ou tabelas: {e}")
        finally:
            cursor.close()
            connection.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    main()
