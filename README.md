# ai_images
Creating AI images using Stable Diffusion (and others?) in the WSL2 with an Nvidia GPU

## nvidia

get latest nvidia drivers

install cuda support in wsl2: https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl2


## install anaconda 
wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

bash Anaconda3-2022.10-Linux-x86_64.sh

### generate a token for huggingface here:
https://huggingface.co/settings/tokens

or easier to simply use `huggingface-cli` after install

## stable diffusion 1.4 https://github.com/CompVis/stable-diffusion

```
conda create --name stable_diff python=3.9.13

conda activate stable_diff

pip install torch --extra-index-url https://download.pytorch.org/whl/cu116

pip install diffusers==0.8.0 transformers scipy ftfy

pip install accelerate

huggingface-cli login

python src/sd14_generate.py
```

## stable diffusion 2.0 https://huggingface.co/stabilityai/stable-diffusion-2

```
conda create --name stable_diff2 python=3.9.13

conda activate stable_diff2

pip install torch --extra-index-url https://download.pytorch.org/whl/cu117

pip install --upgrade git+https://github.com/huggingface/diffusers.git transformers accelerate scipy

pip install omegaconf opencv-python einops torchvision

huggingface-cli login

python src/sd20_generate.py "Beautiful landscape with mountains, inspired by antoni gaudi, sunset"
```

##

```
conda env create -f environment.yaml
conda activate sd2

conda install pytorch torchvision -c pytorch
pip install transformers==4.19.2 diffusers 
pip install -e .

```

## maybe for better memory usage?

```
pip install ninja

pip install -v -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers
```