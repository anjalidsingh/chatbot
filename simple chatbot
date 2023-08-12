import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)
