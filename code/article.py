print("Hello world!")

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

import pandas as pd
df = pd.read_csv('../datasets/temporal.csv')
print(df.head(10)) #View first 10 data rows

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

print(df.describe())

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

print(df.info())

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

print(df)

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

print(df)

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

format_dict = {'data science':'${0:,.2f}', 'Mes':'{:%m-%Y}', 'machine learning':'{:.2%}'}
#We make sure that the Month column has datetime format
df['Mes'] = pd.to_datetime(df['Mes'])
#We apply the style to the visualization
print(df.head().style.format(format_dict))


# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~

print(df.head(10))

# ~~~~~~~~~~~~~~~~~~~~
print("\n\n~~~~~\n\n\n")
# ~~~~~~~~~~~~~~~~~~~~
