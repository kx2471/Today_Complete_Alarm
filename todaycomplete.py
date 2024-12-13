import tkinter as tk
from tkinter import messagebox
import webbrowser
from datetime import datetime
import time

class AlertApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Daily Reminder")
        self.window.geometry("400x200")
        self.window.configure(bg="white")
        self.window.attributes("-topmost", True)

        self.color_index = 0
        self.colors = ["white", "lightyellow", "lightgoldenrod", "lightcoral", "red"]
        self.page_opened = False

        self.label = tk.Label(self.window, text="오늘 한 일을 적으세요!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.open_button = tk.Button(self.window, text="페이지 열기", command=self.open_page)
        self.open_button.pack(pady=10)

        self.close_button = tk.Button(self.window, text="종료", state=tk.DISABLED, command=self.close_app)
        self.close_button.pack(pady=10)

        self.start_time = time.time()
        self.change_color()

        self.window.mainloop()

    def change_color(self):
        elapsed = time.time() - self.start_time
        if elapsed >= 10 and self.color_index < len(self.colors) - 1:
            self.color_index += 1
            self.window.configure(bg=self.colors[self.color_index])
        
        if self.color_index < len(self.colors) - 1:
            self.window.after(1000, self.change_color)

    def open_page(self):
        url = "https://tmobi.atlassian.net/wiki/spaces/DNAVI/pages/915275983/018"
        webbrowser.open(url)
        self.page_opened = True
        self.close_button.config(state=tk.NORMAL)

    def close_app(self):
        if not self.page_opened:
            messagebox.showwarning("경고", "페이지를 열어야 종료할 수 있습니다.")
        else:
            self.window.destroy()

# 백그라운드에서 실행 대기
def check_time():
    target_hour = 17  # 5시
    target_minute = 0  # 정각
    while True:
        now = datetime.now()
        if now.hour == target_hour and now.minute == target_minute:
            AlertApp()  # 알람 실행
            break
        time.sleep(30)  # 30초마다 시간 확인

if __name__ == "__main__":
    check_time()
