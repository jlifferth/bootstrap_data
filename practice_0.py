import numpy as np
import pandas as pd


master_df = pd.read_csv('data/master_df_2.csv')

treatment_cell_lines = ['JHH6_0uM_n1', 'JHH6_0uM_n2', 'JHH6_0uM_n3', 'JHH6_0uM_n4',
                        'JHH6_1uM_n1', 'JHH6_1uM_n2', 'JHH6_1uM_n3', 'JHH6_1uM_n4',
                        'JHH6_2.5uM_n1', 'JHH6_2.5uM_n2', 'JHH6_2.5uM_n3', 'JHH6_2.5uM_n4',
                        'JHH7_0uM_n1', 'JHH7_0uM_n2', 'JHH7_0uM_n3', 'JHH7_0uM_n4',
                        'JHH7_1uM_n1', 'JHH7_1uM_n2', 'JHH7_1uM_n3', 'JHH7_1uM_n4',
                        'JHH7_2.5uM_n1', 'JHH7_2.5uM_n2', 'JHH7_2.5uM_n3', 'JHH7_2.5uM_n4']

treated_df = master_df[master_df.IMAGE_SERIES.isin(treatment_cell_lines)].reset_index(drop=True)
print(treated_df)

my_samples = []
# for _ in range(5000):
#     x = np.random.choice(sample, size=300, replace=True)
#     my_samples.append(x.mean())
#
# print(my_samples)