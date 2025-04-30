
# 📄 ATS Tracking System

ATS Tracking System is a Streamlit-based web application that leverages Google’s Gemini AI to analyze resumes against job descriptions. It simulates how an Applicant Tracking System (ATS) evaluates resumes, helping candidates understand their match score, identify missing keywords, and receive suggestions to improve their chances of passing automated resume screenings.




## 🚀 Features
- 📄 Resume Upload: Upload a PDF resume.

- 📌 Job Description Input: Paste the job description you’re targeting.

- 🧑‍💼 Professional Review: Get a detailed review of how your resume aligns with the job.

- 📊 Percentage Match: Understand how well your resume matches the job using ATS logic.

- 🧠 Gemini AI Integration: Powered by Google’s Generative AI (Gemini 1.5 Flash).




## 🛠️ Tech Stack

- **Python** 3.10

- Streamlit

- `pdf2image` for converting PDFs to images

- `Pillow (PIL)` for image processing

- `dotenv` for environment variable management

- Google Generative AI SDK (`google.generativeai`)


## 📦 Installation

1. 📥 Clone the Repository
Clone the GitHub repository to your local system to get the source code.

```sh
git clone https://github.com/kjoseshalu/Calories-Insight.git
cd Calories-Insight

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

![App Screenshot](https://github.com/kjoseshalu/gemini-ats-tracker/blob/main/output/output-screenshot-1.jpg)

![App Screenshot](https://github.com/kjoseshalu/gemini-ats-tracker/blob/main/output/output-screenshot-2.jpg)
