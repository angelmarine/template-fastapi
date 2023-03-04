import os


class DefaultConfig(object):
    """Config object which load config from system environment variables
    """
    # Azure Storage
    STORAGE_CONNECTION_STRING = os.environ["APPSETTING_STORAGE_CONNECTION_STRING"]

    # DB
    DB_SERVER = os.environ["APPSETTING_DB_SERVER"]
    DB_DATABASE = os.environ["APPSETTING_DB_DATABASE"]
    DB_USERNAME = os.environ["APPSETTING_DB_USERNAME"]
    DB_PW = os.environ["APPSETTING_DB_PW"]

    # ElasticSearch
    ES_SERVER = os.environ["APPSETTING_ES_SERVER"]
    ES_API_KEY = os.environ["APPSETTING_ES_API_KEY"]

    @property
    def DB_CONNECTION_URI(self):
        return 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.DB_SERVER \
            + ';DATABASE=' + self.DB_DATABASE \
            + ';UID=' + self.DB_USERNAME \
            + ';PWD=' + self.DB_PW \
            + ';readonly=True'

