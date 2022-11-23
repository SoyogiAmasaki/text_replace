import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import os
import TextReplace as tr

class Application(tk.Frame):

    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.master.geometry("600x200")
        self.master.title("TextReplace")

        self.create_widgets()

    def create_widgets(self):
        # T.B.D. フレーム間で処理重複のため、共通化したい
        # Rule frame
        self.frame_rule = tk.Frame(self.master, pady=5, padx=5, relief=tk.FLAT, bd=2)

        self.rule_label_file = tk.Label(self.frame_rule)
        self.rule_label_file.configure(text='変換ルールファイルパス:', width=20)
        self.rule_label_file.pack(side=tk.LEFT)

        self.rule_file_path = tk.StringVar()
        self.rule_file_path_entry = tk.Entry(self.frame_rule, width=40)
        self.rule_file_path_entry.configure(textvariable=self.rule_file_path)
        self.rule_file_path_entry.pack(side=tk.LEFT, padx=5)

        self.rule_ref_button = tk.Button(self.frame_rule)
        self.rule_ref_button.configure(text="参照")
        self.rule_ref_button.configure(command = self.click_refer_rule_button)
        self.rule_ref_button.pack(side=tk.LEFT, padx=5)

        self.list_refresh_button = tk.Button(self.frame_rule)
        self.list_refresh_button.configure(text="リスト更新")
        self.list_refresh_button.configure(command = self.click_list_refresh_button)
        self.list_refresh_button.pack(side=tk.LEFT, padx=5)

        self.frame_rule.pack()

        # Src frame
        self.frame_src = tk.Frame(self.master, pady=5, padx=5, relief=tk.FLAT, bd=2)
    
        self.src_label_file = tk.Label(self.frame_src)
        self.src_label_file.configure(text='変換元ファイルパス:', width=20)
        self.src_label_file.pack(side=tk.LEFT)

        self.src_file_path = tk.StringVar()
        self.src_file_path_entry = tk.Entry(self.frame_src, width=40)
        self.src_file_path_entry.configure(textvariable=self.src_file_path)
        self.src_file_path_entry.pack(side=tk.LEFT, padx=5)

        self.src_ref_button = tk.Button(self.frame_src)
        self.src_ref_button.configure(text="参照")
        self.src_ref_button.configure(command = self.click_refer_src_button)
        self.src_ref_button.pack(side=tk.LEFT, padx=5)

        self.frame_src.pack()

        # Dst frame
        self.frame_dst = tk.Frame(self.master, pady=5, padx=5, relief=tk.FLAT, bd=2)
    
        self.dst_label_file = tk.Label(self.frame_dst)
        self.dst_label_file.configure(text='出力ファイルパス:', width=20)
        self.dst_label_file.pack(side=tk.LEFT)

        self.dst_file_path = tk.StringVar()
        self.dst_file_path_entry = tk.Entry(self.frame_dst, width=40)
        self.dst_file_path_entry.configure(textvariable=self.dst_file_path)
        self.dst_file_path_entry.pack(side=tk.LEFT, padx=5)

        self.dst_ref_button = tk.Button(self.frame_dst)
        self.dst_ref_button.configure(text="参照")
        self.dst_ref_button.configure(command = self.click_refer_dst_button)
        self.dst_ref_button.pack(side=tk.LEFT, padx=5)

        self.frame_dst.pack()

        # Gen frame
        self.frame_gen = tk.Frame(self.master, pady=5, padx=5, relief=tk.FLAT, bd=2)

        self.rule_combobox = ttk.Combobox(self.frame_gen)
        self.rule_combobox.configure(width=10)
        self.rule_combobox.pack(side=tk.LEFT)

        self.gen_button = tk.Button(self.frame_gen)
        self.gen_button.configure(text="生成")
        self.gen_button.configure(command = self.click_gen_button)
        self.gen_button.pack(side=tk.LEFT, padx=5)
    
        self.frame_gen.pack()

    # T.B.D. 参照ボタン処理重複のため、共通化したい
    def click_refer_rule_button(self):
        file_type = [("","*.csv")]
        initial_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = tk.filedialog.askopenfilename(filetypes = file_type, initialdir = initial_dir)
        self.rule_file_path.set(file_path)

    def click_refer_src_button(self):
        file_type = [("","*.json")]
        initial_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = tk.filedialog.askopenfilename(filetypes = file_type, initialdir = initial_dir)
        self.src_file_path.set(file_path)

    def click_refer_dst_button(self):
        file_type = [("","*.json")]
        initial_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = tk.filedialog.asksaveasfilename(filetypes = file_type, initialdir = initial_dir)
        self.dst_file_path.set(file_path)

    def click_gen_button(self):
        rule_file_path = self.rule_file_path.get()
        src_file_path = self.src_file_path.get()
        dst_file_path = self.dst_file_path.get()
        rpdata = tr.replace_txt(rule_file_path, src_file_path, self.rule_combobox.get())
        with open(dst_file_path, 'w', encoding='utf-8') as file:
            file.write(rpdata)

    def click_list_refresh_button(self):
        rule_combobox_list = tr.read_col_title(self.rule_file_path.get())
        self.rule_combobox.configure(values=rule_combobox_list)

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()