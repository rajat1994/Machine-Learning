import sklearn
from sklearn import tree
features = [[140, 1],[130, 1], [150,0], [170,0]]
#1 -> "smooth" 
#0 ->  "bumpy"
labels = [0, 0, 1, 1]
#1 -> "orange"
#0- > "apple"
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print clf.predict([[160,0]])