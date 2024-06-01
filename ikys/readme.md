# Human Resources Management System (HRMS)

The Human Resources Management System (HRMS) is a web application designed to facilitate the management, tracking, and evaluation of employees and candidates. This application is built using the Flask framework and operates with an SQLite database.

## Features

- Add, update, delete, and list employees
- Add, update, delete, and list candidates
- Employee performance evaluation
- Manage candidate interview dates
- User-friendly interface

## Installation

### Requirements

- Python 3.8 or higher
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-RESTful

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Fuatorium/Python-Projects-for-Interviews/ikys.git
    cd ikys
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv ikys-env
    # Windows
    ikys-env\Scripts\activate
    # macOS/Linux
    source ikys-env/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    python run.py
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:5000`.



## API Endpoints

### Employees

- **GET /employees**
  - Description: Retrieve a list of all employees.
  - Response: JSON array of employee objects.

- **POST /employees**
  - Description: Add a new employee.
  - Request Body: JSON object with `name`, `position`, `salary`, and optional `performance_score`.
  - Response: JSON message indicating success.

- **GET /employees/<int:id>**
  - Description: Retrieve a specific employee by ID.
  - Response: JSON object of the employee.

- **PUT /employees/<int:id>**
  - Description: Update a specific employee by ID.
  - Request Body: JSON object with `name`, `position`, `salary`, and optional `performance_score`.
  - Response: JSON message indicating success.

- **DELETE /employees/<int:id>**
  - Description: Delete a specific employee by ID.
  - Response: JSON message indicating success.

### Candidates

- **GET /candidates**
  - Description: Retrieve a list of all candidates.
  - Response: JSON array of candidate objects.

- **POST /candidates**
  - Description: Add a new candidate.
  - Request Body: JSON object with `name`, `position_applied`, and optional `interview_date` (YYYY-MM-DD format).
  - Response: JSON message indicating success.

- **GET /candidates/<int:id>**
  - Description: Retrieve a specific candidate by ID.
  - Response: JSON object of the candidate.

- **PUT /candidates/<int:id>**
  - Description: Update a specific candidate by ID.
  - Request Body: JSON object with `name`, `position_applied`, and optional `interview_date` (YYYY-MM-DD format).
  - Response: JSON message indicating success.

- **DELETE /candidates/<int:id>**
  - Description: Delete a specific candidate by ID.
  - Response: JSON message indicating success.

  ## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests


