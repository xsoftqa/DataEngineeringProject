# Owner: Abdul Majid Tahir-Akinyele

# Prepared by: Abdul Majid Tahir-Akinyele, Student - 9053-36819

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
        
        We choose appropriate models for the task (regression, time series analysis, etc.).

**Final Result**

Since the RDS was unavailable to complete the final results, going forward one can use local database and use Tableau to generate the final results using the clean data from the batch processing.

The expected final result of this project should have been a predictive model that can forecast future prices of rice, wheat, and corn based on historical data. This model will be capable of generating predictions for a specified time frame into the future. Additionally, the project will produce visualizations of these predictions, allowing stakeholders to understand and interpret the trends easily.

**Model Evaluation:**
        
        Evaluated the performance of the models using relevant metrics (RMSE for regression, accuracy for classification, etc.).

**Documentation:**
        
        Clearly document the entire process, including data cleaning, transformations, and model training.


**Pipeline Steps:**

**Data Collection:** We will download the dataset from Kaggle website, which includes running batch ingestion script, extracting and loading of the datasets, ensuring that it covers the historical prices of rice, wheat, and corn for the past 30 years. This dataset contains valuable information regarding the prices of these cereals over time

**Data Preprocessing:** We will clean and preprocess the dataset to handle any missing values, outliers, or inconsistencies. This step will involve data wrangling to make the dataset suitable for machine learning.

**Machine Learning Model:** We will train a machine learning model, such as a time series forecasting model, to predict future prices of rice, wheat, and corn. We will use tools and libraries like scikit-learn and TensorFlow for this purpose.

**Visualization:** The predictions will be visualized using data visualization libraries like Matplotlib or Seaborn. Line plots, bar charts, or other relevant graphical representations will be created to effectively communicate the future price trends.

P**ush Transformed Data Back to s3 Bucket:**
After the data has been transformed and the predictions have made, we will push the transformed data as a pickle file, including the predictions, to the s3 bucket. This allows for easy access to the processed data and results for future reference.

Infographics:

    Data Pipeline Architecture:
        
        Tools, Technologies and Architecture section above illustrates the flow of data from source to final model, including tools and storage used.

    Results Infographic:
        
        Intension was to present key metrics and insights derived from the analysis and modeling process.

Thorough Investigation:

 1	Viability Assessment:
 
	◦	Conclusions: Assess the feasibility of scaling the project by evaluating the computational resources, data volume, and model complexity. If the current solution proves scalable, this is a positive outcome. If not, identify
 
 potential bottlenecks and challenges.
 
	◦	Recommendations: If scalability is an issue, consider distributed computing solutions, cloud platforms, or optimizations in the data pipeline. Provide specific recommendations for infrastructure upgrades or changes.
	
 2	Innovativeness:
 
	◦	Assessment: Reflect on the innovative aspects of the project. Did you introduce novel methodologies, unique features, or approaches? Consider how this work compares to existing solutions in the field.
	◦	Recommendations: If the project demonstrates high innovativeness, emphasize the unique aspects in the recommendation. If there's room for improvement, suggest areas where additional innovation can be injected, possibly    through advanced algorithms, novel data sources, or integration with emerging technologies.
 
 3	Technical and Platform Concerns:
 
	◦	Identify Concerns: Discuss any technical challenges or platform-specific concerns encountered during the project. This could include issues related to data compatibility, processing speed, or model deployment.
	◦	Mitigation Strategies: Propose mitigation strategies for each concern. This might involve adopting different tools, refining data preprocessing steps, or exploring alternative platforms.
	
 4 Difficulties and Limitations:
 
	◦	Technical Limitations: Acknowledge any limitations in the model's performance, such as challenges in predicting certain patterns or limitations in handling specific data types.
	◦	Platform Limitations: Discuss limitations related to the chosen platform, including any constraints in terms of data storage, processing speed, or scalability.
	◦	Next Steps for Improvement: Outline steps to address these difficulties and limitations, including potential research directions or areas for further development.
	
 5	Next Steps for Scaling:

 
	◦	Optimization Opportunities: Highlight potential areas for optimization in the existing pipeline. This might involve algorithmic improvements, parallel processing, or more efficient data storage solutions.
	◦	Scalability Enhancements: Propose specific steps for enhancing scalability, such as transitioning to a cloud-based infrastructure, adopting parallel processing techniques, or leveraging distributed computing frameworks.
	◦	Continuous Monitoring: Recommend the implementation of monitoring systems to track the performance of the scaled-up solution. This ensures that any issues can be identified and addressed promptly.

In summary, the Thorough Investigation should provide a holistic view of the project's viability, innovativeness, technical concerns, and a roadmap for scaling. It should equip technical leadership with actionable recommendations for refining and expanding the project.
