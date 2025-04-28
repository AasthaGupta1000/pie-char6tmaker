import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Pie Chart Generator from CSV")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(df)

    # Step 2: Select a column
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if not categorical_cols:
        st.warning("No categorical columns found for pie chart.")
    else:
        column = st.selectbox("Select a column to plot a Pie Chart", categorical_cols)

        # Step 3: Plot Pie Chart
        if column:
            pie_data = df[column].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig) 
        
