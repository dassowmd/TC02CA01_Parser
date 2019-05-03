from src.parser_base import parser_base

class payment_obj(parser_base):
    def __init__(self, key):
        super().__init__(key=key)
        self.mappings = {
            'Pay-Sqn': {'first_char_loc': 20, 'last_char_loc': 22, 'type': str}
            , 'Year of Payment': {'first_char_loc': 22, 'last_char_loc': 26, 'type': str}
            , 'Month of Payment': {'first_char_loc': 26, 'last_char_loc': 28, 'type': str}
            , 'Day of Payment': {'first_char_loc': 28, 'last_char_loc': 30, 'type': str}
            , 'Payment Sub': {'first_char_loc': 30, 'last_char_loc': 32, 'type': str}
            , 'Pay-Bat-Nbr': {'first_char_loc': 32, 'last_char_loc': 36, 'type': str}
            , 'Pay-BatTyp': {'first_char_loc': 36, 'last_char_loc': 37, 'type': str}
            , 'Pay-Amt': {'first_char_loc': 37, 'last_char_loc': 47, 'type': str}
            , 'Pay-Pen-Amt': {'first_char_loc': 47, 'last_char_loc': 57, 'type': str}
            , 'Pay-Redemp-Fee': {'first_char_loc': 57, 'last_char_loc': 61, 'type': str}
            , 'Batch-Sqn': {'first_char_loc': 61, 'last_char_loc': 66, 'type': str}
        }
