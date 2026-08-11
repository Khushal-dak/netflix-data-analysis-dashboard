import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix Data Analysis", layout="wide")
df = pd.read_csv("Netflix_Cleaned_Dataset.csv")

st.title("Netflix Content Analysis Dashboard")

# Dataset overview
st.header("Dataset Overview")
tab1, tab2, tab3, tab4 = st.tabs(["Head", "Shape & Columns", "Describe", "Info / Nulls"])
with tab1:
    st.dataframe(df.head(st.slider("Rows to show", 5, 50, 5)))
with tab2:
    st.write(f"Rows: {df.shape[0]}  |  Columns: {df.shape[1]}")
    st.dataframe(df.dtypes.astype(str).rename("dtype"))
with tab3:
    st.dataframe(df.describe())
    st.dataframe(df.describe(include="object"))
with tab4:
    st.dataframe(df.isnull().sum().rename("null_count"))
    st.write(f"Duplicate rows: {df.duplicated().sum()}")

st.divider()

# Filters
c1, c2 = st.columns(2)
type_filter = c1.multiselect("Content Type", df["type"].unique(), default=list(df["type"].unique()))
year_range = c2.slider("Release Year", int(df["release_year"].min()), int(df["release_year"].max()), (2000, int(df["release_year"].max())))
data = df[df["type"].isin(type_filter) & df["release_year"].between(*year_range)]

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Titles", len(data))
k2.metric("Movies", (data["type"] == "Movie").sum())
k3.metric("TV Shows", (data["type"] == "TV Show").sum())
k4.metric("Countries", data["country"].nunique())

st.divider()

def count_chart(col, kind="bar", top=None, orientation="v"):
    counts = data[col].value_counts().reset_index()
    counts.columns = [col, "count"]
    if top:
        counts = counts.head(top)
    if kind == "bar":
        fig = px.bar(counts, x=col if orientation == "v" else "count",
                     y="count" if orientation == "v" else col,
                     orientation=orientation, text="count")
    else:
        fig = px.pie(counts, names=col, values="count", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)
    return counts

# Content type distribution
st.header("Content Type Distribution")
col1, col2 = st.columns(2)
with col1: count_chart("type")
with col2: count_chart("type", kind="pie")

st.divider()

# Country-wise analysis
st.header("Country-Wise Content Analysis")
col1, col2 = st.columns(2)
with col1:
    top10 = count_chart("country", top=10, orientation="h")
with col2:
    rest = data["country"].nunique() and (len(data) - top10["count"].sum())
    fig = px.pie(names=["Top 10 Countries", "Remaining Countries"], values=[top10["count"].sum(), rest], hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Trend by release year
st.header("Content Production Trend by Release Year")
yearly = data.groupby("release_year").size().reset_index(name="count")
fig = px.line(yearly, x="release_year", y="count", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Rating distribution
st.header("Rating Distribution")
count_chart("rating")

with st.expander("View Raw Data"):
    st.dataframe(data)