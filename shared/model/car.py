from shared.system.base.model import BaseModel, HBKeyProperty
from google.cloud import ndb



class Car(BaseModel):
    garage = HBKeyProperty()
    brand = ndb.StringProperty()

    license_plate = ndb.StringProperty()

    @classmethod
    def list(cls, garage=None):
        cars = list()
        with cls.ndb_context():
            q = cls.query()
            if garage:
                q = q.filter(cls.garage==garage.key)
            cars = q.fetch()
        return cars
