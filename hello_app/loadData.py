from datetime import datetime
from flask import Flask, render_template
#from . import app
import pandas as pd
from os import environ
from sqlalchemy import create_engine, text
import re

db_uri = environ.get('BDD_URI')
engine = create_engine(db_uri, echo=True)
print('engine :', engine)

#URL='https://data.seattle.gov/api/views/2bpz-gwpy/rows.csv?accessType=DOWNLOAD' # 2016
#URL='https://data.seattle.gov/api/views/qxjw-iwsh/rows.csv?accessType=DOWNLOAD' # 2017

data=[
    ['2015', 'h7rm-fz6m'],
    ['2016', '2bpz-gwpy'],
    ['2017', 'qxjw-iwsh'],
    ['2018', 'ypch-zswb'],
    ['2019', '3th6-ticf'],
    ['2020', 'auez-gz8p'],
    ['2021', 'bfsh-nrm6'],
]

for year,code in data:
    url=f"https://data.seattle.gov/api/views/{code}/rows.csv?accessType=DOWNLOAD"
    print(f"=========================================================\n\n{year} : {url}")
    df = pd.read_csv(url)

    with engine.begin() as conn:
        print(conn)
        conn.execute(text(f"""DELETE FROM "SEATTLE" WHERE "DataYear"='{year}'  """))

    cols = [re.sub(r"[()]", "_", c)
            .replace(' ', '')
            .replace('TotalGhgEmissions', 'TotalGHGEmissions')
            .replace('BuildingName', 'PropertyName')
            for c in list(df.columns)]
    df.columns = cols
    print(cols)

    if year=='2015':
        df.drop(['Location', 'OtherFuelUse_kBtu_', 'GHGEmissions_MetricTonsCO2e_', 'GHGEmissions_MetricTonsCO2e_', 'GHGEmissionsIntensity_kgCO2e/ft2_', 'Comment'], axis=1, inplace=True)
    if year=='2018':
        df.drop(['EPABuildingSubTypeName', 'ComplianceIssue'], axis=1, inplace=True)
    if year=='2019':
        df.drop(['ComplianceIssue', 'EPAPropertyType'], axis=1, inplace=True)
    if year=='2020':
        df.drop(['ComplianceIssue', 'EPAPropertyType'], axis=1, inplace=True)
    if year=='2021':
        df.drop(['ComplianceIssue', 'EPAPropertyType'], axis=1, inplace=True)

    df.drop_duplicates(subset=['OSEBuildingID'], inplace=True)

    print(df.head())
    print(df.shape)
    df.to_sql('SEATTLE', engine, if_exists='append', index=False)