import logging

logging.basicConfig(level=logging.DEBUG)

class dbConnector:
    @staticmethod
    def start():
        logging.info('> [database] Starting...')
        logging.info('> [database] Connecting to Postgres...')
        logging.info('> [database] Running migrations...')
        logging.info('> [database] Starting done!')

    @staticmethod
    def stop():
        logging.info('> [database] Stopping...')
        logging.info('> [database] Closing Postgres connection...')
        logging.info('> [database] Stopping done!')