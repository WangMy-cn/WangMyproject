import customtkinter as ctk
import random
import os
from datetime import datetime

class MathExerciseApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("四则运算练习程序")

        self.difficulty = "easy"
        self.difficulty_var = ctk.StringVar(value=self.difficulty)

        self.difficulty_menu = ctk.CTkOptionMenu(self.root, values=["easy", "medium", "hard"], variable=self.difficulty_var, command=self.update_difficulty)
        self.difficulty_menu.pack(pady=10)

        self.score = 0
        self.load_score()

        self.score_label = ctk.CTkLabel(self.root, text=f"当前得分：{self.score}，段位：{self.get_rank()}")
        self.score_label.pack(pady=10)

        self.generate_problem()

        self.problem_label = ctk.CTkLabel(self.root, text=self.get_problem_text(), wraplength=300)
        self.problem_label.pack(pady=20)

        self.answer_entry = ctk.CTkEntry(self.root)
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.submit_answer)

        self.check_button = ctk.CTkButton(self.root, text="检查答案", command=self.check_answer)
        self.check_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self.root, text="", wraplength=300)
        self.status_label.pack(pady=10)

        self.view_stats_button = ctk.CTkButton(self.root, text="查看统计", command=self.view_stats)
        self.view_stats_button.pack(pady=10)

        self.correct_count = 0
        self.incorrect_count = 0

    def generate_problem(self):
        operations = ['+', '-', '*']
        if self.difficulty!= "easy":
            operations.append('/')

        self.operation = random.choice(operations)

        if self.difficulty == "easy":
            self.num1 = random.randint(5, 15)
            self.num2 = random.randint(5, 15)
        elif self.difficulty == "medium":
            self.num1 = random.randint(10, 50)
            self.num2 = random.randint(10, 50)
        elif self.difficulty == "hard":
            self.num1 = random.randint(50, 100)
            self.num2 = random.randint(50, 100)

        if self.operation == '+':
            self.answer = self.num1 + self.num2
        elif self.operation == '-':
            self.answer = self.num1 - self.num2
        elif self.operation == '*':
            self.answer = self.num1 * self.num2
        elif self.operation == '/':
            # Ensure division is possible and results in a whole number
            while True:
                product = self.num1 * random.randint(1, self.num2)
                if product % self.num2 == 0:
                    self.answer = self.num1
                    self.num1 = product
                    break

    def get_problem_text(self):
        return f"{self.num1} {self.operation} {self.num2} =?"

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            if int(user_answer) == self.answer:
                self.status_label.configure(text="正确！")
                self.score += 10
                self.save_score()
                self.score_label.configure(text=f"当前得分：{self.score}，段位：{self.get_rank()}")
                self.generate_problem()
                self.problem_label.configure(text=self.get_problem_text())
                self.answer_entry.delete(0, ctk.END)
                self.correct_count += 1
            else:
                self.status_label.configure(text="错误。再试试吧！")
                self.incorrect_count += 1
        except ValueError:
            self.status_label.configure(text="请输入有效的数字答案。")

    def update_difficulty(self, choice):
        self.difficulty = choice
        self.generate_problem()
        self.problem_label.configure(text=self.get_problem_text())
        self.status_label.configure(text="")

    def load_score(self):
        if os.path.exists("score.txt"):
            with open("score.txt", "r") as f:
                try:
                    self.score = int(f.read())
                except ValueError:
                    self.score = 0
        else:
            self.score = 0

    def save_score(self):
        with open("score.txt", "w") as f:
            f.write(str(self.score))

    def submit_answer(self, event=None):
        self.check_answer()

    def view_stats(self):
        today = datetime.now().date()
        stats_file = f"stats_{today}.txt"
        if os.path.exists(stats_file):
            with open(stats_file, "r") as f:
                lines = f.readlines()
                score = lines[0].strip()
                correct = lines[1].strip()
                incorrect = lines[2].strip()
                ctk.messagebox.showinfo("统计信息", f"今日得分：{score}\n答对题数：{correct}\n答错题数：{incorrect}")
        else:
            ctk.messagebox.showinfo("统计信息", "今日暂无统计数据。")
    #看起来中二的段位
    def get_rank(self):
        if self.score < 100:
            return "青铜 1 级"
        elif self.score < 200:
            return "青铜 2 级"
        elif self.score < 300:
            return "青铜 3 级"
        elif self.score < 400:
            return "白银 1 级"
        elif self.score < 500:
            return "白银 2 级"
        elif self.score < 600:
            return "白银 3 级"
        elif self.score < 700:
            return "黄金 1 级"
        elif self.score < 800:
            return "黄金 2 级"
        elif self.score < 900:
            return "黄金 3 级"
        elif self.score < 1000:
            return "铂金 1 级"
        elif self.score < 1100:
            return "铂金 2 级"
        elif self.score < 1200:
            return "铂金 3 级"
        elif self.score < 1300:
            return "钻石 1 级"
        elif self.score < 1400:
            return "钻石 2 级"
        elif self.score < 1500:
            return "钻石 3 级"
        elif self.score < 1600:
            return "星耀 1 级"
        elif self.score < 1700:
            return "星耀 2 级"
        elif self.score < 1800:
            return "星耀 3 级"
        else:
            return "计算之王"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MathExerciseApp()
    app.run()
