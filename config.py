import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# --- Classifier ---
VALID_LABELS = ["interview", "solo", "panel", "narrative"]

# --- Data ---
DATA_PATH = "./data"
TRAIN_FILE = "train_episodes.json"
TEST_FILE = "test_episodes.json"
LABELS_FILE = "my_labels.json"
