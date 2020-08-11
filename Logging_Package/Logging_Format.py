import logging

logging.basicConfig( level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y:')


logging.warning("This is waring mesage")
logging.critical("Thisi is critical error message")
logging.info("This is ok message")
#logging.error("This is error message")