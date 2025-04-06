# 🛳️ ANTAQ Data Pipeline – Coleta, Tratamento e Visualização com Power BI

Este projeto tem como objetivo transformar dados públicos do setor aquaviário brasileiro em insights acionáveis, utilizando um pipeline de dados estruturado. Os dados foram extraídos da [Agência Nacional de Transportes Aquaviários (ANTAQ)](https://www.gov.br/antaq/pt-br) e organizados segundo a arquitetura em camadas: 
### **Bronze → Silver → Gold**.

### Dashboard:
[Dashboard] (https://app.powerbi.com/view?r=eyJrIjoiZTA2NDJjMmMtOTUyMy00ZTJlLWIwZGMtYWZkYTE2NDNiMjlmIiwidCI6IjY5ZjgzNmIxLTU5NzktNDMxMi04ODYyLTEyZjliZmFkOTJjYyJ9)

---

## 📂 Estrutura do Projeto
```
📦 Projeto
├── 📁🥉 Bronze_Layer
   ├── *Gerados por `main.ipynb`:*
   ├── Atracacao_2021.zip
   ├── Atracacao_2022.zip
   ├── Atracacao_2023.zip
   ├── Carga_2021.zip
   ├── Carga_2022.zip
   ├── Carga_2023.zip
   ├── CargaConteineirizada_2021.zip
   ├── CargaConteineirizada_2022.zip
   └── CargaConteineirizada_2023.zip
├── 📁🥈 Silver_Layer
   ├── *Gerados por `main.ipynb`:*
   ├── 📁 Atracacao_2021
   ├── 📁 Atracacao_2022
   ├── 📁 Atracacao_2023
   ├── 📁 Carga_2021
   ├── 📁 Carga_2022
   ├── 📁 Carga_2023
   ├── 📁 CargaConteineirizada_2021
   ├── 📁 CargaConteineirizada_2022
   └── 📁 CargaConteineirizada_2023
├── 📁🥇 Gold_Layer
   ├── 📁 Modelos
      └── Antaq_dash.pbix
├── 📁 scripts
   ├── .env
   ├── main.ipynb
   ├── antaq_mysql_database.py
   └── import_data.py
├── requirements.txt
└── 📄 README.md
```

---
## 🔄 Fluxo de trabalho

#### 📥 Passo 01 - download de pré-requisitos 
Inicialmente deve-se baixar todas as bibliotecas necessárias utilizando o comando:
```
pip install requirements.txt
```

#### 🔧 Passo 02 - ETL
- Toda a etapa de testes, extração, tratamento e disponibilização é realizada executando o notebook: "./scripts/main.ipynb"

#### 🏦 Passo 03 - banco de dados MySQL
- OBS. Antes de tudo, será necessário configurar as informações presentes em: "./scripts/.env"
- O banco de dados, juntamente com as tabelas pode ser criado usando:
```
python ./scripts/antaq_mysql_database.py
```

- A importação dos dados pode ser realizada usando:
```
python ./scripts/import_data.py
```

#### 📊 Passo 04 - Conexão com Power BI

- A análise interativa pode ser visualizada em: "./Gold_Layer/antaq_dash.pbix"

#### 🚀 Passo 05 - Deploy e Compartilhamento 
- Foi realizado o upload do projeto neste GitHub.


#### Créditos:
- Esse projeto foi desenvolvido por Cleber Furtado Aksenen


