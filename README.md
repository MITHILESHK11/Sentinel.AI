# Sentinel.AI — AI Monitoring Agent 🛡️

## About

Sentinel.AI is an AI-powered monitoring agent designed to help developers automatically monitor application performance, detect issues, and simulate ticket/report creation — all powered by a generative AI model (e.g. Google Gemini).  
It offers both a web-based UI (via Streamlit) and a command-line interface, enabling seamless integration into different development or deployment workflows.  

Key use cases include:  
- Monitoring and analyzing log files or application performance metrics.  
- Detecting potential issues or anomalies (errors, performance degradation, crashes, etc.).  
- Simulating ticket creation for detected issues (e.g., GitHub or Jira), or generating human-readable reports / email summaries.  
- Serving as a proof-of-concept for automated monitoring + AI-assisted alerting / reporting pipelines.

---

## Features

- **Web UI** — A friendly chat-style interface (Streamlit) to interact with the monitoring agent.  
- **CLI Mode** — Run the agent from the command line for integration in scripts or CI/CD pipelines.  
- **Log & Performance Monitoring** — Parse and analyze performance and error logs to detect anomalies or issues.  
- **Issue Detection & Ticket Simulation** — On detecting issues, simulate creating tickets (e.g., GitHub / Jira) or send report emails.  
- **Mock Log Support** — Useful for testing or demonstrations (e.g. with synthetic / mock logs).  
- **Flexible Configuration** — Use a `.env` file to securely provide API keys (e.g. `GOOGLE_API_KEY`) and configure agent behavior.

---

## Getting Started

### Prerequisites

- Python 3.x  
- (Optional but recommended) Virtual environment  

### Installation

```bash
git clone https://github.com/MITHILESHK11/Sentinel.AI.git
cd Sentinel.AI
python -m venv venv            # optional
source venv/bin/activate       # on Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### Configuration

Create a `.env` file in the root directory with your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

You can copy from `.env.example` (if present) to get a template.

### Usage

#### Web UI (Recommended)

```bash
streamlit run src/app.py
```

This will start the Streamlit-based interactive UI where you can view logs, chat with the agent, and get insights on issues.

#### CLI Mode

```bash
python src/main.py
```

This runs the agent in terminal mode — useful for automation or integration with CI/CD pipelines.

---

## Project Structure

```
Sentinel.AI/
│
├── src/                   # Source code (main logic)
│   ├── app.py             # Streamlit web UI entrypoint
│   ├── main.py            # CLI entrypoint
│   └── ...                # Other modules for log parsing, analysis, reporting, etc.
│
├── prompts/               # Prompt templates used by AI model  
├── requirements.txt       # Python dependencies  
├── .env                   # Environment variables (e.g. API keys)  
├── test_agent_interaction.py  # Sample tests / sanity checks  
├── test_import.py         # Import test  
└── README.md              # This file
```

---

## Why Sentinel.AI?

If you are working on small-to-medium scale projects and want **automated monitoring + AI-assisted alerting/reporting** — without setting up heavy infrastructure — Sentinel.AI can serve as a lightweight yet flexible solution. It can also serve as a base for building more advanced monitoring & observability tools (e.g., real log ingestion, real alerting, integration with real ticketing systems, dashboards, ML-based anomaly detection).

---

## Contributing

Contributions, suggestions and improvements are welcome! Feel free to open issues or submit pull requests. Some ideas for future enhancements:

* Integrate real logging frameworks / log ingestion (e.g. from production servers).
* Add anomaly detection or ML-based pattern detection on logs/performance metrics.
* Real integration with ticketing systems (e.g. GitHub Issues API, Jira API) for actual ticket creation.
* Email / Slack / Teams / other notification support for alerts.
* Extend UI: richer dashboard, historical logs, trend graphs, filtering, etc.

---

## License

You can choose an open-source license (e.g. MIT, Apache 2.0, etc.) to specify the terms — (currently no license file is present).

---

## Acknowledgements

Built and tested using Python + Streamlit + Google Gemini (or any compatible generative-AI model).

---
