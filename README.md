
# Gemini SQL Query Generator

The Gemini SQL Query Generator is a web application that leverages Google's Gemini Pro model to convert natural language questions into SQL queries. Built with Streamlit for the frontend and SQLite for the database, this tool simplifies data retrieval by allowing users to interact with databases using plain English.




## 🚀 Features
- Natural Language to SQL: Transform plain English questions into SQL queries using Google's Gemini Pro model.

- Database Interaction: Execute generated SQL queries on a SQLite database and display results.

- User-Friendly Interface: Interact with the application through an intuitive Streamlit web interface.




## 🛠️ Tech Stack

- **Python** 3.10

- Streamlit: Framework for building the web interface.

- SQLite: Lightweight database for storing and retrieving data.

- Google Gemini Pro: AI model for natural language processing and SQL generation


## 📁 Project Structure
```
Gemini-SQL-Query-Generator/
├── app.py             # Main application file
├── sql.py             # Database setup and utility functions
├── student.db         # SQLite database file
├── requirements.txt   # Python dependencies
├── .env               # Environment variables
└── README.md          # Project documentation

```


## 📦 Installation

1. 📥 Clone the Repository
Clone the GitHub repository to your local system to get the source code.

```sh
git clone https://github.com/kjoseshalu/Gemini-SQL-Query-Generator.git
cd Gemini-SQL-Query-Generator


```

This command copies the repository files to your machine and changes the current directory to the project folder.

2. 🐍 Create a Virtual Environment

Create an isolated Python environment using conda to manage dependencies easily.
```sh
conda create -p venv python=3.10 -y
```
-p venv creates a virtual environment in a folder named venv.
python=3.10 specifies the Python version.
-y auto-confirms the environment creation.

3. ⚡ Activate the Virtual Environment

Activate the environment you just created.
```sh
conda activate venv/
```
This ensures all the packages are installed and run within the isolated environment.

4. 📦 Install Required Dependencies
Install all the Python libraries specified in requirements.txt.
```sh
pip install -r requirements.txt
```
This step is crucial to ensure the app runs without missing any dependencies.

5. 🔐 Create a .env File
Create a .env file in the root directory of your project and add your Google API Key.
```sh
GOOGLE_API_KEY=your-api-key

```
This file is used to securely store sensitive credentials.
🔑 You need a valid API key from [Google AI Studio](https://makersuite.google.com/) .

✅ Model Selection: gemini-1.5-flash

This model is chosen for:

- Fast response time

- Low latency

- Adequate performance for resume analysis and job matching

6. 🚀 Run the Streamlit App
Start the application using Streamlit.

```sh
streamlit run app.py
```
7. 🌐 Open the App in Your Browser
Open the following URL in your browser:
```sh
http://localhost:8501
```
This is the default address where Streamlit apps run locally.

    
## Output

![App Screenshot](https://github.com/kjoseshalu/Gemini-SQL-Query-Generator/blob/main/Output/Screenshot-1.png)

![App Screenshot](https://github.com/kjoseshalu/Gemini-SQL-Query-Generator/blob/main/Output/screenshot-2.png)

![App Screenshot](https://github.com/kjoseshalu/Gemini-SQL-Query-Generator/blob/main/Output/screenshot-3.png)
