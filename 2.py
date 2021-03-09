#散布図
plt.scatter(setosa["SepalLabel"], setosa["Sepalwidth"])
plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
plt.show()

#setosaのSepalLabelとSepaWidthの相関係数
corr = np.corrcoef(setosa["SepalLength"],  setosa["SepaWidth"])
print(corr[0,1])

#散布図行列
pd.tools.plotting.scatter_matrix(setosa)
plt.tight_layout()
plt.show()

#単回帰分析
from sklearn import linear_model
LinerRegr = linear_model.LinearRegression()
X = setosa[["sepalLength"]]
Y = setosa[["SepalWidth"]]
LinerRegr.fit(x, Y)
plt.scatter(X,Y,color="brack")
px = np.arange(X.min(),X.max(),.01)[:,np.newaxis]
py = LinerRegr.predict(px)
plt.plot(px, py, color="bule",linewidth=3)
plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
plt.show()
print(LinerRegr.coef_)#回帰係数
print(LinerRegr.intercept_)#切片

Linerregr.score(X,Y)#決定係数

