# AI Data Assistant

An AI-powered data cleaning and analysis chatbot built with Python and Streamlit.
This application allows users to upload datasets, automatically clean the data, and ask questions about it using an AI language model.

## Features

* Upload CSV or Excel datasets
* Automatic data cleaning
* Cleaning report generation
* Download cleaned dataset
* AI chatbot to answer questions about data
* Interactive web interface

## Tech Stack

* Python
* Streamlit
* Pandas
* LangChain
* OpenRouter API

## Project Structure

ai-data-assistant/
│
├── app.py
├── data_cleaner.py
├── llm_helper.py
├── requirements.txt
├── .gitignore
└── README.md

## Installation

Clone the repository

git clone https://github.com/yourusername/ai-data-assistant.git

Navigate to the project folder

cd ai-data-assistant

Create virtual environment

python -m venv venv

Activate environment

Windows
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the root folder and add your API key:

OPENAI_API_KEY=your_openrouter_api_key

## Run the Application

streamlit run app.py

## Example Workflow

1. Upload a CSV or Excel dataset
2. Click **Clean Data**
3. View cleaning report
4. Download cleaned dataset
5. Ask questions about the dataset

## Future Improvements

* Dataset visualization
* Advanced EDA automation
* Database integration
* Natural language to SQL queries

## Author

Swarup Rait

GitHub: https://github.com/yourusername
