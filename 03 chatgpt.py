import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a fitness coach"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Workout Coach")

demo.launch(share=True)