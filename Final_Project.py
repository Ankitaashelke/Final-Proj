
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Disable the warning about pyplot's global use
st.set_option('deprecation.showPyplotGlobalUse', False)

data = pd.read_csv(r'C:\Users\admin\Desktop\Ankitaa\Assignments\Informatics\week 13\new-folder\Informatics_Project\Week11_dataset.csv')

# Display data
st.write(data.head())

# User input
categories = data['Category'].unique()
category_entry = st.selectbox('Select a product category:', categories)

cities = data['ship-city'].unique()
city_entry = st.selectbox('Select a city:', cities)

# Function to get category details
def category_details(category, city):
    category_city = data[(data['Category'] == category) & (data['ship-city'] == city)]

    # Convert 'Date' column to datetime
    category_city['Date'] = pd.to_datetime(category_city['Date'])

    # Extract month and year
    category_city['Month'] = category_city['Date'].dt.month

    # Group by month and sum the quantity
    sales_by_month = category_city.groupby('Month')['Quantity'].sum().reset_index()

    # Sort by total sales in descending order and select top 3 months
    top_months = sales_by_month.nlargest(3, 'Quantity')

    # Plotting the top 3 months with highest sales
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Month', y='Quantity', data=top_months, palette='viridis', ax=ax)
    ax.set_title(f"Top 3 Months with Highest Sales for {category} in {city}")
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Sales')

    # Set tick labels based on available months in the data
    available_months = top_months['Month'].unique()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax.set_xticks(available_months)
    ax.set_xticklabels([month_names[i - 1] for i in available_months])

    st.pyplot(fig)

# Display category details based on user input
if st.button('Show Details'):
    category_details(category_entry, city_entry)
