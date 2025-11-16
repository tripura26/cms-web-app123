import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'your-storage-key'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
