X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, y)

print(clf.predict([[2]]))