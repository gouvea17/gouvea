import tkinter as tk
import subprocess as sb


def abrir_janela1():
    sb.Popen(["python", "janela1.py"])


def abrir_janela2():
    sb.Popen(["python", "janela2.py"])


janela = tk.Tk()
janela.geometry("500x500")
janela.title("RetroTech")



janela.config(bg="#2E2E2E")


titulo = tk.Label(janela, text="Bem-vindo ao RetroTech", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#2E2E2E")
titulo.pack(pady=40)

janela1 = tk.Button(janela, text="Abrir Janela 1", command=abrir_janela1, font=("Arial", 16), fg="#FFFFFF", bg="#4CAF50", relief="raised", bd=5)
janela1.pack(pady=20, ipadx=10, ipady=10)


janela2 = tk.Button(janela, text="Abrir Janela 2", command=abrir_janela2, font=("Arial", 16), fg="#FFFFFF", bg="#FF5722", relief="raised", bd=5)
janela2.pack(pady=20, ipadx=10, ipady=10)


janela.mainloop()
