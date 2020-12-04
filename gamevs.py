import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv



link_data = 'https://raw.githubusercontent.com/hustducnv/test/master/data/ign.csv'
data = read_csv(link_data, index_col=0, sep=";")



genre_data = data['genre']
genre = []
for record in genre_data:
    record = str(record)
    if record.find(",") != -1:
        record = record.split(',')
        for re in record:
            re = re.strip()
            genre.append(re)
    else:
        genre.append(record)
gen = list(set(genre))
value = []
for g in gen:
    value.append(genre.count(g))
plt.pie(value, labels=gen, autopct='%0.f%%', shadow=True, startangle=90)
plt.show()