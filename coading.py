import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# page configuration
st.set_page_config(page_title="Dataset Visualization App",layout="wide")
#set title
st.title("Dataset Visualization using Streamlit")
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file",type=["CSV"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # show dataframe
    st.subheader("DataFrame")
    st.dataframe(df.head(),use_container_width=True)
    st.write("*Shape of the DataFrame:*",df.shape)
    st.write("*Columns:*",list(df.columns))

    #data selection for visualization
    st.sidebar.header("Visualization options")
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()

    if len(numeric_cols) >= 2:
        x_col=st.sidebar.selectbox("Select X-axis",numeric_cols)
        y_col=st.sidebar.selectbox("Select Y-axis",numeric_cols)
        chart_type=st.sidebar.radio("Select Chart Type",["Line Chart","Bar Chart","Scatter Plot","Histogram"])

        #visualization area
        st.subheader(f"{chart_type} of {y_col} vs {x_col}")

        fig, ax = plt.subplots()
        if chart_type == "Line Chart":
            ax.plot(df[x_col], df[y_col])
        elif chart_type == "Bar Chart":
            ax.bar(df[x_col], df[y_col])
        elif chart_type == "Scatter Plot":
            ax.scatter(df[x_col], df[y_col])
        elif chart_type == "Histogram":
            ax.hist(df[x_col], bins=20)

        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)
    else:
        st.warning("please upload a dataset with at least two numeric columns.")
else:
    st.info("Please upload a CSV file to get started.")
