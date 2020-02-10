import logging

from shared.system.base_handler import BaseHandler


class WorkerHandler(BaseHandler):
    """A basic handler used by the Worker. All requests are route to here."""

    def get(self, topic):
        """
        GET which get called by the gae RequestHandler which we no longer use.

        Args:
            topic: the topic defined in the url.
        Returns:
            None

        """
        logging.info('Called worker get')

    def post(self, topic):
        """
        POST which get called by the gae RequestHandler which we no longer use.

        Args:
            topic: the topic defined in the url
        Returns:
            None

        """
        logging.info('Called worker post')
