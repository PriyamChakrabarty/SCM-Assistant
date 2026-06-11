import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "SCM Assistant"

DATA_FILE = "data/supplier_performance_data.csv"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")