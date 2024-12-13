import tkinter as tk
from tkinter import messagebox
import webbrowser
import time

class AlertApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Daily Reminder")
        self.window.geometry("400x200")
        self.window.configure(bg="white")
        
        # 창을 최상위로 유지
        self.window.attributes("-topmost", True)
        
        # 초기 색상 및 상태
        self.color_index = 0
        self.colors = ["white", "lightyellow", "lightgoldenrod", "lightcoral", "red"]
        self.page_opened = False
        
        # 안내 메시지
        self.label = tk.Label(self.window, text="오늘 한 일을 적으세요!", font=("Arial", 14))
        self.label.pack(pady=20)
        
        # 버튼
        self.open_button = tk.Button(self.window, text="페이지 열기", command=self.open_page)
        self.open_button.pack(pady=10)
        
        self.close_button = tk.Button(self.window, text="종료", state=tk.DISABLED, command=self.close_app)
        self.close_button.pack(pady=10)
        
        # 색상 변화 타이머 시작
        self.start_time = time.time()
        self.change_color()
        
        self.window.mainloop()

    def change_color(self):
        elapsed = time.time() - self.start_time
        if elapsed >= 10 and self.color_index < len(self.colors) - 1:
            self.color_index += 1
            self.window.configure(bg=self.colors[self.color_index])
        
        if self.color_index < len(self.colors) - 1:  # 10초 넘었지만 마지막 색상이 아님
            self.window.after(1000, self.change_color)

    def open_page(self):
        url = "https://tmobi.atlassian.net/wiki/spaces/DNAVI/pages/915275983/018"
        webbrowser.open(url)
        self.page_opened = True
        self.close_button.config(state=tk.NORMAL)
        #messagebox.showinfo("페이지 열림", "페이지가 열렸습니다. 종료 버튼이 활성화되었습니다.")

    def close_app(self):
        if not self.page_opened:
            messagebox.showwarning("경고", "페이지를 열어야 종료할 수 있습니다.")
        else:
            self.window.destroy()

# 애플리케이션 실행
if __name__ == "__main__":
    AlertApp()
