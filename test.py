import os
import shutil
import tkinter as tk
from tkinter import filedialog

def copy_file():
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_name = os.path.basename(selected_file)
        current_dir = os.getcwd()
        
        folder_1 = os.path.join(current_dir, "tool/PROJECT")
        folder_2 = os.path.join(current_dir, "tool/MANAGE_DBC")

        file_path_1 = os.path.join(folder_1, file_name).replace("\\","/")
        file_path_2 = os.path.join(folder_2, file_name)

        if os.path.exists(file_path_1) and os.path.exists(file_path_2):
            entry_path.delete(0, tk.END)
            entry_path.insert(tk.END, file_path_1)
        else:
            if not os.path.exists(file_path_1):
                shutil.copy(selected_file, folder_1)
                entry_path.delete(0, tk.END)
                entry_path.insert(tk.END, f"{file_path_1}")
            if not os.path.exists(file_path_2):
                shutil.copy(selected_file, folder_2)
                entry_path.delete(0, tk.END)


def on_closing():
    current_dir = os.getcwd()
    folder_2 = os.path.join(current_dir, "tool/PROJECT")
    
    # Xóa tất cả các file trừ hai file có tên adi_define.yml và new_signal.yml
    for file_name in os.listdir(folder_2):
        file_path = os.path.join(folder_2, file_name)
        try:
            if os.path.isfile(file_path) and file_name not in ["adi_define.yml", "new_signal.yml"]:
                os.remove(file_path)
        except Exception as e:
            print(f"Lỗi khi xóa file: {e}")

    root.destroy()

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Sao chép file vào hai thư mục")

# Tạo button để chọn file và gọi hàm copy_file khi nhấn
btn_choose_file = tk.Button(root, text="Chọn file để sao chép", command=copy_file)
btn_choose_file.pack(pady=20)

# Entry để hiển thị đường dẫn
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=10)

# Gọi hàm on_closing khi cửa sổ đóng lại
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
