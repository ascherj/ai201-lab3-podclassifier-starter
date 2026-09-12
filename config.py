import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Groq retired every Llama chat model in 2026. gpt-oss-20b is a Production-tier
# replacement. It reasons before it answers, and those tokens count against
# max_tokens, so keep max_tokens at 200 or more or content comes back empty.
LLM_MODEL = "openai/gpt-oss-20b"

# --- Classifier ---
VALID_LABELS = ["interview", "solo", "panel", "narrative"]

# --- Data ---
DATA_PATH = "./data"
TRAIN_FILE = "train_episodes.json"
TEST_FILE = "test_episodes.json"
LABELS_FILE = "my_labels.json"
