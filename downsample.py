import pandas as pd

def downsample():               # Downsample function is used to downsample the data - 1 sample/minute
    for i in ['detailTemp.csv','detailVol.csv','detail.csv']:           
        df = pd.read_csv(i,parse_dates=['Realtime'],index_col=['Realtime'])
        df = df.resample('1Min').sum()
        df.to_csv(i.strip('.csv')+'Downsampled'+'.csv',header=True)
