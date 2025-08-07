import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import os
import subprocess

def run_detection(image_path):
    output_dir = 'yolov5/runs/detect/exp'

    # Xóa thư mục cũ
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)

    # Dòng lệnh đúng đường dẫn detect.py
    cmd = f"python yolov5/detect.py --weights best.pt --img 640 --conf 0.3 --source \"{image_path}\" --save-txt"
    print("Running command:", cmd)
    subprocess.run(cmd, shell=True)

    filename = os.path.basename(image_path)
    output_image_path = os.path.join(output_dir, filename)

    # Kiểm tra tồn tại ảnh
    if not os.path.exists(output_image_path):
        print("❌ Không tìm thấy ảnh kết quả!")
        return None, 0

    # Đếm unoccupied
    txt_file = os.path.join(output_dir, 'labels', os.path.splitext(filename)[0] + '.txt')
    count_unoccupied = 0
    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            for line in f:
                class_id = int(line.split()[0])
                if class_id == 1:  # sửa theo class unoccupied của bạn
                    count_unoccupied += 1

    return output_image_path, count_unoccupied


def open_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    output_image, unoccupied_count = run_detection(file_path)

    img = Image.open(output_image)
    img = img.resize((640, 480))
    img_tk = ImageTk.PhotoImage(img)
    panel.config(image=img_tk)
    panel.image = img_tk

    result_label.config(text=f"Unoccupied Slots Detected: {unoccupied_count}")

# GUI setup
root = tk.Tk()
root.title("Parking Slot Detector")

panel = Label(root)
panel.pack()

btn = tk.Button(root, text="Chọn ảnh để nhận diện", command=open_image)
btn.pack(pady=10)

result_label = Label(root, text="Unoccupied Slots Detected: 0", font=("Helvetica", 14))
result_label.pack()

root.mainloop()

