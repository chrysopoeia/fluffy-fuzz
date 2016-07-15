import re


class SceneReader(object):
    allowed_features = {
        'some_feature': None,
        'another_feature': None,
        'third_feature': None,
    }
    
    def read(self, file_location):
        with open(file_location, 'r') as scene_file:
            raw_scene = scene_file.read()
        
        # pattern = r'<[^/].+?>.*?</.+?>'
        # pattern = r'<([^/].*?)>(.*?)</(.+?)>'
        
        pattern = r'<([^/].*?)>(.*?)</(.+?)>'
        result = re.findall(pattern, raw_scene, flags=re.DOTALL)
        
        print result
        print '======================================================'
        
        for x in result:
            print x
            print '------------------------------------------------------'


if __name__ == '__main__':
    reader = SceneReader()
    reader.read('test.sc')
