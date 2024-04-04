# -*- coding: utf-8 -*-
"""objectdetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H5xfMGpqslDxY_YsA7C7TNJfl_mT3ftQ

## Let's mount google drive first for a storage and GPU
"""

from google.colab import drive
drive.mount('/content/gdrive')

# make sure you use Tesla K80 GPU (12GB), by changing 'runtmie type'
!nvidia-smi

"""## Clone YoloV5 GitHub repository"""

!git clone https://github.com/ultralytics/yolov5  # clone repo
!pip install -r yolov5/requirements.txt  # install dependencies

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov5

"""## Upload the testing video file"""

from google.colab import files
uploaded = files.upload()

"""## Implement Detection on testing video file"""

!python detect.py --source trafficmini.mp4

"""## Download the output  File"""

from google.colab import files
files.download('/content/yolov5/runs/detect/.jpg')

pr