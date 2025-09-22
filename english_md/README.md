# IRMV Medical Datasets Collection [English Version](./english_md/README.md)

**Version**: 1.1.0  
**Date**: September 22, 2025  
**Editor**: Hsieh Cheng-Tai [@IRMV LAB](https://irmv.sjtu.edu.cn/)

## 📖 Project Description

This repository collects and organizes **public datasets for 3D vision tasks and robotic perception in endoscopic surgical scenes**.  
The datasets include **endoscopic images, video sequences, depth maps, 3D models, point clouds, and camera calibration information**, supporting the following research directions:  

- Visual SLAM  
- Structured-light / Neural rendering 3D reconstruction  
- Camera calibration and validation  
- Geometric learning  
- Surgical navigation algorithm evaluation  
- Tissue landmark tracking  
- Surgical instrument segmentation  

The project aims to promote research on **autonomous perception, mapping, and localization** of **medical robots** in complex surgical scenarios.

## 📂 Dataset List

### Dataset Index
- [EndoNeRF Dataset](#endonerf-dataset)  
- [SCARED2019 Dataset](#scared2019-dataset)  
- [StereoMIS Dataset](#stereomis-dataset)  
- [C3VD Dataset](#c3vd-dataset)  

---

### EndoNeRF Dataset
**Name**: `endonerf_sample_datasets`  
**Source**: [https://med-air.github.io/EndoNeRF/](https://med-air.github.io/EndoNeRF/)  
**Type**: Endoscopic images  
**Description**: Contains two subsets: `cutting_tissues_twice` and `pulling_soft_tissues`. Data are stored in **LLFF** format and are suitable for NeRF-based multi-view 3D reconstruction and novel view synthesis tasks.  
**Original Format**: [**LLFF**](https://github.com/Fyusion/LLFF) format (with camera poses and image sequences), widely used for real-scene reconstruction and view synthesis with [NeRF](https://github.com/bmild/nerf).  

[EndoNeRF Dataset Documentation](./datasets_and_codes/endonerf)

---

### SCARED2019 Dataset
**Name**: `Stereo Correspondence and Reconstruction of Endoscopic Data`  
**Source**: [https://endovissub2019-scared.grand-challenge.org/](https://endovissub2019-scared.grand-challenge.org/)  
**Type**: Stereo endoscopic images  
**Description**: Based on three pig cadavers, each dataset includes 5 keyframes and corresponding structured-light depth information. Designed specifically for stereo correspondence and 3D reconstruction tasks.  
**Original Format**: **TIFF depth maps**, **PNG images**, camera parameters, and video sequences (preprocessing required).  

[SCARED2019 Dataset Documentation](./datasets_and_codes/scared)

---

### StereoMIS Dataset
**Name**: `StereoMIS Data`  
**Source**: [https://zenodo.org/records/7727692](https://zenodo.org/records/7727692)  
**Type**: Stereo endoscopic video sequences  
**Description**: Collected with the da Vinci Xi surgical robot, includes **11 intraoperative sequences** (breathing, instrument manipulation, tissue deformation, etc.). Released by the same research team as SCARED. Suitable for SLAM and dynamic scene modeling tasks.  
**Original Format**: **PNG image sequences, masks, camera parameters, and video streams**  

[StereoMIS Dataset Documentation](./datasets_and_codes/stereomis)

---

### C3VD Dataset
**Name**: `Colonoscopy 3D Video Dataset (C3VD)`  
**Source**: [https://durrlab.github.io/C3VD/](https://durrlab.github.io/C3VD/)  
**Type**: Colonoscopy video and CT data  
**Description**: The first public colonoscopy dataset with registered clinical colonoscopy videos and CT scans, providing corresponding **3D mesh models (PLY)**. Suitable for registration, reconstruction, and localization research.  
**Original Format**: **Video (MP4), CT (DICOM), 3D meshes (PLY), annotations, and registration information**  

[C3VD Dataset Documentation](./datasets_and_codes/c3vd)

---

### SUPER Framework Dataset
**Name**: `SUPER Framework`  
**Source**: [https://sites.google.com/ucsd.edu/super-framework](https://sites.google.com/ucsd.edu/super-framework)  
**Type**: Endoscopic video, tissue landmark tracking, and surgical instrument segmentation annotations  
**Description**: Provides a small-scale surgical scene dataset with **58 frames**, each containing ~**20 tissue landmarks**, along with **surgical instrument segmentation annotations**. Can be used for **tissue landmark tracking** and **instrument segmentation** tasks, supporting visual SLAM, scene understanding, and instrument detection.  
**Original Format**: **Image frames (PNG/JPEG), tissue landmark annotations (JSON/CSV), segmentation masks (PNG)**  

---

### STIR Dataset
**Name**: `STIR (Surgical Tattoos InfraRed)`  
**Source**: [https://ieee-dataport.org/open-access/stir-surgical-tattoos-infrared](https://ieee-dataport.org/open-access/stir-surgical-tattoos-infrared)  
**Type**: Infrared fluorescence tissue annotations and video data  
**Description**: STIR uses indocyanine green (ICG) dye to mark tissues in vivo or ex vivo, providing ground-truth via infrared imaging. Unlike single-point annotation, STIR offers **small region labels**, useful for **tissue region detection, tracking, surgical navigation, and registration**. A rare dataset with **infrared fluorescence ground truth**.  
**Original Format**: **Infrared video sequences (AVI/MP4), region masks (PNG/TIFF), metadata files**  

---

## 📜 License
Each dataset follows its official usage agreement. Please refer to the corresponding documentation.  

## 📬 Contact
- **Lab Teams**: [IRMV](https://irmv.sjtu.edu.cn/), [SIRIUS](https://banyutong.github.io/sirius_lab_website/)  
- **Email**: hsiehtpe_sjtu@sjtu.edu.cn (Hsieh Cheng-Tai)  
- **Dataset Request & Download**: see individual dataset documentation  

## 📝 Changelog
- 2025-05-16  Repository created  
- 2025-05-19  Added EndoNeRF  
- 2025-05-20  Added SCARED2019  
- 2025-05-25  Added StereoMIS  
- 2025-07-15  GitHub Page v1.0 release  
- 2025-07-22  Minor update v1.0.1  
- 2025-09-22  
  - ***v1.1.0*** Optimized GitHub page; added C3VD dataset page; added tissue landmark tracking dataset description.  

## 🤝 Contribution Guide
- **Data Submission**:  
  To contribute a new dataset, please send an email with a dataset description (recommended: [template4dataset.md](./datasets_and_codes/template4dataset.md)).  

- **Issue Reporting**:  
  For questions or suggestions, please contact us via email.  

- **Recommended Reference**:  
  [Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset)

- **Contributor List**:  
  Thanks to the following contributors for their support (in chronological order):  
  - Hsieh Cheng-Tai hsiehtpe_sjtu@sjtu.edu.cn  
  - Zhan Bohan zhanbh2000@sjtu.edu.cn  

More contributors are welcome!  

---

## ✅ Todo List

### GitHub Page Maintenance
- [x] Create page  
- [ ] Optimize index  

### Dataset Collection
- [x] EndoNeRF  
- [x] SCARED2019  
- [x] C3VD  

### Preprocessing Code
- [ ] C3VD  
- [ ] StereoMIS
