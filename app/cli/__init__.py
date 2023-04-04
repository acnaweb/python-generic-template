import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


__version__ = '0.1.0'