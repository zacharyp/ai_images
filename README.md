# ai_images
Creating AI images using Stable Diffusion (and others?)


## anaconda 
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
bash Anaconda3-2022.10-Linux-x86_64.sh

### generate a token for huggingface here:
https://huggingface.co/settings/tokens

## stable diffusion 1.4
conda create --name stable_diff2 python=3.9.13

conda activate stable_diff

pip install torch --extra-index-url https://download.pytorch.org/whl/cu116

pip install diffusers==0.8.0 transformers scipy ftfy
pip install accelerate

huggingface-cli login

vim sd_generate.py


## stable diffusion 2.0
conda create --name stable_diff2 python=3.9.13
conda activate stable_diff2

pip install torch --extra-index-url https://download.pytorch.org/whl/cu116

pip install --upgrade git+https://github.com/huggingface/diffusers.git transformers accelerate scipy

huggingface-cli login

## maybe?  NOPE, fucked up torch without cuda gets installed
conda install xformers -c xformers/label/dev
