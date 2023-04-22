import gradio as gr
import openai 
import os
os.environ.get('OPENAI_API_KEY')

with gr.Blocks() as interface:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def OpenAI(history):
        messages_arr = [{"role": "user", "content": message[0]} for message in history]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages_arr,
            temperature=0.8,
            max_tokens=1024,
            stream=True,
            )
        history[-1][1] = ""
        for chunk in response: 
            if 'choices' in chunk:
                delta = chunk['choices'][0]['delta']
                if delta.get('content'):
                    if isinstance(delta['content'], str) and delta['content'].strip():
                        history[-1][1] += delta['content']
                        print(history)
                        yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
    OpenAI, chatbot, chatbot
    )    
    clear.click(lambda: None, None, chatbot, queue=False)

interface.queue()
interface.launch()
