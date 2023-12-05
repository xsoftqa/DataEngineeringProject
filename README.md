# Predicting Future Rice, Wheat, and Corn Prices and Visualizing the Predictions
Rice, Wheat and Corn Prices Changes Taking into Account Inflation

<img width="492" alt="image" src="https://github.com/xsoftqa/DataEngineeringProject/assets/69432871/50eae896-405a-4d10-81a0-bf29958df0f9">



A data pipeline with Batch Ingestion, Extract, Load, Amazon s3 Bucket, Docker, Airflow, Pandas, Amazon AWS and much more!

**Description**

The project will address these questions by utilizing historical cereal price data and leveraging a data engineering pipeline that encompasses data preprocessing, machine learning, and visualization components. The results will be presented in an easily interpretable graphical format, allowing users to gain insights into future price trends for these essential agricultural commodities

**Objective**

The objective of this data engineering project is to develop a predictive model for the future prices of rice, wheat, and corn, and to visualize these predictions. The project aims to address the following key questions:

1. What are the future price trends for rice, wheat, and corn based on historical data?
2. Can we identify patterns and factors that influence the prices of these cereals?
3. How can we effectively visualize and communicate the price predictions for stakeholders?

**Dataset**

The project was started by an author, who not long time ago formed a dataset titled ☕Coffee, Rice and Beef Prices Changes for 30 Years and it inspired my to look for some more interesting data that would be rather curious to visualize, and I found… Below you can find some more information concerning formed dataset. If you are not sure about any data, you can check my sources in dataset details.

**Tools & Technologies**

1. Cloud - Amazon Cloud Platform
2. Containerization - Docker, Docker Compose
3. Batch Processing - Batch Ingestion, Extract, Load
4. Orchestration - Airflow
5. Transformation - Pandas
6. Data Lake - s3 Bucket Storage
7. Data Warehouse - s3 Bucket Storage
8. Data Visualization - Tableau was the intended visualization tool
9. Language - Python

**Architecture**

![image](https://github.com/xsoftqa/DataEngineeringProject/assets/69432871/6314bba3-4b24-48e3-b57f-81f6e46e8bd0)

**Data Quality Assessment:**

    **Data Overview:**
        
        We check for missing values, duplicate records, and outliers.

    S**tatistical Analysis:**
        
        Intension was to perform basic statistical analyses (mean, median, standard deviation) on relevant columns to identify trends and potential issues.

    D**ata Visualization:**
        
        The intension was to create visualizations (e.g., histograms, box plots) to understand the distribution of key variables.

    **Correlation Analysis:**
        
        Explore correlations between variables to identify relationships.

   **Domain Knowledge:**
        
        Leverage any domain knowledge to identify anomalies or unexpected patterns.


**Data Transformation Models used:**

    **Pre-processing:**
        Address missing values and outliers appropriately.
        Convert categorical variables to numerical format (one-hot encoding, label encoding).
        Normalize or scale numerical features if necessary.

    **Feature Engineering:**
        Create new features that might enhance model performance.

    **Model Selection:**
        Choose appropriate models for the task (regression, time series analysis, etc.).

**Final Result**

Since the RDS was unavailable to complete the final results, going forward one can use local database and use Tableau to generate the final results using the clean data from the batch processing.

**Model Evaluation:**
        
        Evaluate the performance of your models using relevant metrics (RMSE for regression, accuracy for classification, etc.).

**Documentation:**
        
        Clearly document the entire process, including data cleaning, transformations, and model training.


**Pipeline Steps:**

**Data Collection:** We will download the dataset from Kaggle website, which includes running batch ingestion script, extracting and loading of the datasets, ensuring that it covers the historical prices of rice, wheat, and corn for the past 30 years. This dataset contains valuable information regarding the prices of these cereals over time

**Data Preprocessing:** We will clean and preprocess the dataset to handle any missing values, outliers, or inconsistencies. This step will involve data wrangling to make the dataset suitable for machine learning.

**Machine Learning Model:** We will train a machine learning model, such as a time series forecasting model, to predict future prices of rice, wheat, and corn. We will use tools and libraries like scikit-learn and TensorFlow for this purpose.

**Visualization:** The predictions will be visualized using data visualization libraries like Matplotlib or Seaborn. Line plots, bar charts, or other relevant graphical representations will be created to effectively communicate the future price trends.

P**ush Transformed Data Back to s3 Bucket:**
After the data has been transformed and the predictions have made, we will push the transformed data as a pickle file, including the predictions, to the s3 bucket. This allows for easy access to the processed data and results for future reference.

Final Results:

    
Infographics:

    Data Pipeline Architecture:
        
        Illustrate the flow of data from source to final model, including tools and storage used.

    Results Infographic:
        Present key metrics and insights derived from the analysis and modeling process.

Code:

Provide a link to your GitHub repository containing:

    Jupyter notebooks or scripts detailing data cleaning, transformation, and modeling steps.
    README file explaining the repository structure and usage.



