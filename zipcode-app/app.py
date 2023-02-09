from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

zipcodes = {
    'Milpitas': '95035',
    'Fremont': '94539',
    'Sunnyvale': '94043'
}

class Zipcode(Resource):
    def get(self, area):
        if area in zipcodes:
            return {area: zipcodes[area]}
        else:
            return {'error': 'Area not found'}, 404

api.add_resource(Zipcode, '/zipcode/<string:area>')

if __name__ == '__main__':
    app.run(debug=True)