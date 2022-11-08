# Lane Segmentation

:rocket: This project is built based on [InSPyReNet (ACCV 2022)](https://github.com/plemeri/InSPyReNet). Please refer to the original repository for training and other details.

![Teaser](./figures/Teaser.gif)

## 1. Create environment
  + Create conda environment with following command `conda create -y -n lane python`
  + Activate environment with following command `conda activate lane`
  + Install requirements with following command `pip install -r requirements.txt`

## 2. Preparation
  ### Pre-trained Checkpoint
  + Download ImageNet pre-trained checkpoint for backbone network from [Link](https://postechackr-my.sharepoint.com/:u:/g/personal/taehoon1018_postech_ac_kr/EdnCVk9__w1Gh5npELiIWSIBO9DpZhHoiSLZUfGtUkwn3g?e=9zLWtn&download=1)
  + Download checkpoint from [Link](https://postechackr-my.sharepoint.com/:u:/g/personal/taehoon1018_postech_ac_kr/EaKumdLe9iBHv1OWkjisoZ4B9ppCSvs0yZ6pxllgnGorfQ?e=9dp81y&download=1)
  + Move file as follows `./snapshots/HighwayLane/latest.pth`. Create folder if needed.

  ### Dataset
  + [Train](https://postechackr-my.sharepoint.com/:u:/g/personal/taehoon1018_postech_ac_kr/EfUnpxrl8jRMklEcHmp1cTcBHlQhZhSl7soRNbG0jjLb8w?e=Tj5hbe&download=1)
  + [Test](https://postechackr-my.sharepoint.com/:u:/g/personal/taehoon1018_postech_ac_kr/ERVEPxwzk2ZElqM7-n05COoBjcztlOnqar1bNd19tlA3Qg?e=wm6Tzh&download=1)

## 3. Inference
  + Prepare your image folder
  + `python run/Inference.py --source [IMAGE_FOLDER_DIR]`

## Performance - KAIST Highway Dataset
  + Maximum F1 Score: 94.8
  + Maximum IoU: 88.5
  + Throughput: 43 fps
  + GPU Mem Usage: 1.5 GB
