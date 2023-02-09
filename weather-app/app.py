from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

weathers = {
    '95035': {'temperature': 65, 'condition': 'Rainy'},
    '94539': {'temperature': 70, 'condition': 'Snow'},
    '94043': {'temperature': 40, 'condition': 'Sunny'}
}
class Weather(Resource):
    def get(self, zipcode):
        # Get weather information for the zipcode using a weather API
        if zipcode in weathers:
            return weathers[zipcode]
        else:
            return {'message': 'Zipcode not found'}, 404

api.add_resource(Weather, '/weather/<string:zipcode>')

if __name__ == '__main__':
    app.run(debug=True)