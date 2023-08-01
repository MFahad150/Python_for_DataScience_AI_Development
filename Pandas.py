import pandas as pd

#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

# x = df[['ID']]

# Exercise 1
# import pandas as pd

a = {'Student':['David', 'Samuel', 'Terry', 'Evan'], 'Age':['27', '24', '22', '32'], 'Country':['UK', 'Canada', 'China', 'USA'], 'Course':['Python','Data Structures','Machine Learning','Web Development'], 'Marks':['85','72','89','76']}
df1 = pd.DataFrame(a)
df1

# Exercise 2
b = df1[["Marks"]]
b

# Exercise 3
c = df1[["Country","Course"]]
c


