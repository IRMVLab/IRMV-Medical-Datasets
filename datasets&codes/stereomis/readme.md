
# StereoMIS 数据集说明

## 📌 基本信息
StereoMIS 是一个用于内窥镜手术中同时定位与建图（SLAM）的数据集。  
该数据集使用达芬奇 Xi 手术机器人捕获立体视频流及相机前向运动学数据。  
数据来自三个体内猪受试者，总计 11 个手术序列，涵盖呼吸、手术工具运动及组织变形场景。


## 🌐 官方网页
[https://zenodo.org/records/7727692](https://zenodo.org/records/7727692)  
> ⚠ 需要 VPN 打开网页查看


## 💾 数据集下载

### 【Official】
- 下载数据集：
  ```bash
  wget 'https://zenodo.org/records/8154924/files/StereoMIS_0_0_1.zip?download=1'
  ```
- 下载 License：
  ```bash
  wget -c 'https://zenodo.org/records/8154924/files/License?download=1'
  ```

### 【DingPan】

Contact e-mail or group chat for more infomation.


\* **_irmv & sirius member only_**

## 📂 Dataset Example
第一个视频序列包含手术器械遮挡、视频、位姿真值及相机参数。


## 🚀 数据集下载说明
- 可以使用 `wget -c` 断点续传，或 `wget -b` 后台下载。
- 请务必下载 **版本 0.0.1**，版本 0.0.0 存在缺失数据问题。

**0.0.1 更新日志：**
- 补充缺失的 P3 数据
- 补充序列起始与结束帧信息


## 📝 论文引用信息

```bibtex
@article{hayoz2023pose,
  title={Learning how to robustly estimate camera pose in endoscopic videos},
  author={Michel Hayoz, Christopher Hahne, Mathias Gallardo, Daniel Candinas, Thomas Kurmann, Max Allan, Raphael Sznitman},
  journal={International Journal of Computer Assisted Radiology and Surgery 2023},
  doi={https://doi.org/10.1007/s11548-023-02919-w}
}

@dataset{hayoz_michel_2023_8154924,
  author       = {Hayoz Michel and Allan Max},
  title        = {StereoMIS},
  month        = mar,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {0.0.1},
  doi          = {10.5281/zenodo.8154924},
  url          = {https://doi.org/10.5281/zenodo.8154924},
}
```


## 🗂 数据集结构

```bash
StereoMIS/
├── sequences.txt
├── P1/
├── P2_0/
│   ├── groundtruth.txt
│   ├── StereoCalibration.ini
│   ├── xxx.mp4
│   └── masks/
│       ├── 000001l.png
│       ├── ...
│       └── 010737l.png
├── P2_1/
...
├── P2_8/
```


## 📈 序列信息表

| 序列 | 时长    | 总轨迹长度 | 原始帧率 | 提取帧率 | 分割用途 |
|------|---------|------------|----------|----------|----------|
| P1   | 5m19s   | 1323 mm    | 60 fps   | 30 fps   | train    |
| P2_0 | 3m28s   | 434 mm     | 52.6 fps | 26.3 fps | test     |
| P2_1 | 2m36s   | 1155 mm    | 54.4 fps | 27.2 fps | test     |
| P2_2 | 2m37s   | 736 mm     | 54.4 fps | 27.2 fps | test     |
| P2_3 | 2m35s   | 302 mm     | 54.4 fps | 27.2 fps | test     |
| P2_4 | 2m37s   | 1824 mm    | 54.4 fps | 27.2 fps | test     |
| P2_5 | 3m18s   | 1671 mm    | 54.2 fps | 27.1 fps | test     |
| P2_6 | 52s     | 205 mm     | 26.1 fps | 26.1 fps | test     |
| P2_7 | 2m26s   | 725 mm     | 37.0 fps | 37.0 fps | test     |
| P2_8 | 3m55s   | 950 mm     | 39.0 fps | 39.0 fps | test     |
| P3** | 2m58s   | 545 mm     | 60.0 fps | 30.0 fps | test     |

> 📝 **说明：**  
> P3 在数据集原始版本（0.0.0）中缺失。


## 📝 数据说明

- 视频文件为立体内窥镜视频（上下拼接左右眼图像）。
- 左眼图像已生成对应的手术器械掩码，可用于目标检测和分割。
- 同步的相机前向运动学数据提供随时间变化的位姿信息，用于三维重建和运动分析。
- 起止帧号 CSV 文件标记每段手术有效帧范围。


## 📊 维度与属性

| Modality    | Task Type | Sensor Type                  | Data Volume | File Format      |
|-------------|-----------|------------------------------|-------------|------------------|
| 2D Endoscope| SLAM      | Structured light + Binocular | 11.2GB      | .png, .mp4       |


## ⚙ 预处理代码

下载后需预处理视频：  
[https://github.com/aimi-lab/robust-pose-estimator](https://github.com/aimi-lab/robust-pose-estimator)

> 请在 `configuration/train.yaml` 中修改数据集路径。  
> P1 序列处理后约生成 17GB `video_frames` 文件夹。


## ✍ 编辑记录

- **作者**: 谢承泰 @IRMV
- **最后修改日期**: 2025-05-26
- **编辑历史**:
    - 2025-05-22 创建文档
    - 2025-05-24 补充数据集信息
    - 2025-05-26 更新预处理代码与下载链接


## ⚖ 使用条款

### English
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.  
View license at: [http://creativecommons.org/licenses/by-nc-sa/4.0/](http://creativecommons.org/licenses/by-nc-sa/4.0/)

### 中文
本作品采用 知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议 进行许可。  
协议副本： [http://creativecommons.org/licenses/by-nc-sa/4.0/](http://creativecommons.org/licenses/by-nc-sa/4.0/)  
如有差异，以英文版本为准。
