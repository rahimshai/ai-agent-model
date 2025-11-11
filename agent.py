from ollama_connector import OllamaChatModel
import sys
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def main():
    print(Fore.CYAN + "\n🤖 Local AI Assistant — Powered by Ollama\n")
    print(Fore.YELLOW + "Type 'exit' or 'quit' to end the chat.\n")

    # Ask which model to use
    model_name = input(Fore.GREEN + "Enter model name (default: gemma3:1b): ").strip() or "gemma3:1b"
    system_prompt = input(Fore.GREEN + "Set assistant role (default: Helpful AI): ").strip() or "You are a helpful AI assistant."

    ai = OllamaChatModel(model_name=model_name, system_prompt=system_prompt)

    while True:
        user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL)
        if user_input.lower() in ["exit", "quit"]:
            print(Fore.CYAN + "\n👋 Exiting chat. Goodbye!\n")
            sys.exit()

        reply = ai.chat(user_input)
        print(Fore.MAGENTA + "AI: " + Style.RESET_ALL + reply + "\n")

if __name__ == "__main__":
    main()
