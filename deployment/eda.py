import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    # Set title
    st.title('Exploratory Data Analysis')

    # Load data
    df = pd.read_csv('bank.csv',sep=';')

    # Display descriptive statistics of the dataframe
    sns.set_theme(style="whitegrid")

# Membuat histogram menggunakan Seaborn
    plt.hist(df['age'], bins=20, color='skyblue')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribusi Umur')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Visualisasi 2: Balance dan hubungannya dengan umur
    st.header('Scatterplot: Balance vs Age with Default Status')
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='age', y='balance', hue='default', data=df, palette='coolwarm')
    plt.xlabel('Age')
    plt.ylabel('Balance')
    plt.title('Balance dan hubungannya dengan umur')
    plt.legend(title='Default')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Visualisasi 3: Marital Status Distribution
    st.header('Pie Chart Marital Status')
    marital_counts = df['marital'].value_counts()
    plt.pie(marital_counts, labels=marital_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'lightblue', 'lightcoral'])
    plt.title('Marital Status Distribution')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Visualisasi 4: Education Distribution
    st.header('Bar chart Education Level')
    education_counts = df['education'].value_counts()
    plt.bar(education_counts.index, education_counts.values, color='salmon')
    plt.xlabel('Education Level')
    plt.ylabel('Count')
    plt.title('Education Level Distribution')
    plt.xticks(rotation=45)
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
    app()
