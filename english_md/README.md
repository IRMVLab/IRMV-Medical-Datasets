# IRMV Medical Datasets README

**Version**: 1.0.1  
**Date**: July 22, 2025  
**Author**: Hsieh Cheng-Tai [@**IRMV LAB**](https://irmv.sjtu.edu.cn/)

## Project Description

This dataset is specifically designed for **3D vision tasks and robotic perception tasks in endoscopic surgery scenarios**, covering high-quality endoscopic image data and corresponding geometric information (such as point clouds, depth maps, camera poses, and calibration parameters).

The dataset supports various research tasks including **visual SLAM, structured light 3D reconstruction, camera calibration validation, geometric learning, and surgical navigation algorithm evaluation**, suitable for advancing the autonomous perception and localization capabilities of **medical robots** in complex surgical environments.

## Dataset List

### EndoNeRF Dataset

**Name**: `endonerf_sample_datasets`

**Source**: [https://med-air.github.io/EndoNeRF/](https://med-air.github.io/EndoNeRF/)  
**Type**: Endoscopic images  
**Description**: Contains two folders, `cutting_tissues_twice` and `pulling_soft_tissues`  
**Original Format**: **LLFF**

[See DingTalk document attachment "EndoNeRF_Dataset"](https://alidocs.dingtalk.com/i/nodes/l6Pm2Db8D4rEryL0hgp2yyAp8xLq0Ee4?doc_type=wiki_doc&iframeQuery=anchorId%3DX02maqg6ltisp5gn1405q)

### SCARED2019 Dataset

**Name**: `Stereo Correspondence and Reconstruction of Endoscopic Data`

**Source**: [https://endovissub2019-scared.grand-challenge.org/](https://endovissub2019-scared.grand-challenge.org/)  
**Type**: Stereo endoscopic images  
**Description**: Includes three datasets (from three different pigs), each containing 5 keyframes. Keyframes are single-frame images taken at unique positions with the endoscope, along with structured light illuminator images taken at multiple positions.  
**Original Format**: **TIFF** depth maps, **PNG** photos, camera parameter information, and video sequences (preprocessing required)

[See DingTalk document attachment "SCARED2019_Dataset"](https://alidocs.dingtalk.com/i/nodes/l6Pm2Db8D4rEryL0hgp2yyAp8xLq0Ee4?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mawao1mrjtyjem3jele)

### StereoMIS Dataset

**Name**: `StereoMIS Data`

**Source**: [https://zenodo.org/records/7727692](https://zenodo.org/records/7727692)  
**Type**: Stereo endoscopic video sequences  
**Description**: StereoMIS is a dataset for simultaneous localization and mapping (SLAM) in endoscopic surgery. It was captured using the da Vinci Xi surgical robot, recording stereo video streams and forward kinematics. It consists of three in vivo pig subjects with 11 surgical sequences, including breathing, tool motion, and tissue deformation. The author is the same as SCARED.  
**Original Format**: **PNG** format **Masks**, camera parameter information, and video sequences (preprocessing required)

[StereoMIS Dataset Documentation](stereomis/stereo_mis.md)

## License

Refer to the usage documentation of each dataset for details.

## Contact

* **Lab Team**: [**IRMV**](https://irmv.sjtu.edu.cn/), [**SIRIUS**](https://banyutong.github.io/sirius_lab_website/)
* **Email**: hsiehtpe_sjtu@sjtu.edu.cn Hsieh Cheng-Tai
* **Data Application & Download**: Refer to the usage documentation of each dataset for details

## Changelog

* 2025-05-16 Document created
* 2025-05-19 EndoNeRF updated
* 2025-05-20 SCARED2019 updated
* 2025-05-25 StereoMIS updated
* 2025-07-15 GitHub page updated v1.0
* 2025-07-22 Minor update v1.0.1

## Data Download & Alibaba Cloud Usage Instructions

### coming soon

## Contribution Guide

* **Data Submission**  
  To contribute a new dataset, please contact via email and provide a data description document.

* **Feedback**  
  Send an email to the contact address for discussion.

* **Recommended Reference Website:**  
  [Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset)

## Todo List

### GitHub Page Maintenance

* [x] Create page

### Alibaba Cloud Usage Instructions

* [ ] Write aliyunpan download introduction

### Dataset Collection

* [x] endonerf
* [x] scared2019
* [x] stereomis
    * [x] Preprocessing code written
* [ ] c3vd 