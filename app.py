from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

import os
import streamlit as st
import sqlite3
import pandas as pd
import google.generativeai as genai



# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model and return SQL query as a string
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    # Strip any markdown formatting (like ```sql) if present
    cleaned_response = response.text.strip().strip("`").replace("sql", "").strip()
    return cleaned_response

# Run the generated SQL query on the SQLite database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.OperationalError as e:
        rows = [(f"SQL Error: {e}",)]
    finally:
        connection.close()
    return rows

# Prompt to guide Gemini to return only SQL code
prompt = ["""
You are an expert in converting English questions to SQL queries.
The SQL database is named STUDENT and has the following columns: NAME, CLASS, SECTION, and MARKS.

Examples:
1. Question: How many entries of records are present?
   SQL: SELECT COUNT(*) FROM STUDENT;

2. Question: Tell me all the students studying in Data Science class?
   SQL: SELECT * FROM STUDENT WHERE CLASS='Data Science';

Respond ONLY with the SQL query (no explanations, no ```sql or quotes).
"""]

# Streamlit UI setup
st.set_page_config(page_title="Gemini SQL Query Generator")
st.title("🧠 Gemini SQL Query Generator")

# User input
question = st.text_input("Enter your question in plain English:", key="input")
submit = st.button("Generate and Execute SQL")

# If the button is clicked
if submit and question:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(response, language="sql")

    data = read_sql_query(response, "student.db")

    st.subheader("Query Result:")
    if data:
        if isinstance(data[0], tuple):
            if len(data[0]) == 1:
            # One-column result, display each in bold
                for row in data:
                    st.markdown(f"**{row[0]}**")
            else:
            # Multi-column result, display as table
                df = pd.DataFrame(data)
                st.dataframe(df)
        else:
            for row in data:
                st.write(row)
    else:
        st.write("No data returned.")

