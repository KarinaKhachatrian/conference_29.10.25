import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bigsoldb/BigSolDBv2.0.csv')

# plt.subplot(3, 1, 1)
# plt.hist(df['Solubility(mole_fraction)'], color='blue', bins=50)
# plt.xlabel('Растворимость, мольная доля')
# plt.ylabel('Частота')

plt.subplot(3, 1, 2)
plt.hist(df['Solubility(mol/L)'], color='purple', bins=50)
plt.xlabel('Растворимость, моль/л')
plt.ylabel('Частота')
#
# plt.subplot(3, 1, 3)
# plt.hist(df['LogS(mol/L)'], color='turquoise', bins=50)
# plt.xlabel('Растворимость, log10 (моль/л)')
# plt.ylabel('Частота')

plt.show()