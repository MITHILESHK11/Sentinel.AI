# AI Monitoring Agent

This agent monitors application performance and reports issues using Google's Gemini model.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

### Web UI (Recommended)
Run the Streamlit app:
```bash
streamlit run src/app.py
```

### CLI
Run the agent in the console:
```bash
python src/main.py
```

## Features

- **Web UI**: Chat interface with log file analysis.
- **Performance Monitoring**: Fetches mock performance logs.
- **Issue Detection**: Fetches mock error logs.
- **Ticket Creation**: Simulates creating tickets in GitHub/Jira.
- **Reporting**: Simulates sending email reports.
