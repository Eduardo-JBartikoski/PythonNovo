import tkinter as tk
import requests
import os

API_KEY = os.getenv("API_KEY")
URL = os.getenv("WEATHER_URL")

def buscar_tempo():
    parametros = {
        "key": API_KEY,
        "q": "Novo Hamburgo",
        "lang": "pt"
    }

    try:
        resposta = requests.get(URL, params=parametros)
        if resposta.status_code == 200:
            dados = resposta.json()
            cidade = dados["location"]["name"]
            estado = dados["location"]["region"]
            pais = dados["location"]["country"]
            temp = dados["current"]["temp_c"]
            condicao = dados["current"]["condition"]["text"]

            resultado["text"] = (
                f"Cidade: {cidade}\n"
                f"Estado: {estado}\n"
                f"País: {pais}\n"
                f"Temperatura: {temp}°C\n"
                f"Condição: {condicao}"
            )
        else:
            resultado["text"] = "Erro ao buscar dados."
    except Exception as e:
        resultado["text"] = f"Erro: {e}"

# Interface gráfica
janela = tk.Tk()
janela.title("Tempo em Novo Hamburgo")
janela.geometry("320x240")
janela.resizable(False, False)

# Cores e estilo
janela.configure(bg="#0688BB")  # Azul céu
fonte_padrao = ("Segoe UI", 12)

# Título
titulo = tk.Label(janela, text="Clima Atual", font=("Segoe UI", 16, "bold"), bg="#0688BB", fg="white")
titulo.pack(pady=10)

fonte_titulo = ("Segoe UI", 16, "bold")
fonte_resultado = ("Segoe UI", 12, "bold")

# Botão estilizado
botao = tk.Button(
    janela,
    text="Atualizar Tempo",
    command=buscar_tempo,
    font=fonte_padrao,
    bg="#ffffff",
    fg="#333333",
    relief="raised",
    bd=2
)
botao.pack(pady=10)

# Label para exibir resultado
resultado = tk.Label(
    janela,
    text="",
    font=fonte_padrao,
    bg="#0688BB",
    fg="white",
    justify="center"
)
resultado.pack(pady=10)

# Inicia a janela
janela.mainloop()