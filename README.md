# My YOLOv5 Project

YOLOv5: Mô hình phát hiện đối tượng thời gian thực, dùng để xác định vị trí biển số xe trong ảnh.

PyTorch: Framework deep learning phục vụ huấn luyện và triển khai mô hình YOLOv5 và VietOCR.

OpenCV: Xử lý ảnh, tiền xử lý và trích xuất vùng biển số từ ảnh gốc.

Pillow (PIL): Hỗ trợ đọc, ghi và chuyển đổi định dạng ảnh.

Tkinter: Xây dựng giao diện người dùng (GUI) để tải ảnh, hiển thị kết quả phát hiện và nhận dạng.

# Requirements

- Other dependencies in `requirements.txt`

# Installation

1. Clone the repo:  git clone https://github.com/Lm4river/Finding-and-counting-pariking-lots.git 

2. Create virtual environment:

python -m venv venv
venv\Scripts\activate  

Install dependencies:
pip install -r requirements.txt

3. Clone YOLOv5:  git clone https://github.com/ultralytics/yolov5.git

4. Add to head of file "yolov5\detect.py" :

import pathlib

pathlib.PosixPath = pathlib.WindowsPath

Thay dòng trong file yolov5/detect.py:  from ultralytics.utils.plotting import Annotator, colors, save_one_box
             
Dòng thay thế:                          from utils.plots import Annotator, colors, save_one_box

(Vì yolov5 vừa thay đổi cấu trúc ultralytics nên em fix bằng cách này )

5. Run file:  GUI.py
