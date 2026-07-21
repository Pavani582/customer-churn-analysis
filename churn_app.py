import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Churn Dashboard",
                   layout="wide")

st.title("📊 Customer Churn Analysis Dashboard")

df = pd.read_csv(r'c:\Users\HOME\Downloads\Bank Customer Churn Prediction\Bank Customer Churn Prediction\Churn_Modelling.csv')

st.sidebar.header("Filters")

geo = st.sidebar.multiselect(
    "Geography",
    df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

df = df[
    (df["Geography"].isin(geo)) &
    (df["Gender"].isin(gender))
]

col1,col2,col3,col4 = st.columns(4)

col1.metric("Customers",len(df))

col2.metric("Churned",
            df["Exited"].sum())

retention=((len(df)-df["Exited"].sum())/len(df))*100

col3.metric("Retention %",
            f"{retention:.2f}%")

col4.metric("Average Age",
            round(df["Age"].mean(),1))

fig,ax=plt.subplots()

sns.countplot(x="Exited",
              data=df,
              ax=ax)

st.pyplot(fig)

fig,ax=plt.subplots()

sns.countplot(
    x="Gender",
    hue="Exited",
    data=df,
    ax=ax
)

st.pyplot(fig)

fig,ax=plt.subplots(figsize=(8,4))

sns.countplot(
    x="Geography",
    hue="Exited",
    data=df,
    ax=ax
)

st.pyplot(fig)

fig,ax=plt.subplots()

sns.histplot(df["Age"],
             kde=True)

st.pyplot(fig)

fig,ax=plt.subplots()

sns.histplot(df["Balance"],
             kde=True)

st.pyplot(fig)

df1=df.copy()

df1["Gender"]=df1["Gender"].map({
    "Male":1,
    "Female":0
})

df1=pd.get_dummies(
    df1,
    columns=["Geography"],
    drop_first=True
)

fig,ax=plt.subplots(figsize=(10,7))

sns.heatmap(
    df1.corr(),
    cmap="coolwarm"
)

st.pyplot(fig)

