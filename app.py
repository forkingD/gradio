import gradio as gr
import openai 
openai.api_key = "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"

def greet(name):
    return "Hello " + name + "!"

def generate_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        #stop="\n\n"
        )
    message = response['choices'][0]['message']['content']
    cost = response['usage']['total_tokens']
    return message.strip()


interface = gr.Interface(
    fn=generate_reply,
    inputs=gr.inputs.Textbox(label="User Input"),
    outputs=gr.outputs.Textbox(label="Chatbot Response")
)

interface.launch()
