# T20 Cricket Final Score Prediction

## Overview
This project aims to predict the final score in T20 cricket matches using various machine learning techniques. It involves data preprocessing, feature engineering, model training, and evaluation. The project is structured to provide clear insights and reliable predictions based on the given dataset.

## Key Features
- **Data Preprocessing**: Cleans and prepares the raw dataset for analysis.
- **Feature Engineering**: Generates meaningful features such as current score, overs left, wickets in hand, and run rate.
- **Model Training**: Implements multiple regression models to predict the final score.
- **Evaluation**: Compares model performance using metrics like Mean Absolute Error (MAE) and R-squared.

## Project Flow 
1. **Introduction**
   - Objective and project description.

2. **Data Loading and Preprocessing**
   - Reads the dataset.
   - Handles missing values and data cleaning.

3. **Exploratory Data Analysis (EDA)**
   - Analyzes patterns, correlations, and distributions in the data.

4. **Feature Engineering**
   - Constructs relevant features such as overs remaining and wickets.

5. **Model Building**
   - Splits the dataset into training and testing sets.
   - Trains regression models, including Linear Regression, Decision Tree, and Random Forest.

6. **Model Evaluation**
   - Evaluates models using performance metrics.
   - Visualizes results for better interpretability.

7. **Conclusion**
   - Summarizes findings and highlights the best-performing model.

## How to Use
1. **Environment Setup**: Ensure you have Python installed along with required libraries such as Pandas, Scikit-learn, and Matplotlib.
2. **Run the Notebook**: Execute each cell in sequence to reproduce the results.
3. **Modify the Data**: Replace the dataset with your own data to make predictions on new matches.

## Dependencies
- Python 3.7+
- gradio
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
  
## Results
- The project  identifies the most effective regression model for predicting T20 match scores based on various metrics.
- This project was developed for predictive analytics in sports, specifically focusing on T20 cricket matches.
## Dataset 
[Dataset Link](https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket)

## Interface Demo
Demo of the interface for predicting score of a ongoing T20 match.
<img width="938" alt="Screenshot 2025-01-20 033303" src="https://github.com/user-attachments/assets/a2bb48f7-5d74-4e9f-96e7-d6152cd7b92b" />
