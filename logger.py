import logging

logging.basicConfig(filename='logfile.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Isso é uma mensagem de informação.')
logging.warning('Isso é uma mensagem de aviso.')
logging.error('Isso é uma mensagem de erro.')