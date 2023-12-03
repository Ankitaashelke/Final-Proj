



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests
import seaborn as sns

def get_most_sales_cities(df, category):
    city_sales = df[df['Category'] == category].groupby('ship-city')['Quantity'].sum()
    sorted_cities = city_sales.sort_values(ascending=False)
    return sorted_cities.index[:3].tolist()

def get_marketing_formats(df, category):
    marketing_formats = df[df['Category'] == category]['Marketing Channel'].value_counts()
    return marketing_formats.idxmax()

def main():
    st.title("Product Sales Analysis")
    st.write("Welcome to the Sales Analysis Dashboard!")

    file_url = 'https://github.com/Ankitaashelke/Informatics/raw/main/Week11_dataset.csv'

    content = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%B')  # Get month names

    st.subheader("Subset of the Sales Data")
    st.dataframe(df.head(10))

    categories = df['Category'].unique()
    selected_category = st.selectbox("Select a product category:", categories)

    if st.button("Show Details"):
        most_sales_cities = get_most_sales_cities(df, selected_category)
        marketing_format = get_marketing_formats(df, selected_category)
        
        st.write(f"{selected_category} has most sales in these cities: {', '.join(most_sales_cities)}.")
        st.write(f"{selected_category} was sold more through {marketing_format} marketing.")

    if st.button("Show More"):
        top_months = df[df['Category'] == selected_category].groupby('Month')['Quantity'].sum().nlargest(5)
        
        # Plotting
        fig, ax = plt.subplots()
        sns.barplot(x=top_months.values, y=top_months.index, palette='viridis', ax=ax)
        ax.set_title(f'Top 5 Months with Highest Sales for {selected_category}')
        ax.set_xlabel('Total Sales')
        ax.set_ylabel('Month')

        # Display plot in Streamlit
        st.pyplot(fig)

if __name__ == "__main__":
    main()
