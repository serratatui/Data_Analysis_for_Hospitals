import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# write your code here
ds_gen = pd.read_csv("test/general.csv")
ds_pre = pd.read_csv("test/prenatal.csv")
ds_pre.columns = ds_gen.columns
ds_sport = pd.read_csv("test/sports.csv")
ds_sport.columns = ds_gen.columns
out = pd.concat([ds_gen, ds_pre, ds_sport], ignore_index=True)

out.drop(['Unnamed: 0'], axis=1, inplace=True)
out.dropna(how="all", inplace=True)
out.replace(to_replace={np.nan: 0}, inplace=True)
out.replace(to_replace={'gender': {'woman': 'f', 'man': 'm'}}, inplace=True)

# stage 4/5 counting metrics
# First question
# print("The answer to the 1st question is " + out.hospital.value_counts().idxmax())
# Second question
# print("The answer to the 2nd question is " + str(round(out[(out.hospital == 'general') & (out.diagnosis == 'stomach')].hospital.count() / out[out.hospital == 'general'].hospital.count(), 3)))
# Third question
# print("The answer to the 3rd question is " + str(round(out[(out.hospital == 'sports') & (out.diagnosis == 'dislocation')].hospital.count() / out[out.hospital == 'sports'].hospital.count(), 3)))
# Fourth question
# print("The answer to the 4th question is " + str(out[(out.hospital == 'general')].age.median() - out[(out.hospital == 'sports')].age.median()))

# stage 5/5 counting metrics
# pd.set_option('display.max_columns', None)
# print(ds_gen.head(20))
# print(ds_pre.head(20))
# print(ds_sport.head(20))
# First question
out['hospital'].value_counts().plot(y=['hospital'], kind='bar', grid=True)
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(10))
plt.show()
print("The answer to the 1st question: general")
plt.close()

# Second question
# out['diagnosis'].value_counts().pie(y=['diagnosis'], figsize=(5, 5))
plot = out['diagnosis'].value_counts().plot(y=['diagnosis'], kind='pie')
plt.show()
plt.close()
print("The answer to the 2nd question: pregnancy")

# Third question
sns.set_theme(style="whitegrid")
ax = sns.violinplot(x="hospital", y="height", data=out)
plt.show()
plt.close()
print("The answer to the 3rd question: It's because of different measure units)")
