from database import dbConnector
from webserver import webServerCreator
import logging

logging.basicConfig(level=logging.DEBUG)

class coreCreator:
    def __init__(self):
        self.database = dbConnector()
        self.webserver = webServerCreator()

    def start(self):
        logging.info('> [core] Starting...')
        self.database.start()
        self.webserver.start()
        logging.info('> [core] Starting done! System running!')

    def stop(self):
        logging.info('> [core] Stopping...')
        self.webserver.stop()
        self.database.stop()
        logging.info('> [core] Stopping done!')
