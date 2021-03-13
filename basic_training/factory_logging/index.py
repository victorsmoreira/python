from core import coreCreator
import logging

logging.basicConfig(level=logging.DEBUG)

core = coreCreator()

try:
    core.start()
    core.stop()
except Exception as error:
    # logging.error('[index] Uncaught error!', exc_info=True)
    logging.exception('[index] Uncaught error!')