# Cancer Type Prediction

This project aims to predict the type of cancer (malignant or benign) using various machine learning models. The dataset used for this project contains features extracted from breast cancer images.

## Table of Contents

- [Installation](#installation)
- [Data](#data)
- [Models](#models)
- [Visualization](#visualization)
- [Results](#results)
- [Usage](#usage)

## Installation

You can install the required libraries using pip:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Data

The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) dataset. It contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. You can download the dataset from the following link:

[Download Breast Cancer Wisconsin (Diagnostic) Dataset](https://www.kaggle.com/datasets/erdemtaha/cancer-data)

## Models

The following models were used in this project:

- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machine
- Naive Bayes
- Decision Tree
- Random Forest
- XGBoost
- AdaBoost

Hyperparameter tuning was performed using GridSearchCV for the SVM, Logistic Regression, and AdaBoost models.

## Visualization

Various visualizations were created to understand the data and model performance:

- Count plot for the distribution of the 'diagnosis' variable
- Box plots and violin plots for each feature grouped by 'diagnosis'
- Heatmap of the correlation matrix

## Results

The performance of each model was evaluated using accuracy, F1-score, precision, recall, and AUC-ROC curve. The best parameters for each model were obtained using GridSearchCV.

## Usage

To run the project, you can use the provided Jupyter notebook `cancer_type_predict.ipynb`.

1. Open the notebook in Jupyter or any compatible environment.
2. Run the cells step by step to see the data preprocessing, model training, evaluation, and visualizations.
