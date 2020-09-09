import numpy as np
import pandas as pd
values=np.random.binomial(1,0.5,20)
ans=pd.DataFrame(values,columns=["outcome"]) #dataframe containing 20 coin flips

((ans[ans['outcome']==1].count())/20)*100 #Percentage of 1s in the output space, reaches close to 50% for large no of trials



