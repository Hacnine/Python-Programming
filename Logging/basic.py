from logging import *

LOG_FORMAT = '  %(lineno)d - %(asctime)s -- %(message)s'
basicConfig(filename='logfile.log', level=DEBUG, filemode='w', format=LOG_FORMAT)

logger = getLogger('custom')

debug('Its debugging')
info('Your app info')
warning('Its a warning')
error('Its a debug message')
critical('Its critical')