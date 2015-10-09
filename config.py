from ConfigParser import RawConfigParser as ConfigParser

current = ConfigParser()


def load(config_name):
    current.read(['default.cfg', config_name])
    
    with open(config_name, 'wb') as config_file:
        current.write(config_file)


# def generate_from_dict(config_object):
#     config_object.add_section('video')
#     config_object.set('video', 'mode', (640,480))
#     config_object.set('video', 'fullscreen', True)
