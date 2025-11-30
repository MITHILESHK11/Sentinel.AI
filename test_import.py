try:
    from src.config import GOOGLE_API_KEY
    from src.tools import tools_list
    from src.agent import MonitoringAgent
    print("Imports successful.")
except ImportError as e:
    print(f"Import failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
