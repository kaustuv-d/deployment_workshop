#pip install fastapi
#pip install uvicorn
#pip install gradio_client

from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from gradio_client import Client


app = FastAPI()

def gen_image(prompt):
  client = Client("https://nota-ai-compressed-stable-diffusion.hf.space/")
  result = client.predict(
				prompt,	# str  in 'Input Prompt' Textbox component
				" ",	# str  in 'Negative Prompt' Textbox component
				4,	# int | float (numeric value between 4 and 11) in 'Guidance Scale' Slider component
				10,	# int | float (numeric value between 10 and 75) in 'Denoising Steps' Slider component
				0,	# int | float (numeric value between 0 and 999999) in 'Random Seed' Slider component
				fn_index=1
  )
  img_p=result[0]
  return img_p

@app.get("/")
async def root():
  return "Working"

@app.post("/generate")
async def generate_image(prompt: str):
    img_path = gen_image(prompt)
    return FileResponse(img_path)

if __name__ == "__main__":
  uvicorn.run(app, port=8000, host="127.0.0.1")


