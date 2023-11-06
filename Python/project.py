import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import preprocessing
path="E:\programming\data\Tadawul stcks_1.csv"
dt=pd.read_csv(path)
#print(dt)
dt.drop(['symbol','date']   ,axis=1)

dt.nunique()
dt.select_dtypes(exclude=["object"])
dt.isnull().sum()




path = r"E:\programming\data\Tadawul stcks_1.csv"
data22 = pd.read_csv(path)

from sklearn import SimpleImputer
#كود ملئ الخلايا المفقودة مع تحديد الاعمدة اللي فيها فقد 
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
data22[["open", "high","low"]] = imputer.fit_transform(data22[["open", "high","low"]])

print(data22)

#كود حفظ الملف بعد الملئ او التعديل
data22.to_csv(r"E:\programming\data\Tadawul_stocks_imputed.csv", index=False)

print("Data saved to CSV file.")

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import preprocessing
path="E:\programming\data\Tadawul_stocks_imputed.csv"
do=pd.read_csv(path)
#print(dt)
do.drop(['symbol','date']   ,axis=1)

#مهم عشان اعرف كام خليه مفقودة و اي العمود اللي فيه فقد
do.isnull().sum()

do.nunique()
do.select_dtypes(exclude=["object"])

df=do.corr()
sb.heatmap(df, annot=True)
plt.show()

plt.scatter(df["perc_Change"],df["volume_traded "])
plt.show()