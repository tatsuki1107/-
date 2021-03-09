#データ加工
setosa = iris[iris["Name"] == "Iris-setosa"]
versicolor = iris[iris["Name"] == "Iris-versicolor"]
virginica = iris[iris["Name"] == "Iris-virginica"]

setosa.sum() #合計
setosa.mean() #平均
setosa.median() #中央値
setosa.min() #最小値
setosa.max() #最大値
setosa.corr() #相関係数
setosa.var() #分散
setosa.std() #標準偏差
setosa.cov() #共分散

#品種ごとの平均値
iris.groupby("Name").mean()

#ヒストグラム
plt.figure()
plt.hist(iris["SepalLength"])
plt.xlabel("SepalLength")
plt.ylabel("Freq")
plt.show()

#setosaについてSepalLengthのヒストグラムを書く
plt.figure()
plt.hist(setosa["SepalLength"])
plt.xlabel("SepalLength")
plt.ylabel("Freq")
plt.show()

#箱ひげ図
data = [setosa["SepalLength"], versicolor["SepalLength"], virginica["SepalLength"]]
plt.figure()
plt.boxplot(data, sym="k.")
plt.xlabel("Name")
plt.ylebal("SepalLength")
ax = plt.gca()
plt.setp(ax, xticklabels=["setosa", "versicolor", "virginica"])
plt.show()
