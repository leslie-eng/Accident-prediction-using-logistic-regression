# Accident Prediction System Using Logistic Regression
## Project Overview
This project builds a machine learning classification model to predict the likelihood of road accidents based on driving and environmental factors. 
Since real-world accident datasets can be incomplete, biased, or inaccessible, this project uses synthetically generated data to simulate realistic accident scenarios. The goal is to demonstrate the end-to-end data science workflow from data generation to model deployment insights.

## Problem Statement
Road accidents are influenced by multiple factors such as:
1) Driver age
2) Weather conditions
3) Vehicle speed
4) Road Type
5) Time of day
6) Driver experience

## Technologies Used
- Python
- Pandas - Data Manipulation
- Numpy - Numerical computations
- Matplotlib - Data visualization
- Scikit-Learn - Machine Learning
- Jupyter Notebook

## Features
- Synthetic accident dataset generation
- Data preprocessing and Clearing
- Exploratory Data Analysis
- Feature selection
- Logistic Regression classification model
- Model evaluation using:
    - Accuracy Score
- Visualiation of insights

## Project Workflow
1) Synthetic Data Generation
- Created artifical dataset simulating real-world accident conditions
- Controlled distributions for variables such as age, speed, weather
- Generated binary target variable
- Addition of the latitude and longitudes of 47 counties.

2) Exploratory Data Analysis
- ![accident count balance](https://github.com/user-attachments/assets/ada745ed-6033-457b-ac1c-343012f7cdd6)
- Distribution of target variable (Accident vs No Accident)
- ![hist of kenyan drivers](https://github.com/user-attachments/assets/c3b446fc-5bed-47ce-a16a-5cfca674e9ff)
- Distribution of Ages of Kenyan drivers
- ![gender vs age](https://github.com/user-attachments/assets/97a4c2a2-a260-4c08-a7d6-e7f29afb0bca)
-
- ![accidents based on demographics](https://github.com/user-attachments/assets/20af9d8f-be64-42d3-8601-f49088bbd3c7)

- ![correlation](https://github.com/user-attachments/assets/bfdf9527-ce27-4925-80fe-d6ca3b1e06fa)

- ![boxplot](https://github.com/user-attachments/assets/892f4770-db2d-48c6-b65e-9539c82091e5)

- ![boxplot years driven](https://github.com/user-attachments/assets/db3700ce-cac7-46ee-9cc2-d8d6491dfd3b)
When drawing the boxplot for accidents based on years driven, the expectation was the lower the experience level the higher the accident count.

3) Data Preprocessing
- Handling categorical variables (Encoding)
- Feature scaling
- Feature removal; leaky features, high and low categorical features
- Train-Test-Split

4) Pivot table
- A pivot table is a bar plot of the sorted values of a particular feature based on the mean. Which road conditions lead to road accidents
 ![pivot table road condition](https://github.com/user-attachments/assets/318ed3de-b065-43bc-9a43-dcbf75f1e884)
Fair to bad roads have a higher chance of causing accidents

- are accidents more prone based on the weather.
![wether pivot table](https://github.com/user-attachments/assets/82f44a68-fb38-43be-be5e-bca3ea50c9a5)
The rainy season bar has a higher count thus indicating it as a major cause of accidents.
- Are accidents more prone based on the sign visibility?
![sign visibility](https://github.com/user-attachments/assets/0832f82f-1b2b-4e6e-99fa-fc64294d6763)

-This is a mapbox of the accident frequency based on the counties
![county mapbox](https://github.com/user-attachments/assets/fce7ed7a-1efa-4e7e-80b8-57d30042b41c)


6) Iterate
- Model builiding through a pipeline. SimpleImputer was used for Nan values and the method was mean. One hot encoder was used for categorical data

7) Model Evaluation
- Accuracy Score: the training accuracy was 70% and the test accuracy was 70% which is fair.

8) Confusion Matrix
![confusion matrix](https://github.com/user-attachments/assets/ba7c2952-2888-436c-8216-25abc84bd41b)
This matrix is a reminder of how imbalanced our data is, and why acccuracy isn't always the best metric for judging whether or not a model is giving us what we want. 90% of all the observations said they had never seen an accident, all the model has to do is always predict accident: False and it will be 90% correct, but this output is dangerous. it never predicts class 1(accident). Accuracy = (TN + Tp)/ Total
= (142+0)/(142+61)
= 70%
the recall for accidents is 0%. This model fails completely at detecting accidents. After noticing this major flaw in the model design, the model was rebalanced and the new confusion matrix is illustrated below:
![after prediction confusion matrix](https://github.com/user-attachments/assets/ced666c5-bc3f-4cb0-9a20-b52d2dba94d0)

![precision recall](https://github.com/user-attachments/assets/a6b08a71-b864-4882-b56d-607144f26b8d)
for accident prediction, accuracy is usually not the metric you care about most. 0.34 is the precision which means the model will give false negatives 0.34% of the time. the recall which is the most important one is 0.54 which means an accident can be flagged as false alarm rather than the previous one which had 0% recall.

8) Communicating Results
Imbalanced data features
![feture importance](https://github.com/user-attachments/assets/b501e29a-e3d5-4705-af20-f379e4d5a359)
Based on the feature importance, rainy season, male riders, and sign visiblity are the top reasons for accidents.

Balanced data features
![updated feature imp](https://github.com/user-attachments/assets/c21006b8-1b75-456d-aa2a-10915fc7c481)


10) Limitations
- Dataset is synthetic(not real-world validated)
- Model performance depends on synthetic assumptions
- Logistic Regression assumes linear relationship between log-odds and features
- The dataset was limited to 1000 observations thus generalization was low.
- Severe class imbalance
- No class weighting
- No resampling
- Threshold fixed at 0.5

10) Future Improvements
- use real-world accident datasets
- integrate real-time accident risk scoring
- Deploy as a web app


Author
Leslie Angu
Data Science | Machine Learning | Predictive Modeling





