import parser
import modify_output
import pandas as pd

class handler:
    def __init__(self):
        self.parser = parser.parser()

    def run(self):
        output_fp = "Cleaned_Output.csv"
        self.parser.run(output_fp=output_fp)
        df = pd.read_csv(output_fp, low_memory=False)
        df = modify_output.get_tax_record_count(df=df)
        df = modify_output.get_payment_record_count(df=df)

        df = modify_output.set_column_order(df=df)
        df.to_csv(output_fp, index=False)

if __name__ == '__main__':
    h = handler()
    h.run()