"""
Debug
info
Warning
Error
Critical
"""


import logging

# logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.warning("This is waring mesage")
logging.critical("Thisi is critical error message")
logging.info("This is ok message")
logging.error("This is error message")