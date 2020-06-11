from flask import Blueprint
from flask import render_template
from models import Post
# 1 - название blueprint'a
# 3 - все шаблоны хранятся в папке templates -> posts (пусть не смущает posts\templates\posts это от дублирования имен как и в Django)
# для того чтобы зарегать blueprint надо импортировать posts в app.py
posts = Blueprint('posts', __name__, template_folder='templates')

# вроде бы обращаемся к корню но мы зарегали blueprint по url_prefix='/blog' и получается url = /blog/
@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

#<имя параметра>
@posts.route('/<slug>')
# здесь тоже что и в <>, т.е slug
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=post)
