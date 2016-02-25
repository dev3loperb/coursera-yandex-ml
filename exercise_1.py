import numpy as np
import pandas
import re

titanic = pandas.read_csv('titanic.csv', index_col='PassengerId')

sex = titanic['Sex'].value_counts()
male_count = sex['male']
female_count = sex['female']

with open('1.txt', 'w') as f:
    f.write(str(male_count) + ' ' + str(female_count))

survived_count = titanic['Survived'].value_counts()[1]
passengers_count = len(titanic)

with open('2.txt', 'w') as f:
    f.write(str(np.around(survived_count / passengers_count.real * 100.0, decimals=2)))

first_class_passengers_amount = titanic['Pclass'].value_counts()[1]

with open('3.txt', 'w') as f:
    f.write(str(np.around(first_class_passengers_amount / passengers_count.real * 100.0, decimals=2)))

finiteAges = titanic[np.isfinite(titanic['Age'])]['Age']
meanAges = np.mean(finiteAges)
medianAges = np.median(finiteAges)

with open('4.txt', 'w') as f:
    f.write(str(np.around(meanAges, decimals=2)) + ' ' + str(medianAges))

with open('5.txt', 'w') as f:
    f.write(str(np.around(np.corrcoef(titanic['SibSp'].tolist(), titanic['Parch'].tolist())[0, 1], decimals=2)))

women_names = titanic[['Sex', 'Name']][(titanic.Sex == 'female')]['Name']

print(women_names.tolist())


def take_first_name(name):
    m = re.search("Miss\.\s(\w+)", name)
    if m:
        return m.group(1)
    m = re.search("Mrs\..*?\((\w+)", name)
    if m:
        return m.group(1)


names = pandas.DataFrame.from_dict(list(map(take_first_name, women_names)))
most_popular_name = names[0].value_counts().idxmax()

with open('6.txt', 'w') as f:
    f.write(most_popular_name)
