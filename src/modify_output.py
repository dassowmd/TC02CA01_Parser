import pandas as pd

def get_tax_record_count(df):
    tax_record_count = df[df['record_type'] == 'tax_record_obj'][['key', 'record_type_count']].groupby(['key'])['record_type_count'].max()
    tax_record_count = tax_record_count.rename(columns={'record_type_count': 'Tax_Record_Count'})
    res_df = df.merge(tax_record_count.rename('tax_record_count'), left_on=df['key'], right_on=tax_record_count.index, how='left')
    res_df.drop(columns=['key_0'], inplace=True)
    return res_df

def get_payment_record_count(df):
    payment_record_count = df[df['record_type'] == 'payment_obj'][['key', 'record_type_count']].groupby(['key'])['record_type_count'].max()
    payment_record_count = payment_record_count.rename(columns={'record_type_count': 'Payment_Record_Count'})
    res_df = df.merge(payment_record_count.rename('payment_record_count'), left_on=df['key'], right_on=payment_record_count.index, how='left')
    res_df.drop(columns=['key_0'], inplace=True)
    return res_df

def set_column_order(df):
    primary_col_order = ['Situs_Street_Number', 'Situs_Street_Direction', 'Situs_Street_Name','Situs_Street_Name_Suffix','Situs_Street_Number_Suffix','Situs_Unit_Number','APN','APN_Suf','TDN', 'tax_record_count', 'payment_record_count']
    df_columns = df.columns
    for c in primary_col_order:
        if c not in df_columns:
            raise KeyError('%s not in df' % c)
    secondary_col_order = []
    for col in df_columns:
        if col not in primary_col_order:
            secondary_col_order.append(col)

    primary_col_order.extend(secondary_col_order)
    return df[primary_col_order]
