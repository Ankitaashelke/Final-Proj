Task: 

Streamlit Web App and Repository
At the end of the course, you will submit a URL to your project's GitHub repository, as well as a link to your web app. The GitHub repository should contain all code used in your project, as well as a README file which should include the following:

Abstract. Briefly summarize the main purpose of your project, and what came out of it.

Data Description. Describe the data you extracted/cleaned.

Algorithm Description. Outline the algorithm(s) driving your web app.

Tools Used. List all the tools you used for this project, describing the purpose(s) of each.






Solution: 



 Abstract:
 
 This project revolves around creating a user-friendly web application using Streamlit, focusing on simplifying the interpretation of sales data to help in marketing.
 The primary objective is to understand sales analytics, finding top-selling products across different locations and months and using this information in the business.
 The tool gives us details such as product performance in specific regions or during particular periods.
 It provides a direct answer to the users by taking input from them and giving them their desired answers.
 By taking input, the tool generates informative visuals like barplots and analyzes the trend.
 These visuals help businesses in identifying optimal locations, effective marketing channels, and potential target demographics for their products or services.
 By utilizing data analytics and visualization techniques, this project empowers businesses to make informed decisions about their marketing strategies. 
 Ultimately, the aim is to enhance marketing efficiency and increase overall impact.









Data Description: 


The dataset represents information related to attributes. Below are the attributes included in the dataset:
Index: Sequential number assigned to each entry.
Order ID: Unique identifier for each order.
Date: Date of the order placement.
Status: Current status of the order.
Fulfillment: Level of order fulfillment (e.g., pending, complete).
Marketing Channel: The channel used for marketing the product.
Style: The style or type of product.
Category: Categorization of the product.
Rating: Customer rating or feedback for the product.
Courier Status: Status of the courier service used.
Quantity: Number of items ordered.
Amount: Total cost or amount for the order.
Ship City: City where the order is to be shipped.
Ship State: State where the order is to be shipped.
Ship Postal Code: Postal code for the shipping address.

Data Cleaning Process
Initially, the dataset contained numerous columns and rows. 
For cleaning, these processes were done: 
Displayed the first few rows of unclean data to understand its structure.
Removed extra words from the 'Status' column for standardization.
Dropped unnecessary columns to streamline the dataset.
Converted certain float columns into integer columns for consistency.
Removed all null values to ensure data integrity.
Eliminated outliers to enhance data reliability.
The resulting clean dataset was saved for further analysis.
Displayed visualizations derived from the cleaned dataset to showcase insights.





Algorithm Description: 


#importing 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests
import seaborn as sns


#Setting the icon
st.set_page_config(page_icon=":moneybag:")


#  Calculating most sales in the city for a given product category

def most_sales_cities(dataframe, category):
    
    city_sales= dataframe[dataframe['Category']== category].groupby('ship-city')['Quantity'].sum()
    sorted_cities =city_sales.sort_values(ascending=False)
    return sorted_cities.index[:3].tolist()

#  Identifying the most used marketing channel for a given product category

def marketing_formats(dataframe, category):

    marketing_formats= dataframe[dataframe['Category']== category]['Marketing Channel'].value_counts()
    return marketing_formats.idxmax()

# Main function and setting up the title

def main():
    st.title("Marketing via analysis")
    st.write("Welcome to the sales analysis tool!")

    # Loading the dataset 
    
    file_url ='https://raw.githubusercontent.com/Ankitaashelke/Marketing_app/master/Week11_dataset.csv'
    content= requests.get(file_url).content
    df =pd.read_csv(io.StringIO(content.decode('utf-8')))

    # Data frame
    df['Date'] =pd.to_datetime(df['Date'])
    df['Month']= df['Date'].dt.strftime('%B')

    #subheader adding
    st.subheader("Data sample:")

    #showing first few rows
    st.dataframe(df.head(10))

    #  selecting a product category (user will select input)
    
    categories =df['Category'].unique()
    selected_category= st.selectbox("Select a product category:", categories)

    if st.button("Show Details"):

        #  Calculating and showing cities with most sales for the selected category
        
        most_sales_cities_list= most_sales_cities(df, selected_category)
        marketing_format =marketing_formats(df, selected_category)
        
        st.write(f"{selected_category} has most sales in these cities: {', '.join(most_sales_cities_list)}.")
        st.write(f"{selected_category} was sold more through {marketing_format}.")

        # Average Rating and Total Sales
        
        filtered_df =df[df['Category'] == selected_category]
        average_rating= round(filtered_df["Rating"].mean(), 1)
        total_sales =filtered_df["Amount"].sum()
        
        st.write(f"Average Rating: {average_rating}")
        st.write(f"Total Sales: INR {total_sales:,}")

    if st.button("Show More"):
        # Show top months with highest sales for the selected category
        top_months= df[df['Category']== selected_category].groupby('Month')['Quantity'].sum().nlargest(10)
        
        fig, ax =plt.subplots()
        sns.barplot(x=top_months.values,y=top_months.index, palette='viridis', ax=ax)
        ax.set_title(f'Top Months with Highest Sales for {selected_category}')
        ax.set_xlabel('Total Sales')
        ax.set_ylabel('Month')
        st.pyplot(fig)

if __name__ == "__main__":
    main()







Tools Used:


Python 3.9
Streamlit
Pandas
Matplotlib
Seaborn
Requests
GitHub
Jupyter Notebook
Io Module
CSV File
Markdown
Pyplot (Matplotlib)
NumPy
