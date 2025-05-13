import tkinter as tk

def fazer_botao():
    janela.geometry("1280x600")

def fazer_botao2():
    janela.geometry("400x400")

janela = tk.Tk()
janela.geometry("400x400")  
janela.title("RetroTech")


janela.config(bg="#2E2E2E")


botao = tk.Button(janela, text="Redimensionar", command=fazer_botao, font=("Arial", 14), fg="#FFFFFF", bg="#4CAF50", relief="raised", bd=5)
botao.pack(pady=50, ipadx=20, ipady=10)

botao2 =tk.Button(janela, text="Default",command=fazer_botao2, font=("Arial", 14), fg="#FFFFFF", bg="#4CAF50", relief="raised", bd=5)
botao2.pack(pady=20, ipadx=20, ipady=10)

janela.mainloop()
