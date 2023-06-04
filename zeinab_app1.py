import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('heart stroke data.csv')


# Drop rows with missing values
df = df.dropna()

# Set custom colors
color_female = "#FF69B4"  # Pink
color_male = "#4169E1"    # Blue

# Create a Streamlit app
st.title("Stroke Dataset Dashboard")

# Bar plot for stroke vs. gender
st.subheader("Gender vs. Stroke")
fig_gender = px.bar(df, x='gender', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_gender)

# Box plot for stroke vs. age
st.subheader("Age vs. Stroke")
fig_age = px.box(df, x='stroke', y='age', color='stroke', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_age)

# Bar plot for stroke vs. hypertension
st.subheader("Hypertension vs. Stroke")
fig_hypertension = px.bar(df, x='hypertension', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_hypertension)

# Bar plot for stroke vs. heart disease
st.subheader("Heart Disease vs. Stroke")
fig_heart_disease = px.bar(df, x='heart_disease', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_heart_disease)

# Bar plot for stroke vs. ever married
st.subheader("Marital Status vs. Stroke")
fig_marital_status = px.bar(df, x='ever_married', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_marital_status)

# Bar plot for stroke vs. work type
st.subheader("Work Type vs. Stroke")
fig_work_type = px.bar(df, x='work_type', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
fig_work_type.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig_work_type)

# Bar plot for stroke vs. residence type
st.subheader("Residence Type vs. Stroke")
fig_residence_type = px.bar(df, x='Residence_type', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_residence_type)

# Scatter plot for stroke vs. average glucose level
st.subheader("Average Glucose Level vs. Stroke")
fig_avg_glucose = px.scatter(df, x='avg_glucose_level', y='stroke', color='stroke', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_avg_glucose)

# Scatter plot for stroke vs. BMI
st.subheader("BMI vs. Stroke")
fig_bmi = px.scatter(df, x='bmi', y='stroke', color='stroke', color_discrete_sequence=[color_female, color_male])
st.plotly_chart(fig_bmi)

# Bar plot for stroke vs. smoking status
st.subheader("Smoking Status vs. Stroke")
fig_smoking_status = px.bar(df, x='smoking_status', color='stroke', barmode='group', color_discrete_sequence=[color_female, color_male])
fig_smoking_status.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig_smoking_status)

# Display the dataset as a table
st.subheader("Dataset")
st.dataframe(df)

# Save the Streamlit app
st.button("Save Dashboard")
