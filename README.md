# Project Description

## Business Objective

Bank XYZ has a growing customer base where the majority of them are liability customers (depositors) vs. borrowers (asset customers). The bank is interested in expanding the borrower’s base rapidly to bring in more business via loan interests.

A campaign that the bank ran in the last quarter showed an average single-digit conversion rate. In the last town hall, the marketing head mentioned that digital transformation is the core strength of the business strategy, and devising effective campaigns with better target marketing is essential to increase the conversion ratio to double-digit with the same budget as the last campaign.

As a data scientist, I was asked to develop a machine learning model to identify potential borrowers to support focused marketing.

## Data Description

The dataset has 2 CSV files:
- **Data1**: 5000 rows and 8 columns
- **Data2**: 5000 rows and 7 columns

## Aim

Build a machine learning model to perform focused digital marketing by predicting the potential customers who will convert from liability customers to asset customers.

## Tech Stack

- **Language**: Python
- **Libraries**: numpy, pandas, matplotlib, seaborn, sklearn, pickle, imblearn

## Approach

### Data Preparation
1. **Importing the required libraries and reading the dataset**
2. **Merging the two datasets**
3. **Understanding the dataset**

### Exploratory Data Analysis (EDA)
1. **Data Visualization**
2. **Feature Engineering**
   - Dropping of unwanted columns
   - Removal of null values
   - Checking for multi-collinearity and removal of highly correlated features

### Model Building
1. **Performing train-test split**
2. **Building various models**:
   - Logistic Regression Model
   - Weighted Logistic Regression Model
   - Naive Bayes Model
   - Support Vector Machine Model
   - Decision Tree Classifier
   - Random Forest Classifier

### Model Validation
1. **Metrics**:
   - Accuracy score
   - Confusion matrix
   - Area Under Curve (AUC)
   - Recall score
   - Precision score
   - F1-score

2. **Handling the unbalanced data using imblearn**
3. **Hyperparameter Tuning (GridSearchCV) for Support Vector Machine Model**

### Final Model
1. **Creating the final model and making predictions**
2. **Saving the model with the highest accuracy in the form of a pickle file**

## MLOps Objective

MLOps is a means of continuous delivery and deployment of a machine learning model. Practicing MLOps means advocating for automation and monitoring at all steps of ML system construction, including integration, testing, releasing, deployment, and infrastructure management.

In this project, we will be deploying the machine learning application for the Build Classification Algorithms for Digital Transformation [Banking]. Hence, it is advised to go through this project first. This project uses Amazon EKS (cloud platform), Amazon EC2, Elastic Load Balancing, and other services. Amazon EKS is a fully managed service that makes it easy to deploy, manage, and scale containerized applications using Kubernetes on AWS.

## Aim

Deploy a machine learning model to identify potential borrower customers to support focused marketing and deploy them through a cloud provider (AWS).

## Tech Stack

- **Language**: Python
- **Services**: AWS EKS, ECR, Load Balancer, Code Commit, Code Deploy, Code Pipeline

## Prerequisites

It is advisable to have a basic knowledge of the following services to understand the project:

- Flask
- AWS ECR
- AWS ECS
- AWS EC2 Load Balancer
- AWS Code Commit
- AWS Code Build
- AWS Code Deploy
- AWS Code Pipeline

## Approach

### Cluster Creation Steps
1. Create an EKS cluster master node.
2. Create Node groups in the EKS cluster.
3. Create OIDC connection in the AWS Identity provider with EKS
