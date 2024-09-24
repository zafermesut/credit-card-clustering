# Credit Card Clustering 💳

This project aims to segment credit card users based on their financial behaviors, such as purchasing habits, credit limits, and other relevant factors. Credit card clustering, also known as credit card segmentation, helps businesses understand customer behavior, enabling more targeted marketing strategies and better customer service.

## Overview

Using Machine Learning techniques, we perform clustering analysis to group credit card holders into different categories. This helps businesses to:

- Identify potential customer segments.
- Tailor marketing strategies accordingly.
- Improve customer targeting for services like credit limits, rewards programs, etc.

For this project, we use a dataset that contains the buying history and financial data of credit card holders. The dataset includes various features that are essential for analyzing and clustering the customers.

## Dataset

The dataset used for this project contains the following features:

- **CUST_ID**: Unique identification number of the customer
- **BALANCE**: Balance in the customer's bank account
- **BALANCE_FREQUENCY**: Frequency at which the balance is updated (1: frequently, 0: rarely)
- **PURCHASES**: Total purchases made by the customer
- **ONEOFF_PURCHASES**: Maximum amount of one-time purchase
- **INSTALLMENTS_PURCHASES**: Amount spent on installment purchases
- **CASH_ADVANCE**: Cash advances taken by the customer
- **PURCHASES_FREQUENCY**: Frequency of purchases (1: high, 0: low)
- **ONEOFF_PURCHASES_FREQUENCY**: Frequency of one-time purchases (1: high, 0: low)
- **PURCHASES_INSTALLMENTS_FREQUENCY**: Frequency of installment purchases (1: high, 0: low)
- **CASH_ADVANCE_FREQUENCY**: Frequency of cash advances
- **CASH_ADVANCE_TRX**: Number of cash advance transactions
- **PURCHASES_TRX**: Number of purchase transactions
- **CREDIT_LIMIT**: Customer's credit limit
- **PAYMENTS**: Total amount of payments made by the customer
- **MINIMUM_PAYMENTS**: Minimum payments made by the customer
- **PRC_FULL_PAYMENT**: Percentage of full payments made by the customer
- **TENURE**: Duration of the customer's credit card usage

## Project Workflow

1. **Data Preprocessing**:

   - Handle missing values.
   - Normalize and scale the features.

2. **Clustering**:

   - Apply clustering algorithms such as K-Means to group customers based on similar financial behaviors.

3. **Evaluation**:
   - Analyze the clusters and interpret customer segments.

## Deployment on Hugging Face Spaces

This project is also deployed as an interactive application on Hugging Face Spaces. You can try it out here:

[Credit Card Clustering - Hugging Face Space](https://huggingface.co/spaces/zafermbilen/credit-card-clustering)

The deployment provides an easy-to-use interface where you can upload data and visualize the clustering results.

## Results

After applying clustering, customers are grouped into distinct segments based on their behavior. Each cluster represents a group of customers with similar patterns, such as:

- **High spenders** who prefer installment payments.
- **Low spenders** with infrequent transactions.
- **Customers heavily reliant on cash advances**.

By understanding these clusters, businesses can make more informed decisions about offering credit, targeting rewards programs, or launching specific marketing campaigns.
