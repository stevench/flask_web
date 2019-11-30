# -*- encoding: utf-8 -*-
from flask_restful import Api, Resource

api = Api()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/helloworld')
