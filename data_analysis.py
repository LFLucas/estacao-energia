import pandas as pd

def data_pipe(dataframe):
    dataframe['Data_Registro'] = pd.to_datetime(dataframe['Data_Registro'])
    dataframe = dataframe.dropna()\
           .applymap(lambda x: abs(x) if type(x) == float else x, na_action='ignore')\
           .groupby(dataframe['Data_Registro'].dt.to_period('M')).mean()
    return dataframe

correlation_columns = [ 'Tensao_Fase_RS_V',    'Tensao_Fase_ST_V',     'Tensao_Fase_TR_V',  
                        'Corrente_Fase_R_A',   'Corrente_Fase_S_A',     'Corrente_Fase_T_A', 
                        'Demanda_kW',          'Potencia-Ativa_kW']

data_frame = pd.read_csv('Estação_Energia.csv', delimiter=';')
data_frame_monthly = data_pipe(data_frame)
data_frame_correlation = data_frame_monthly[correlation_columns].corr()

data_frame_monthly.to_csv('data_frame_monthly.csv')
data_frame_correlation.to_csv('data_frame_correlation.csv')

print("DATAFRAME #####################################\n", data_frame, "\n\n\n",
      "MEDIA #####################################\n", data_frame_monthly, "\n\n\n",
      "CORRELAÇAO #####################################\n", data_frame_correlation)


