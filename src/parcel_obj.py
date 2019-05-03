from .parser_base import parser_base
from .legal_sector_obj import legal_sector_obj
from .payment_obj import payment_obj
from .tax_record_obj import tax_record_obj

class parcel_obj(parser_base):
    def __init__(self, key):
        super().__init__(key=key)
        self.tax_records = []
        self.payment_records = []
        self.legal_sector_records = []
        self.mappings = {
            'APN': {'first_char_loc': 0, 'last_char_loc': 8, 'type': str}
            , 'APN_Suf': {'first_char_loc': 8, 'last_char_loc': 10, 'type': str}
            , 'TDN': {'first_char_loc': 10, 'last_char_loc': 19, 'type': str}
            , 'Rec_Typ': {'first_char_loc': 19, 'last_char_loc': 20, 'type': str}
            , 'Rec_Sts_Cde': {'first_char_loc': 20, 'last_char_loc': 21, 'type': str}
            , 'Curr_TRA': {'first_char_loc': 21, 'last_char_loc': 26, 'type': str}
            , 'Prev_TRA': {'first_char_loc': 26, 'last_char_loc': 31, 'type': str}
            , 'Prev_APN': {'first_char_loc': 31, 'last_char_loc': 39, 'type': str}
            , 'Prev_APN_Suf': {'first_char_loc': 39, 'last_char_loc': 41, 'type': str}
            , 'Orig_TRA': {'first_char_loc': 41, 'last_char_loc': 46, 'type': str}
            , 'Orig_APN': {'first_char_loc': 46, 'last_char_loc': 54, 'type': str}
            , 'Orig_APN_Suf': {'first_char_loc': 54, 'last_char_loc': 56, 'type': str}
            , 'Situs_Street_Number': {'first_char_loc': 56, 'last_char_loc': 61, 'type': str}
            , 'Situs_Street_Number_Suffix': {'first_char_loc': 61, 'last_char_loc': 63, 'type': str}
            , 'Situs_Street_Direction': {'first_char_loc': 62, 'last_char_loc': 65, 'type': str}
            , 'Situs_Street_Name': {'first_char_loc': 65, 'last_char_loc': 90, 'type': str}
            , 'Situs_Street_Name_Suffix': {'first_char_loc': 90, 'last_char_loc': 92, 'type': str}
            , 'Situs_Unit_Number': {'first_char_loc': 92, 'last_char_loc': 97, 'type': str}
            , 'Situs_City_Code': {'first_char_loc': 97, 'last_char_loc': 99, 'type': str}
            , 'Mult_Flag': {'first_char_loc': 99, 'last_char_loc': 100, 'type': str}
            , 'Comb_Parcel': {'first_char_loc': 100, 'last_char_loc': 101, 'type': str}
            , 'Dte_Deeded_Year': {'first_char_loc': 101, 'last_char_loc': 105, 'type': str}
            , 'Dte_Deeded_Month': {'first_char_loc': 105, 'last_char_loc': 107, 'type': str}
            , 'Dte_Deeded_Day': {'first_char_loc': 107, 'last_char_loc': 109, 'type': str}
            , 'Dte_Recorded_Year': {'first_char_loc': 109, 'last_char_loc': 113, 'type': str}
            , 'Dte_Recorded_Month': {'first_char_loc': 113, 'last_char_loc': 115, 'type': str}
            , 'Dte_Recorded_Day': {'first_char_loc': 115, 'last_char_loc': 117, 'type': str}
            , 'Doc_Ref_Nbr': {'first_char_loc': 117, 'last_char_loc': 128, 'type': str}
            , 'Upd_Flg': {'first_char_loc': 128, 'last_char_loc': 129, 'type': str}
            , 'Paid_Flg': {'first_char_loc': 129, 'last_char_loc': 130, 'type': str}
            , 'Install_Start_Year': {'first_char_loc': 130, 'last_char_loc': 134, 'type': str}
            , 'Install_Month': {'first_char_loc': 134, 'last_char_loc': 136, 'type': str}
            , 'Point_Bill_Ind': {'first_char_loc': 136, 'last_char_loc': 137, 'type': str}
            , 'Lost_Hist_Yr': {'first_char_loc': 137, 'last_char_loc': 141, 'type': str}
            , 'Upd_Dte_Year': {'first_char_loc': 141, 'last_char_loc': 145, 'type': str}
            , 'Upd_Dte_Month': {'first_char_loc': 145, 'last_char_loc': 147, 'type': str}
            , 'Upd_Dte_Day': {'first_char_loc': 147, 'last_char_loc': 149, 'type': str}
            , 'Install_Paid_Year': {'first_char_loc': 149, 'last_char_loc': 153, 'type': str}
            , 'Install_Paid_Month': {'first_char_loc': 153, 'last_char_loc': 155, 'type': str}
            , 'Install_Paid_Day': {'first_char_loc': 155, 'last_char_loc': 157, 'type': str}
            , 'Install_Paid_99': {'first_char_loc': 157, 'last_char_loc': 159, 'type': str}
            , 'No_XRef_Flag': {'first_char_loc': 159, 'last_char_loc': 160, 'type': str}
            , 'Pre_JPA_Flg': {'first_char_loc': 160, 'last_char_loc': 161, 'type': str}
            , 'TDN_Sts_CDE': {'first_char_loc': 161, 'last_char_loc': 163, 'type': str}
            , 'Bor_Nbr': {'first_char_loc': 163, 'last_char_loc': 175, 'type': str}
            , 'Board_Dte_Year': {'first_char_loc': 175, 'last_char_loc': 179, 'type': str}
            , 'Board_Dte_Month': {'first_char_loc': 179, 'last_char_loc': 181, 'type': str}
            , 'Board_Dte_Day': {'first_char_loc': 181, 'last_char_loc': 183, 'type': str}
            , 'Bor_Rsn_Cde': {'first_char_loc': 183, 'last_char_loc': 185, 'type': str}
            , 'Fnds_On_Deposit': {'first_char_loc': 185, 'last_char_loc': 196, 'type': float, 'decimal_precision':2}
            , 'Inst_Pay_Off_Amt': {'first_char_loc': 196, 'last_char_loc': 207, 'type': float, 'decimal_precision':2}
        }

    def add_legal_sector_record(self, line):
        lsr = legal_sector_obj(key=self.key)
        lsr.map_line(line=line)
        self.legal_sector_records.append(lsr)

    def add_tax_record(self, line):
        tr = tax_record_obj(key=self.key)
        tr.map_line(line=line)
        self.tax_records.append(tr)

    def add_payment_record(self, line):
        pr = payment_obj(key=self.key)
        pr.map_line(line=line)
        self.payment_records.append(pr)