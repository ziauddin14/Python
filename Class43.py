import pandas as pd

df = pd.read_csv('Chocolate_Sales.csv')

print(df.info())

# Clean Amount column properly
df['Amount'] = (
    df['Amount']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

print(df['Amount'])

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) #Date format is DD/MM/YYYY
print(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()
print(df.info())
print(df.head())

#Null values
print(df.isnull().sum())
print(df.describe())

#Total revenue
total_revenue = df['Amount'].sum()
print("Total Revenue: $", total_revenue)
#Average order value
average_order_value = df['Amount'].mean()
print("Average Order Value: $", average_order_value)
#min and maxx sale
min_sale = df['Amount'].min()
max_sale = df['Amount'].max()
print("Minimum Sale: $", min_sale, max_sale)
#Revenue by country
revenue_country = df.groupby('Country')['Amount'].sum().sort_values(ascending=False)
print(revenue_country)

#boxes shipped by country
# boxes_country = df.groupby('Country')['Boxes'].sum().sort_values(ascending=False)
# print(boxes_country)

#which product is premium
premium_product = df.groupby('Product')['Amount'].sum().sort_values(ascending=False)
print(premium_product)

#which salseperson genereate more revenue
top_salesperson = df.groupby('Sales Person')['Amount'].sum().sort_values(ascending=False).head(1)
print(top_salesperson)

#Who shipped most boxes?
top_shipper = df.groupby('Sales Person')['Boxes Shipped'].sum().sort_values(ascending=False).head(1)
print(top_shipper)

#Sales above avg sale value
above_avg_sales = df[df['Amount'] > average_order_value].head(1)
print(above_avg_sales)

#Orders above $10000
orders_above_10000 = df[df['Amount'] > 10000].head(1)
print(orders_above_10000)

#High-value and high-volume orders
high_value_volume_orders = df[(df['Amount'] > 10000) & (df['Boxes Shipped'] > 200)].head(1)
print(high_value_volume_orders)

# Monthly trend and sort by month-name
monthly_revenue = df.groupby('Month_Name')['Amount'].sum().sort_index()
print(monthly_revenue)



#*******************Matplotlib Library*********************** is used for data visualization
import matplotlib.pyplot as plt

revenue_country.plot(kind='bar', title='Revenue by Country')
plt.xlabel('Country')
plt.ylabel('Revenue ($)')
plt.show()

monthly = df.groupby('Month')['Amount'].sum()
monthly.plot(kind='line', title='Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.show()