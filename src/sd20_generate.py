import sys
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

model_id = "stabilityai/stable-diffusion-2"

# Use the Euler scheduler here instead
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Beautiful landscape with mountains, inspired by antoni gaudi, sunset"

if sys.argv[1]:
    prompt = sys.argv[1]

print("generating image for prompt: " + prompt)

steps = 70

for i in range(4):
    image = pipe(prompt, height=768, width=768, num_inference_steps=steps).images[0]
    image_name = prompt.replace(" ", "_")
    image.save("img/" + image_name + "_" + str(i) + ".png")
