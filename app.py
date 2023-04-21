import gradio

def greet(name):
    return "Hello " + name + "!"

demo = gradio.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(server_name=0.0.0.0, server_port=8000)
