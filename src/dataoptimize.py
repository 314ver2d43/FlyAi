import os
import pandas as pd
import numpy as np
import struct
os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_feather("connectome-weights-male-cns-v1.0-minconf-0.5.feather")
col_pre = df.columns[0]
col_post = df.columns[1]
col_weight = df.columns[2]
df_filtered = df[df[col_weight] >= 3].copy()
unique_nodes = np.unique(np.concatenate([df_filtered[col_pre].values, df_filtered[col_post].values]))
node_to_idx = {node_id: idx for idx, node_id in enumerate(unique_nodes)}
with open("brain.bin", "wb") as f:
    f.write(struct.pack("<II", len(unique_nodes), len(df_filtered)))
    for pre, post, weight in zip(df_filtered[col_pre], df_filtered[col_post], df_filtered[col_weight]):
        f.write(struct.pack("<IIH", node_to_idx[pre], node_to_idx[post], int(weight)))
print("brain.bin готов")