import os

base_dir = os.path.abspath(os.path.dirname(__file__))
db_name = 'flask_hello.db'
db_path = os.path.join(base_dir, db_name)


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = ',mxczvk'
    SECRET_KEY = 'zlxkcvnzdfvp;d'
    # DATABASE = os.path.join(base_dir, db_name)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://webuser:web_password@localhost/webuser_db'

    DEBUG_TB_ENABLED = True
    DEBUG_TB_HOSTS = "*"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # DEBUG_TB_PANELS = []
    # DEBUG_TB_PROFILER_ENABLED = True
    # DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
