import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.agent import MonitoringAgent

def test_agent():
    print("Initializing agent...")
    try:
        agent = MonitoringAgent()
    except Exception as e:
        print(f"Failed to initialize agent: {e}")
        return

    print("Agent initialized. Sending test message...")
    test_message = "Show me the performance logs for today."
    print(f"User: {test_message}")
    
    response = agent.send_message(test_message)
    print(f"Agent Response:\n{response}")

if __name__ == "__main__":
    test_agent()
