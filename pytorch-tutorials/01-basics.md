# Basics
Here my notes on my processes of learning Pytorch from Pytorch official tutorials.
URL: https://pytorch.org/tutorials/

Ok, this page says I will become a ninja ML killer developer. :ninja:

It will teach the whole ML Workflow development:
- Working with data
- Creating models
- Optimizing model parameters
- Saving and deploying trained models

We will use FashionMNIST data set becase we like clothes and we are cool :shirt:


## Pre-reqs

We first need to create an isolated python environment, `conda` can help here:
```bash
source /opt/miniconda3/etc/profile.d/conda.sh
conda create -n dev python=3.8
conda activate dev
```

We can confirm we are inside our "virtual python box":
```bash
(dev) ~z➤ whereis pip
pip: /usr/bin/pip /opt/anaconda/bin/pip /opt/miniconda3/bin/pip /home/n0kt/.conda/envs/dev/bin/pip /home/n0kt/.local/bin/pip /usr/share/man/man1/pip.1.gz
(dev) ~z➤ which pip
/home/n0kt/.conda/envs/dev/bin/pip
```

Now we proceed to install required libs by pytorch:
`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 `
