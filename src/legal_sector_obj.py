from src.parser_base import parser_base

class legal_sector_obj(parser_base):
    def __init__(self, key):
        super().__init__(key=key)
        self.mappings = {
            'Legal-SQN': {'first_char_loc': 20, 'last_char_loc': 22, 'type': str}
            , 'Legal-Type': {'first_char_loc': 22, 'last_char_loc': 23, 'type': str}
            , 'Legal-Description': {'first_char_loc': 23, 'last_char_loc': 48, 'type': str}
        }
