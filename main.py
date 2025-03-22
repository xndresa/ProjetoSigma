import tkinter as tk
import time

def atualizar_relogio():
    hora_atual = time.strftime("%H:%M:%S")
    label.config(text=hora_atual)
    label.after(1000, atualizar_relogio)

janela = tk.Tk()
janela.title("Relógio Digital")

label = tk.Label(janela, font=("Arial", 50), fg="white", bg="black")
label.pack(pady=20)

atualizar_relogio()
janela.mainloop()
