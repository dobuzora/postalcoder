import sys
import tkinter as tk

class PostalCoder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("postalcoder")
        master.geometry("400x300")
        self.pack()
        self.create_widgets()
        self.address = {}
        self.input_data()

    def input_data(self):
        fp = open("./okinawa-post/47OKINAW.CSV", "rt", encoding="shift_jis")
        for line in fp:
            line = line.replace(' ', '')
            line = line.replace('"', '')
            cells = line.split(",")
            zipno = cells[2] # 郵便番号
            ken = cells[6] # 都道府県
            shi = cells[7] # 市区
            cho = cells[8] # 市区以下
            title = ken + shi + cho
            self.address[zipno] = title
        fp.close()

    def create_widgets(self):
        # ラベル
        self.label = tk.Label(self)
        self.label["text"] = "\n郵便番号を入力してください"
        self.label.pack()

        # 入力フォーム
        self.edit_box = tk.Entry(self)
        self.edit_box.pack()

        # 検索ボタンアクション
        self.search = tk.Button(self)
        self.search["text"] = "検索"
        self.search["command"] = self.post_search
        self.search.pack(side="top")

        # 警告用
        self.warning = tk.Label(self)
        self.warning["text"] = ""
        self.warning.pack()

        # 住所出力
        self.ans = tk.Label(self)
        self.ans["text"] = ""
        self.ans.pack()
        
        # 終了アクション
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def post_search(self):
        value = self.edit_box.get()
        self.ans["text"] = self.validate(value)
        self.ans.pack()

    def validate(self, text):
        try :
            num = int(text)
        except:
            self.error("不適切な入力です")
            return ""
        
        if text in self.address:
            return self.address[text]
        else : 
            self.error("対応する住所がありません")
            return ""

    def error(self, msg):
        print("[ERROR] ", msg)
        self.warning["text"] = msg
        self.warning.pack()

root = tk.Tk()
app = PostalCoder(master=root)
app.mainloop()

