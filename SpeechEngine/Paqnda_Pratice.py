from typing import Collection
import pandas as pd
import numpy as np
"""
sr1 =pd.Series(["raj", "Sam","Sita"], index=["a", "b", "c"])
print(sr1)

d1 = {"tomatoe": "red", "peas": "green", "carrot":"orange"}
sr2 = pd.Series(d1)
print(sr2)

sr3 = pd.Series(np.arange(1, 7, 1), index=["a", "b", "c","d", "e", "f"])
print(sr3)
print(sr3[0:3])
print(sr3["a":"e"])
sr3.name = "values of data"
print(sr3)
sr3.index.name = "srno"
print(sr3)
print(sr3.values)
print(sr3.size)
print(sr3.head(2))
print(sr3.tail(2))
print(sr1 +sr2)
"""
ar1 = np.array([1000, 2000, 3000])
ar2 = np.array([10, 20, 30])
ar3 = np.array([-1000, -2000, -3000])
fr1 = pd.DataFrame([ar1, ar2, ar3], columns= ["A", "B", "C"], index= ["I", "II", "III"])
print(fr1)
d1 = [{"a": 10, "b": 20}, {"a": 15, "b": 25}]
fr2 = pd.DataFrame(d1)
print(fr2)
d2 = {"Name": ["Assam", "Delhi", "Kerala"],"area":[74838, 1483, 38852], "pop":[33333, 4.6, 174632788775] }
fr3 = pd.DataFrame(d2)
print(fr3)
sr1 =pd.Series([10, 20, 30],index = ["Math","Science", "English"] )


sr2 =pd.Series([30, 22, 36],index = ["Math","Science", "English"] )


sr3 =pd.Series([23, 36, 32],index = ["Math","Science", "English"] )
fr4 = pd.DataFrame([sr1, sr2, sr3])
print(fr4)
d3 = {"Raj": sr1, "Rohan": sr2, "Sita": sr3} 

fr5 = pd.DataFrame(d3)
print(fr5)
fr5 ["Raj"] = [35, 34, 33]
print(fr5)

fr5.loc["Math"] = [74, 35, 13]
print(fr5)
fr5.loc["Hindi"] = [67, 89, 98]
print(fr5)
fr5 = fr5.drop("Hindi", axis=0)

print(fr5)
fr5 = fr5.drop("Sita", axis=1)
print(fr5)


print(fr5["Raj"])


print(fr5.loc["Math"])


print(fr5.index)


print(fr5.columns)


print(fr5.values)


print(fr5.shape)


print(fr5.size)


print(fr5.T)


print(fr5.head(2))

print(fr5.tail(2))

print(fr5.describe())



print(fr5)
