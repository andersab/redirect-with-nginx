import argparse
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

APP_NUMBER = '0'


class TestController(Resource):

    def get(self):
        return {"response": APP_NUMBER}

    def post(self):
        return {"response": APP_NUMBER}


def main():
    parser = argparse.ArgumentParser('test-app')
    parser.add_argument('port_number')
    parser.add_argument('app_number')
    parsed_args = parser.parse_args()
    global APP_NUMBER
    APP_NUMBER = parsed_args.app_number
    print('******** APP NUMBER STARTING: %s ********' % APP_NUMBER)
    app.run(debug=True, port=parsed_args.port_number)


api.add_resource(TestController, '/')


if __name__ == '__main__':
    main()