import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")

        label = tk.Label(self, text="Hello World!")
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)

def main():
    window = Window()  #建立實體
    window.mainloop()  #一直重複
    
if __name__ == "__main__":
    main()