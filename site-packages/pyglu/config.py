from ConfigParser import RawConfigParser as ConfigParser

current = ConfigParser()


def load(config_list):
    current.read(config_list)
    target_config = config_list[-1]
    
    with open(target_config, 'wb') as config_file:
        current.write(config_file)
    
    return current
