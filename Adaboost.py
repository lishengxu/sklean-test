X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

from sklearn.ensemble import AdaBoostClassifier

clf = AdaBoostClassifier()

clf.fit(X, y)

print clf.predict([[4]])