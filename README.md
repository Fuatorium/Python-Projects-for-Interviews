# Python Projects for Interviews

This repository contains various Python projects that can be used in job interviews. Each project targets a specific problem area and provides solutions. Below are brief descriptions of the projects and information on how to access each one.

## Contents

- [AutoDataAnalyzer](#autodataanalyzer)
- [FinancePredictor](#financepredictor)
- [Smart Surveillance System](#smart-surveillance-system)
- [FuatGPT.05](#fuatgpt05)
- [Customer Segmentation](#customer-segmentation)
- [Human Resources Management System (HRMS)](#human-resources-management-system-hrms)

## AutoDataAnalyzer

The AutoDataAnalyzer project performs automatic data analysis, quickly summarizing and visualizing datasets. This project provides great convenience for data scientists and analysts.

- **Features**:
  - Automatic analysis of datasets
  - Visualization and summarization
  - Easy-to-use interface

For more information, check the [AutoDataAnalyzer README file](./AutoDataAnalyzer/README.md).

## FinancePredictor

The FinancePredictor project uses a machine learning model to predict future prices of cryptocurrencies like Bitcoin. The project is based on time series analysis.

- **Features**:
  - Fetching and preprocessing historical cryptocurrency price data
  - Predicting prices using an LSTM model
  - Visualizing prediction results
  - Calculating model performance metrics

For more information, check the [FinancePredictor README file](./FinancePredictor/README.md).

## Smart Surveillance System

The Smart Surveillance System project performs real-time video stream analysis, including human face recognition, object recognition, and behavior analysis.

- **Features**:
  - Real-time video stream analysis
  - Human face recognition
  - Object recognition
  - Behavior analysis

For more information, check the [Smart Surveillance System README file](./Smart%20Surveillance%20System/README.md).

## FuatGPT.05

The FuatGPT.05 project is a chatbot application using OpenAI's GPT-3.5-turbo model.

- **Features**:
  - Real-time chat interface
  - Integration with OpenAI's GPT-3.5-turbo model
  - Flask backend to handle API requests
  - React frontend for user interaction

For more information, check the [FuatGPT.05 README file](./FuatGPT.05/README.md).

## Customer Segmentation

The Customer Segmentation project uses machine learning to categorize customers into different segments based on their demographic and behavioral data.

- **Features**:
  - Analyzing customer data
  - Categorizing customers into segments
  - Providing segment descriptions
  - Visualizing segment characteristics

For more information, check the [Customer Segmentation README file](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/customer-segmentation/readme.md).

## Human Resources Management System (HRMS)

The Human Resources Management System (HRMS) is a web application designed to facilitate the management, tracking, and evaluation of employees and candidates. This application is built using the Flask framework and operates with an SQLite database.

- **Features**:
  - Add, update, delete, and list employees
  - Add, update, delete, and list candidates
  - Employee performance evaluation
  - Manage candidate interview dates
  - User-friendly interface

For more information, check the [HRMS README file](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/HRMS/README.md).

## Setup

### Requirements

- Python 3.7 or newer
- Anaconda (recommended)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/fuatorium/Python-Projects-for-Interviews.git
    cd Python-Projects-for-Interviews
    ```

2. Install dependencies for each project. For example, for `FinancePredictor`:
    ```sh
    cd FinancePredictor
    conda create --name finance-prediction-env python=3.8
    conda activate finance-prediction-env
    pip install -r requirements.txt
    ```

## Contributing

If you would like to contribute, please open a pull request or create an issue. Your contributions will help improve the project.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
