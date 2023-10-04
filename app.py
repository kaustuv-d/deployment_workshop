#!pip install gradio
#!pip install transformers
import gradio as gr
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")

def generate_caption(input_image_path):
    try:
        raw_image = Image.open(input_image_path).convert('RGB')
        inputs = processor(raw_image, return_tensors="pt").to("cuda")

        # Generate a caption
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return caption
    except Exception as e:
        return str(e)

input_image = gr.inputs.Image(type="filepath", label="Upload an image")
output_caption = gr.outputs.Textbox(label="Generated Caption")

iface = gr.Interface(
    fn=generate_caption,
    inputs=input_image,
    outputs=output_caption,
    title="Image Captioning App",
    description="Upload an image and get its caption.",
)

# Launch the Gradio app
iface.launch()