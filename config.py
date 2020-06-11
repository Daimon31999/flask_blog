#конфигурация Flask'a
class Configuration(object):
    DEBUG = True
    # Эта функция будет выпилена из Фласка, чтобы небыло warning message
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #mysql://username:password@server/db
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/test'