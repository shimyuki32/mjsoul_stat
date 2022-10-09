import json
import os
import matplotlib.pyplot as plt
import statistics
import math
import itertools
import seaborn as sns

dir = 'haihu/'
files = os.listdir('haihu/')

df = []
oya_tensu = []
ko_tensu = []
for i, file in enumerate(files):
    print(file)

    with open(dir + file, encoding="utf-8") as f:
        df.append(json.load(f))


    for j in range(len(df[i]['log'])):
        kyoku = df[i]['log'][j][0][0]
        tensu = df[i]['log'][j][16]
        oya = (kyoku % 4)
        try:
            oya_tensu.append(tensu[1].pop(oya))
            ko_tensu.append(tensu[1])
        except:
            continue

ko_tensu = list(itertools.chain.from_iterable(ko_tensu))

print(statistics.mean(oya_tensu))
print(statistics.mean(ko_tensu))

# x_max = max(max(oya_tensu), max(ko_tensu))
# x_min = min(min(oya_tensu), min(ko_tensu))
range_bin_width = range(-36000)

sns.distplot(oya_tensu,bins=range_bin_width,kde_kws={"clip":(-18000,18000)}, hist_kws={"range":(-18000,18000)},norm_hist=True)
sns.distplot(ko_tensu,bins=range_bin_width,kde_kws={"clip":(-18000,18000)}, hist_kws={"range":(-18000,18000)}, norm_hist=True)
plt.legend(labels=["oya","ko"])
plt.show()