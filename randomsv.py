import pandas as pd

df = pd.read_csv('danh-sach-sinh-vien.csv')
df_random = df.sample(n=7)
print(df_random)

export_csv = df_random.to_csv(r'D:\bt random\random.csv',index=False)