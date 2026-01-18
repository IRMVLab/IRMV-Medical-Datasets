# IRMV Medical Datasets Collection <sup>[中文版本](../README.md)</sup> <!-- omit from toc -->

**Version**: 1.2.0  
**Date**: January 18, 2026  
**Editor**: HSIEH Cheng-Tai [@IRMV LAB](https://irmv.sjtu.edu.cn/)

## Table of Contents <!-- omit from toc -->
- [📖 Project Description](#-project-description)
- [📂 Dataset Overview](#-dataset-overview)
  - [Dataset List](#dataset-list)
  - [EndoNeRF Dataset](#endonerf-dataset)
  - [SCARED2019 Dataset](#scared2019-dataset)
  - [StereoMIS Dataset](#stereomis-dataset)
  - [C3VD Dataset](#c3vd-dataset)
  - [SUPER Framework Dataset](#super-framework-dataset)
  - [STIR Dataset](#stir-dataset)
  - [SurgT Dataset](#surgt-dataset)
  - [SurgicalMotion Dataset](#surgicalmotion-dataset)
  - [MIMIC-CXR-JPG Dataset](#mimic-cxr-jpg-dataset)
- [📜 License](#-license)
- [📬 Contact](#-contact)
- [📝 Changelog](#-changelog)
- [🤝 Contribution Guidelines](#-contribution-guidelines)
- [🎬 Coming Soon](#-coming-soon)

## 📖 Project Description

This repository collects and curates publicly available datasets for **endoscopic surgical scenes and medical visual modeling**.

The datasets cover multi-modal data including **endoscopic images, video sequences, depth maps, 3D models, point clouds, and camera calibration information**, aiming to provide high-quality benchmarks and evaluation resources for visual understanding and intelligent perception in complex medical environments.

This project targets both **medical robotic perception** and **medical vision foundation models**, supporting research on large-scale medical image understanding, structured reasoning, and cross-modal learning.

By systematically organizing these datasets, we aim to provide a reusable, comparable, and extensible experimental foundation for researchers in medical robotics, computer vision, and medical artificial intelligence.

## 📂 Dataset Overview

### Dataset List
<!-- no toc -->
- [C3VD](#c3vd-dataset)
- [EndoNeRF](#endonerf-dataset)
- [MIMIC-CXR-JPG](#mimic-cxr-jpg-dataset)
- [SCARED2019](#scared2019-dataset)
- [StereoMIS](#stereomis-dataset)
- [STIR](#stir-dataset)
- [SurgT](#surgt-dataset)
- [SurgicalMotion](#surgicalmotion-dataset)
- [SUPER Framework](#super-framework-dataset)
---

### EndoNeRF Dataset
**Name**: `endonerf_sample_datasets`  
**Source**: https://med-air.github.io/EndoNeRF/  
**Modality**: Endoscopic images  
**Description**:  
Includes two subsets: `cutting_tissues_twice` and `pulling_soft_tissues`. The data is stored in **LLFF** format and is suitable for NeRF-based multi-view 3D reconstruction and novel view synthesis tasks.  
**Original Format**:  
[**LLFF**](https://github.com/Fyusion/LLFF) format with camera poses and image sequences, commonly used for real-scene reconstruction and novel view synthesis using methods such as [NeRF](https://github.com/bmild/nerf).

[EndoNeRF Dataset Documentation](./datasets_and_codes/endonerf)

---

### SCARED2019 Dataset
**Name**: `Stereo Correspondence and Reconstruction of Endoscopic Data`  
**Source**: https://endovissub2019-scared.grand-challenge.org/  
**Modality**: Stereo endoscopic images  
**Description**:  
Collected from three porcine subjects. Each sequence contains five keyframes with corresponding structured-light depth ground truth. The dataset is specifically designed for stereo matching and 3D reconstruction tasks.  
**Original Format**:  
TIFF depth maps, PNG images, camera parameters, and video sequences (preprocessing required).

[SCARED2019 Dataset Documentation](./datasets_and_codes/scared)

---

### StereoMIS Dataset
**Name**: `StereoMIS Data`  
**Source**: https://zenodo.org/records/7727692  
**Modality**: Stereo endoscopic video sequences  
**Description**:  
Captured using the da Vinci Xi surgical robot, consisting of **11 in-vivo surgical sequences** involving respiration, instrument interaction, and tissue deformation. Released by the same research group as SCARED, it is suitable for SLAM and dynamic scene modeling.  
**Original Format**:  
PNG image sequences, masks, camera parameters, and video streams.

[StereoMIS Dataset Documentation](./datasets_and_codes/stereomis)

---

### C3VD Dataset
**Name**: `Colonoscopy 3D Video Dataset (C3VD)`  
**Source**: https://durrlab.github.io/C3VD/  
**Modality**: Colonoscopy videos and CT data  
**Description**:  
The first publicly available dataset aligning **clinical colonoscopy videos** with **CT scans**, providing corresponding **3D mesh models (PLY)**. It supports research on registration, reconstruction, and localization.  
**Original Format**:  
Videos (MP4), CT scans (DICOM), 3D meshes (PLY), annotations, and registration data.

[C3VD Dataset Documentation](./datasets_and_codes/c3vd)

---

### SUPER Framework Dataset
**Name**: `SUPER Framework`  
**Source**: https://sites.google.com/ucsd.edu/super-framework  
**Modality**: Endoscopic videos with tissue landmark tracking and instrument segmentation annotations  
**Description**:  
A small-scale surgical dataset containing **58 tissue images**, each annotated with approximately **20 tissue landmarks**, along with corresponding **instrument segmentation masks**. It supports **tissue landmark tracking** and **instrument segmentation**, and is applicable to SLAM, surgical scene understanding, and instrument detection.  
**Original Format**:  
Image frames (PNG/JPEG), tissue landmark annotations (JSON/CSV), and instrument segmentation masks (PNG).

---

### STIR Dataset
**Name**: `STIR (Surgical Tattoos InfraRed)`  
**Source**: https://ieee-dataport.org/open-access/stir-surgical-tattoos-infrared  
**Modality**: Infrared fluorescence videos with tissue annotations  
**Description**:  
STIR uses indocyanine green (ICG) fluorescence to mark tissue regions in vivo or ex vivo, providing infrared imaging-based ground truth. Unlike point annotations, STIR provides **region-level labels**, supporting tissue detection, tracking, surgical navigation, and registration. It is one of the few datasets offering **infrared fluorescence ground truth**.  
**Original Format**:  
Infrared video sequences (AVI/MP4), region annotation masks (PNG/TIFF), and metadata files.

---

### SurgT Dataset
**Name**: `SurgT`  
**Source**: https://surgt.grand-challenge.org/  
**Modality**: Stereo endoscopic videos with tissue tracking annotations  
**Description**:  
Designed for **tissue tracking**, SurgT contains **25,000+ stereo frames**, each annotated with a single tissue landmark. It supports tissue motion estimation, stereo vision, and intraoperative navigation research.  
**Original Format**:  
Stereo video sequences (AVI/MP4) and single-point annotations (CSV/JSON).

---

### SurgicalMotion Dataset
**Name**: `SurgicalMotion`  
**Source**: https://github.com/zhanbh1019/SurgicalMotion  
**Modality**: Endoscopic videos with tissue landmark tracking annotations  
**Description**:  
Consists of 20 video sequences, each with approximately **60 frames**, and **25 tissue landmarks per frame**. Compared to SurgT, SurgicalMotion provides richer multi-point annotations, supporting tissue motion modeling, geometric scene understanding, and medical robotic perception.  
**Original Format**:  
Video sequences (MP4) and multi-point annotation files (CSV/JSON).

### MIMIC-CXR-JPG Dataset
**Name**: `MIMIC-CXR-JPG v2.1.0`  
**Source**: https://physionet.org/content/mimic-cxr-jpg/2.1.0/  
**Modality**: Chest X-ray images (CXR), structured medical labels  
**Description**: MIMIC-CXR-JPG is a large-scale real-world clinical chest X-ray dataset containing **over 370,000 radiographic images** collected from **tens of thousands of patients**. Each image is associated with **structured pathology labels** automatically extracted from corresponding radiology reports, making it suitable for medical image understanding, disease classification, abnormality detection, and training and evaluation of medical vision foundation models.  
**Original Format**: **JPEG images (converted from original DICOM), structured label files (CSV), image- and study-level metadata**

---

## 📜 License
All datasets follow their respective official licenses. Please refer to the corresponding dataset documentation for detailed usage terms.

## 📬 Contact
- **Research Groups**: [IRMV](https://irmv.sjtu.edu.cn/), [SIRIUS](https://banyutong.github.io/sirius_lab_website/)  
- **Email**: hsiehtpe_sjtu@sjtu.edu.cn (Hsieh Cheng-Tai)  
- **Dataset Access**: Refer to individual dataset documentation

## 📝 Changelog
- 2025-05-16  Initial documentation  
- 2025-05-19  EndoNeRF update  
- 2025-05-20  SCARED2019 update  
- 2025-05-25  StereoMIS update  
- 2025-07-15  GitHub page release ***v1.0***  
- 2025-07-22  Minor update ***v1.0.1***  
- 2025-09-22  
  - ***v1.1.0*** GitHub page optimization; C3VD documentation added; visual tracking datasets expanded; English version updated  
- 2026-01-18  Dataset expansion and task taxonomy update ***v1.2.0***

## 🤝 Contribution Guidelines
- **Dataset Submission**:  
  To contribute new datasets, please send an email with a dataset description document (template recommended: [template4dataset.md](./datasets_and_codes/template4dataset.md)).

- **Issue Reporting**:  
  For questions or suggestions, please contact us via email.

- **Reference Projects**:  
  [Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset)

- **Contributors**:  
  We thank the following contributors for their support (sorted by contribution time):  
  - HSIEH Cheng-Tai — hsiehtpe_sjtu@sjtu.edu.cn  
  - ZHAN Bohan — zhanbh2000@sjtu.edu.cn  

We welcome more contributors to join!

## 🎬 Coming Soon

*Coming soon*
