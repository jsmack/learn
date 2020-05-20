import logging

import log

#logging.basicConfig(level=logging.INFO,filename='test.log')
logging.basicConfig(level=logging.INFO)

logging.info('info')


#logger.setLevel(logging.DEBUG)
#logger.info('info1')
#logger.debug('debug2')

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'a' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('form main a = "test"')


#log.do_something()