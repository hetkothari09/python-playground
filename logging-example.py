import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger.debug("DEBUG: This mssg should go to the log file")
logger.info("INFO: This should too")
logger.warning("WARNING: So should this")
logger.error("ERROR: this too!")
logger.critical("CRITICAL: this is most important!")