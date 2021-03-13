import logging

logging.basicConfig(level=logging.DEBUG)

class webServerCreator:
    @staticmethod
    def start():
        logging.info('> [webserver] Starting...')
        logging.info('> [webserver] Waiting for port to be available...')
        logging.info('> [webserver] Starting done!')

    @staticmethod
    def stop():
        logging.info('> [webserver] Stopping...')
        logging.info('> [webserver] Gracefully waiting for all clients...')
        logging.info('> [webserver] Closing all ports...')
        logging.info('> [webserver] Stopping done!')