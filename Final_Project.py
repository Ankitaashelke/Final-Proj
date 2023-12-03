
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

def main():
    st.title("This is my Streamlit App")
    st.write("Welcome to my informatics project!")


    file_url='https://github.com/Ankitaashelke/Informatics/raw/main/Week11_dataset.csv'


    content=requests.get(file_url).content
    df =pd.read_csv(io.StringIO(content.decode('utf-8')))

    st.subheader("Subset of the Sales Data")

    st.dataframe(df.head(10))  





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests

# Workaround to avoid Matplotlib attribute error
import matplotlib
matplotlib.use("agg")

def category_details(df, category, city):
    category_city = df[(df['Category'] == category) & (df['ship-city'] == city)]

    category_city['Month'] = pd.to_datetime(category_city['Date']).dt.month
    category_city['Year'] = pd.to_datetime(category_city['Date']).dt.year
    category_city['Month'] = category_city['Month'].map({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'})

    sales_by_month = category_city.groupby(['Year', 'Month'])['Quantity'].sum().reset_index()
    top_months = sales_by_month.nlargest(3, 'Quantity')

    plt.figure(figsize=(8, 6))
    sns.barplot(x='Month', y='Quantity', data=top_months, palette='viridis')
    plt.title(f'Top 3 Months with Highest Sales for {category} in {city}')
    plt.xlabel('Months')
    plt.ylabel('Total Sales')
    return plt

def main():
    st.title("Product Sales Analysis")
    st.write("Welcome to the Sales Analysis Dashboard!")

    file_url = 'https://github.com/Ankitaashelke/Informatics/raw/main/Week11_dataset.csv'

    content = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))

    st.subheader("Subset of the Sales Data")
    st.dataframe(df.head(10))

    categories = df['Category'].unique()
    selected_category = st.selectbox("Select a product category:", categories)

    cities = df['ship-city'].unique()
    selected_city = st.selectbox("Select a city:", cities)

    fig = category_details(df, selected_category, selected_city)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
