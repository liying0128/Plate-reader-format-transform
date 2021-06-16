import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
abs1=pd.read_excel('abs3.xlsx')
abs1=abs1.iloc[2:,1:]
data=np.zeros((72,96))
data=pd.DataFrame(data)
for k in range(97):
    for i in range(72):
        if k<12:
            data.iat[i,k]=abs1.iat[i*10,k]
        elif k<24:
            data.iat[i,k]=abs1.iat[1+(i*10),k-12]
        elif k<36:
            data.iat[i,k]=abs1.iat[2+(i*10),k-24]
        elif k<48:
            data.iat[i,k]=abs1.iat[3+(i*10),k-36]
        elif k<60:
            data.iat[i,k]=abs1.iat[4+(i*10),k-48]
        elif k<72:
            data.iat[i,k]=abs1.iat[5+(i*10),k-60]
        elif k<84:
            data.iat[i,k]=abs1.iat[6+(i*10),k-72]
        elif k<96:
            data.iat[i,k]=abs1.iat[7+(i*10),k-84]
data.to_excel('abs3_curve.xlsx')
            