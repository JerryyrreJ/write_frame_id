import os
from flask import Flask, request, send_file, render_template
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# 确保上传文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 允许的文件扩展名
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_video(input_path, position, color):
    # 读取视频
    cap = cv2.VideoCapture(input_path)
    
    # 获取视频属性
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 创建输出视频文件
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    # 设置文字属性
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    
    # 转换颜色格式（移到循环外）
    color_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    color_bgr = (color_rgb[2], color_rgb[1], color_rgb[0])  # BGR format
    
    # 处理每一帧
    frame_count = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 先进行图像翻转
        frame = cv2.flip(frame, -1)  # -1表示同时沿x轴和y轴翻转（上下左右翻转）
        
        # 准备文字
        text = f'Frame: {frame_count}'
        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
        
        # 根据位置设置文字坐标
        if position == 'top-left':
            org = (10, text_height + 10)
        elif position == 'top-right':
            org = (frame_width - text_width - 10, text_height + 10)
        elif position == 'bottom-left':
            org = (10, frame_height - 10)
        else:  # bottom-right
            org = (frame_width - text_width - 10, frame_height - 10)
        
        # 添加文字
        cv2.putText(frame, text, org, font, font_scale, color_bgr, thickness)
        
        # 写入输出视频
        out.write(frame)
        frame_count += 1
    
    # 释放资源
    cap.release()
    out.release()
    
    return output_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'video' not in request.files:
        return 'No video file uploaded', 400
        
    file = request.files['video']
    if file.filename == '':
        return 'No selected file', 400
        
    if not allowed_file(file.filename):
        return 'Invalid file type', 400
    
    # 保存上传的视频
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)
    
    # 获取位置和颜色参数
    position = request.form.get('position', 'bottom-right')
    color = request.form.get('color', '#ffffff')
    
    # 处理视频
    output_path = process_video(input_path, position, color)
    
    # 删除原始视频
    os.remove(input_path)
    
    # 返回处理后的视频
    return send_file(output_path, as_attachment=True, download_name='processed_video.mp4')

if __name__ == '__main__':
    app.run(debug=True)