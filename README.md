# Project Setup Guide

## Prerequisites
Before starting, ensure you have the following installed:
- Python (>=3.8, preferably 3.10 for compatibility)
- Git
- Miniconda (optional, if using Conda environments)
- pip

## Cloning the Repository
```sh
git clone https://github.com/HEILLER4/caps
cd https://github.com/HEILLER4/caps
```

## Creating Virtual Environments
Each component (NanoDet, Lotus, ZoeDepth) will have its own virtual environment.
## Nanodet, Lotus and ZoeDepth repository
```git
https://github.com/EnVision-Research/Lotus
https://github.com/RangiLyu/nanodet
https://github.com/isl-org/ZoeDepth
```

### 1. Setting up NanoDet Environment
```sh
python -m venv venv_nanodet
source venv_nanodet/bin/activate  # On Windows, use `venv_nanodet\Scripts\activate`
```
#### Install Dependencies
```sh
pip install -r nanodet/requirements.txt
```

### 2. Setting up Lotus Environment
```sh
python -m venv venv_lotus
source venv_lotus/bin/activate
```
#### Install Dependencies
```sh
pip install -r lotus/requirements.txt
```

### 3. Setting up ZoeDepth Environment
```sh
python -m venv venv_zoedepth
source venv_zoedepth/bin/activate
```
#### Install Dependencies
```sh
pip install -r ZoeDepth/requirements.txt
```

## Installing Common Dependencies
```sh
pip install -r requirements.txt
```

## Running the Project
Activate the appropriate environment before running any module.

For NanoDet:
```sh
source venv_nanodet/bin/activate
python scripts/nanodet.py
```

For Lotus:
```sh
source venv_lotus/bin/activate
python scripts/lotus.py
```

For ZoeDepth:
```sh
source venv_zoedepth/bin/activate
python scripts/zoedepth.py
```

## Troubleshooting
- **Dependency Conflicts**: If you encounter issues, consider creating a new virtual environment and reinstalling dependencies.
- **Torch Compatibility**: Ensure all libraries use the same version of PyTorch by specifying the compatible version in `requirements.txt`.

## Additional Notes
- Edit `requirements.txt` as needed for updated dependencies.
- Use `deactivate` to exit a virtual environment.
- If using Conda, replace `python -m venv` with `conda create --name <env_name> python=3.x` and activate using `conda activate <env_name>`.
- for models of nanodet, lotus and zoedepth, please go to their site and select the appropriate version of model.

Happy coding! 🚀

This project is still not Finished and in development, and may not run accordingly.
