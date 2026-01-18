""" 中文 使用前请阅读
代码用途: 将c3vd数据集从官网下载的格式转换为tum数据集格式
作者: Hsieh Cheng-Tai @IRMV
邮箱: hsiehtpe_sjtu@sjtu.edu.cn
创建日期: 2025年3月24日
最后修改日期: 2025年09月22日
版权所有: Hsieh Cheng-Tai @IRMV, 保留所有权利

使用说明:
1. 下载并解压c3vd数据集到本地目录。
2. 运行脚本并指定输入文件夹路径和可选的开始帧和结束帧编号。
3. 脚本将自动处理数据并生成符合TUM数据集格式的输出文件夹。

注意事项:
- 确保输入文件夹中包含所有必要的文件(如color.png, depth.tiff等)
- 确保安装了所有必要的Python库, 如opencv, numpy等
- 输出文件夹将自动创建并包含处理后的数据
- 畸变恢复系数和内参矩阵来自于@IRMV Feng Qiyu, 可以根据实际情况进行修改

范例命令:
    如果下载并解压后的文件夹路径为./desc_t4_a，则可以使用以下命令运行脚本:
    python c3vd2tum.py --input_folder ./desc_t4_a --start_frame 0 --end_frame 300 --del_raw
    如果不删除原始文件夹，则不需要添加--del_raw参数
"""

""" English Version, Please read before use
Purpose: This script is mainly used for converting the C3VD dataset format to the TUM dataset format.
Author: Hsieh Cheng-Tai @IRMV
email: hsiehtpe_sjtu@sjtu.edu.cn
Created Date: 2025 March 24
Last Modified Date: 2025 September 22
Copyright: Hsieh Cheng-Tai @IRMV, All rights reserved

Usage Instructions:
1. Download and extract the C3VD dataset to a local directory.
2. Run the script and specify the input folder path along with optional start and end frame numbers.
3. The script will automatically process the data and generate an output folder that conforms to the TUM dataset format.

Notes:
- Make sure the input folder contains all necessary files (such as color.png, depth.tiff, etc.)
- Ensure all necessary Python libraries are installed, such as opencv, numpy, etc.
- The output folder will be created automatically and will contain the processed data.
- The distortion correction coefficients and intrinsic matrix are provided by @IRMV Feng Qiyu, and can be modified according to actual conditions.

Example Command:
    If the downloaded and extracted folder path is ./desc_t4_a, you can run the script using the following command:
    python c3vd2tum.py --input_folder ./desc_t4_a --start_frame 0 --end_frame 300 --del_raw
    If you do not want to delete the original folder, you do not need to add the --del_raw parameter.
"""

import argparse
import os
import shutil
import cv2
import numpy as np
from scipy.spatial.transform import Rotation as R
from PIL import Image

def file_classification(input_folder, output_folder, start_frame, end_frame):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    rgbraw_output_folder = os.path.join(output_folder, 'rgb_raw')
    depthraw_output_folder = os.path.join(output_folder, 'depth_raw')
    normal_output_folder = os.path.join(output_folder, 'normal')
    occlusion_output_folder = os.path.join(output_folder, 'occlusion')
    flow_output_folder = os.path.join(output_folder, 'flow')
    rgb_output_folder = os.path.join(output_folder, 'rgb')
    depth_output_folder = os.path.join(output_folder, 'depth')
    if not os.path.exists(rgbraw_output_folder):
        os.makedirs(rgbraw_output_folder)
    if not os.path.exists(depthraw_output_folder):
        os.makedirs(depthraw_output_folder)
    if not os.path.exists(normal_output_folder):
        os.makedirs(normal_output_folder)
    if not os.path.exists(occlusion_output_folder):
        os.makedirs(occlusion_output_folder)
    if not os.path.exists(flow_output_folder):
        os.makedirs(flow_output_folder)
    if not os.path.exists(rgb_output_folder):
        os.makedirs(rgb_output_folder)
    if not os.path.exists(depth_output_folder):
        os.makedirs(depth_output_folder)

    frames_num = int(len(os.listdir(input_folder)) / 5)
    for frame_num in range(frames_num):
        # 如果4位数字的index没找到，尝试不补全4位的名字组合
        rgbraw_file = os.path.join(input_folder, f'{frame_num:04d}_color.png')
        if not os.path.exists(rgbraw_file):
            rgbraw_file = os.path.join(input_folder, f'{frame_num}_color.png')
        depth_output_file = os.path.join(input_folder, f'{frame_num:04d}_depth.tiff')
        normal_output_file = os.path.join(input_folder, f'{frame_num:04d}_normals.tiff')
        occlusion_output_file = os.path.join(input_folder, f'{frame_num:04d}_occlusion.png')
        flow_output_file = os.path.join(input_folder, f'{frame_num:04d}_flow.tiff')
        
        if os.path.exists(rgbraw_file) and os.path.exists(depth_output_file) and \
            os.path.exists(normal_output_file) and os.path.exists(occlusion_output_file):
            
            shutil.copy(rgbraw_file, os.path.join(rgbraw_output_folder, f'{frame_num:04d}_rawcolor.png'))
            shutil.copy(depth_output_file, os.path.join(depthraw_output_folder, f'{frame_num:04d}_rawdepth.tiff'))
            shutil.copy(normal_output_file, os.path.join(normal_output_folder, f'{frame_num:04d}_normal.tiff'))
            shutil.copy(occlusion_output_file, os.path.join(occlusion_output_folder, f'{frame_num:04d}_occlusion.png'))
            if frame_num != 0:
                shutil.copy(flow_output_file, os.path.join(flow_output_folder, f'{frame_num:04d}_flow.tiff'))
    rgb_undistored(rgbraw_output_folder, rgb_output_folder)
    rgb_undistored(depthraw_output_folder, depth_output_folder)

def rgb_undistored(input_folder, output_folder):
    # 确保输出目录存在

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # # 参数设置
    # width = 1350
    # height = 1080
    # cx = 679.544839263292
    # cy = 543.975887548343
    # fx = 769.243600037458
    # k1 = -0.000812770624150226
    # k2 = 6.25674244578925e-07
    # k3 = -1.19662182144280e-09
    # p1 = 0.00288273829525059
    # p2 = -0.00296316513429569
    # g = 0.999986882249990
 
    # 构建相机内参矩阵和畸变系数
    # camera_matrix = np.array([[fx, 0, cx],
    #                         [0, fx / g, cy],
    #                         [0, 0, 1]])
    camera_matrix = np.array([[769.243, 0, 679.544], [0, 769.243, 543.975], [0, 0, 1]])
    # dist_coeffs = np.array([k1, k2, p1, p2, k3])
    dist_coeffs = np.array([-0.42234, 0.10654, 0, 0])

    # 遍历输入目录中的所有文件
    for i, file_name in enumerate(sorted(os.listdir(input_folder))):
        input_path = os.path.join(input_folder, file_name)

        # 检查文件是否是图像
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            if file_name.lower().endswith(('.tiff')):
                output_path = os.path.join(output_folder, f'{i:04d}_depth.tiff')
            else:
                output_path = os.path.join(output_folder, f'{i:04d}_color.png')


        # 加载图像
        if file_name.lower().endswith(('.tiff')):
            image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
        else:
            image = cv2.imread(input_path)
        
        if image is None:
            print(f"无法加载图像：{input_path}")
            return
        
        image = cv2.undistort(image, camera_matrix, dist_coeffs)
        if file_name.lower().endswith(('.tiff')):
            Image.fromarray(image).save(output_path, compression=None)
        else:
            cv2.imwrite(output_path, image)

def depth_undistored(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 相机内参矩阵和畸变系数
    camera_matrix = np.array([[769.243, 0, 679.544],
                              [0, 769.243, 543.975],
                              [0, 0, 1]])
    dist_coeffs = np.array([-0.42234, 0.10654, 0, 0])

    # 获取图像尺寸（从第一张深度图获取）
    first_file = next((f for f in sorted(os.listdir(input_folder)) if f.lower().endswith('.tiff')), None)
    if first_file is None:
        print("没有找到TIFF图像文件。")
        return

    depth_img_sample = cv2.imread(os.path.join(input_folder, first_file), cv2.IMREAD_UNCHANGED)
    height, width = depth_img_sample.shape

    # 生成remap映射关系
    new_camera_matrix = camera_matrix.copy()  # 可自定义（无畸变的内参）
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(
        camera_matrix, dist_coeffs, np.eye(3), new_camera_matrix, (width, height), cv2.CV_16SC2)

    # 遍历输入目录中的所有深度图文件
    for i, file_name in enumerate(sorted(os.listdir(input_folder))):
        if file_name.lower().endswith('.tiff'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, f'{i:04d}_depth.tiff')

            # 加载深度图
            depth_image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
            if depth_image is None:
                print(f"无法加载深度图：{input_path}")
                continue

            # 使用remap进行畸变校正（最近邻插值，防止深度错误）
            depth_image_undistorted = cv2.remap(depth_image, map1, map2, interpolation=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=0)

            # 保存校正后的深度图
            cv2.imwrite(output_path, depth_image_undistorted , [cv2.IMWRITE_TIFF_COMPRESSION, 0])

def generate_depth_map_list(input_folder, output_file, start_timestamp=0.0, time_interval=0.1000):
    """
    根据目录中的图片生成深度图文件列表。

    参数:
        directory (str): 图片所在目录路径。
        output_file (str): 输出的深度图列表文件路径。
        start_timestamp (float): 起始时间戳。
        time_interval (float): 每张图片的时间间隔（单位：秒）。
    """
    try:
        # 获取目录中的所有图片文件，支持的扩展名
        image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(image_extensions)]
        image_files.sort()  # 按文件名排序

        if not image_files:
            print(f"No valid image files found in directory '{input_folder}'.")
            return

        with open(output_file, 'w') as outfile:
            # 写入头部信息
            outfile.write("# depth maps\n")
            outfile.write(f"# file: 'c3vd_{os.path.basename(os.path.dirname(input_folder))}_tiff depth'\n")
            outfile.write("# timestamp filename\n")

            # 初始化时间戳
            current_timestamp = start_timestamp

            # 遍历图片文件并写入格式化内容
            for image_file in image_files:
                # 生成文件路径
                relative_path = os.path.join('depth', image_file)
                # 写入目标格式
                outfile.write(f"{current_timestamp:.6f} {relative_path}\n")
                # 更新时间戳
                current_timestamp += time_interval


    except Exception as e:
        print(f"Error during file generation: {e}")

def generate_rgb_map_list(input_folder, output_file, start_timestamp=0.0, time_interval=0.1000):
    """
    根据目录中的图片生成RGB图文件列表。

    参数:
        directory (str): 图片所在目录路径。
        output_file (str): 输出的RGB图列表文件路径。
        start_timestamp (float): 起始时间戳。
        time_interval (float): 每张图片的时间间隔（单位：秒）。
    """
    try:
        # 获取目录中的所有图片文件，支持的扩展名
        image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(image_extensions)]
        image_files.sort()  # 按文件名排序

        if not image_files:
            print(f"No valid image files found in directory '{input_folder}'.")
            return

        with open(output_file, 'w') as outfile:
            # 写入头部信息
            outfile.write("# rgb maps\n")
            outfile.write(f"# file: 'c3vd_{os.path.basename(os.path.dirname(input_folder))}_rgb.txt'\n")
            outfile.write("# timestamp filename\n")

            # 初始化时间戳
            current_timestamp = start_timestamp

            # 遍历图片文件并写入格式化内容
            for image_file in image_files:
                # 生成文件路径
                relative_path = os.path.join('rgb', image_file)
                # 写入目标格式
                outfile.write(f"{current_timestamp:.6f} {relative_path}\n")
                # 更新时间戳
                current_timestamp += time_interval
    except Exception as e:
        print(f"Error during file generation: {e}")

def convert_pose_file(input_file, output_file, start_timestamp=0.0, time_interval=0.1000):
    """
    直接将4x4矩阵格式位姿文件转换为带时间戳和四元数的目标格式。

    参数:
        input_file (str): 输入4x4矩阵格式的位姿数据文件路径。
        output_file (str): 输出目标格式位姿数据文件路径。
        start_timestamp (float): 起始时间戳。
        time_interval (float): 每帧的时间间隔。
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # 写入目标文件的头部信息
        outfile.write("# ground truth trajectory\n")
        outfile.write(f"# file: 'c3vd_{os.path.basename(os.path.dirname(input_file))}'\n")
        outfile.write("# timestamp tx ty tz qx qy qz qw\n")

        current_timestamp = start_timestamp

        for frame_index, line in enumerate(infile):
            values = list(map(float, line.strip().split(',')))
            if len(values) != 16:
                print(f"Skipping malformed line {frame_index}: {line}")
                continue

            transformation_matrix = np.array(values).reshape(4, 4)

            # 提取平移向量
            tx, ty, tz = transformation_matrix[3, :3]

            # 提取旋转矩阵并转换为四元数
            rotation_matrix = transformation_matrix[:3, :3]
            quat = R.from_matrix(rotation_matrix).as_quat()  # [qx, qy, qz, qw]

            outfile.write(f"{current_timestamp:.6f} {tx:.6f} {ty:.6f} {tz:.6f} {quat[0]:.6f} {quat[1]:.6f} {quat[2]:.6f} {quat[3]:.6f}\n")

            current_timestamp += time_interval

    # print(f"Pose data successfully converted and saved to {output_file}")

def main():
    # 加载数据集信息
    parser = argparse.ArgumentParser(description="将C3VD数据集转换成TUM数据集格式")
    parser.add_argument('--input_folder', type=str, required=True, \
                        help='输入需要转换的C3VD文件夹路径')
    parser.add_argument('--start_frame', type=int, required=False, default=0, help='开始帧编号')
    parser.add_argument('--end_frame', type=int, required=False, default=300, help='结束帧编号')
    parser.add_argument('--del_raw', action='store_true', required=False, help='是否删除原始未处理数据')

    args = parser.parse_args()
    input_folder = args.input_folder
    output_folder = input_folder + '_tum'

    # 创建输出文件夹, 并将各类数据放入对应文件夹，同时完成去畸变
    file_classification(input_folder, output_folder, args.start_frame, args.end_frame)
    # 生成tum数据集格式所需要的txt文档
    generate_depth_map_list(os.path.join(output_folder, 'depth'), os.path.join(output_folder, 'depth.txt'))
    generate_rgb_map_list(os.path.join(output_folder, 'rgb'), os.path.join(output_folder, 'rgb.txt'))
    convert_pose_file(os.path.join(input_folder, 'pose.txt'), os.path.join(output_folder, 'groundtruth.txt'))
    # 如果del_raw参数为True，则删除input_folder
    if args.del_raw:
        print(f"正在删除原始文件夹: {input_folder}")
        shutil.rmtree(input_folder)

if __name__ == "__main__":
    main()