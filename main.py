#janela
#titulo
#campos para selecionar as moedas de origem e destino
#botão para coverter
#lista de exibição com os nomes das moedas
 
 
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda
 
#importar biblioteca que vai fazer a janea
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
 
janela = customtkinter.CTk()
janela.geometry("400x600")
janela.title("Conversor de Moedas")
janela.iconbitmap("calculadora.ico")
 
dic_conversoes_disponiveis = conversoes_disponiveis()
 
#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 15))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 20))
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font= ("", 13))
 
def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])
 
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["selecione uma moeda de origem"])
 
def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
            cotacao = pegar_cotacao_moeda
            texto_conotacao_moeda.configure (text=f"1{moeda_origem} = {cotacao} {moeda_destino} ")
 
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)
 
lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_conotacao_moeda = customtkinter.CTkLabel(janela, text="")
 

moedas_disponiveis = nomes_moedas()
 
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()
 
#moeda1 =customtkinter.CTkLabel(lista_moedas, text="USD: dólar americano")
#moeda2 =customtkinter.CTkLabel(lista_moedas, text="EUR: euro")
#moeda3 =customtkinter.CTkLabel(lista_moedas, text="BRL: real brasileiro")
#moeda4 =customtkinter.CTkLabel(lista_moedas, text="BTC: bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()
 
#colocar os elementos criados na tela
titulo.pack(padx=8, pady=8)
texto_moeda_origem.pack(padx=9, pady=9)
campo_moeda_origem.pack(padx=9, pady=9)
texto_moeda_destino.pack(padx=9, pady=9)
campo_moeda_destino.pack(padx=9, pady=9)
botao_converter.pack(padx=7, pady=7)
texto_conotacao_moeda.pack (padx=10, pady=10)
lista_moedas.pack(padx=9, pady=9)
#rodar janela
 
janela.mainloop()