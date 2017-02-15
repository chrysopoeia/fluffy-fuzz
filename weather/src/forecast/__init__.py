import logging

logger = logging.getLogger('forecast')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger.addHandler(console)
logger.setLevel(logging.DEBUG)
