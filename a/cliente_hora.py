import socket

HOST = '127.0.0.1'
PORTA = 8000

def solicitar_horario():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORTA))
    
    cliente.send("SOLICITAR_HORARIO".encode('utf-8'))
    resposta = cliente.recv(1024).decode('utf-8')
    
    print(f"[+] Horário recebido do servidor: {resposta}")
    cliente.close()

if __name__ == "__main__":
    solicitar_horario()
