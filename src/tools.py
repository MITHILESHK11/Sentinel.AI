import random
from datetime import datetime, timedelta

def fetch_performance_logs(date_range: str = "today"):
    """
    Fetches performance logs for the specified date range.
    Args:
        date_range: "today", "yesterday", or "last_week"
    """
    print(f"[System] Fetching performance logs for: {date_range}")
    # Mock data
    return {
        "avg_latency": f"{random.randint(100, 500)}ms",
        "slowest_api": "/api/v1/checkout",
        "throughput": f"{random.randint(1000, 5000)} req/min",
        "error_rate": f"{random.uniform(0.1, 2.0):.2f}%"
    }

def fetch_error_logs(severity: str = "High"):
    """
    Fetches error logs filtered by severity.
    Args:
        severity: "Low", "Medium", "High", or "Critical"
    """
    print(f"[System] Fetching error logs with severity: {severity}")
    # Mock data
    errors = []
    for i in range(random.randint(1, 5)):
        errors.append({
            "id": f"ERR-{random.randint(1000, 9999)}",
            "timestamp": datetime.now().isoformat(),
            "module": random.choice(["Auth", "Payment", "Inventory"]),
            "message": f"Timeout in {random.choice(['database', 'external api'])} connection",
            "severity": severity
        })
    return errors

def create_ticket(system: str, title: str, description: str):
    """
    Creates a ticket in the specified system (GitHub or Jira).
    """
    print(f"[System] Creating {system} ticket: {title}")
    return {
        "status": "success",
        "ticket_id": f"{system.upper()}-{random.randint(100, 999)}",
        "link": f"https://{system.lower()}.com/issues/{random.randint(100, 999)}"
    }

def send_report(email: str, content: str):
    """
    Sends a report to the specified email address.
    """
    print(f"[System] Sending report to {email}...")
    return {"status": "sent", "timestamp": datetime.now().isoformat()}

# List of tools for Gemini
tools_list = [fetch_performance_logs, fetch_error_logs, create_ticket, send_report]
