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
# %matplotlib inline

# Version
# print(mpl.__version__)  #> 3.0.0
# print(sns.__version__)  #> 0.9.0




nhadat = pd.read_csv("aloNhaDatData2.csv")
sample = nhadat.head(20)
gia_nha = sample['giá'].values
dien_tich  = sample['diện tích'].values
vi_tri = sample['địa chỉ'].values


#giá nhà
price = []
for gia in gia_nha:
    raw_price = gia.split('tỷ')[0].replace(",", ".")
    price.append(float(raw_price))

# diện tích    
area = []
for dt in dien_tich:
    raw_area = dt.split('m vuông')[0]
    area.append(float(raw_area))

#vị trí
street = []
ward = []
district = []
for vt in vi_tri:
    vt = vt.split(",")
    street.append(vt[0])
    ward.append(vt[1])
    district.append(vt[2])
    

chung_cu = {'area': area, 'price': price}
df = pd.DataFrame(chung_cu)
# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)    
sns.stripplot(df.area, df.price, jitter=0.25, size=8, ax=ax, linewidth=.5)

# Decorations
# plt.gca().set(xlim=(0.0, 25), ylim=(0, 100),
#               xlabel='Area', ylabel='Population')


plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
plt.show()



#visualize    
categories = np.unique(district)    
import pdb; pdb.set_trace()
print("DONE!!!")