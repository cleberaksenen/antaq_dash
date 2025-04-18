# 🛳️ ANTAQ Data Pipeline – Collection, Processing, and Visualization with Power BI

This project aims to transform public data from the Brazilian waterway transport sector into actionable insights using a structured data pipeline.  
The data was extracted from the [National Agency for Waterway Transportation (ANTAQ)](https://www.gov.br/antaq/pt-br) and organized according to a layered architecture:  
### **Bronze → Silver → Gold**

![image](https://github.com/user-attachments/assets/f800cea1-8af6-4848-bea6-b9c96ace8692)

### Dashboard:
[Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZTA2NDJjMmMtOTUyMy00ZTJlLWIwZGMtYWZkYTE2NDNiMjlmIiwidCI6IjY5ZjgzNmIxLTU5NzktNDMxMi04ODYyLTEyZjliZmFkOTJjYyJ9)

---

## 📂 Project Structure
```
📦 Project
├── 📁🥉 Bronze_Layer
   ├── *Generated by `main.ipynb`:*
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
   ├── *Generated by `main.ipynb`:*
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
   ├── 📁 Models
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
## 🔄 Workflow

#### 📥 Step 01 - Download prerequisites
Start by installing all required libraries using the command:
```
pip install requirements.txt
```

#### 🔧 Step 02 - ETL
- All steps for testing, extraction, transformation, and loading are handled in the notebook:
```
./scripts/main.ipynb
```

#### 🏦 Step 03 - banco de dados MySQL
- ⚠️ First, make sure to configure the connection credentials in:
```
./scripts/.env
```
- Create the database and tables by running:
```
python ./scripts/antaq_mysql_database.py
```
- Then import the processed data using:
```
python ./scripts/import_data.py
```

#### Step 04 - Connect to Power BI
- The interactive analysis can be opened with Power BI from the file:
```
./Gold_Layer/Models/antaq_dash.pbix
```

#### 🚀 Step 05 - Deployment and Sharing
- The project was uploaded and shared on this GitHub repository.


#### 👤 Credits
- This project was developed by Cleber Furtado Aksenen


