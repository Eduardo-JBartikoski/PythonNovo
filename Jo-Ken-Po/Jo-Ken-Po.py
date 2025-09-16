import tkinter as tk
import random

class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__escolha = None

    def escolher(self):
        self.__escolha = random.choice(["pedra", "papel", "tesoura"])

    def get_nome(self):
        return self.__nome

    def get_escolha(self):
        return self.__escolha

class Jogo:
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2

    def jogar(self):
        self.__jogador1.escolher()
        self.__jogador2.escolher()

        e1 = self.__jogador1.get_escolha()
        e2 = self.__jogador2.get_escolha()

        resultado = self.__comparar(e1, e2)

        return (
            f"{self.__jogador1.get_nome()} escolheu: {e1}\n"
            f"{self.__jogador2.get_nome()} escolheu: {e2}\n\n"
            f"{resultado}"
        )

    def __comparar(self, e1, e2):
        regras = {
            "pedra": "tesoura",
            "tesoura": "papel",
            "papel": "pedra"
        }

        if e1 == e2:
            return "EMPATE!"
        elif regras[e1] == e2:
            return f"{self.__jogador1.get_nome()} venceu!"
        else:
            return f"{self.__jogador2.get_nome()} venceu!"

# Interface gráfica
janela = tk.Tk()
janela.title("Jo-Ken-Pô Animado")
janela.geometry("400x300")
janela.configure(bg="#1E1E2F")

fonte_titulo = ("Segoe UI", 18, "bold")
fonte_resultado = ("Segoe UI", 12, "bold")

titulo = tk.Label(janela, text="🔥 Jo-Ken-Pô 🔥", font=fonte_titulo, bg="#1E1E2F", fg="#FFD700")
titulo.pack(pady=15)

resultado = tk.Label(janela, text="Clique em Play para começar!", font=fonte_resultado, bg="#1E1E2F", fg="#FFFFFF", justify="center")
resultado.pack(pady=10)

# controle da animação
animando = False
opcoes = ["pedra", "papel", "tesoura"]
indice = 0

def animar():
    global indice
    if animando:
        resultado["text"] = f"Jogador 1: {opcoes[indice]}\nJogador 2: {opcoes[(indice+1)%3]}"
        indice = (indice + 1) % 3
        janela.after(100, animar) #100ms

def jogar_partida():
    global animando
    if not animando:
        animando = True
        botao["text"] = "Parar"
        animar()
    else:
        animando = False
        botao["text"] = "▶ Play"
        j1 = Jogador("Jogador 1")
        j2 = Jogador("Jogador 2")
        partida = Jogo(j1, j2)
        texto = partida.jogar()

        # Destaque visual
        if "venceu" in texto:
            resultado.configure(fg="#FF4500")
        elif "EMPATE" in texto:
            resultado.configure(fg="#00CED1")
        else:
            resultado.configure(fg="#FFFFFF")

        resultado["text"] = texto

botao = tk.Button(janela, text="▶ Play", command=jogar_partida, font=("Segoe UI", 12, "bold"), bg="#FFD700", fg="#1E1E2F", activebackground="#FFA500", bd=2, relief="raised")
botao.pack(pady=20)

janela.mainloop()
