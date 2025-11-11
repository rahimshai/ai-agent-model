import ollama

class OllamaChatModel:
    def __init__(self, model_name="gemma3:1b", system_prompt="You are a helpful AI assistant."):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.chat_history = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(self, user_input):
        self.chat_history.append({"role": "user", "content": user_input})

        try:
            response = ollama.chat(model=self.model_name, messages=self.chat_history)
            reply = response['message']['content']
            self.chat_history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"⚠️ Error communicating with model '{self.model_name}': {e}"
