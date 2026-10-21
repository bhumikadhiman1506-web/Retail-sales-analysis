import pandas as pd 
import matplotlib.pyplot as plt
import calendar


retail_data=pd.read_csv("retail_sales_dataset.csv")
print(retail_data)
print(retail_data.columns)
retail_data["Date"]=pd.to_datetime(retail_data["Date"],format="%Y-%m-%d")
retail_data["Year"]=retail_data["Date"].dt.year
retail_data["Month"]=retail_data["Date"].dt.month
print(retail_data.dtypes)
print(retail_data.head())

print("No of rows:",retail_data.shape[0])
print("No. of columns:",retail_data.shape[1])

print("Total Null Values:",retail_data.isnull().sum())
print("Null Columns:",retail_data.isnull().any(axis=0))
print("Total number of duplicate records:",retail_data.duplicated().sum())

statistics=retail_data.describe(include=["int64"])
print("Dataset Statistics:",statistics.round(2))

unique_data=retail_data[["Customer ID","Product Category","Transaction ID"]].nunique(axis=0)
print("Number of Unique Values:",unique_data)
print("Size of Dataset:",retail_data.size)

mean_age=retail_data["Age"].mean()
print("Mean age:",mean_age.round(2))
standard_dev=retail_data["Age"].std()
print("Standard Deviation:",standard_dev.round(2))
median_age=retail_data["Age"].median()
print("Median Age:",median_age)
print("Minimum Age:",retail_data["Age"].min())
print("Maximum Age:",retail_data["Age"].max())
#std=Ages show a noticeable amount of variation around the mean
#median=Half the customers are aged 42 or below, and half are 42 or above.
#min=The youngest customer is 18.
#max=The oldest customer is 64

mean_quantity=retail_data["Quantity"].mean()
print("Mean Quantity:",mean_quantity.round(2))
standard_quan=retail_data["Quantity"].std()
print("Standard Quantity:",standard_quan.round(2))
median_quan=retail_data["Quantity"].median()
print("Median Quantity:",median_quan)
min_quan=retail_data["Quantity"].min()
print("Minimum Quantity:",min_quan)
max_quan=retail_data["Quantity"].max()
print("Maximum Quantity:",max_quan)
#Since the quantity values can only be 1, 2, 3, or 4, the standard deviation of 1.13 indicates a moderate spread across this small range.

# mean_ppu=retail_data["Price per Unit"].mean()
# print("Mean Price per Unit:",mean_ppu.round(2))
# std_ppu=retail_data["Price per Unit"].std()
# print(std_ppu.round(2))
# median_ppu=retail_data["Price per Unit"].median()
#or
ppu_aggregation=retail_data["Price per Unit"].agg(["mean","median","max","min","std"])
print(ppu_aggregation.round(2))
#The mean (179.89) is much higher than the median (50). This suggests that some higher-priced items may be pulling the mean upward. The distribution may be right-skewed, although we would need to examine it to confirm.
number_transactions_each_unit_price=retail_data["Price per Unit"].value_counts().sort_index()
print("Number of Transactions Each Unit Price:",number_transactions_each_unit_price)
print("Top 5 Most Frequently Occurring Unit Prices:",retail_data["Price per Unit"].value_counts().head(5))

amount_aggregation=retail_data["Total Amount"].agg(["sum","mean","max","min","median"])
print(amount_aggregation)
amount_per_category=retail_data.groupby("Product Category")["Total Amount"].sum()
print("Total Sales Amount by Each Category:",amount_per_category.sort_index(ascending=False))

total_quantity=retail_data.groupby("Product Category")["Quantity"].sum()
print("Total Quantity Sold in each Product Category:",total_quantity)

total_sales_gender=retail_data.groupby("Gender")["Total Amount"].sum()


avg_rev_per_unit=amount_per_category/total_quantity
print("Average Revenue per Unit:",avg_rev_per_unit.round(2))

total_amount_gender=retail_data.groupby(["Product Category","Gender"])["Total Amount"].sum()
print("Total Sales Amount by Product Category and Gender:",total_amount_gender)

prod_categ_ppu=retail_data.groupby("Product Category")["Price per Unit"].mean()
print("Average Price per Unit by Product Category:",prod_categ_ppu.round(2))
total_sales=(retail_data["Quantity"] * retail_data["Price per Unit"]).sum()
print("Total Sales from Quantity and Unit Price:",total_sales)


total_sales_per_month=retail_data.groupby("Month")["Total Amount"].sum()
print("Total Sales in each Month:",total_sales_per_month)

avg_sales_per_month=total_sales_per_month.mean()
print("Average Sales in each Month:",avg_sales_per_month.round(2))

monthly_sales_percentage=(total_sales_per_month/total_sales_per_month.sum())*100
print("Monthly Sales Percentage:",monthly_sales_percentage.round(2)) 
highest_sales_month=total_sales_per_month.idxmax()
print("Highest Sales Month:",total_sales_per_month[highest_sales_month])

lowest_sales_month=total_sales_per_month.idxmin()
print("Lowest Sales Month:",total_sales_per_month[lowest_sales_month])

print("Top 3 months by Total Sales Amount:",total_sales_per_month.sort_values(ascending=False).head(3))
print("Months with Sales Above the Average Monthly Sales:",total_sales_per_month[total_sales_per_month>avg_sales_per_month])

sales_by_gender=retail_data.groupby(["Month","Gender"])["Total Amount"].sum()
print("Monthly Sales Amount by Gender:",sales_by_gender)

may_data=retail_data[retail_data["Month"]==5]
print("May Total Sales:",may_data["Total Amount"].sum())
print("Quantity Sold:",may_data["Quantity"].sum())
total_sales_may=may_data.groupby("Product Category")["Total Amount"].sum()
print("Total Sales Amount in May:",total_sales_may)



sept_data=retail_data[retail_data["Month"]==9]
print("Sept Total Sales:",sept_data["Total Amount"].sum())
print("Quantity Sold:",sept_data["Quantity"].sum())
total_sales_sept=sept_data.groupby("Product Category")["Total Amount"].sum()
print("Total Sales Amount in September:",total_sales_sept)


#total amount in each category
plt.bar(amount_per_category.index,amount_per_category.values)
plt.title("Total Sales Amount by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales Amount")
plt.show()

#total quantity each category 
plt.bar(total_quantity.index,total_quantity.values)
plt.title("Quantity Sold by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Quantity Sold")
plt.show()

#monthly sales trends 
month_names=[calendar.month_name[m] for m in total_sales_per_month.index]
plt.plot(month_names,total_sales_per_month.values,marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# total sales by gender
plt.bar(total_sales_gender.index,total_sales_gender.values)
plt.title("Total Sales Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales Amount")
plt.show()


total_quantity=retail_data.groupby("Product Category")["Quantity"].sum()

amount_per_category=retail_data.groupby("Product Category")["Total Amount"].sum()
fig,ax=plt.subplots(1,2,figsize=(12,5))
ax[0].bar(total_quantity.index,total_quantity.values)
ax[0].set_title("Total Quantity Sold by Category")
ax[0].set_xlabel("Product Category")
ax[0].set_ylabel("Total Quantity")

ax[1].bar(amount_per_category.index,amount_per_category.values)
ax[1].set_title("Total Sales Amount by Category")
ax[1].set_xlabel("Product Category")
ax[1].set_ylabel("Total Sales Amount")
plt.tight_layout()
plt.show()

#pie chart
plt.pie(amount_per_category.values,labels=amount_per_category.index,autopct="%1.1f%%",startangle=90)
plt.title("Sales Contribution by Product Category")
plt.show()
#Electronics generated the highest total sales amount (₹156,905), followed closely by Clothing (₹155,580). Beauty recorded the lowest total sales amount (₹143,515).
#Clothing had the highest sales volume, with 894 units sold, followed by Electronics with 849 units. Beauty had the lowest sales volume, with 771 units sold.
#Although Electronics sold fewer units (849) than Clothing (894), it generated higher total sales revenue. This may indicate that Electronics products have a higher average selling price, allowing the category to generate more revenue despite having a lower sales volume.
#Electronics generated the highest revenue (₹156,905) despite selling fewer units than Clothing. Its average price per unit (₹181.90) was higher than Clothing's (₹174.29), which may have contributed to the difference in revenue.
#May recorded the highest sales (₹53,150), while September recorded the lowest sales (₹23,620). The business can compare product categories, quantities sold, and revenue in both months to identify differences in customer purchasing behavior. Based on the findings, it can introduce targeted promotions, discounts, or marketing campaigns to improve sales during lower-performing months

