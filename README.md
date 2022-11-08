# Lane Segmentation

![Teaser](./Teaser.gif)

## 1. Create environment
  + Create conda environment with following command `conda create -y -n lane python=3.8`
  + Activate environment with following command `conda activate lane`
  + Install requirements with following command `pip install -r requirements.txt`

## 2. Preparation
  + Download checkpoint from [Link](https://postechackr-my.sharepoint.com/:u:/g/personal/taehoon1018_postech_ac_kr/EaKumdLe9iBHv1OWkjisoZ4B9ppCSvs0yZ6pxllgnGorfQ?e=9dp81y&download=1)
  + Move file as follows `./snapshots/HighwayLane/latest.pth`. Create folder if needed.

## 3. Inference
  + Prepare your image folder
  + `python run/Inference.py --source [IMAGE_FOLDER_DIR]`

## Performance - KAIST Highway Dataset
  + Maximum F1 Score: 94.8
  + Maximum IoU: 88.5
  + Throughput: 43 fps
  + GPU Mem Usage: 1.5 GB
