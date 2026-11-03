import socket
import threading

HOST = '127.0.0.1'
PORTA = 8000

def tratar_cliente(conexao, endereco):
    print(f"[-] Cliente conectado: {endereco}")
    try:
        dado = conexao.recv(1024).decode('utf-8')
        if dado:
            string_revertida = dado[::-1]
            conexao.send(string_revertida.encode('utf-8'))
    finally:
        conexao.close()
        print(f"[-] Conexão encerrada com {endereco}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen()
    print(f"[*] Servidor de Reversão de String rodando em {HOST}:{PORTA}...")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
