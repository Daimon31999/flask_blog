#точка входа
from app import app
#чтобы Flask знал что есть вьюха
import view
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')
app.run()