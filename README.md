# IRMV Medical Datasets Collection <sup>[English Version](./english_md/README.md)</sup> <!-- omit from toc -->


**版本**: 1.2.0  
**日期**: 2026年1月18日  
**编者**: HSIEH Cheng-Tai [@IRMV LAB](https://irmv.sjtu.edu.cn/)

## 目录 <!-- omit from toc -->
- [📖 项目描述](#-项目描述)
- [📂 数据集列表](#-数据集列表)
  - [数据集目录](#数据集目录)
  - [EndoNeRF 数据集](#endonerf-数据集)
  - [SCARED2019 数据集](#scared2019-数据集)
  - [StereoMIS 数据集](#stereomis-数据集)
  - [C3VD 数据集](#c3vd-数据集)
  - [SUPER Framework 数据集](#super-framework-数据集)
  - [STIR 数据集](#stir-数据集)
  - [SurgT 数据集](#surgt-数据集)
  - [MIMIC-CXR-JPG 数据集](#mimic-cxr-jpg-数据集)
  - [SurgicalMotion 数据集](#surgicalmotion-数据集)
- [📜 许可协议](#-许可协议)
- [📬 联系方式](#-联系方式)
- [📝 更新日志](#-更新日志)
- [🤝 贡献指南](#-贡献指南)
- [🎬 即将推出](#-即将推出)
  
## 📖 项目描述

本仓库收录并整理适用于 **内窥镜手术场景与医疗视觉建模** 的视觉与感知数据集资源。

数据集覆盖 **内窥镜图像、视频序列、深度图、三维模型、点云、相机标定信息** 等多模态数据，旨在为复杂医疗场景中的视觉理解与智能感知提供高质量基准数据与评估平台。

本项目面向 **医疗机器人感知** 研究与**医疗视觉大模型** 的训练、评估与应用探索，例如大规模医学影像理解、结构化推理与跨模态学习。

通过系统化整理数据资源，我们希望为医疗机器人、计算机视觉与医学人工智能领域的研究者提供可复用、可对比、可扩展的实验基础。

## 📂 数据集列表

### 数据集目录
<!-- no toc -->
  - [C3VD](#c3vd-数据集)
  - [EndoNeRF](#endonerf-数据集)
  - [MIMIC-CXR-JPG](#mimic-cxr-jpg-数据集)
  - [SCARED2019](#scared2019-数据集)
  - [StereoMIS](#stereomis-数据集)
  - [STIR](#stir-数据集)
  - [SurgT](#surgt-数据集)
  - [SurgicalMotion](#surgicalmotion-数据集)
  - [SUPER Framework](#super-framework-数据集)
  
### EndoNeRF 数据集
**名称**: `endonerf_sample_datasets`  
**来源**: [https://med-air.github.io/EndoNeRF/](https://med-air.github.io/EndoNeRF/)  
**类型**: 内窥镜图像  
**简介**: 包含两个子集：`cutting_tissues_twice` 与 `pulling_soft_tissues`。数据以 **LLFF** 格式存储，适用于 NeRF 等多视角三维重建与新视角合成任务。  
**原格式**:  [**LLFF**](https://github.com/Fyusion/LLFF)格式（含相机位姿与图像序列），常用于使用[神经辐射场NeRF](https://github.com/bmild/nerf)等方法的真实场景重建和新视角合成任务。  

[EndoNeRF 数据集阅读文档](./datasets_and_codes/endonerf)

---

### SCARED2019 数据集
**名称**: `Stereo Correspondence and Reconstruction of Endoscopic Data`  
**来源**: [https://endovissub2019-scared.grand-challenge.org/](https://endovissub2019-scared.grand-challenge.org/)  
**类型**: 双目内窥镜图像  
**简介**: 来自三只猪实验体，每个数据集包含 5 个关键帧及对应的结构光深度信息。该数据集专为双目匹配与三维重建任务设计。  
**原格式**: **TIFF 格式深度图**、**PNG 图像**、相机参数与视频序列（需预处理）  

[SCARED2019 数据集阅读文档](./datasets_and_codes/scared)

---

### StereoMIS 数据集
**名称**: `StereoMIS Data`  
**来源**: [https://zenodo.org/records/7727692](https://zenodo.org/records/7727692)  
**类型**: 双目内窥镜视频序列  
**简介**: 由达芬奇 Xi 手术机器人采集，包括 **11 段体内手术序列**（呼吸、器械操作、组织变形等）。与 SCARED 数据集同一研究团队发布，适合 SLAM 与动态场景建模任务。  
**原格式**: **PNG 图像序列、Masks、相机参数与视频流**  

[StereoMIS 数据集阅读文档](./datasets_and_codes/stereomis)

---

### C3VD 数据集
**名称**: `Colonoscopy 3D Video Dataset (C3VD)`  
**来源**: [https://durrlab.github.io/C3VD/](https://durrlab.github.io/C3VD/)  
**类型**: 结直肠内窥镜视频与 CT 数据  
**简介**: 首个公开的结直肠内窥镜视频与三维模型配准数据集，包含 **临床结直肠镜视频** 与 **CT 扫描**，并提供对应的 **3D 网格模型（PLY）**。适用于配准、重建与定位研究。  
**原格式**: **视频（MP4）、CT（DICOM）、3D 网格（PLY）、标注与配准信息**  

[C3VD 数据集阅读文档](./datasets_and_codes/c3vd)

---

### SUPER Framework 数据集
**名称**: `SUPER Framework`  
**来源**: [https://sites.google.com/ucsd.edu/super-framework](https://sites.google.com/ucsd.edu/super-framework)  
**类型**: 内窥镜视频、组织点追踪与手术器械分割标注  
**简介**: SUPER 提供一个小规模的手术场景数据集，包含 **58 帧组织图像**，每帧约 **20 个组织特征点（landmarks）**，以及相应的 **手术器械分割标注**。该数据集可用于 **组织点追踪（Tissue Landmark Tracking）** 和 **手术器械分割（Instrument Segmentation）** 任务，支持视觉 SLAM、手术场景理解和器械检测研究。  
**原格式**: **图像帧（PNG/JPEG）、组织点标注（JSON/CSV）、器械分割掩码（PNG）**  

---

### STIR 数据集
**名称**: `STIR (Surgical Tattoos InfraRed)`  
**来源**: [https://ieee-dataport.org/open-access/stir-surgical-tattoos-infrared](https://ieee-dataport.org/open-access/stir-surgical-tattoos-infrared)  
**类型**: 红外荧光组织标注与视频数据  
**简介**: STIR 使用吲哚菁绿 (ICG) 荧光染料在体内或体外组织上进行标记，通过红外成像获取组织的“真值”。不同于单点标注，STIR 提供的是 **小区域标记**，可用于 **组织区域检测、追踪、手术导航和配准** 等任务，是目前少见的 **红外荧光标记真值数据集**。  
**原格式**: **红外视频序列（AVI/MP4）、区域标注掩码（PNG/TIFF）、元数据说明文件** 

---

### SurgT 数据集
**名称**: `SurgT`  
**来源**: [https://surgt.grand-challenge.org/](https://surgt.grand-challenge.org/)  
**类型**: 双目内窥镜视频、组织点追踪标注  
**简介**: SurgT 是一个专为 **组织追踪（Tissue Tracking）** 设计的数据集，基于 **双目内窥镜视频**，共包含 **25000+ 帧**。每帧提供 **一个组织标注点**，可用于组织运动估计、双目图像处理与术中导航研究。  
**原格式**: **双目内窥镜视频序列（AVI/MP4）、单点标注文件（CSV/JSON）**  

### MIMIC-CXR-JPG 数据集
**名称**: `MIMIC-CXR-JPG v2.1.0`  
**来源**: https://physionet.org/content/mimic-cxr-jpg/2.1.0/  
**类型**: 胸部 X 光图像（CXR）、结构化医学标签  
**简介**: MIMIC-CXR-JPG 是一个大规模的真实临床胸部 X 光数据集，包含 **37 万余张胸片图像**，来自 **数万名患者** 的临床检查记录。每张图像均关联由放射科报告自动提取的 **结构化病变标签**，适用于医学图像理解、疾病分类、异常检测以及医疗视觉大模型的训练与评估。  
**原格式**: **JPEG 图像（由原始 DICOM 转换）、结构化标签文件（CSV）、影像与检查级元数据**

---

### SurgicalMotion 数据集
**名称**: `SurgicalMotion`  
**来源**: [https://github.com/zhanbh1019/SurgicalMotion](https://github.com/zhanbh1019/SurgicalMotion)  
**类型**: 内窥镜视频、组织点追踪标注  
**简介**: SurgicalMotion 由 20 个视频组成，每个视频约 **60 帧**，每帧包含 **25 个组织特征点（landmarks）**。相比 SurgT 的单点标注，SurgicalMotion 提供更丰富的 **多点组织追踪标注**，适用于组织运动建模、场景几何理解与医疗机器人视觉感知研究。  
**原格式**: **视频序列（MP4）、多点标注文件（CSV/JSON）**  



## 📜 许可协议
各数据集均遵循其官方发布的使用协议，请参考对应的说明文档。  

## 📬 联系方式
- **实验室团队**: [IRMV](https://irmv.sjtu.edu.cn/), [SIRIUS](https://banyutong.github.io/sirius_lab_website/)  
- **电子邮件**: hsiehtpe_sjtu@sjtu.edu.cn (Hsieh Cheng-Tai)  
- **数据申请与下载**: 详见各数据集文档说明  

## 📝 更新日志
- 2025-05-16  文档创立  
- 2025-05-19  更新 EndoNeRF  
- 2025-05-20  更新 SCARED2019  
- 2025-05-25  更新 StereoMIS  
- 2025-07-15  ***v1.0.0*** 发布 GitHub 页面   
- 2025-07-22  ***v1.0.1*** 小型更新 
- 2025-09-22  
  - ***v1.1.0*** 优化github页面；增加c3vd数据集页面说明；增加视觉点追踪数据集描述；英文版本的更新。  
- 2026-01-18  
  - ***v1.2.0*** 数据拓展与任务分类更新 
  - ***v1.2.1*** 添加目录，添加英文版本markdown



## 🤝 贡献指南
- **数据提交**:  
  如需贡献新数据集，请发送邮件并附带数据说明文档（推荐使用模板 [template4dataset.md](./datasets_and_codes/template4dataset.md)）。  

- **问题反馈**:  
  如有疑问或改进建议，请通过邮件联系。  

- **推荐参考项目**:  
  [Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset)

- **贡献者清单**:  
  感谢以下贡献者对本项目的支持与付出（按贡献时间排序）：  
  - HSIEH Cheng-Tai hsiehtpe_sjtu@sjtu.edu.cn
  - ZHAN Bohan  zhanbh2000@sjtu.edu.cn

欢迎更多贡献者加入！  

## 🎬 即将推出

*coming soon*

---
