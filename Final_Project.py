
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

    
    st.write("Can you show Total Sales Amount by Category? ")

    sales_by_category =df.groupby('Category')['Amount'].sum().reset_index()

    fig, ax =plt.subplots(figsize=(8,6))
    ax.bar(sales_by_category['Category'],sales_by_category['Amount'],color='skyblue')

    ax.set_title('Total Sales Amount by Category')

    ax.set_xlabel('Category')
    ax.set_ylabel('Total Sales Amount')

    ax.tick_params(axis='x',rotation=45)  

    st.pyplot(fig)

if __name__ == "__main__":
    main()