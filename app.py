import gradio

def greet(name):
    return "Hello " + name + "!"

demo = gradio.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(host="0.0.0.0", port=8000)
