import tkinter as tk
from tkinter import messagebox

def calcular_media_necessaria(media_final):
  peso_semestre = 2
  limiteMedia = 15
  nota_semestre_ponderada = media_final * peso_semestre
  media_necessaria = limiteMedia - nota_semestre_ponderada
  return media_necessaria

def calcular_e_mostrar_media():
  try:
    media_final = float(entry_media_final.get())
    media_necessaria = calcular_media_necessaria(media_final)

    if media_final < 2.5 or media_final > 6.9:
      messagebox.showinfo(
        "Resultado", "Você está todo estourado na calçada, já perdeu pae")
    else:
      messagebox.showinfo(
        "Resultado",
        f"Você precisa tirar {media_necessaria:.1f} pontos para passar! Trágico!"
      )
  except ValueError:
    messagebox.showerror(
      "Erro",
      "Digite um valor numérico válido para a média final que esteja entre 2,5 e 6,9."
    )

# Criar a janela principal
root = tk.Tk()
root.title("Urubu da Repescagem")

# Definir o tamanho da janela
root.geometry("400x300")

# Criar elementos da interface
label_instrucoes = tk.Label(root,
                            text="Digite a média final com . em vez da ,:")
entry_media_final = tk.Entry(root)
botao_calcular = tk.Button(root,
                           text="Calcular",
                           command=calcular_e_mostrar_media)

# Posicionar elementos na interface
label_instrucoes.pack(pady=10)
entry_media_final.pack(pady=5)
botao_calcular.pack(pady=10)

# Iniciar loop da interface
root.mainloop()
