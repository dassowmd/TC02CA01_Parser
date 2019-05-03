import pandas as pd


class parser_base(object):
    def __init__(self, key):
        self.key = key
        self.mappings = {}
        self.ignore_fields = ['ignore_fields', 'mappings']

    def map_line(self, line):
        for key in self.mappings:
            parsed_value = self.parse_value_from_line(key, line)
            self.__setattr__(key, parsed_value)

    def parse_value_from_line(self, key, line):
        mapping = self.mappings[key]
        value = line[mapping['first_char_loc']:mapping['last_char_loc']].strip()
        return value

    def flatten(self):
        d = {}
        d['record_type'] = type(self).__name__
        d['record_type_count'] = 1
        for k, v in self.__dict__.items():
            if k in self.ignore_fields:
                continue
            if type(self.__getattribute__(k)) is list:
                temp_res = None
                count = 1
                for i in v:
                    temp_dict = i.flatten()
                    for t in temp_dict:
                        t['record_type'] = type(i).__name__
                        t['record_type_count'] = count
                        count += 1
                        yield t

            else:
                d[k] = v
        yield d

    # def flatten(self, obj):
    #     if obj is None or obj in self.ignore_fields:
    #         return None
    #     elif hasattr(obj, '__dict__') and obj.__dict__:
    #         return dict([(k, self.flatten(v)) for (k, v) in obj.__dict__.items()])
    #     elif isinstance(obj, (dict,)):
    #         return dict([(k, self.flatten(v)) for (k, v) in obj.items()])
    #     elif isinstance(obj, (list,)):
    #         return [self.flatten(x) for x in obj]
    #     elif isinstance(obj, (tuple,)):
    #         return tuple([self.flatten(x) for x in obj])
    #     else:
    #         return obj