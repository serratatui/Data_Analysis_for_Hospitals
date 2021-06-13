# import pandas as pd
#
# grades = {'Student': {0: 'Ann', 1: 'Bob', 2: 'Chris', 3: 'Drake', 4: 'Emma', 5: 'Finn', 6: 'Ginny'}, 'Algebra': {0: 10, 1: 8, 2: 9, 3: 3, 4: 8, 5: 4, 6: 6}, 'Geometry': {0: 8, 1: 6, 2: 9, 3: 6, 4: 9, 5: 4, 6: 5}, 'Physics': {0: 7, 1: 3, 2: 9, 3: 5, 4: 4, 5: 7, 6: 10}, 'Computer_science': {0: 10, 1: 4, 2: 6, 3: 7, 4: 5, 5: 6, 6: 4}, 'English': {0: 9, 1: 9, 2: 9, 3: 10, 4: 5, 5: 8, 6: 10}, 'Biology': {0: 8, 1: 9, 2: 7, 3: 4, 4: 5, 5: 7, 6: 3}}
# df = pd.DataFrame(grades)

# your code here
# print(df.mean(axis='columns'))
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('D:/2015.csv')
# df['Region'].value_counts().plot(y=['Region'], kind='barh', grid=True, alpha=0.5)
#
# plt.show()
# plt.close()
# print(round(data[data.labels == "M"].null_deg.median(), 3), round(data[data.labels == "R"].null_deg.median(), 3))
# print(data.describe(include='all'))
n = int(input())
i = 0
n_blocks = 1
while i < n:
    str = '$' * n_blocks
    print(str.center(n * 2 - 1))
    i += 1
    n_blocks += 2
