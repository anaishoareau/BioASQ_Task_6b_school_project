# -*- coding: utf-8 -*-

""" IMPORTS """

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import read_excel

""" DATASET LOADING """

sheet_name = 'Sheet1'
file_name = './data/Questions.xlsx'
dataset = read_excel(file_name, sheet_name = sheet_name )

#Column labelisation
columns = ['question','question_type']
dataset.columns = columns

# Data Display
print("\n -> Dataset head:\n")
print(dataset.head())

""" CSV Conversion """

dataset.to_csv('./data/questions.csv')

""" GENERAL STUDY ABOUT THE DATASET """

print("\n -> General information about the dataset:")

# Dataset size
len_dataset =len(dataset)
print("\nNumber of labellised data: {}".format(len_dataset))

# Empty cells
not_empty = [0]*2
for i in range(0, 2) : 
    not_empty[i] = dataset.iloc[:,i].count()
    print("Number of empty cells for the", columns[i] , " column: {}".format(len(dataset) - not_empty[i]))


#We display the number of elements in each category of the column "question_type"
#to see the distribution in the dataset of our labels
print("\n -> The following graphics give the number of questions in each question type (summary, list, yesno, factoid).\n" )
sns.countplot(x='question_type', data = dataset)
plt.show()

print("\n -> Precise number of questions in each question type (summary, list, yesno, factoid):\n" )
print(dataset.groupby('question_type')['question_type'].count().sort_values(ascending=False))
