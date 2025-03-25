# Project: Object Detection and Depth Estimation

## Overview

This project utilizes NanoDet for object detection and Lotus/ZoeDepth for depth estimation. It is designed to run on Python with `venv` or Conda for managing dependencies.

## Prerequisites

- Python 3.8 - 3.10 (Recommended)
- Git
- A dedicated GPU (for faster processing, but CPU is supported)
- **(Optional)** Conda for environment management

## Installation

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-repo/project-name.git
cd project-name
```

### **2️⃣ Create and Activate Virtual Environment**

#### **Using ****************************`venv`**************************** (Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

#### **Using Conda (Alternative)**

```bash
conda create --name project-env python=3.10 -y
conda activate project-env
```

### **3️⃣ Install Dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **4️⃣ Install Torch Manually (If Needed)**

Check [PyTorch Official Site](https://pytorch.org/get-started/locally/) for the best installation for your system.
For example:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  # GPU (CUDA 11.8)
pip install torch torchvision torchaudio  # CPU only
```

## Running the Project

```bash
python main.py
```

## Troubleshooting

- **If ********\`\`******** versions conflict:** Install compatible versions manually.
- **If OpenMP error (**\`\`\*\* conflict):\*\* Set environment variable:
  ```bash
  set KMP_DUPLICATE_LIB_OK=TRUE  # Windows
  export KMP_DUPLICATE_LIB_OK=TRUE  # Linux/macOS
  ```
- **For missing dependencies:** Reinstall:
  ```bash
  pip install -r requirements.txt --force-reinstall
  ```

## Notes

- If using a Raspberry Pi, ensure dependencies are compatible with ARM.
- GPU is recommended for real-time processing.

---

