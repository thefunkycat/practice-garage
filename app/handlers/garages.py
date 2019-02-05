from app.handlers import BasicHandler
from app.model.garage import Garage
import json
import logging

class Garages(BasicHandler):
    """ Handler for Garage

        Supports up to 3 parameters
        key = always a garage id
        topic = what you want to do
        ident = Can be id of another class as child from Garage
    """

    def get(self, key="", topic="", ident=""):
        if not key:
            garages = Garage.query()
            garages = json.dumps([p.to_dict() for p in Garage.query().fetch()])
            self.render_json(garages)
        else:
            garage = Garage.get(key)
            logging.warning("Got garage " + garage.name)
            pass

    def post(self, key="", topic="", ident=""):
        if not key:
            Garage.add(self.params.params)
        else:
            # edit garage
            pass
