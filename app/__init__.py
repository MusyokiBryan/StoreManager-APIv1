from flask import Flask
from flask_restplus import Api
from Instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    api = Api(app=app, description="Store Manager is a web application that helps store owners manage sales"
                                   " and product inventory records. This application"
                                   " is meant for use in a single store.",
              title="Store Manager",
              version='1.0',
              doc='/api/v1/documentation'
              )

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    from .api.V1.views import product_api, sales_api, user_api, admin_api
    api.add_namespace(product_api, path="/api/v1")
    api.add_namespace(sales_api, path="/api/v1")
    api.add_namespace(user_api, path="/api/v1")
    api.add_namespace(admin_api,path="/api/v1")

    return app
