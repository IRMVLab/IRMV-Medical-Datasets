"""中文版本, 使用前请阅读
代码用途: 将经过robust-pose-estimator预处理后的StereoMIS数据集转换为TUM格式
作者: Hsieh Cheng-Tai @IRMV
邮箱: hsiehtpe_sjtu@sjtu.edu.cn
创建日期: 2025年07月22日
最后修改日期: 2025年09月24日
版权所有: Hsieh Cheng-Tai @IRMV, 保留所有权利

使用说明:
1. 需要使用robust-pose-estimator预处理StereoMIS数据集，方才能使用此脚本进行转换；
2. StereoMIS数据集并不包含深度图，在此脚本中使用RGB数据的右视图代替；

注意事项:
- StereoMIS数据集使用储存空间较大，转换前请确保有足够的存储空间；

范例命令:
    如果下载并解压后的文件夹路径为./P2_6, 则执行以下命令:
    python stereomis2tum.py --pre_dir P2_6 --start 1 --end 1000
"""

"""English Version, Please read before use
Purpose: This script is mainly used for converting the StereoMIS dataset preprocessed by robust-pose-estimator into TUM format
Author: Hsieh Cheng-Tai @IRMV
email: hsiehtpe_sjtu@sjtu.edu.cn
Created Date: July 22, 2025
Last Modified Date: September 24, 2025
Copyright: Hsieh Cheng-Tai @IRMV, All rights reserved

Usage Instructions:
1. Need to preprocess the StereoMIS dataset using robust-pose-estimator before using this script for conversion;
2. The StereoMIS dataset does not include depth images, in this script the right view of the RGB data is used instead;

Notes:
- The StereoMIS dataset uses a large amount of storage space. Please ensure that you have enough storage space before conversion

Example Command:
    If the path of the downloaded and extracted folder is ./P2_6, execute the following command:
    python stereomis2tum.py --pre_dir P2_6 --start 1 --end 1000
"""

import os
import shutil
import argparse
from pathlib import Path

def extract_tum_subset(in_dir, out_path, start_frame, end_frame, step):
    """
    从 in_dir 下的 groundtruth.txt 按起始帧、结束帧和 step 抽取数据，重编 timestamp 并输出 TUM 格式。
    """
    in_dir = Path(in_dir)
    gt_file = in_dir / "groundtruth.txt"
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    step = max(1, step)
    start_frame = max(0, start_frame)
    # 如果 end_frame <= 0，则取到最后一帧
    with gt_file.open("r") as fin, out_path.open("w") as fout:
        fout.write("# ground truth trajectory\n")
        fout.write(f"# file: {in_dir.name} {gt_file.name}\n")
        fout.write("# timestamp tx ty tz qx qy qz qw\n")
        idx = 0
        for i, line in enumerate(fin):
            if line.startswith("#") or line.strip() == "":
                continue
            if i < start_frame:
                continue
            if end_frame > 0 and i > end_frame:
                break
            if (i - start_frame) % step == 0:
                parts = line.strip().split()
                ts = f"{idx * 0.01:.6f}"
                fout.write(" ".join([ts] + parts[1:]) + "\n")
                idx += 1
    print(f"[OK] 已生成 {out_path}，共 {idx} 帧")

def extract_images(src_dir, dst_dir, start_frame=0, end_frame=10000, step=1):
    """
    只抽取末尾带'l'的图片，按start、end、step抽取并重命名。
    """
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)
    dst_dir.mkdir(exist_ok=True)
    # 除了深度图选右视图RGB，其余只选取左视图
    if 'depth' in dst_dir.name:
        img_files = sorted([p for p in src_dir.glob("*r.png")])
    else:
        img_files = sorted([p for p in src_dir.glob("*l.png")])
    img_files = img_files[start_frame:end_frame+1]
    for idx, img_path in enumerate(img_files):
        if idx % step == 0:
            new_name = f"{int(idx/step)*0.01:.6f}.png"
            shutil.copy(img_path, dst_dir / new_name)
    print(f"[OK] 已抽取图片到 {dst_dir}")

def generate_img_txt(img_dir, txt_path):
    """
    生成类似 TUM 格式的 rgb.txt 或 depth.txt 文件。
    """
    img_dir = Path(img_dir)
    txt_path = Path(txt_path)
    img_files = sorted(img_dir.glob("*.png"), key=lambda x: float(x.stem))
    with txt_path.open("w") as f:
        f.write("# timestamp filename\n")
        for img in img_files:
            ts = img.stem
            f.write(f"{ts} {img_dir.name}/{img.name}\n")
    print(f"[OK] 已生成 {txt_path}，共 {len(img_files)} 帧")

def copy_extra_files(in_dir, out_dir):
    """
    复制 StereoCalibration.ini 和 testsplit*.csv 文件到输出目录
    """
    in_dir = Path(in_dir)
    out_dir = Path(out_dir)
    # StereoCalibration.ini
    ini_file = in_dir / "StereoCalibration.ini"
    if ini_file.exists():
        shutil.copy(ini_file, out_dir / "StereoCalibration.ini")
        print(f"[OK] 已复制 {ini_file.name}")
    # testsplit*.csv
    for csv_file in in_dir.glob("test_split.csv"):
        shutil.copy(csv_file, out_dir / csv_file.name)
        print(f"[OK] 已复制 {csv_file.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="转换为 TUM 格式数据集")
    parser.add_argument("--pre_dir", type=str, required=True, help="经预处理的数据路径")
    parser.add_argument("--start", type=int, default=0, help="起始帧编号，默认 0")
    parser.add_argument("--end", type=int, default=10000, help="结束帧编号，默认 0")
    parser.add_argument("--step", type=int, default=1, help="抽取步长，默认 1")
    args = parser.parse_args()

    in_dir = args.pre_dir
    start_frame = args.start
    end_frame = args.end if args.end > 0 else 10000
    step = args.step if args.step > 0 else 1
    out_dir = in_dir + "_tum"
    out_file = f"{out_dir}/groundtruth.txt"

    copy_extra_files(in_dir, out_dir)
    extract_tum_subset(in_dir, out_file, start_frame, end_frame, step)
    extract_images(os.path.join(in_dir, "video_frames"), f"{out_dir}/rgb", start_frame, end_frame, step)
    # stereomis没有深度图，在函数中用RGB数据的右视图代替
    extract_images(os.path.join(in_dir, "video_frames"), f"{out_dir}/depth", start_frame, end_frame, step)
    extract_images(os.path.join(in_dir, "masks"), f"{out_dir}/masks", start_frame, end_frame, step)
    generate_img_txt(f"{out_dir}/rgb", f"{out_dir}/rgb.txt")
    generate_img_txt(f"{out_dir}/depth", f"{out_dir}/depth.txt")


