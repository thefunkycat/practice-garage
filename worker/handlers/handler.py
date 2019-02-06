import logging

from shared.system.base_handler import BaseHandler


class WorkerHandler(BaseHandler):

    def get(self, topic):
        logging.info('Called worker get')

    def post(self, topic):
        logging.info('Called worker post')
