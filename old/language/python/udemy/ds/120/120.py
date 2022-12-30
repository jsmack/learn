import logging


#logging.basicConfig(level=logging.INFO,filename='test.log')
formatter = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(level=logging.INFO,format=formatter)


logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')


logging.info('info {}'.format('test'))
logging.info('info %s','test')
logging.info('info %s %s', 'test1','test3')
