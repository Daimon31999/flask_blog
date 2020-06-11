###################
# Добавить ТЭГ в БД
#   from app import db
#   from models import Tag
#   tag = Tag(name='python')
#   db.session.add(tag) //добавить в сессию
#   db.session.commit() //запись в БД
#
#
#
#
#
#
#







from app import db
from datetime import datetime
# regular expression lib
import re


# класс отвечает за хранение постов
def slugify(s):
    # \w+ - все буквы и цифры и _
    # ^ - не
    pattern = r'[^\w+]'
    # sub - substitution, замена(что заменять, на что заменять, где ищем)
    return re.sub(pattern, '-', s).lower()


class Post(db.Model):
    # id это колонка(хранит int, первичный ключ)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    # slug - это ЧПУ - человеко-понятный url, url - уникален
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    # *args - позиционные аргум.(список) **kwargs - именованные аргум.(словарь key-word)
    def __init__(self, *args, **kwargs):
        # вызвать конструктор предка(SQLAlchemy.Model)
        # супер класс класса Post, self - ссылка на экземпляр конкретного класса
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    # representation(представление при выводе на экран(аналог toString))
    def __repr__(self):
        return '<Post id: {0}, title: {1}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}>'.format(self.id, self.name)
