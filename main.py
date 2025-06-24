import tkinter as tk
import guincho_gui as gg

def fechar():
    janela_principal.destroy()          

janela_principal = tk.Tk()
janela_principal.geometry("300x200")

frame_botoes = tk.Frame(janela_principal)
frame_botoes.pack(pady=65)
bt_entrar = tk.Button(frame_botoes,text="Entrar", command=gg.abrir_j_selecionar_login)
bt_entrar.pack(side='left',padx=5)

bt_fechar = tk.Button(frame_botoes,text="fechar", command=fechar)
bt_fechar.pack(side='left',padx=5)

#teste empresa guincho rapido456 rapido@guincho.com
#teste seguradora seg003 suporte@segurototal.com
#teste usuario adm senha123 admin1@empresa.com
janela_principal.mainloop()
