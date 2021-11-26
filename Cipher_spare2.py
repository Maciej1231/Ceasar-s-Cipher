from tkinter import *

root = Tk()
root.title('Raytheon Cyber Academy     Maciej Kowalski')
root.geometry("500x400")
my_label = Label(root)

my_label_frame= LabelFrame(root, text="Caesar's Cipher")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10,padx=20)

enter_text_label= Label(my_frame,text = "Enter Text")
enter_text_entry = Entry(my_frame, font=("Helvetica",14),borderwidth=2)

shift_label = Label(my_frame,text="Shift Number")
shift_entry = Entry(my_frame,font =("Helvetica", 14),borderwidth=2)

enter_text_label.grid(row=0, column = 0)
enter_text_entry.grid(row=0, column=1,pady=10)

shift_label.grid(row=1,column=0)
shift_entry.grid(row=1,column=1,)
def myDelete():
    my_label.destroy()

def encrypt():
    new_text = enter_text_entry.get()
    cipher =""
    shift_1 = shift_entry.get()
    shift =int(shift_1)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    new_ind = 0
    for i in new_text:
        if i.upper()in alphabet:
            new_ind = alphabet.index(i) +shift
            cipher+=alphabet[new_ind % 26]
        elif i.lower()in alphabet:
            new_ind = alphabet.index(i) +shift
            cipher+=alphabet[new_ind % 26]
        else:
            cipher +=i
    global my_label        
    my_label=Label(root, text= cipher , font=("Helvetica",14))
    my_label.pack()
    
my_label = Label(root)
my_label.destroy()

my_button = Button(my_label_frame, text="  __Encrypt__  ",fg="red", command=encrypt)
my_button.pack(pady=20)    

delete_button =Button(my_label_frame, text= "____Clear_____", command=myDelete)
delete_button.pack(pady=10,)


root.mainloop()