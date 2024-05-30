# Python Projects for Interviews

This repository contains various Python projects that can be used in job interviews. Each project targets a specific problem area and provides solutions. Below are brief descriptions of the projects and information on how to access each one.

## Contents

- [AutoDataAnalyzer](#autodataanalyzer)
- [FinancePredictor](#financepredictor)

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
