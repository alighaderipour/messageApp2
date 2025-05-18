import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:Aa%40123456@DESKTOP-ICP5P36/messageApp?driver=ODBC+Driver+17+for+SQL+Server"


    SQLALCHEMY_TRACK_MODIFICATIONS = False
