# Gemini Data Insights & Analytics Tool

An interactive web application built with **Python**, **Streamlit**, and the **Google Gemini API** that provides intelligent data analysis, automated insights, and conversational querying for structured datasets.

---

## Features

* **Interactive File Upload:** Support for CSV and Excel datasets with immediate data preview and structural overview.
* **AI-Powered Data Insights:** Leverages Google Gemini to automatically generate statistical summaries, identify trends, and highlight anomalies in your data.
* **Natural Language Querying:** Ask questions about your dataset in plain English and receive instant, context-aware answers generated via LLM analysis.
* **Dynamic Visualizations:** Built-in charting tools to visualize key metrics, distributions, and correlations using Pandas and Streamlit components.
* **Secure Configuration:** Designed with environment variable handling for API keys to maintain secure local deployments and version control hygiene.

---

## Tech Stack

* **Frontend & UI:** Streamlit
* **AI & LLM Integration:** Google GenAI SDK (`google-genai` / Gemini API)
* **Data Processing:** Pandas, NumPy
* **Environment Control:** Python-Dotenv

---

## Project Structure

```text
gemini-data-insights/
│
├── app.py                 # Main Streamlit application entry point
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (API keys)
└── README.md              # Project documentation
Getting Started
Prerequisites
Python 3.10 or higher

A valid Google Gemini API Key (Get one here)

Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/g4auransh/gemini-data-insights.git](https://github.com/g4auransh/gemini-data-insights.git)
cd gemini-data-insights
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure your environment variables:
Create a .env file in the root directory and add your Gemini API key:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
Run the application:

Bash
streamlit run app.py
Usage Guide
Launch the app using the Streamlit command.

Enter your Gemini API key in the sidebar (if not using the .env configuration file).

Upload your dataset (.csv or .xlsx).

Review the automatically generated summary metrics and data previews.

Use the chat or prompt interface to ask specific analytical questions about your data.
