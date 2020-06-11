from app import manager
from main import *

#его запускаем из консоли =>
#   1) python manage.py db init - создает папку migrations и фиксирует первоначальное состояние
#   2) вносим измпенения в приложении (создаем класс Tag)
#   3) делаем файл миграции (в папке versions):  python manage.py db migrate
#   4) чтобы записать в базу данных миграцию: python manage.py db upgrade (появилась таблица Tag в БД)
if __name__ == '__main__':
    manager.run()