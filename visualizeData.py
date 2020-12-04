import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

# Version
# print(mpl.__version__)  #> 3.0.0
# print(sns.__version__)  #> 0.9.0




nhadat = pd.read_csv("alnd_0412.csv")
sample = nhadat.head(20)
gia_nha = sample['giá'].values
dien_tich  = sample['diện tích'].values
vi_tri = sample['quận'].values

    
chung_cu = {'area': vi_tri, 'price': gia_nha}
df = pd.DataFrame(chung_cu)
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)    
sns.stripplot(df.area, df.price, jitter=0.25, size=8, ax=ax, linewidth=.5)

plt.title('giá nhà theo quận huyện', fontsize=22)
plt.show()
print("DONE!!!")