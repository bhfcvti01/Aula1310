import tkinter as tk

janela = tk.Tk()
janela.title("Minha janela")
janela.geometry("300x200")

rotulo = tk.Label(janela,
                  text="Ola, Mundo!")
rotulo.pack(pady=20)

janela.mainloop()