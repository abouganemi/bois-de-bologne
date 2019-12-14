import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(columns=["c1", "c2", "c3", "c4"],
                  index=["L1", "L2", "L3"],
                  data=[np.arange(10, 14),
                        np.arange(20, 24),
                        np.arange(30, 34)])

print(df.shape)
print(df.columns)

print(df.head(2))

print(df[["c1", "c2"]])

print(df.info())
