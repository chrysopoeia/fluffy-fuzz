from . import config
from . import event


def init(config_path):
    config.load(config_path)
