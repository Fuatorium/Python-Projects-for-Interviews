# FuatGPT.05

FuatGPT.05 is a chatbot application that utilizes OpenAI's GPT-3.5-turbo model to provide intelligent and context-aware responses. The project consists of a Flask backend to handle API requests and a React frontend for user interaction.

![FuatGPT.05](https://github.com/Fuatorium/Python-Projects-for-Interviews/blob/main/FuatGPT.05/gpt.png)

## Features

- **Real-time Chat Interface**: Users can chat with the bot in real-time.
- **GPT-3.5-turbo Integration**: Uses OpenAI's powerful language model for generating responses.
- **Flask Backend**: Manages API requests and responses.
- **React Frontend**: Provides an interactive and user-friendly interface.

## Setup

### Requirements

- Python 3.7 or newer
- Node.js and npm
- OpenAI API key

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/fuatorium/Python-Projects-for-Interviews.git
    cd Python-Projects-for-Interviews/FuatGPT.05
    ```

2. Setup the backend:
    - Create a virtual environment and activate it:
        ```sh
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```
    - Install the required packages:
        ```sh
        pip install -r requirements.txt
        ```
    - Create a `.env` file in the backend directory and add your OpenAI API key:
        ```
        OPENAI_API_KEY=your_openai_api_key
        ```
    - Start the Flask server:
        ```sh
        python app.py
        ```

3. Setup the frontend:
    - Navigate to the frontend directory:
        ```sh
        cd frontend
        ```
    - Install the dependencies:
        ```sh
        npm install
        ```
    - Start the React development server:
        ```sh
        npm start
        ```

4. Access the application:
    - Open your browser and go to `http://localhost:3000` to interact with the chatbot.

## Usage

- Type your message in the chat input box and press "Send".
- The bot will respond based on the input message using OpenAI's GPT-3.5-turbo model.

## Project Structure

- **backend**: Contains the Flask server and API logic.
- **frontend**: Contains the React application for the user interface.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
