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
  <img src="Images/Block Diagram-Schematics.png">
</p>

<div align = "center">
  
  :small_orange_diamond: Figure : Block diagram of proposed work
  
</div>

## <div align="center">Acknowledgements</div>
Before installing and running the project, ensure you have the following prerequisites:
  
  :grey_exclamation: **For DRR generation using Plastimatch** ( file : *DRR Generation*)
 
 :wavy_dash:  See the [PerX2CT](https://github.com/dek924/PerX2CT) for full documentation on deployment.
 
:wavy_dash: Paper Title: PerX2CT - Perspective Projection-Based 3D CT Reconstruction from Biplanar X-rays

 <br/>
 
:grey_exclamation: **For general structure of VGG-19** ( file: *VGG-19*)

:wavy_dash:  See the [Neural Transfer Using PyTorch](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html) for the official Pytorch tutorial for neural style transfer

 
## <div align="center">Installation</div>
:arrow_right:Clone the Repository
```bash
git clone https://github.com/Deepa-Ramki/Spine-Style-Reimagining-Style-Transfer-on-Radiographs.git
```

:arrow_right:Navigate to the Project Directory
```bash
cd Spine-Style-Reimagining-Style-Transfer-on-Radiographs
```
:arrow_right:Install Dependencies
```bash
pip install -r requirements.txt
```


## <div align="center">Environments</div>

<div align="center">
  <a href="https://jupyter.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/120px-Jupyter_logo.svg.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="https://www.spyder-ide.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Spyder_logo.svg/1200px-Spyder_logo.svg.png" width="20%" /></a>
</div>

