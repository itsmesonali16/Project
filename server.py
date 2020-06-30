import socket
from threading import Thread
class ClientThread(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.client=ip
        self.addr=port
        print ("[+] New server socket Thread Started")
    
    def run(self):
        print("GOT A CONNECTION FROM",self.addr[0],":",self.addr[1])
        
        while True:
            data=self.client.recv(1024)
            so=data.decode("utf-8")
            decrypted = decrypt(so)
            print(decrypted)
            print("RECIVED",decrypted,"FROM THE CLIENT")
            print("PROCESING data........")
            if decrypted=="Hii" or decrypted == "hii":
                s="Hello Client"
                encrypted=encrypt(s)
                a=bytes(encrypted,'utf-8')
                self.client.send(a)
                print("Procecing Done \n Reply sent ")
            elif decrypted == "disconnect" or decrypted=="Disconnect":
                    s1="Good Bye"
                    en=encrypt(s1)
                    aa=bytes(en,'utf-8')
                    self.client.send(aa)
                    self.client.close()
                    break
            elif decrypted=="Request Resource" or decrypted == "request resources":
                b="Granted Resource"
                encrypted=encrypt(b)
                a=bytes(encrypted,'utf-8')
                self.client.send(a)
                print("Procecing Done \n Reply sent ")
            else:
                    s2="Invalid Data"
                    e=encrypt(s2)
                    b=bytes(e,'utf-8')
                    self.client.send(b)
                    print(" Processing done.Invalid data.\nReply sent")
def encrypt(plaintext):
        """Encrypt the string and return the ciphertext"""
        result = ''
        n=5
        key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for l in plaintext.lower():
            try:
                i = (key.index(l) + n) % 52
                result += key[i]
            except ValueError:
                result += l
        return result.lower()
def decrypt(ciphertext):
        """Decrypt the string and return the plaintext"""
        result = ''
        n=5
        key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for l in ciphertext:
            try:
                i = (key.index(l) - n) % 52
                result += key[i]
            except ValueError:
                result += l
        return result    
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ip='127.0.0.1'
port=1240
address=(ip,port)
server.bind(address)
threads=[]
while True:
    server.listen(4)
    print("Multithreading Python Server: Waiting for connection from client")
    client,addr=server.accept()
    newthread = ClientThread(client,addr)
    newthread.start()
    threads.append(newthread)
for t in threads:
    t.join()
print("Total Clients"+thread)
