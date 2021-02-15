import xlrd
import pandas as pd
import os
import pathlib
def excel2csv(excel_file):
    workbook=xlrd.open_workbook(filename=excel_file)
    sheet_names=workbook.sheet_names()
    for worksheet_name in sheet_names:
        data_xls=pd.read_excel(excel_file,worksheet_name,index_col=None)
        data_xls.to_csv(path_or_buf=open(os.path.join(pathlib.Path().absolute(), worksheet_name+'.csv'), 'w'),index=None,encoding='utf-8',header=None)
        querystr=f'bcp {worksheet_name} in {worksheet_name}.csv -S neo4j-metadata.cjwdtb9o2fdi.us-east-1.rds.amazonaws.com,1433 -U admin -P UQ19-XPN -d Metadata -c -t \',\''
        os.system(querystr)
        print(querystr)

if __name__ == '__main__':
    common_str='sqlcmd -S neo4j-metadata.cjwdtb9o2fdi.us-east-1.rds.amazonaws.com,1433 -U admin -P UQ19-XPN'

    # drop database 'Metadata'
    os.system(f'{common_str} -Q \"EXECUTE msdb.dbo.rds_drop_database  N\'Metadata\';\"')
    # create database 'Metadata'
    os.system(f'{common_str} -Q \"Create Database Metadata;\"')
    # create schema in 'Metadata'
    os.system(f'{common_str} -d Metadata -i Metadata_Group1.sql')
    
    # convert excel sheets to csv files
    excel2csv(os.path.join(pathlib.Path().absolute(), 'Metadata.xlsx'))
