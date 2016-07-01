

class SceneReader(object):
    allowed_features = {
        'some_feature': None,
        'another_feature': None,
        'third_feature': None,
    }
    
    descriptor_tags = {
        '#': None,
    }
    
    def read(self, file_location):
        with open(file_location, 'r') as scene_file:
            raw_scene = scene_file.readlines()
        
        for line in raw_scene:
            print line


if __name__ == '__main__':
    reader = SceneReader()
    reader.read('test.sc')
