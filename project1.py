import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


data=pd.read_csv("YourPath")
#print(data.head())
#print(data.describe())
#print(data.info())

#print(data.isnull().sum())

"""Dropping Column"""
data.drop("Unnamed: 0",axis=1)



"""Changing weekly study hours """

data['WklyStudyHours']=data['WklyStudyHours'].str.replace('5 - 10','05-12')
#print(data.head())

'''gende distribution'''

# ax=sb.countplot(data=data,x="Gender")
# ax.bar_label(ax.containers[0])
#plt.show()



"""Group By"""

# gb=data.groupby('ParentEduc').agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
# print(gb)

# sb.heatmap(gb,annot=True)#annot for value
# plt.show() 


"Group by marital status "

# gb=data.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
# print(gb)

# sb.heatmap(gb,annot=True)
#plt.title("Impact on Student's Education")
# plt.show()


"For Outliers"
# sb.boxplot(data=data,x="MathScore")
# plt.show()


"Ethnic Group"
print(data["EthnicGroup"].unique())

groupA=data.loc[(data['EthnicGroup']=="group A")].count()
groupB=data.loc[(data['EthnicGroup']=="group B")].count()
groupC=data.loc[(data['EthnicGroup']=="group C")].count()
groupD=data.loc[(data['EthnicGroup']=="group D")].count()
groupE=data.loc[(data['EthnicGroup']=="group E")].count()

mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
l=["GroupA","groupB","groupC","groupD","groupE"]
plt.pie(mlist,labels=l,autopct="%1.2f%%")#autopct used for percentage

#plt.show()





