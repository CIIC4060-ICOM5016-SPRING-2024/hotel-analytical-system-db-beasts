ETL (Extract, Transform, Load) Tool

## Table of Contents

- [Project Description](#project-description)
- [Usage](#usage)
- [Functionality](#functionality)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

> [!IMPORTANT]
> ## Project Description

The ETL tool is designed to extract data from various sources, transform it, and load it into a relational database. This tool partially functions and serves as a base for future development phases. It successfully transforms files into CSV format and creates nine tables in a local container.

Please note that this ETL tool was not used in a Heroku environment. However, it can be adapted and utilized in other setups as needed. 
> [!WARNING]
> Additionally, there is a version of this program called "_pruebas" that has been partially adapted to fill empty, pre-existing tables. Seven out of the nine tables are functioning correctly.

> [!WARNING]
> It's important that every file that's to be converted, it must be in the ETL directory. 

> [!IMPORTANT]
> ## Usage
Place the files to be converted. Transform the information from the database. Using transform_data.py the tables will be created by using multiple files as input.

> [!IMPORTANT]
> ## Functionality
transform_data.py will create the tables using several write and read functions as well as for loops to analyze the data and convert them. An empty database with the name of the files is created as well. The tables were created in a local container.

> [!IMPORTANT]
> ## Known Issues
transform_data.py doesnt work with existing tables in the database. When the tables haven't been created, one out of the 9 tables remain empty. If the tables were pre-made and filled with the extracted data, then two remained empty while 7 were properly filled.
