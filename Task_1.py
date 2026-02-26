import customtkinter as ctk
import sqlite3

# --- Database Management ---
class DatabaseHelper:
    def __init__(self, db_name="tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_text TEXT NOT NULL,
                priority TEXT NOT NULL,
                is_completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_task(self, text, priority):
        self.cursor.execute("INSERT INTO tasks (task_text, priority, is_completed) VALUES (?, ?, 0)", (text, priority))
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks ORDER BY is_completed ASC, id DESC")
        return self.cursor.fetchall()

    def toggle_task(self, task_id, is_completed):
        self.cursor.execute("UPDATE tasks SET is_completed = ? WHERE id = ?", (is_completed, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

# --- Main UI Application ---
class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # App Configuration
        self.title("Taskes To-Do")
        self.geometry("500x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.db = DatabaseHelper()
        
        # Priority Colors
        self.priority_colors = {"High": "#ff4a4a", "Medium": "#ffb84d", "Low": "#4dff88"}

        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        # Header
        self.header_label = ctk.CTkLabel(self, text="My Tasks", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.pack(pady=(20, 10))

        # Input Frame (Entry + Dropdown + Button)
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter a new task...", width=250)
        self.task_entry.pack(side="left", padx=(0, 10))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        self.priority_var = ctk.StringVar(value="Medium")
        self.priority_menu = ctk.CTkOptionMenu(self.input_frame, values=["High", "Medium", "Low"], variable=self.priority_var, width=90)
        self.priority_menu.pack(side="left", padx=(0, 10))

        self.add_button = ctk.CTkButton(self.input_frame, text="Add", width=60, command=self.add_task)
        self.add_button.pack(side="left")

        # Scrollable Task List
        self.task_list_frame = ctk.CTkScrollableFrame(self, width=450, height=400)
        self.task_list_frame.pack(pady=10, padx=20, fill="both", expand=True)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        priority = self.priority_var.get()
        
        if task_text:
            self.db.add_task(task_text, priority)
            self.task_entry.delete(0, 'end')
            self.load_tasks()

    def load_tasks(self):
        # Clear existing widgets in the scrollable frame
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        tasks = self.db.get_all_tasks()
        
        for task in tasks:
            task_id, task_text, priority, is_completed = task
            self.create_task_row(task_id, task_text, priority, is_completed)

    def create_task_row(self, task_id, task_text, priority, is_completed):
        row_frame = ctk.CTkFrame(self.task_list_frame, corner_radius=8)
        row_frame.pack(fill="x", pady=5, padx=5)

        # Checkbox for completion
        check_var = ctk.IntVar(value=is_completed)
        
        def on_toggle(t_id=task_id, var=check_var):
            self.db.toggle_task(t_id, var.get())
            self.load_tasks() # Refresh to sort completed to bottom

        checkbox = ctk.CTkCheckBox(
            row_frame, 
            text=task_text, 
            variable=check_var, 
            command=on_toggle,
            font=ctk.CTkFont(overstrike=bool(is_completed), size=14)
        )
        checkbox.pack(side="left", padx=10, pady=10)

        # Priority Indicator
        priority_label = ctk.CTkLabel(
            row_frame, 
            text=f" {priority} ", 
            text_color=self.priority_colors[priority],
            font=ctk.CTkFont(size=10, weight="bold")
        )
        priority_label.pack(side="right", padx=10)

        # Delete Button
        delete_btn = ctk.CTkButton(
            row_frame, 
            text="✕", 
            width=30, 
            fg_color="#ff4a4a", 
            hover_color="#cc0000",
            command=lambda t_id=task_id: self.delete_task(t_id)
        )
        delete_btn.pack(side="right", padx=5)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)
        self.load_tasks()

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()