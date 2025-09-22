# IRMV Medical Datasets Collection [English Version](./english_md/README.md)

**版本**: 1.1.0  
**日期**: 2025年9月22日  
**编者**: Hsieh Cheng-Tai [@IRMV LAB](https://irmv.sjtu.edu.cn/)

## 📖 项目描述

本仓库收录并整理了适用于 **内窥镜手术场景中的三维视觉任务与机器人感知任务** 的公开数据集。  
数据包含 **内窥镜图像、视频序列、深度图、三维模型、点云、相机标定信息** 等，支持以下研究方向：  

- 视觉 SLAM  
- 结构光/神经渲染三维重建  
- 相机标定与验证  
- 几何学习  
- 手术导航算法评估
- 组织点追踪
- 手术器械分割  

本项目旨在促进 **医疗机器人** 在复杂手术场景中的 **自主感知、建图与定位能力** 等研究。

## 📂 数据集列表

### 数据集目录
- [EndoNeRF 数据集](#endonerf-数据集)
- [SCARED2019 数据集](#scared2019-数据集)
- [StereoMIS 数据集](#stereomis-数据集)
- [C3VD 数据集](#c3vd-数据集)
  
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
- 2025-07-15  发布 GitHub 页面 v1.0  
- 2025-07-22  小型更新 v1.0.1
- 2025-09-22  
  - ***v1.1.0*** 优化github页面；增加c3vd数据集页面说明；增加视觉点追踪数据集描述；英文版本的更新。  


## 🤝 贡献指南
- **数据提交**:  
  如需贡献新数据集，请发送邮件并附带数据说明文档（推荐使用模板 [template4dataset.md](./datasets_and_codes/template4dataset.md)）。  

- **问题反馈**:  
  如有疑问或改进建议，请通过邮件联系。  

- **推荐参考项目**:  
  [Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset)

- **贡献者清单**:  
  感谢以下贡献者对本项目的支持与付出（按贡献时间排序）：  
  - Hsieh Cheng-Tai hsiehtpe_sjtu@sjtu.edu.cn
  - Zhan Bohan  zhanbh2000@sjtu.edu.cn

欢迎更多贡献者加入！  

## ✅ Todo List

### GitHub 页面维护
- [x] 创建页面
- [ ] 优化目录  

### 数据集收集
- [x] EndoNeRF  
- [x] SCARED2019  
- [x] StereoMIS
- [x] C3VD  

### 预处理代码
- [ ] C3VD
- [ ] StereoMIS
---
