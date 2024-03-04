import sys
import torch
from diffusers import StableDiffusionPipeline, StableDiffusionUpscalePipeline, EulerDiscreteScheduler
from io import BytesIO

model_id = "stabilityai/stable-diffusion-2"
model_id2 = "stabilityai/stable-diffusion-x4-upscaler"

# Use the Euler scheduler here instead
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Beautiful landscape with mountains, inspired by antoni gaudi, sunset"

if sys.argv[1]:
    prompt = sys.argv[1]

print("generating image for prompt: " + prompt)

steps = 100

pipe2 = StableDiffusionUpscalePipeline.from_pretrained(model_id2, torch_dtype=torch.float16)
pipe2 = pipe2.to("cuda")

# image = pipe(prompt, height=768, width=768, num_inference_steps=steps).images[0]
image = pipe(prompt, height=256, width=256, num_inference_steps=steps).images[0]
image_name = prompt.replace(" ", "_")
image_file_name = "img/" + image_name
fn_with_ex = image_file_name + ".png"
image.save(fn_with_ex)

# with open(filepath, "rb") as fh:
    # buf = BytesIO(fh.read())
upscaled_image = pipe2(prompt=prompt, image=image, num_inference_steps=50).images[0]
upscaled_image.save( image_file_name + "_upsampled.png")
