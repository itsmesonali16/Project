from threading import Thread
import tkinter
import socket
client=socket.socket()
port=1240
client.connect(('127.0.0.1',port))
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l)+n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result
def send(event=None):
    s=my_msg.get()
    my_msg.set(" ")
    encrypted= encrypt(5,s)
    arr=bytes(encrypted,'utf-8')
    client.send(arr)
    if s=="{quit}":
        client.close()
        top.quit()
    
def recive(event=None):
    a=client.recv(1024)
    sr=a.decode('utf-8')
    decrypted = decrypt(5,sr)
    print(decrypted)
    msg_list.insert(tkinter.END,decrypted)
top = tkinter.Tk()
top.title("Chatter")
messages_frame=tkinter.Frame(top)
my_msg=tkinter.StringVar()
my_msg.set(" ")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list=tkinter.Listbox(messages_frame)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field=tkinter.Entry(top,textvariable=my_msg)
entry_field.bind("<Return>",send)
entry_field.pack()
send_button=tkinter.Button(top,text="Send",command=send)
send_button.pack()
top.protocol("WM_DELETE_WINDOW",)
recive_thread=Thread(target=recive)
recive_thread.start()
top.mainloop()
