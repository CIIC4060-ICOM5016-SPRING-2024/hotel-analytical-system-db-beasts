# ETL (Extract, Transform, Load) Tool

> [!TIP]
> The etl branch has all the different versions of the transform_data.<br >
> In the one located in the main there is only the one that creates the tables in an empty database.<br >
> The transform_data_pruebas is the last one carried out so that it will work with empty databases and also with pre-existing tables.<br >

## Table of Contents

- [Project Description](#project-description)
- [Usage](#usage)
- [Functionality](#functionality)
- [Known Issues](#known-issues)

> [!IMPORTANT]
> ## Project Description

The ETL tool is designed to extract data from various sources, transform it and load it into a relational database.<br >

This tool is partially functional and serves as a basis for future development phases. Successfully transform files to CSV format and create the tables in the database.

Please note that this ETL tool was not used in a Heroku environment. However, it can be adapted and used in other configurations as needed.
> [!WARNING]
> Additionally, there is a version of this program called "transform_data_tests" that has been partially adapted to fill pre-existing empty tables.<br  >
> Seven of the nine tables are working correctly.

> [!WARNING]
> It's important that every file that's to be converted, it must be in the ETL directory. 

> [!IMPORTANT]
> ## Usage
1. Place the files to be converted.<br > 
2. Provide the database information.<br > 
3. Then using transform_data.py the tables will be created using multiple files as input and using the file names.

> [!IMPORTANT]
> ## Functionality
The transform_data.py will create the tables using various read and write functions as well as for loops to parse the data and convert it.<br >
A database is also created with the name of the files and the data provided in it.<br >
These tests were created in a local container.

> [!IMPORTANT]
> ## Known Issues

> [!CAUTION]
>The transform_data.py does not work with existing tables in the database.<br >

> [!CAUTION]
>In transform_data_tests.py, when the tables have not been created, one of the 9 tables remains empty.<br >

> [!CAUTION]
>In transform_data_pruebas.py, if the tables were prefab and filled with the already named attributes along with their domains, then two remained empty while seven were filled correctly.
