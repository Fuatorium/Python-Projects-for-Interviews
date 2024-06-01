# Customer Segmentation

This project uses machine learning to categorize customers into different segments based on their demographic and behavioral data. The goal is to better understand the customer base and tailor marketing strategies accordingly.

## Features

- **Analyzing customer data:** Extract insights from customer data to understand different segments.
- **Categorizing customers into segments:** Use KMeans clustering to divide customers into meaningful segments.
- **Providing segment descriptions:** Offer detailed descriptions for each segment to help with targeted marketing.
- **Visualizing segment characteristics:** Graphically represent the average characteristics of each segment.

## Overview

Customer segmentation is a crucial aspect of marketing and business strategy. By understanding the different segments within a customer base, businesses can create more effective marketing campaigns, improve customer satisfaction, and increase profitability.

## Project Structure

- `models/`: Contains the trained models and encoders.
  - `model.py`: Script to train the KMeans model and save the encoders.
  - `kmeans_model.pkl`: Trained KMeans model.
  - `scaler.pkl`: StandardScaler used for feature scaling.
  - `gender_encoder.pkl`: LabelEncoder for gender data.
  - `profession_encoder.pkl`: LabelEncoder for profession data.
  - `segment_descriptions.pkl`: Descriptions of each segment.
- `static/`: Contains static files such as CSS and images.
  - `styles.css`: Stylesheet for the web application.
  - `segment_means.png`: Visualization of the average characteristics of each segment.
- `templates/`: Contains HTML templates for the web application.
  - `index.html`: Main page to input customer data and get the segment prediction.
  - `segments.html`: Page to display segment descriptions and visualizations.
- `app.py`: Flask application to serve the web interface and handle API requests.

## Setup

### Requirements

- Python 3.7 or newer
- Anaconda (recommended)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/Fuatorium/Python-Projects-for-Interviews.git
    cd Python-Projects-for-Interviews/customer-segmentation
    ```

2. Install dependencies:
    ```sh
    conda create --name customer-segmentation-env python=3.8
    conda activate customer-segmentation-env
    pip install -r requirements.txt
    ```

3. Train the model and generate segment descriptions:
    ```sh
    python models/model.py
    ```

4. Start the Flask application:
    ```sh
    python app.py
    ```

## Usage

### Web Interface

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter customer data such as age, gender, annual income, spending score, profession, work experience, and family size.
3. Click "Tahmin Et" to get the segment prediction and description.

![Web Interface](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/customer-segmentation/get.png)

### Segment Descriptions and Visualizations

1. Navigate to `http://127.0.0.1:5000/segments` to view detailed descriptions of each segment and visualize their average characteristics.

![Segment Analysis](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/customer-segmentation/gat.png)

## Detailed Explanation

### Data Processing

- **Categorical Data Encoding:** Gender and profession data are encoded using `LabelEncoder`.
- **Feature Scaling:** All features are scaled using `StandardScaler` to ensure that they contribute equally to the clustering process.

### Model Training

- **Clustering Algorithm:** The KMeans algorithm is used to cluster customers into 5 segments based on their demographic and behavioral data.
- **Segment Descriptions:** After clustering, the average characteristics of each segment are calculated to provide meaningful descriptions.

### Visualization

- **Segment Characteristics:** The average characteristics of each segment are visualized using bar plots to help understand the differences between segments.

## Contributing

If you would like to contribute, please open a pull request or create an issue. Your contributions will help improve the project.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
