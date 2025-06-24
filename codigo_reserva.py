import tkinter as tk 
from tkinter import messagebox
import funcoes_banco as model
from datetime import datetime

j_principal = tk.Toplevel()
j_principal.title('')
j_principal.geometry("500x400+200+200")

text_principal = tk.Label(j_principal,text='Solicitações pendentes')
text_principal.grid(row=0,column=0,padx=10,pady=10)

lista_box = tk.Listbox(j_principal, width=60)
lista_box.grid(row=1,column=1,padx=10,pady=10)

registros = model.buscar_solicitacoes_guincho()
for reg in registros:
    texto = f" Placa: {reg[0]} | Origem: {reg[1]} | Destino: {reg[2]} "
    lista_box.insert(tk.END, texto)

botao_aceitar = tk.Button(j_principal,text = 'Aceitar')
botao_aceitar.grid(row=1,column=0,padx=10,pady=10)

botao_cancelar = tk.Button(j_principal,text = 'Cancelar')
botao_cancelar.grid(row=2,column=0,padx=10,pady=10)
