from customtkinter import *
import socket
import threading
from PIL import Image

def get_user_name():
    app1 = CTk()
    app1.geometry("400x300")
    app1.resizable(width=False, height=False)

    name = CTkLabel(master=app1, text="Enter your name:",font=("verdana",17))
    name.pack(pady = 20)

    name_entry = CTkEntry(master=app1, width=100)
    name_entry.pack(pady=20)

    def ok_button_click():
        app1.result = name_entry.get()
        app1.destroy()

    ok_button = CTkButton(master=app1, text="OK", command=ok_button_click)
    ok_button.pack()

    app1.mainloop()
    return app1.result if hasattr(app1, 'result') else "Unknown"

def start_client():
    user_name = get_user_name()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    def send_message():
        message = entry.get()
        textbox.configure(state="normal")
        textbox.insert("end", f"{user_name}: {message}\n")
        textbox.configure(state="disabled")
        entry.delete(0, "end")
        client.send(message.encode("utf-8"))

    app = CTk()
    app.geometry("750x600")
    app.resizable(width=False, height=False)

    #***********************************************   Frames    **************************************************

    frame0 = CTkFrame(master=app , border_color="grey" , border_width=2 , height=600, width=520)
    frame0.pack(expand=True,anchor="sw" , side="left")

    frame2 = CTkFrame(master=app, width=250 , height=600 , fg_color="grey", border_width=2 , border_color="grey")
    frame2.pack(expand = True ,anchor = "se", side="left")


    #**************************************************************************************************************

    entry = CTkEntry(master=frame0, width=420, height=45, text_color="white", font=("Arial", 16))
    entry.place(relx=0, rely=1, anchor="sw")
    entry.bind("<Return>", lambda event: send_message())

    img_path = r"C:\Users\ghrib\Desktop\python\chat python\Projet vids\Main Project\send.png"
    img = Image.open(img_path)
    button = CTkButton(master=frame0, text="Send", fg_color="#4158D0", hover_color="grey",
                    font=("Arial", 15), height=45, width=100, command=send_message, image=CTkImage(img))
    button.place(relx=1, rely=1, anchor="se")
    


    textbox = CTkTextbox(master=frame0, width=600, height=555, state="disabled", font=("Arial", 18))
    textbox.place(anchor="nw")

    def receive_messages():
        while True:
            try:
                msg = client.recv(1024).decode("utf-8")
                if not msg:
                    break
                textbox.configure(state="normal")
                textbox.insert("end", msg + "\n")
                textbox.configure(state="disabled")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    app.mainloop()

if __name__ == "__main__":
    start_client()
