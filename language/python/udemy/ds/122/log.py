import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    logging.info('logger test')
    logger.info('from log info')
    logger.debug('from log debug')