from google.appengine.ext import ndb
import logging


class MixinDefaults(object):

    def fill(self, props):
        """
        attempts to write props to the model.

        :param props: dict with props ( from json ) thats needs to be set
        :return:
        """
        unused = list()
        if props is None:
            return unused

        for attr, value in props.iteritems():
            try:
                if hasattr(self, attr):
                    setattr(self, attr, value)
                else:
                    unused.append({attr: value})
            except Exception, e:
                logging.exception(e)
                unused.append({attr: value})
        return unused


class BaseModel(ndb.Model, MixinDefaults):
    
    @property
    def id(self):
        """
        """
        if self.key:
            return self.key.integer_id()
        logging.error("Model %s instance not stored yet!" % self.__class__.__name__)
        return None
    
    @classmethod
    def get(cls, key, parent=None):
        """
        """
        return cls.get_by_id(int(key), parent)

    def update(self, props):
        """
        """
        unused = self.fill(props=props)
        if unused:
            logging.info('Not all props have been processed: %s' % unused)
        return self.save()
    
    def save(self):
        """
        """
        self.put()
        return self
