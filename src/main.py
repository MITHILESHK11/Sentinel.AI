import sys
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import MonitoringAgent

console = Console()

def main():
    console.print(Panel.fit("[bold blue]AI Application Monitoring Agent[/bold blue]\n[italic]Powered by Gemini[/italic]"))
    
    try:
        agent = MonitoringAgent()
    except Exception as e:
        console.print(f"[bold red]Failed to initialize agent:[/bold red] {e}")
        return

    console.print("[green]Agent initialized. Type 'exit' to quit.[/green]")

    while True:
        try:
            user_input = console.input("[bold yellow]You > [/bold yellow]")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            with console.status("[bold cyan]Thinking...[/bold cyan]"):
                response = agent.send_message(user_input)
            
            console.print(Panel(Markdown(response), title="[bold blue]Agent[/bold blue]", border_style="blue"))
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
