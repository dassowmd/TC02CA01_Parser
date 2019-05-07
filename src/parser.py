import os
from src.parcel_obj import parcel_obj
from tqdm import tqdm
import pandas as pd

class parser:
    def __init__(self, filename=None):
        self.parcel_objs = {}
        self.lines = self.load_text_file(filename=filename)

    def load_text_file(self, filename=None):
        # Load File
        if filename is None:
            filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'TC02CA01.txt')
        with open(filename, 'r') as f:
            lines = f.readlines()
            return lines

    def get_parcel_by_line(self, line):
        key = self.parse_key_from_line(line=line)
        return self.get_parcel_by_id(id=key)

    def get_parcel_by_id(self, id):
        try:
            parcel = self.parcel_objs.pop(id)
            self.add_parcel(parcel=parcel)
            return parcel
        except KeyError:
            return None
        except Exception as e:
            print(e)

    def add_parcel(self, parcel):
        self.parcel_objs[parcel.key] = parcel

    def create_parcel(self, line):
        key = self.parse_key_from_line(line=line)
        parcel = parcel_obj(key=key)
        parcel.map_line(line=line)
        self.parcel_objs[key] = parcel
        return parcel

    def parse_key_from_line(self, line):
        key = line[:8] + line[8:10] + line[10:18]
        return key

    def run(self, output_fp=None):
        self.iterate()
        self.save_results(output_fp=output_fp)

    def iterate(self):
        # Iterate through each line
        for line in tqdm(self.lines[:]):
        # for line in self.lines:
            # Determine line 'type'
            parcel = self.get_parcel_by_line(line=line)
            # if parcel is not found, must be the first line so create a new parcel_obj
            if parcel is None:
                # Build parcel obj
                self.create_parcel(line=line)
                # Parse into respective fields

            else:
                if line[19] == '4':
                    parcel.add_legal_sector_record(line=line)
                elif line[19] == '7':
                    parcel.add_tax_record(line=line)
                elif line[19] == '9':
                    parcel.add_payment_record(line=line)
                else:
                    raise NotImplemented('Rec-Typ %s not recognized' %line[19])

    def save_results(self, output_fp=None):
        if output_fp is None:
            output_fp = 'Cleaned_Output.csv'
        # Save results to csv
        res = []
        print("Parcel Count: ", len(self.parcel_objs))
        for k, obj in self.parcel_objs.items():
            gen = obj.flatten()
            for i in gen:
                res.append(i)

        df = pd.DataFrame(res)
        df.to_csv(output_fp, index=False)

if __name__=='__main__':
    p = parser()
    p.run()
