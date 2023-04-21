import gradio as gr
import openai 
import os
openai.api_key = os.getenv(OPEN_API_KEY)

def greet(name):
    return "Hello " + name + "!"

def generate_reply(prompt, chat_history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        #stop="\n\n"
        )
    message = response['choices'][0]['message']['content']
    cost = response['usage']['total_tokens']
    chat_history.append((message, message))
    return message.strip(), chat_history

#interface = gr.Interface(
#    fn=generate_reply,
#    inputs=gr.Textbox(label="User Input"),
#    outputs=gr.Textbox(label="Chatbot Response")
#)
#interface.launch()


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(generate_reply, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()