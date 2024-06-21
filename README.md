# Execution

Run .exe file

# Launch Programm

## 1. For Ubuntu

### 1. Download Anaconda Installation Script

wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh

### 2. Install Development Packages

sudo apt-get install libxcb-xinerama0

### 3. Run Anaconda Installation Script

bash Anaconda3-2024.02-1-Linux-x86_64.sh

### 4. Activate Anaconda Virtual Environment

cd ../..
source /home/user/anaconda3/bin/activate
conda activate

### 5. Initialize Conda Configuration

conda init

### 6. Install Python Packages

pip install PyQt6 typing-extensions Self pandas datetime numpy xarray tk pyexcel_ods psycopg2 scikit-learn cryptography

### 7. Install Development Packages

sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
sudo apt install qtwayland5

### 8. Launch .py

python app.py

## 2. For Windows

### 1. Install VSCode

https://code.visualstudio.com

### 2. Install Python Packages

pip install PyQt6 typing-extensions Self pandas datetime numpy xarray tk pyexcel_ods psycopg2 scikit-learn cryptography

### 3. Launch .py

python app.py

# Security

The data used to train a decision tree forest model are original.