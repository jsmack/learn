import logging.config


logging.config.fileConfig('logging.ini')


#logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleExpamle')


logger.debug('debug messages')
logger.info('info messages')
logger.warning('warning messages')
logger.error('error messages')
logger.critical('critical messages')