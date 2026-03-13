# Telecom Customer Churn Prediction and Analysis

## Live Deployment
[Click here to view the deployed app](https://huggingface.co/spaces/Rhythm22/Telecom_Customer_Churn_Prediction)

---

# Project Overview

This project aims to combat customer churn in the telecom industry by developing a robust machine learning model integrated into a real-time dashboard. Our solution empowers telecom companies to predict customer churn and implement proactive retention strategies, ultimately enhancing customer satisfaction and reducing churn rates.

---

# Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results and Insights](#results-and-insights)
- [Future Scope](#future-scope)
- [Contributors](#contributors)


# Introduction

Customer churn is a significant challenge in the telecom industry. This project focuses on predicting churn using machine learning models and visualizing the results through an interactive dashboard.

By identifying customers likely to churn, telecom companies can take targeted actions to retain them and improve overall customer satisfaction.

The system combines **data analysis, predictive modeling, and a real-time prediction web application** to provide a complete churn prediction solution.

---

# Features

### Data Analysis
Exploratory Data Analysis (EDA) was performed on a dataset of more than **7000 telecom customers** to uncover patterns, correlations, and key insights related to customer churn.

### Predictive Modeling
Machine learning models were developed using **Decision Tree and Random Forest algorithms** to predict whether a customer is likely to churn.

### Real-time Prediction
A **Flask-based web application** was developed where users can input customer data and instantly receive churn predictions.

### Interactive Dashboard
A **Power BI dashboard** was created to visualize key performance indicators and customer behavior, making it easier for telecom companies to understand churn patterns.

---

# Tech Stack

### Languages
Python  
SQL  

### Libraries
pandas  
numpy  
matplotlib  
seaborn  
scikit-learn  

### Framework
Flask  

### Tools
Power BI  

### Deployment
Hugging Face Spaces

---

# Installation

### Clone the repository
git clone https://github.com/Rhythm22Sharma/MLProject-ChurnPrediction.git


### Navigate to the project directory
cd MLProject-ChurnPrediction


### Install the required libraries
pip install -r requirements.txt


---

# Usage

### Run the Flask Application

### Access the Web Application

Open your browser and go to:http://127.0.0.1:5000/



Enter customer details in the web interface and the system will predict whether the customer is likely to churn.

### Explore the Power BI Dashboard

Open the **Power BI dashboard file** to visualize churn analysis, customer behavior, and key performance indicators.

---

# Methodology

## Data Collection and Cleaning

A telecom customer dataset containing **7000+ records and 21 features** was used for this project.

Data preprocessing steps included:

- Handling missing values
- Converting categorical variables
- Data cleaning and formatting
- Removing unnecessary columns
- Preparing the dataset for machine learning models

Python libraries used for analysis include:

- pandas
- numpy
- matplotlib
- seaborn

---

## Model Development

Machine learning models were built using **scikit-learn**.

Algorithms used:

- Decision Tree Classifier
- Random Forest Classifier

The models were trained to classify customers into two categories:

- Customers who will churn
- Customers who will stay

Model performance was evaluated using classification metrics.

---

## Deployment

The trained model was deployed using a **Flask web application**.

The workflow of the system is:

User Input → Data Processing → Model Prediction → Result Display

Users can enter customer details and the application predicts the likelihood of churn.

The application is also deployed online using **Hugging Face Spaces** for public access.

---

# Results and Insights

### Churn Prediction Efficiency

The automated churn prediction system helps telecom companies quickly identify customers at risk of leaving.

### Key Factors Identified

Through analysis, several important churn factors were identified:

- Contract type
- Monthly charges
- Internet service type
- Customer tenure

### Business Impact

The system enables telecom companies to take proactive retention actions and reduce churn rates through data-driven strategies.

---

# Future Scope

### Expansion to Other Industries

The churn prediction system can be adapted for other industries such as:

- Banking
- Subscription services
- E-commerce platforms

### Automation

Future improvements can automate the entire pipeline including:

- Data extraction
- Model retraining
- Dashboard updates

### Advanced Features

Additional enhancements may include:

- Integration with Apache Airflow for automated workflows
- Cloud deployment for scalability
- Advanced machine learning models like XGBoost
- Real-time customer retention alerts

---

# Contributors

Rhythm Sharma  
Mehul Sagotia  
Vinal Jain  



