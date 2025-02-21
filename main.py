from colorama import Fore, Style
from rich.console import Console
from rich.markdown import Markdown
import os
import requests
from dotenv import load_dotenv
import time
import json

load_dotenv()
console = Console()
api_key = os.getenv("API_KEY")  # add your openrouter.ai API KEY in the .env file


def show_menu():
    console.print(
        "[magenta bold]============== MAIN MENU ==============[/magenta bold]"
    )
    console.print(f"[green]1.[/green] Chat with AI")
    console.print(f"[green]2.[/green] View chat history")
    console.print(f"[green]3.[/green] Export chat history to a text file")
    console.print(f"[green]4.[/green] Clear chat history")
    console.print(f"[green]5.[/green] Exit")
    console.print(
        "[magenta bold]=======================================[/magenta bold]"
    )


def clear_console():
    os.system("cls")


def typing_animation():
    animation_chars = ["|", "/", "-", "\\"]
    for _ in range(10):
        for char in animation_chars:
            print(f"\r{Fore.YELLOW}Thinking... {char}", end="", flush=True)
            time.sleep(0.1)
    print("\r", end="", flush=True)


def print_markdown(text):
    md = Markdown(text)
    console.print(
        md,
    )


def get_ai_response(messages):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "deepseek/deepseek-chat:free",  # find your preferred AI model at openrouter.ai
            "messages": messages,
        },
    )
    data = response.json()

    console.print(
        "[bold yellow]Generating AI response... (this may take a few seconds)[/bold yellow]\n"
    )
    typing_animation()

    return data["choices"][0]["message"]["content"]


def chat_loop(chat_history):
    console.print(
        "[yellow]Entering chat mode. Type 'quit' to return to main menu.[/yellow]\n"
    )
    while True:
        user_input = input(f"{Fore.BLUE}You: {Fore.RESET}")

        if user_input.strip().lower() == "quit":
            break

        chat_history.append({"role": "user", "content": user_input})
        save_chat_history(chat_history)

        ai_response = get_ai_response(chat_history)
        console.print("AI:", style="magenta", end=" ")
        print_markdown(ai_response)

        chat_history.append({"role": "assistant", "content": ai_response})
        save_chat_history(chat_history)


def save_chat_history(chat_history):
    with open("chat_history.json", "w", encoding="utf-8") as file:
        json.dump(chat_history, file, indent=2, ensure_ascii=False)


def load_chat_history():
    if not os.path.exists("chat_history.json"):
        return []

    try:
        with open("chat_history.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


def view_chat_history(chat_history):
    if not chat_history:
        console.print("[red]No chat history available.[/red]\n")
        return
    console.print("[blue bold]=== CHAT HISTORY ===[/blue bold]\n")
    for i, msg in enumerate(chat_history, start=1):
        role_color = "blue" if msg["role"] == "user" else "magenta"
        console.print(
            f"[{role_color}]{i}. {msg['role'].title()}: {msg['content']}[/{role_color}]"
        )
    console.print()


def export_chat_history(chat_history):
    output_file = "chat_history_export.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        for msg in chat_history:
            role = msg["role"].title()
            content = msg["content"]
            file.write(f"{role}: {content}\n\n")
    console.print(f"[green]Chat history exported to {output_file}[/green]\n")


def clear_chat_history():
    if os.path.exists("chat_history.json"):
        os.remove("chat_history.json")
        console.print("[yellow]Chat history cleared.[/yellow]\n")
    else:
        console.print("[red]No chat history to clear.[/red]\n")


def main():
    chat_history = load_chat_history()
    clear_console()

    while True:
        clear_console()
        show_menu()
        choice = input(f"{Fore.GREEN} Enter your choice (1-5): {Fore.RESET}")
        clear_console()

        if choice == "1":
            chat_loop(chat_history)
        elif choice == "2":
            view_chat_history(chat_history)
            input(f"{Fore.YELLOW}Press Enter to return to the menu...{Style.RESET_ALL}")
        elif choice == "3":
            export_chat_history(chat_history)
            input(f"{Fore.YELLOW}Press Enter to return to the menu...{Style.RESET_ALL}")
        elif choice == "4":
            clear_chat_history()
            chat_history = []
            input(f"{Fore.YELLOW}Press Enter to return to the menu...{Style.RESET_ALL}")
        elif choice == "5":
            break


main()


"""
Created by Mahdi Olamaei for a video tutorial posted on www.aparat.com/exxzamTutorials
you can contact me on telegram: @exxzam
"""
