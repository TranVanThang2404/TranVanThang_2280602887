from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

server_key = RSA.generate(2048)

clients = []

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:] 
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def handle_client(client_socket, client_address):
    print(f'New connection from {client_address}')
    
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    client_recieved_key = RSA.import_key(client_socket.recv(2048))
    aes_key = get_random_bytes(16)
    
    cipher_rsa = PKCS1_OAEP.new(client_recieved_key)
    
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)
    
    clients.append((client_socket, aes_key))
    
    while True:
        encrypted_message = client_socket.recv(1024)
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print(f'Received from {client_address}: {decrypted_message}')
        
        for client, key in clients:
            if client != client_socket:
                encrypted_message_to_send = encrypt_message(decrypted_message, key)
                client.send(encrypted_message_to_send)
                
        if decrypted_message == 'exit':
            break   
    
    clients.remove((client_socket, aes_key))    
    client_socket.close()
    print(f'Connection from {client_address} closed')
    
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()