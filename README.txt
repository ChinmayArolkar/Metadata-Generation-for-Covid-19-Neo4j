---Group 1---

# Description

This project is to create and design database to load metadata.

Belows tables are designed in the SQL Server Management Studio
1. Domain
2. DomainRelationship
3. BusinessTerms
4. DomainTermsRelationship
5. TechnicalTerms
6. TechBusBridge

# Steps to create metadata

Step 1:
Create Database Metadata 

Step 2:
Create all the table in the Metadata database by running the Metadata sql script

Step 3:
Create csv of the same structure to store the data to be loaded in the SQL Server metadata database


# Steps to Extract Technical Metadata in Neo4j

Step 1: 
Install APOC plugins in the Neo4j database

Step 2:
Run the technical metadata extraction script

Step 3:
Export the technical metadata in csv format

# Authors
Foram Javia
Chinmay Arolkar
Aishwarya Kumar

---Group 2----

Preparation for extraction:

3.x python

Latest Neo4j(run the neo4j database with APOC plugin installed before executing the script )

Neo4j Python Driver 4.2

Pandas

Run:
python neo4j_extraction.py

You will be asked to give three variables of accessing the neo4j database, example:
[@ZachL:Desktop]$ python3 neo4j_extraction.py 
Please give the user name:python
Password:123456
Database name:neo4j
The metadata are generated in 'metadata.csv'


Requirements for running import_metadata.py:

For macOS: 
install client tools for remote MS sql server:
/usr/bin/ruby -e “$(curl - fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
brew tap microsoft/mssql-release
brew update
brew install msodbcsql mssql-tools

Put Metadata_Group1.sql Metadata_Group1.xlsx and import_metadata.py into one directory
Run:
python import_metadata.py

For windows:
Install SQL Server Management Studio and login with address(neo4j-metadata.cjwdtb9o2fdi.us-east-1.rds.amazonaws.com,1433), username(admin) and pwd(UQ19-XPN) to access the database in the AWS.

If you prefer to have it locally, just use SQL Server Management Studio manually import all csv files in the metadata.zip

# Authors
Bhaghirathi Kundu
Ashwin Lakshman
Zhe Liu

---Group 3 ---

An app which displays the metadata

# Description
This project is about viewing metadata on frontend. There are six buttons on the page. Each button when clicked displays the information about it.
Below are the button names
1. Domain: Lists all the domains.
2. BusinessTerms: Lists all the business terms.
3. DomainRelationship: Lists parents and children.
4. DomainTermsRelationship: Lists all the technical terms related to a child.
5. Technical Terms: Lists all the technical terms.
6. TechBusBridge: Lists the bridge table with business and technical terms relationship.

# Installation
You can run this in two ways:
Web: https://nameless-spire-63573.herokuapp.com/
Locally: You can download the project from GITHUB: https://github.com/yvgr00/Metadata

Install:
1. An environment to run javascript such as Atom, Visual Studio Code.
2. Install Node.js.
3. Install nodemon to run your server.
4. Install npm which manages packages in the project
5. Install Git
6. Run command 'npm ci' to clean install all the packages locally for the project to run.

# Authors
Venu Gopal Reddy Yerragunta
Rushali Udhani