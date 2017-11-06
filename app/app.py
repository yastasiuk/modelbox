from flask import Flask
from roads.roads import Road


class Application:

    def __init__(self):
        self.app = Flask(__name__)
        self.add_routing()

    def add_routing(self):
        self.add_endpoint(endpoint='/get_route/<longitude_from>/<latitude_from>/<longitude_to>/<latitude_to>',
                          endpoint_name='main', handler=Road.get_duration_and_distance)

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler)


if __name__ == "__main__":
    app = Application()
    app.run()