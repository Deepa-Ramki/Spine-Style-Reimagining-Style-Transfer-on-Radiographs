<h1 align="center">SpineStyle: Reimagining Style Transfer on Radiographs for Image-Guided Spine Surgery </h1>

<p  align="center">  
  
Intraoperative radiographs are crucial for `image-guided robotic surgery` of the spine, facilitating essential tasks such as `2D/3D registration` and `3D reconstruction`. Ensuring stylistic consistency between input radiographs and digitally reconstructed radiographs (DRRs) is pivotal for training deep learning models used in these tasks. While `neural style transfer` techniques have seen extensive application in artistic imagery, their adoption in medical imaging, particularly spinal radiographs, remains limited. This work introduces SpineStyle, an advanced end-to-end pipeline that employs a modified `VGG-19` architecture to perform style transfer from DRRs to input radiographs. Unlike traditional `generative adversarial network` (GAN) approaches that demand large datasets, SpineStyle achieves superior results using single input and DRR images.
</p>

<h3 > <i>Index Terms</i> </h3> 

 :diamond_shape_with_a_dot_inside:YOLOv5
  :diamond_shape_with_a_dot_inside: Deep Learning
  :diamond_shape_with_a_dot_inside:Image-based planning
  :diamond_shape_with_a_dot_inside:GUI planning
  :diamond_shape_with_a_dot_inside:Vertebrae Segmentation
</div>

## <div align="center">Features</div>

- **End-to-End Style Transfer Pipeline**: Seamlessly transfers DRR style onto input radiographs.
  <br/>
  
- **Modified VGG-19 Architecture**: Enhances style transfer accuracy and anatomical integrity.
- **📊 Novel Evaluation Metrics**:
  - **`Style Transfer Extent (STE)`**: Quantifies the degree of style transfer from DRR to input radiograph.
  - **`Anatomical Content Preservation (ACP)`**: Evaluates the retention of anatomical details post style transfer.
- **Superior Performance 🚀**: Outperforms standard neural style transfer methods in rigorous comparative studies.
  
## <div align="center">Getting Started</div>

....
.........
..............

## <div align="center">Methodology</div>

<p align="center">
  <img src=Figure_commonmark/Screenshot%202024-06-04%20161929.png>
</p>
<div align = "center">
  
  :small_orange_diamond: Fig 4:Block diagram of proposed work: Graphical user interface (GUI) using Vertebrae  3D segmentation
</div>

## <div align="center">Pre-requisites</div>
Before installing and running the project, ensure you have the following prerequisites:

 :grey_exclamation: Download and install Qt from the `Qt website`. 
 
 :wavy_dash:  The version for this project is **Qt 4.6.1**.
  
  :grey_exclamation: YOLOv5 

 
 :wavy_dash:  See the [YOLOv5 Docs](https://docs.ultralytics.com/yolov5) for full documentation on training, testing and deployment. See below for quickstart examples.
 
:grey_exclamation: Eigen

:wavy_dash: `Eigen 4.3.1` is required for the project. Eigen is a C++ template library for linear algebra.

To include Eigen in your project, follow these steps:

1. Download Eigen 4.3.1 from the official [Eigen GitHub repository](https://github.com/eigenteam/eigen-git-mirror):

    ```bash
    git clone https://github.com/eigenteam/eigen-git-mirror.git
    cd eigen-git-mirror
    git checkout 4.3.1
    ```

2. Extract the contents to a directory on your system if you downloaded a compressed file. If you cloned the repository, you can skip this step.

3. Include the Eigen directory in your project's include path. 

## <div align="center">Installation</div>
:arrow_right:Clone the Repository
```bash
git clone https://github.com/yourusername/GUI-planning-.git
```

:arrow_right:Navigate to the Project Directory
```bash
cd GUI-planning-
```
:arrow_right:Install Dependencies
```bash
pip install -r requirements.txt
```
## <div align="center">Environments</div>

<div align="center">
  <a href="https://opencv.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://www.tensorflow.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://bit.ly/yolov5-paperspace-notebook">
    <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-gradient.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://matplotlib.org/">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Matplotlib_logo.svg/120px-Matplotlib_logo.svg.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://pypi.org/project/QtPy/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Pytorch_logo.png" width="10%" /></a>
</div>
