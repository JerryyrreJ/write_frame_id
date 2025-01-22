# 视频帧处理工具

这是一个基于Web的视频处理工具，可以为视频添加帧计数器，并支持自定义文字位置和颜色。

## 功能特点

- 支持多种视频格式（MP4、AVI、MOV）
- 拖拽上传视频文件
- 自定义文字位置（左上角、右上角、左下角、右下角）
- 自定义文字颜色
- 自动添加帧计数器

## 技术栈

- Python 3.x
- Flask 2.0.1
- OpenCV 4.5.3
- NumPy 1.21.2

## 安装步骤

1. 克隆项目到本地

2. 安装依赖包
```bash
pip install -r requirements.txt
```

## 使用方法

1. 启动服务器
```bash
python app.py
```

2. 在浏览器中访问 `http://localhost:5000`

3. 使用界面
   - 点击或拖拽上传视频文件
   - 选择文字显示位置
   - 选择文字颜色
   - 点击"处理视频"按钮
   - 等待处理完成后自动下载处理后的视频

## 注意事项

- 支持的视频格式：.mp4、.avi、.mov
- 上传文件大小限制：16MB
- 处理后的视频会自动下载，文件名为 processed_video.mp4

## 目录结构

```
.
├── app.py          # 主应用程序
├── requirements.txt # 依赖包列表
├── templates/      # HTML模板
│   └── index.html  # 主页面
└── uploads/        # 上传文件临时存储目录
```

## 开发说明

- 视频处理核心功能在 `process_video` 函数中实现
- 使用 Flask 框架处理文件上传和下载
- 使用 OpenCV 进行视频处理和帧操作
- 前端使用原生 JavaScript 实现文件拖拽上传