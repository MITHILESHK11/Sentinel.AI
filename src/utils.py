import requests
import os

def fetch_log_content(source: str) -> str:
    """
    Fetches log content from a URL or local file path.
    """
    try:
        if source.startswith("http://") or source.startswith("https://"):
            response = requests.get(source)
            response.raise_for_status()
            return response.text
        elif os.path.exists(source):
            with open(source, "r", encoding="utf-8") as f:
                return f.read()
        else:
            return f"Error: File or URL not found: {source}"
    except Exception as e:
        return f"Error fetching log: {str(e)}"
