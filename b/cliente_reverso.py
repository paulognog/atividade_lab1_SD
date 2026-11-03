import socket

HOST = '127.0.0.1'
PORTA = 8000

def enviar_mensagem():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORTA))
    
    mensagem = "Olá, Mundo Distribuído"
    print(f"[+] Enviando mensagem: {mensagem}")
    cliente.send(mensagem.encode('utf-8'))
    
    resposta = cliente.recv(1024).decode('utf-8')
    print(f"[+] Resposta recebida (revertida): {resposta}")
    cliente.close()

if __name__ == "__main__":
    enviar_mensagem()
