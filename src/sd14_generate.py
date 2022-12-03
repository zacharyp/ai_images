# %% 
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
# get your token at https://huggingface.co/settings/tokens
token = "TOKEN_HERE"
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", 
revision="fp16", torch_dtype=torch.float16, use_auth_token=token)

pipe.to("cuda")

torch.cuda.empty_cache()

# %% 
prompt = "man eating french bread"
steps = 100
width = 512
height = 512

with autocast("cuda"):
  for i in range(4):
    output = pipe(prompt, width=width, height=height, num_inference_steps=steps)
    #image = output["sample"][0]
    image = output.images[0]
    file = prompt.replace(" ", "_").replace(",", "")
    image.save(f"{file}-{i}.png")

