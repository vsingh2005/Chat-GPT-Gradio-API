import gradio as gr
import openai
openai.api_key = "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"
def openai_chatbot(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " Ring0:"]
    )
    return response.choices[0].text

gr.Interface(openai_chatbot, inputs="text", outputs="text").launch()