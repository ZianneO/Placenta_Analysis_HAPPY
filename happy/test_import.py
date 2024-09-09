import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    import happy
    print("Happy module imported successfully.")
except ImportError as e:
    print(f"ImportError: {e}")
