import random
import tkinter as tk
from tkinter import messagebox

def check_guess():
    try:
        user_guess = int(entry.get())
        if user_guess == number_to_guess:
            messagebox.showinfo("Результат", "Поздравляем! Вы угадали число.")
            reset_game()
        elif user_guess < number_to_guess:
            messagebox.showwarning("Результат", "Загаданное число больше.")
        else:
            messagebox.showwarning("Результат", "Загаданное число меньше.")
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите действительное число.")
        entry.delete(0, tk.END)

def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    entry.delete(0, tk.END)

number_to_guess = random.randint(1, 100)

root = tk.Tk()
root.title("Игра 'Угадай число'")

label = tk.Label(root, text="Угадайте число от 1 до 100:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Проверить", command=check_guess)
guess_button.pack(pady=10)

reset_game()
root.mainloop()
