from src.parser_base import parser_base

class tax_record_obj(parser_base):
    def __init__(self, key):
        super().__init__(key=key)
        self.mappings = {
            'Tax_Asm_Yr': {'first_char_loc': 20, 'last_char_loc': 24, 'type': str}
            , 'Tax_Type': {'first_char_loc': 24, 'last_char_loc': 26, 'type': str}
            , 'Tax_Amt': {'first_char_loc': 26, 'last_char_loc': 36, 'type': str}
            , 'Tax_Install_Typ': {'first_char_loc': 36, 'last_char_loc': 37, 'type': str}
        }
