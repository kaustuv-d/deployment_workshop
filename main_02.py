#!pip install diffusers
import torch
import uvicorn
from diffusers import StableDiffusionPipeline
from fastapi import FastAPI, HTTPException

app = FastAPI()

model_id = "CompVis/stable-diffusion-v1-4"
device = "cpu"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

@app.get("/")
async def root():
  return "Working"

@app.post("/generate_image/")
async def generate_image(prompt: str):
    try:
        # Generate the image using the provided prompt
        image = pipe(prompt).images[0]

        # Save the image to a file
        image_path = os.path.join(output_dir, "generated_image.png")
        with open(image_path, "wb") as image_file:
            image_file.write(image.numpy())

        # Return the image as a FileResponse
        return FileResponse(image_path, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")