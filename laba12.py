import tkinter as tk
from tkinter import messagebox
import json
import requests

def get_repo_data():
    repo_name = entry.get()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория в формате owner/repo")
        return

    url = f"https://api.github.com/repos/{repo_name}"
    try:
        response = requests.get(url)
        data = response.json()
        fields = ['company', 'created_at', 'email', 'id', 'name', 'url']
        
        selected_data = {}
        for field in fields:
            selected_data[field] = data.get(field)

        with open("file.json", 'w', encoding='utf-8') as f:
            json.dump(selected_data, f, ensure_ascii=False, indent=4)


    except requests.RequestException:
        messagebox.showerror("Ошибка запроса")


root = tk.Tk()
root.title("Бакутин Кирилл")

tk.Label(root, text="Введите имя репозитория (owner/repo):").pack(padx=150, pady=100)
entry = tk.Entry(root, width=40)
entry.pack(padx=4,  pady=3)
btn = tk.Button(root, text="Получить данные", command=get_repo_data)
btn.pack(padx=2, pady=2)

root.mainloop()
