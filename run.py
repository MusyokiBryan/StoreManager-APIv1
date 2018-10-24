import os
from app import create_app
from werkzeug.contrib.fixers import ProxyFix


config_name = os.getenv('APP_SETTINGS')
app = create_app(config=config_name)
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run(debug=True)
