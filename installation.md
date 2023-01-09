QuShape Installation
====================

QuShape can be use with operating systems supporting Miniconda (Windows, Linux, MacOs, etc.)

## Install
Installation is made using conda.

1. Install miniconda : https://docs.conda.io/en/latest/miniconda.html
2. Download or clone this repository.
3. From root of QuShape repos, create conda env
```bash
conda env create --name qushape --file misc/conda-env.yml
```
4. If your are using a unix like system, your need to correct a missing symbolic link
```bash
# Go in the lib folder of your conda environement
cd ~/miniconda3/envs/qushape/lib
# Link bsddb3 dynamic lib
ln -s ../site-packages/bsddb3/_pybsddb.so _bsddb.so
```
Without this step, you will not be able to Load / Save projects.

## Launch QuShape

1. Activate conda env

```bash
conda activate qushape
# or
source activate qushape
```

2. Launch qushape 
```bash
python src/main.py
```

##  Generate conda project

```bash
mamba build . -c free
anaconda upload $(mamba build . -c free --output) 
```
