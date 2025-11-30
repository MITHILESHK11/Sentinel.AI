import google.generativeai as genai
from src.config import GOOGLE_API_KEY
from src.tools import tools_list
import os

class MonitoringAgent:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Load system prompt
        prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "system_prompt.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_instruction = f.read()

        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=self.system_instruction,
            tools=tools_list
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def send_message(self, message: str):
        """
        Sends a message to the agent and returns the response.
        """
        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    def analyze_log(self, log_content: str):
        """
        Sends a log content to the agent for analysis.
        """
        try:
            message = f"Please analyze the following log file content and identify any issues:\n\n{log_content[:10000]}" # Truncate to avoid token limits
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error analyzing log: {str(e)}"
