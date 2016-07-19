import re

# some working patterns for experimental file formats
CLOSING_TAG_PATTERN = r'<([^/].*?)>(.*?)</(.+?)>'
NEW_LINE_PATTERN = r'<(.*?)>(.*?)\n\n'

# exprimental patterns
BLAH_NEW_LINE_PATTERN = r'<(.*?)>(.*?)'


class SceneReader(object):
    allowed_features = {
        'some_feature': None,
        'another_feature': None,
        'third_feature': None,
    }
    
    def read(self, file_location):
        with open(file_location, 'r') as scene_file:
            raw_scene = scene_file.read()
        
        pattern = BLAH_NEW_LINE_PATTERN
        result = re.findall(pattern, raw_scene, flags=re.DOTALL)
        
        for x in result:
            print x
            print '------------------------------------------------------'


if __name__ == '__main__':
    reader = SceneReader()
    reader.read('test.sc')
