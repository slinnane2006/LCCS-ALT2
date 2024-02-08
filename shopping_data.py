import statistics
import pandas

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('shopping_data.csv')

# Filter out the column, value_eur
OnLine_Amt = df['Amt-OnLine']
print(OnLine_Amt)
storeAmt_ = df['Amt_InShop']
print(storeAmt_)
