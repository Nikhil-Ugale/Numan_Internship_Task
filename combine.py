import pandas as pd

def combine():           # Combine function - this is used to combine the sheets into a single csv file
    for i in ['data.xlsx','data_1.xlsx']:
        if(i=='data.xlsx'):
            df = pd.concat(pd.read_excel('data.xlsx', sheet_name=['Detail_67_1_1_1','Detail_67_1_1_2', 'Detail_67_1_1_3','Detail_67_1_1_4',
                                                      'Detail_67_1_1_5', 'Detail_67_1_1_6']))
            df_vol = pd.concat(pd.read_excel('data.xlsx', sheet_name=['DetailVol_67_1_1', 'DetailVol_67_1_1_1', 'DetailVol_67_1_1_2', 'DetailVol_67_1_1_3',
                                                          'DetailVol_67_1_1_4', 'DetailVol_67_1_1_5','DetailVol_67_1_1_6']))
            df = df.rename(columns={'Absolute Time': 'Realtime'})
            df.to_csv('detail.csv',header=True)
            df_vol.to_csv('detailVol.csv',header=True)
        else:
            df_temp_1 = pd.concat(pd.read_excel('data.xlsx', sheet_name=['DetailTemp_67_1_1', 'DetailTemp_67_1_1_1', 'DetailTemp_67_1_1_2']))
            df_temp_1 = pd.concat(pd.read_excel('data_1.xlsx', sheet_name=['DetailTemp_67_1_1_3', 'DetailTemp_67_1_1_4', 'DetailTemp_67_1_1_5', 'DetailTemp_67_1_1_6']))
            df_temp_1.to_csv('detailTemp.csv',header=True)
