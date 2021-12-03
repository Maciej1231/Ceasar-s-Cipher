from tkinter import *

#creating tkinter box with labels and buttons

root = Tk()
root.title('Raytheon Cyber Academy     Maciej Kowalski')
root.geometry("600x400")
my_label = Label(root)

my_label_frame= LabelFrame(root, text="Caesar's Cipher")
my_label_frame.pack(pady=30)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=10,padx=20)

enter_text_label= Label(my_frame,text = "Enter Text")
enter_text_entry = Entry(my_frame, font=("Helvetica",14),borderwidth=2)

shift_label = Label(my_frame,text="Shift Number")
shift_entry = Entry(my_frame,font =("Helvetica", 14),borderwidth=2)

cipher_label = Label(my_frame,text="Encrypted Msg")
cipher_entry = Entry(my_frame,font =("Helvetica", 14),borderwidth=2)

enter_text_label.grid(row=0, column = 0)
enter_text_entry.grid(row=0, column=1,pady=10)

shift_label.grid(row=1,column=0)
shift_entry.grid(row=1,column=1)


#clear output and input function
def myDelete():
    my_label.destroy()
    shift_entry.delete(0,END)
    enter_text_entry.delete(0,END)
    
    
#encryption function
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

# encrypt button 
my_button = Button(my_label_frame, text="  Encrypt  ",fg="red", command=encrypt)
my_button.pack(pady=20)    

# clear button
delete_button =Button(my_label_frame, text= "    Clear    ", command=myDelete)
delete_button.pack(pady=10,)


root.mainloop()
