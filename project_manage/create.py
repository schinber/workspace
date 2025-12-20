import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import datetime


class FlaskProjectGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Flask项目结构生成器")
        self.root.geometry("900x700")
        self.root.resizable(True, True)

        # 项目结构定义（不包含注释）
        self.project_structure = {
            'app': {
                '__init__.py': '',
                'models.py': '',
                'routes.py': '',
                'static': {
                    'css': {
                        'style.css': ''
                    }
                },
                'templates': {
                    'base.html': '',
                    'login.html': '',
                    'admin': {
                        'dashboard.html': '',
                        'manage_users.html': '',
                        'manage_students.html': ''
                    },
                    'teacher': {
                        'dashboard.html': ''
                    },
                    'student': {
                        'profile.html': ''
                    }
                }
            },
            'config.py': '',
            'run.py': '',
            'requirements.txt': ''
        }

        self.setup_ui()

    def setup_ui(self):
        # 主容器
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="Flask项目结构生成器",
            font=('Arial', 18, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # 输入区域
        input_frame = ttk.LabelFrame(main_frame, text="项目配置", padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

        # 项目名称
        ttk.Label(input_frame, text="项目名称：").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.project_name_var = tk.StringVar(value="student_management_system")
        self.project_name_entry = ttk.Entry(input_frame, textvariable=self.project_name_var, width=30)
        self.project_name_entry.grid(row=0, column=1, sticky=tk.W, pady=5, padx=(5, 0))

        # 根目录选择
        ttk.Label(input_frame, text="根目录：").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.root_path_var = tk.StringVar(value=os.path.expanduser("~"))
        self.root_path_entry = ttk.Entry(input_frame, textvariable=self.root_path_var, width=30)
        self.root_path_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=(5, 0))

        browse_btn = ttk.Button(input_frame, text="浏览...", command=self.browse_directory)
        browse_btn.grid(row=1, column=2, sticky=tk.W, pady=5, padx=(5, 0))

        # 操作按钮
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=(20, 0))

        create_btn = ttk.Button(button_frame, text="创建项目", command=self.create_project, width=15)
        create_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(button_frame, text="清空表单", command=self.clear_form, width=15)
        clear_btn.pack(side=tk.LEFT, padx=5)

        exit_btn = ttk.Button(button_frame, text="退出", command=self.root.quit, width=15)
        exit_btn.pack(side=tk.LEFT, padx=5)

        # 预览区域
        preview_frame = ttk.LabelFrame(main_frame, text="项目结构预览", padding="10")
        preview_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))

        # 树形视图
        self.tree = ttk.Treeview(preview_frame, height=20)
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 滚动条
        scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)

        # 填充树形视图
        self.populate_tree('', self.project_structure)

        # 状态栏
        self.status_var = tk.StringVar(value="就绪")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))

        # 配置列权重
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(0, weight=1)

    def populate_tree(self, parent, structure):
        """递归填充树形视图"""
        for name, content in structure.items():
            item = self.tree.insert(parent, 'end', text=name, open=True)
            if isinstance(content, dict):
                self.populate_tree(item, content)

    def browse_directory(self):
        """选择根目录"""
        directory = filedialog.askdirectory(initialdir=self.root_path_var.get())
        if directory:
            self.root_path_var.set(directory)

    def create_structure(self, base_path, structure):
        """递归创建目录和文件"""
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                # 创建目录
                try:
                    os.makedirs(path, exist_ok=True)
                    self.status_var.set(f"创建目录: {path}")
                    self.root.update()
                except Exception as e:
                    messagebox.showerror("错误", f"创建目录失败: {path}\n{str(e)}")
                    return False

                # 递归创建子结构
                if not self.create_structure(path, content):
                    return False
            else:
                # 创建文件
                try:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    self.status_var.set(f"创建文件: {path}")
                    self.root.update()
                except Exception as e:
                    messagebox.showerror("错误", f"创建文件失败: {path}\n{str(e)}")
                    return False
        return True

    def create_project(self):
        """创建项目"""
        project_name = self.project_name_var.get().strip()
        root_path = self.root_path_var.get().strip()

        if not project_name:
            messagebox.showwarning("警告", "请输入项目名称！")
            return

        if not root_path:
            messagebox.showwarning("警告", "请选择根目录！")
            return

        if not os.path.exists(root_path):
            messagebox.showwarning("警告", "根目录不存在！")
            return

        # 完整项目路径
        project_path = os.path.join(root_path, project_name)

        # 检查项目是否已存在
        if os.path.exists(project_path):
            if not messagebox.askyesno("确认", f"项目 '{project_name}' 已存在，是否继续并可能覆盖现有文件？"):
                return

        # 创建项目
        self.status_var.set("正在创建项目...")
        self.root.config(cursor="watch")
        self.root.update()

        success = self.create_structure(root_path, {project_name: self.project_structure})

        self.root.config(cursor="")
        if success:
            self.status_var.set(f"项目 '{project_name}' 创建成功！")
            messagebox.showinfo("成功", f"项目 '{project_name}' 已成功创建在:\n{project_path}")
        else:
            self.status_var.set("项目创建失败！")

    def clear_form(self):
        """清空表单"""
        self.project_name_var.set("student_management_system")
        self.root_path_var.set(os.path.expanduser("~"))
        self.status_var.set("就绪")


def main():
    root = tk.Tk()
    app = FlaskProjectGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()