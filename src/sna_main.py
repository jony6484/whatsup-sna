import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

def main():
    conn = sqlite3.connect('database/SocialConversation.db')
    # conv_df = pd.read_csv('database/SocialConversation.csv')
    conv_df = pd.read_sql("select * from conversation", con=conn)
    conv_df.columns = [col.lower() for col in conv_df.columns.to_list()]
    conv_df['date_time'] = pd.to_datetime(conv_df[['date','time']].apply(lambda a: a[0]+a[1], axis=1))
    conv_df = conv_df.sort_values(by='date_time').reset_index()
    dt_0 = conv_df['date_time'][0]
    conv_df['min_from_start'] = (conv_df['date_time'] - dt_0).apply(lambda a: int(a.total_seconds()/60))
    conv_df = conv_df.iloc[1950:15450, :]
    # pd.to_datetime(conv_df.date[0], format='%m/%d/%y')
    # pd.to_datetime(conv_df.time, format=" %I:%M %p ")

    print('end of file ')




if __name__ == '__main__':
    main()