import tkinter as tk
from tkinter import ttk, messagebox

class ScreenGuideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Guide - Screen Time Management")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")

        # Configure style
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("Arial", 16, "bold"))
        self.style.configure("Header.TLabel", font=("Arial", 12, "bold"))
        self.style.configure("Info.TLabel", font=("Arial", 10))

        # Create main notebook for tabs ?????????????????
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.create_dashboard_tab()
        self.create_monitoring_tab()
        self.create_categorization_tab()
        self.create_blockers_tab()
        self.create_chatbot_tab()
        self.create_goals_tab()

        # Status bar ?????????????????
        self.status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_dashboard_tab(self):
        dashboard_frame = ttk.Frame(self.notebook)
        self.notebook.add(dashboard_frame, text="Dashboard")

        # Title
        title_label = ttk.Label(dashboard_frame, text="Screen Time Dashboard", style="Title.TLabel")
        title_label.pack(pady=10)

        # Today's stats frame
        stats_frame = ttk.LabelFrame(dashboard_frame, text="Today's Statistics")
        stats_frame.pack(fill="x", padx=20, pady=10)

        # Stats grid
        stats_grid = ttk.Frame(stats_frame)
        stats_grid.pack(fill="x", padx=10, pady=10)

        # Total screen time
        ttk.Label(stats_grid, text="Total Screen Time:", style="Header.TLabel").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.total_time_label = ttk.Label(stats_grid, text="0h 0m", style="Info.TLabel")
        self.total_time_label.grid(row=0, column=1, sticky="w", padx=5, pady=2)

        # Productive time
        ttk.Label(stats_grid, text="Productive Time:", style="Header.TLabel").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.productive_time_label = ttk.Label(stats_grid, text="0h 0m", style="Info.TLabel")
        self.productive_time_label.grid(row=1, column=1, sticky="w", padx=5, pady=2)

        # Entertainment time
        ttk.Label(stats_grid, text="Entertainment Time:", style="Header.TLabel").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.entertainment_time_label = ttk.Label(stats_grid, text="0h 0m", style="Info.TLabel")
        self.entertainment_time_label.grid(row=2, column=1, sticky="w", padx=5, pady=2)

        # Productivity score
        ttk.Label(stats_grid, text="Productivity Score:", style="Header.TLabel").grid(row=3, column=0, sticky="w", padx=5, pady=2)
        self.productivity_score_label = ttk.Label(stats_grid, text="0%", style="Info.TLabel")
        self.productivity_score_label.grid(row=3, column=1, sticky="w", padx=5, pady=2)

        # Quick actions frame
        actions_frame = ttk.LabelFrame(dashboard_frame, text="Quick Actions")
        actions_frame.pack(fill="x", padx=20, pady=10)

        buttons_frame = ttk.Frame(actions_frame)
        buttons_frame.pack(pady=10)

        ttk.Button(buttons_frame, text="View Report", command=self.view_report).grid(row=0, column=2, padx=5)
        ttk.Button(buttons_frame, text="Settings", command=self.open_settings).grid(row=0, column=3, padx=5)

    def create_monitoring_tab(self):
        monitoring_frame = ttk.Frame(self.notebook)
        self.notebook.add(monitoring_frame, text="Monitoring")

        # Title
        title_label = ttk.Label(monitoring_frame, text="Screen Monitoring", style="Title.TLabel")
        title_label.pack(pady=10)

        # Status frame
        status_frame = ttk.LabelFrame(monitoring_frame, text="Monitoring Status")
        status_frame.pack(fill="x", padx=20, pady=10)

        self.monitoring_status_label = ttk.Label(status_frame, text="Not Monitoring", font=("Arial", 12))
        self.monitoring_status_label.pack(pady=10)

        # Controls frame
        controls_frame = ttk.LabelFrame(monitoring_frame, text="Controls")
        controls_frame.pack(fill="x", padx=20, pady=10)

        button_frame = ttk.Frame(controls_frame)
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(button_frame, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = ttk.Button(button_frame, text="Stop Monitoring", command=self.stop_monitoring, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=5)

        ttk.Button(button_frame, text="Reset Data", command=self.reset_data).grid(row=0, column=2, padx=5)

        # Active apps frame
        apps_frame = ttk.LabelFrame(monitoring_frame, text="Currently Active Applications")
        apps_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview for apps
        columns = ("App", "Time Spent", "Category")
        self.apps_tree = ttk.Treeview(apps_frame, columns=columns, show="headings", height=10)

        for col in columns:
            self.apps_tree.heading(col, text=col)
            self.apps_tree.column(col, width=150)

        self.apps_tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(apps_frame, orient="vertical", command=self.apps_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.apps_tree.configure(yscrollcommand=scrollbar.set)

    def create_categorization_tab(self):
        categorization_frame = ttk.Frame(self.notebook)
        self.notebook.add(categorization_frame, text="Categorization")

        # Title
        title_label = ttk.Label(categorization_frame, text="Content Categorization", style="Title.TLabel")
        title_label.pack(pady=10)

        # Instructions
        info_label = ttk.Label(categorization_frame, text="Categorize on-screen content into study, skills, games, entertainment, etc.", style="Info.TLabel")
        info_label.pack(pady=5)

        # Categories frame
        cats_frame = ttk.LabelFrame(categorization_frame, text="Content Categories")
        cats_frame.pack(fill="x", padx=20, pady=10)

        # Category list
        categories = ["Study/Education", "Skill Development", "Games", "Entertainment", "Social Media", "Productivity Tools", "Other"]

        for i, category in enumerate(categories):
            frame = ttk.Frame(cats_frame)
            frame.pack(fill="x", padx=10, pady=2)

            ttk.Label(frame, text=f"{category}:", width=18).pack(side="left", padx=5)
            ttk.Label(frame, text="0%", width=10).pack(side="left", padx=5)
            progress = ttk.Progressbar(frame, length=200, mode='determinate')
            progress.pack(side="left", padx=5, fill="x", expand=True)
            setattr(self, f"{category.lower().replace('/', '_').replace(' ', '_')}_progress", progress)

       
    def create_blockers_tab(self):
        blockers_frame = ttk.Frame(self.notebook)
        self.notebook.add(blockers_frame, text="Blockers")

        # Title
        title_label = ttk.Label(blockers_frame, text="Content Blockers", style="Title.TLabel")
        title_label.pack(pady=10)

        # Instructions
        info_label = ttk.Label(blockers_frame, text="Create blockers for specific content to help manage screen time", style="Info.TLabel")
        info_label.pack(pady=5)

        # Active blockers frame
        active_frame = ttk.LabelFrame(blockers_frame, text="Active Blockers")
        active_frame.pack(fill="x", padx=20, pady=10)

        # Treeview for blockers
        blocker_columns = ("Target", "Action", "Status")
        self.blockers_tree = ttk.Treeview(active_frame, columns=blocker_columns, show="headings", height=6)

        for col in blocker_columns:
            self.blockers_tree.heading(col, text=col)
            self.blockers_tree.column(col, width=200)

        self.blockers_tree.pack(fill="x", padx=10, pady=10)

        # Scrollbar for blockers
        blocker_scroll = ttk.Scrollbar(active_frame, orient="vertical", command=self.blockers_tree.yview)
        blocker_scroll.pack(side="right", fill="y")
        self.blockers_tree.configure(yscrollcommand=blocker_scroll.set)

        # Add blocker frame
        add_frame = ttk.LabelFrame(blockers_frame, text="Add New Blocker")
        add_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(add_frame, text="Target App/Website:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.blocker_target_entry = ttk.Entry(add_frame, width=30)
        self.blocker_target_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_frame, text="Action:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.blocker_action_var = tk.StringVar()
        action_combo = ttk.Combobox(add_frame, textvariable=self.blocker_action_var,
                                   values=["Block Completely", "Show Warning", "Limit Time"], width=27)
        action_combo.grid(row=1, column=1, padx=5, pady=5)
        action_combo.set("Select Action")

        ttk.Button(add_frame, text="Add Blocker", command=self.add_blocker).grid(row=2, column=0, columnspan=2, pady=10)

    def create_chatbot_tab(self):
        chatbot_frame = ttk.Frame(self.notebook)
        self.notebook.add(chatbot_frame, text="Chatbot")

        # Title
        title_label = ttk.Label(chatbot_frame, text="Screen Time Assistant", style="Title.TLabel")
        title_label.pack(pady=10)

        # Chat display
        chat_frame = ttk.LabelFrame(chatbot_frame, text="Conversation")
        chat_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.chat_display = tk.Text(chat_frame, height=15, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_display.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar for chat
        chat_scroll = ttk.Scrollbar(chat_frame, orient="vertical", command=self.chat_display.yview)
        chat_scroll.pack(side="right", fill="y")
        self.chat_display.configure(yscrollcommand=chat_scroll.set)

        # Input frame
        input_frame = ttk.Frame(chatbot_frame)
        input_frame.pack(fill="x", padx=20, pady=10)

        ttk.Label(input_frame, text="You:").pack(side=tk.LEFT, padx=(0,5))
        self.user_input = ttk.Entry(input_frame, width=50)
        self.user_input.pack(side=tk.LEFT, fill="x", expand=True, padx=5)
        self.user_input.bind("<Return>", self.send_message)

        ttk.Button(input_frame, text="Send", command=self.send_message).pack(side=tk.LEFT, padx=5)

        # Initial message
        self.add_chat_message("Assistant", "Hello! I'm your Screen Time Assistant. I can help you monitor your screen usage, provide productivity tips, and answer questions about managing your digital wellbeing. How can I assist you today?")

    def create_goals_tab(self):
        goals_frame = ttk.Frame(self.notebook)
        self.notebook.add(goals_frame, text="Goals & Streaks")

        # Title
        title_label = ttk.Label(goals_frame, text="Goals and Streaks", style="Title.TLabel")
        title_label.pack(pady=10)

        # Daily goals frame
        daily_frame = ttk.LabelFrame(goals_frame, text="Daily Goals")
        daily_frame.pack(fill="x", padx=20, pady=10)

        goals_grid = ttk.Frame(daily_frame)
        goals_grid.pack(fill="x", padx=10, pady=10)

        ttk.Label(goals_grid, text="Max Screen Time:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.max_time_var = tk.StringVar(value="2 hours")
        ttk.Entry(goals_grid, textvariable=self.max_time_var, width=15).grid(row=0, column=1, sticky="w", padx=5, pady=2)

        ttk.Label(goals_grid, text="Min Productive Time:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.min_productive_var = tk.StringVar(value="1 hour")
        ttk.Entry(goals_grid, textvariable=self.min_productive_var, width=15).grid(row=1, column=1, sticky="w", padx=5, pady=2)

        ttk.Label(goals_grid, text="Max Social Media:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.max_social_var = tk.StringVar(value="30 minutes")
        ttk.Entry(goals_grid, textvariable=self.max_social_var, width=15).grid(row=2, column=1, sticky="w", padx=5, pady=2)

        ttk.Button(goals_grid, text="Save Goals", command=self.save_goals).grid(row=3, column=0, columnspan=2, pady=10)

        # Streaks frame
        streaks_frame = ttk.LabelFrame(goals_frame, text="Your Streaks")
        streaks_frame.pack(fill="x", padx=20, pady=10)

        streaks_grid = ttk.Frame(streaks_frame)
        streaks_grid.pack(fill="x", padx=10, pady=10)

        ttk.Label(streaks_grid, text="Days Met Goals:", style="Header.TLabel").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.streak_label = ttk.Label(streaks_grid, text="0 days", style="Info.TLabel", font=("Arial", 10, "bold"))
        self.streak_label.grid(row=0, column=1, sticky="w", padx=5, pady=2)

        ttk.Label(streaks_grid, text="Current Streak:", style="Header.TLabel").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.current_streak_label = ttk.Label(streaks_grid, text="0 days", style="Info.TLabel")
        self.current_streak_label.grid(row=1, column=1, sticky="w", padx=5, pady=2)

        # Motivational quotes frame
        quote_frame = ttk.LabelFrame(goals_frame, text="Motivation")
        quote_frame.pack(fill="x", padx=20, pady=10)

        self.quote_label = ttk.Label(quote_frame, text='"The best way to predict the future is to create it." - Peter Drucker',
                                   wraplength=400, justify=tk.CENTER)
        self.quote_label.pack(pady=10)

    # Methods for functionality (stubs for now)
    def start_monitoring(self):
        self.monitoring_status_label.config(text="Monitoring Active", foreground="green")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.status_bar.config(text="Monitoring started...")
        messagebox.showinfo("Monitoring", "Screen time monitoring has started.")

    def stop_monitoring(self):
        self.monitoring_status_label.config(text="Not Monitoring", foreground="red")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_bar.config(text="Monitoring stopped.")
        messagebox.showinfo("Monitoring", "Screen time monitoring has stopped.")

    def reset_data(self):
        if messagebox.askyesno("Reset Data", "Are you sure you want to reset all monitoring data?"):
            self.status_bar.config(text="Data reset.")
            messagebox.showinfo("Reset", "All monitoring data has been reset.")

    def view_report(self):
        messagebox.showinfo("Report", "Generating detailed report...\n(Feature coming soon)")

    def open_settings(self):
        messagebox.showinfo("Settings", "Opening settings panel...\n(Feature coming soon)")

    def add_categorization_rule(self):
        app = self.app_entry.get()
        category = self.category_var.get()
        if app and category != "Select Category":
            messagebox.showinfo("Success", f"Added categorization rule: {app} -> {category}")
            self.app_entry.delete(0, tk.END)
            self.category_var.set("Select Category")
        else:
            messagebox.showwarning("Input Error", "Please enter both an application and select a category.")

    def generate_productivity_report(self):
        messagebox.showinfo("Report", "Generating productivity report...\n(Feature coming soon)")

    def export_data(self):
        messagebox.showinfo("Export", "Exporting data...\n(Feature coming soon)")

    def add_blocker(self):
        target = self.blocker_target_entry.get()
        action = self.blocker_action_var.get()
        if target and action != "Select Action":
            # Add to treeview
            self.blockers_tree.insert("", tk.END, values=(target, action, "Active"))
            self.blocker_target_entry.delete(0, tk.END)
            self.blocker_action_var.set("Select Action")
            messagebox.showinfo("Success", f"Added blocker for {target} with action: {action}")
        else:
            messagebox.showwarning("Input Error", "Please enter both a target and select an action.")

    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if message:
            self.add_chat_message("You", message)
            self.user_input.delete(0, tk.END)
            # Simulate bot response (in real app, this would call an AI API)
            self.root.after(500, lambda: self.add_chat_message("Assistant",
                "I understand your concern about screen time. Let me check your current stats and provide personalized advice."))

    def add_chat_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def save_goals(self):
        messagebox.showinfo("Goals Saved", "Your daily goals have been saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenGuideApp(root)
    root.mainloop()