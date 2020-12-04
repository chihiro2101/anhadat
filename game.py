import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')


gamedf = pd.read_csv("ign.csv", error_bad_lines=False)
genre_data = []
for record in gamedf:
    import pdb; pdb.set_trace()
    recordsplit = record.split(';')
    genre_data.append(recordsplit[6])

import pdb; pdb.set_trace()
print("DONE!!!")
