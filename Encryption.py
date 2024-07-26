import tkinter
from tkinter import *
from tkinter import messagebox,ttk,filedialog
import hashlib
from hashlib import sha1,sha256,sha224,sha384,sha512
list=("a","o","e","i","f")

back="grey"
back1="yellow"
back2="darkred"
back3="white"
back4="lightgreen"
screem=tkinter.Tk()
opt=("sha1","sha224","sha384","sha512","sha256")
screem.config(bg=back)

def ok():
    pass                         

btnn=tkinter.Button(text="Suivant..",command=screem.quit,bg=back2,font=("bold",15))
mes3=tkinter.Label(text="Mot de passe:",bg=back,fg=back1,font=("bold",19))
key=tkinter.Entry(screem,show="*",width=50)
combo=ttk.Combobox(screem,values=opt)
combo.current(4)
mess=tkinter.Label(text="Emplacement du fichier:",bg=back,fg=back1,font=("bold",19))
mes2=tkinter.Label(text="",bg=back,fg=back3,font=("bold",15))
combo_lab=tkinter.Label(text="Type de Hash:",bg=back,fg=back1,font=("bold",19))
done=tkinter.Label(text="Done")
def done():
    messagebox.showinfo("Encryption"," effectuer avec succés")

mes2.place(x=300,y=75)
def parcour():
    crypt=0
    btnn.config(command=screem.quit)
    doc=filedialog.askopenfilename()
    mess.place(x=10,y=70)
    mes2.config(text=doc)
    screem.mainloop()
    btn2.destroy()
    keys=good()
    trouver=False
    with open(doc,"r") as doc_input:
                    finding_Cr=doc.find("_Cr")
                    if finding_Cr<0:
                        dock_1=doc
                    else :
                        
                        dock=doc.split("_Cr")
                        trouver=True
                        try:
                            dock_1=str(dock[0])+str(dock[1])
                        except:
                            dock_1=str(dock[0])
                        
                    if trouver==False:       
                        finding_Dcr=doc.find("_Dcr")
                        if finding_Dcr<0:
                            
                            dock_1=doc
                            
                        else:
                            
                            dock=doc.split("_Dcr")
                            try:
                                dock_1=str(dock[0])+str(dock[1])
                            except:
                                dock_1=str(dock[0])

                    try :
                        crypt=0
                        lecture=doc_input.read(6)
                        for elt in list:
                            for elts in lecture:
                                if  str(elts)==elt or str(elts.lower())==elt:
                                    
                                    crypt=int(crypt)+1
                    except:
                        crypt=0
                    doc_out=dock_1.split('.')
                    
                    if int(crypt)!=0:
                        try:
                            doc_out=str(doc_out[0])+"_Cr"+'.'+str(doc_out[1])
                        
                        except:
                            doc_out=str(doc_out[0])+str("_Cr")
                    
                    if int(crypt)==0:
                        try:
                            doc_out=str(doc_out[0]+"_Dcr")+'.'+str(doc_out[1])
                        except:
                            doc_out=str(doc_out[0])+str("_Dcr")
                        
            
    with open (doc,"rb") as doc_input:
                with open (doc_out,"wb") as doc_output:
                    a=0
                    while doc_input.peek():
                            b=ord(doc_input.read(1))
                            c=a% len(keys)
                            d=bytes ([b^keys[c]])
                            doc_output.write(d)
                            a=a+1
                            b=True
    done()
def good():
    if combo.get()=="sha1":
        keys=(sha1((key.get()).encode("utf-8"))).digest()
    elif combo.get()=="sha224":
        keys=(sha224((key.get()).encode("utf-8"))).digest()
    elif combo.get()=="sha512":
        keys=(sha512((key.get()).encode("utf-8"))).digest()
    elif combo.get()=="sha256":
        keys=(sha256((key.get()).encode("utf-8"))).digest()
    elif combo.get()=="sha384":
        keys=(sha384((key.get()).encode("utf-8"))).digest()
    else :
        keys=(sha256((key.get()).encode("utf-8"))).digest()
    return keys
    
def parcourir():
    b=False
    doc=filedialog.askopenfilename()
    mes2.config(text=doc)
    btnn.place(x=600,y=450)
    mess.place(x=20,y=70)
    screem.mainloop()
    btn2.destroy()
    mes3.place(x=10,y=140)
    key.place(x=180,y=150)
    
    btn.config(command=parcour)
    mes2.config(text=doc)
    screem.mainloop()
    btn2.destroy()
    combo_lab.place(x=10,y=210)
    combo.place(x=200,y=220)
    
    btnn1=tkinter.Button(text="sha",command=good)
    messagebox.showwarning("WARNING","Un mauvais hash ou un mauvais mot de passe affecterons le dechiffrement...Merci de bien renseigner les informations.")
    btnn.config(text="Encryption..",bg=back4)
    screem.mainloop()
    keys=good()
    crypt=0
    dock_1=""
    trouver=False
    if b==False:
            with open(doc,"r") as doc_input:
                
                    finding_Cr=doc.find("_Cr")
                    if finding_Cr<0:
                        dock_1=doc
                    else :
                        dock=doc.split("_Cr")
                        trouver=True
                        try:
                            dock_1=str(dock[0])+str(dock[1])
                        except:
                            dock_1=str(dock[0])
                        
                    if trouver==False:       
                        finding_Dcr=doc.find("_Dcr")
                        if finding_Dcr<0:
                            
                            dock_1=doc
                            
                        else:
                            
                            dock=doc.split("_Dcr")
                            try:
                                dock_1=str(dock[0])+str(dock[1])
                            except:
                                dock_1=str(dock[0])
                    try :
                        crypt=0
                        lecture=doc_input.read(6)
                        for elt in list:
                            for elts in lecture:
                                if  str(elts)==elt or str(elts.lower())==elt:
                                    crypt=int(crypt)+1
                    except:
                        crypt=0
                    doc_out=dock_1.split('.')
                    
                    if int(crypt)!=0:
                        try:
                            doc_out=str(doc_out[0])+"_Cr"+'.'+str(doc_out[1])
                        
                        except:
                            doc_out=str(doc_out[0])+str("_Cr")
                    
                    if int(crypt)==0:
                        try:
                            doc_out=str(doc_out[0]+"_Dcr")+'.'+str(doc_out[1])
                        except:
                            doc_out=str(doc_out[0])+str("_Dcr")
                    
            
            with open (doc,"rb") as doc_input:
                
                with open (doc_out,"wb") as doc_output:
                    a=0
                    while doc_input.peek():
                            b=ord(doc_input.read(1))
                            c=a% len(keys)
                            d=bytes ([b^keys[c]])
                            doc_output.write(d)
                            a=a+1
                            b=True
                            
    else :
        pass
    btnn.config(command=ok)
    done()
back5="cadetblue"
def aide ():
    scren1=tkinter.Tk()
    scren1.title("Page d'aide")
    scren1.configure(bg="cadetblue")
    m=tkinter.Label(scren1,text="C'est quand même assez explicite hein",bg=back5)
    m.pack()
    m1=tkinter.Label(scren1,text="Le hash selectionner par defaut est le sha256",bg=back5)
    m1.pack()
    m2=tkinter.Label(scren1,text="Le chiffrement peut se faire avec un 'Mot de passe' =NONE sans inconvenients",bg=back5)
    m2.pack()
    scren1.mainloop()
def about():
    scren2=tkinter.Tk()
    scren2.config(bg=back5)
    me=tkinter.Label(scren2,text="Cr Encryption :Encrypt files",bg=back5)
    me.pack()
    me2=tkinter.Label(scren2,text="Cr Encryption --Verion 1.2",bg=back5)
    me2.pack()
    me3=tkinter.Label(scren2,text="Developped by ACHMELE@Fred All right reserved",bg=back5)
    me3.pack()
    scren2.mainloop()
    
    
screem.geometry("750x500")
screem.title("Cr Encryption")

btn2=tkinter.Button(text="continue",command=screem.quit)
mes=tkinter.Label(text="Selectionner le fichier:",bg=back,fg=back1,font=("bold",19))
btn=tkinter.Button(text="Parcourir",command=parcourir,font=("bold",15),bg=back3)
try:
    tof=tkinter.PhotoImage(file="Cr_logo.png")
    photo=Label(image=tof)
    photo.pack()
    screem.after(4000,photo.destroy)
except:
    pass
mainmenu=tkinter.Menu(screem)
mainmenu.add_command(label="Aide",command=aide)
mainmenu.add_command(label="A propos",command=about)
screem.configure(menu=mainmenu)
mes.place(x=10,y=10)
btn2.destroy()
btn.place(x=300,y=10) 
screem.mainloop()