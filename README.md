# IRMV Medical Datasets README

**版本**: 1.0  
**日期**: 2025年7月15日  
**作者**:  $\color{#0089FF}{谢承泰}$  @ **IRMV LAB**


## 项目描述

本数据集专为**内窥镜手术场景中的三维视觉任务与机器人感知任务**设计，涵盖高质量的内窥镜图像数据与对应的几何信息（如点云、深度图、相机位姿与标定参数）。

数据集支持包括**视觉SLAM、结构光三维重建、相机标定验证、几何学习、手术导航算法评估**在内的多种研究任务，适用于推进**医疗机器人**在复杂手术环境中的自主感知与定位能力。


## 数据集列表

### EndoNeRF数据集

**名称**: `endonerf_sample_datasets`

**来源**: [https://med-air.github.io/EndoNeRF/](https://med-air.github.io/EndoNeRF/)  
**类型**: 内窥镜图像  
**简介**: 包含两个文件夹，`cutting_tissues_twice` 与 `pulling_soft_tissues`   
**原格式**: **LLFF**

[请至钉钉文档查看附件《EndoNeRF\_Dataset》](https://alidocs.dingtalk.com/i/nodes/l6Pm2Db8D4rEryL0hgp2yyAp8xLq0Ee4?doc_type=wiki_doc&iframeQuery=anchorId%3DX02maqg6ltisp5gn1405q)

### SCARED2019数据集

**名称**: `Stereo Correspondence and Reconstruction of Endoscopic Data`

**来源**: [https://endovissub2019-scared.grand-challenge.org/](https://endovissub2019-scared.grand-challenge.org/)  
**类型**: 双目内窥镜图像  
**简介**: 共有三个数据集（分别来自三只不同的猪），每个数据集包含5个关键帧。关键帧是通过内窥镜在唯一位置拍摄的单帧图像，同时配合结构光照明器在多个位置下的拍摄。  
**原格式**: **TIFF**格式深度图、**PNG**格式照片、相机参数信息与视频序列 （需要预处理）

[请至钉钉文档查看附件《SCARED2019\_Dataset》](https://alidocs.dingtalk.com/i/nodes/l6Pm2Db8D4rEryL0hgp2yyAp8xLq0Ee4?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mawao1mrjtyjem3jele)

### StereoMIS数据集

**名称**: `StereoMIS Data`

**来源**: [https://zenodo.org/records/7727692](https://zenodo.org/records/7727692)  
**类型**: 双目内窥镜视频序列  
**简介**: StereoMIS是内窥镜手术中同时定位和建图 (SLAM) 的数据集。使用达芬奇Xi手术机器人捕获立体视频流和相机前向运动学来记录数据集。它由三个体内猪受试者组成，具有11个手术序列，包括呼吸，工具运动和组织变形。与SCARED是同一个作者。  
**原格式**: **PNG**格式**Masks**、相机参数信息与视频序列 （需要预处理）

[StereoMIS 数据集阅读文档](dataset_md_docs/stereo_mis.md)

## 许可协议

详细参考各个数据集使用文档


## 联系方式

*   **实验室团队**: IRMV, SIRIUS
    
*   **技术支持**: hsiehtpe\_sjtu@sjtu.edu.cn  $\color{#0089FF}{谢承泰}$ 
    
*   **数据申请与下载**: 详细参考各个数据集使用文档
    

## 更新日志

*    2025-05-16  文档创立
    
*    2025-05-19  更新endonerf
    
*    2025-05-20  更新scared2019
    
*    2025-05-25  更新stereomis

*    2025-07-15  更新GitHub页面
    


## 数据下载暨阿里云使用说明
 
  ### coming soon

## 贡献指南

*   **数据提交** 
    
    如需贡献新数据集，请联系邮箱并提供数据描述文档。
    
*   **问题反馈** 
    
    发送邮件至联系邮箱进行讨论。
    
*   **推荐参考网页：**  
  
    [Awesome-Medical-Dataset](https://github.com/openmedlab/Awesome-Medical-Dataset)


## Todo List

  ### GitHub 页面维护
    

*   [x] 创建页面
    

  ### 阿里云使用说明
    

*   [ ] 编写aliyunpan下载介绍
    

  ### 数据集收集
    

*   [x] endonerf
    
*   [x] scared2019
    
*   [x] stereomis
    
    *   [x] 预处理代码编写
        
*   [ ] c3vd