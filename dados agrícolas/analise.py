import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados alimenticio.csv')

comparacao_Brasil_e_Cuba = dados.groupby('76')['108'].sum()

plt.figure(figsize=(12, 8))
plt.pie()