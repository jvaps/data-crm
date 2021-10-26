import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
# Classe do dataframe
df = pd.read_csv('test.csv')
x = df['nota'].values.reshape(-1, 1)
y = df['idade'].values.reshape(-1, 1)

reg = LinearRegression()
reg.fit(x, y)

f_previsaoes = reg.predict(x)

plt.figure(figsize = (16,8))
plt.scatter(
    x,
    y,
    c='red')


plt.plot(
    x,
    f_previsaoes,
    c='blue',
    linewidth=3,
    linestyle=':'
)

plt.xlabel("Nota do cliente")
plt.ylabel("Idade do cliente")
plt.show()

X2 = sm.add_constant(x)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())
