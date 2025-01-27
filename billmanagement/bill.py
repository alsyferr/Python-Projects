from tkinter import *
from tkinter import messagebox,filedialog
import random,os,tempfile,smtplib


#functionality Part

# clear
def clear():
    
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    facewashEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    riceEntry.delete(0,END)
    sugarEntry.delete(0,END)
    oilEntry.delete(0,END)
    teaEntry.delete(0,END)
    
    dewEntry.delete(0,END)
    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cocacolaEntry.delete(0,END)
    
    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    facewashEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    riceEntry.insert(0,0)
    sugarEntry.insert(0,0)
    oilEntry.insert(0,0)
    teaEntry.insert(0,0)
    
    dewEntry.insert(0,0)
    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)
    
    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    colddrinkpriceEntry.delete(0,END)
    
    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    colddrinktaxEntry.delete(0,END)
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    
    textarea.delete(1.0,END)
    

# send email
def send_email():
    def send_mail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
        
        
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        
        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
        
        senderLabel=Label(senderFrame,text="Sender's Email",font=('arail',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)
        
        passwordLabel=Label(senderFrame,text="Password",font=('arail',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)
        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)
        
        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)
        
        recieverLabel=Label(recipientFrame,text="Email Address",font=('arail',14,'bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)
        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)
        
        messageLabel=Label(recipientFrame,text="Message",font=('arail',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)
        
        email_textarea=Text(recipientFrame,font=('arail',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))
        
        sendButton=Button(root1,text='SEND',font=('arail',16,'bold'),width=15,command=send_mail)
        sendButton.grid(row=2,column=0,pady=20)
        
        
        root1.mainloop()

# print bill
def print_bill():
    # if textarea.get(1.0,END)=='\n':
    #     messagebox.showerror('Error','Bill is empty')
    # else:
    #     file=tempfile.mktemp('.txt')
    #     open(file,'w').write(textarea.get(1.0,END))
    #     os.startfile(file,'print')
    
    if textarea.get(1.0, END).strip() == '':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        try:
            # Open a save file dialog to choose location and filename
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            
            if save_path:  # If a file path is selected
                # Write the content to the selected file
                with open(save_path, 'w') as file:
                    file.write(textarea.get(1.0, END))
                
                # Optionally, print the file after saving
                os.startfile(save_path, 'print')  # This sends the file to the printer
            else:
                messagebox.showerror('Error', 'No file selected to save.')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')

# search bill
# def search_bill():
#     for i in os.listdir('bills/'):
#         print(i)
#         if i.split('.')[0] == billnumberEntry.get():
#             f=open(f'bills/{i}', 'r')
#             textarea.delete(1.0,END)
#             for data in f:
#                 textarea.insert(END,data)
#             f.close()
#             break
#     else:
#         messagebox.showerror('Error','Invalid Bill Number')
def search_bill():
    bill_number = billnumberEntry.get().strip()  # Ensure no leading/trailing spaces
    for i in os.listdir('bills/'):
        if i.endswith('.txt') and i.split('.')[0].strip() == bill_number:
            with open(f'bills/{i}', 'r') as f:
                textarea.delete(1.0, END)
                for data in f:
                    textarea.insert(END, data)
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)
        

billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and colddrinkpriceEntry.get()=='':
        messagebox.showerror('Error','No Products are selected')
    elif cosmeticpriceEntry.get()=='$ 0 ' and grocerypriceEntry.get()=='$ 0 ' and colddrinkpriceEntry.get()=='$ 0 ':
        messagebox.showerror('Error','No Products are selected')
    else:
    
        textarea.delete(1.0,END)
        
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n=====================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n=====================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t${soapprice}')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t${hairsprayprice}')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t${hairgelprice}')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t${facecreamprice}')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t${facewashprice}')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t${bodylotionprice}')
        
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t${riceprice}')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t${oilprice}')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t${daalprice}')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t${wheatprice}')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t${sugarprice}')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t${teaprice}')
        
        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t${maazaprice}')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t${pepsiprice}')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t${spriteprice}')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t${dewprice}')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t${frootiprice}')
        if cocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t${cocacolaprice}')
        
        textarea.insert(END,'\n-----------------------------------------------------')
        
        if cosmetictaxEntry.get()!='$ 0.0 ':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='$ 0.0 ':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if colddrinktaxEntry.get()!='$ 0.0 ':
            textarea.insert(END,f'\nCold Drink Tax\t\t\t\t{colddrinktaxEntry.get()}')
            
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t$ {totalbill}')
        
        textarea.insert(END,'\n-----------------------------------------------------')
        
        save_bill()
    
    

def total():
    global soapprice,hairsprayprice,hairgelprice,facecreamprice,facewashprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice
    global maazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cocacolaprice
    global totalbill
   
    #cosmetics price calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60
    
    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'$ {totalcosmeticprice} ')
    
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'$ {cosmetictax} ')
    
    #Grocery price calculation
    riceprice=int(riceEntry.get())*30
    oilprice=int(oilEntry.get())*100
    daalprice=int(daalEntry.get())*120
    wheatprice=int(wheatEntry.get())*50
    sugarprice=int(sugarEntry.get())*140
    teaprice=int(teaEntry.get())*80
    
    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'$ {totalgroceryprice} ')
    
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'$ {grocerytax} ')
    
    #Cold drinks price calculation
    maazaprice=int(maazaEntry.get())*20
    pepsiprice=int(pepsiEntry.get())*50
    spriteprice=int(spriteEntry.get())*100
    dewprice=int(dewEntry.get())*150
    frootiprice=int(frootiEntry.get())*80
    cocacolaprice=int(cocacolaEntry.get())*60
    
    totalcolddrinkprice=maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice
    colddrinkpriceEntry.delete(0,END)
    colddrinkpriceEntry.insert(0,f'$ {totalcolddrinkprice} ')
    
    colddrinktax=totalcolddrinkprice*0.08
    colddrinktaxEntry.delete(0,END)
    colddrinktaxEntry.insert(0,f'$ {colddrinktax} ')
    
    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinkprice+cosmetictax+grocerytax+colddrinktax


#UI Part
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')

# image_icon=PhotoImage(file="bill.png")
# root.iconphoto(False,image_icon)


headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)


phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)


productsFrame=Frame(root)
productsFrame.pack()

#products1 

cometicsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
cometicsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cometicsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cometicsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cometicsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cometicsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10,)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cometicsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10,)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cometicsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10,)
bodylotionEntry.insert(0,0)


#products2 

GroceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
GroceryFrame.grid(row=0,column=1)

riceLabel=Label(GroceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(GroceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(GroceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10,)
daalEntry.insert(0,0)

wheatLabel=Label(GroceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10,)
wheatEntry.insert(0,0)

sugarLabel=Label(GroceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10,)
sugarEntry.insert(0,0)

teaLabel=Label(GroceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,)
teaEntry.insert(0,0)


#products3 

colddrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
colddrinksFrame.grid(row=0,column=2)

maazaLabel=Label(colddrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(colddrinksFrame,text='sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10,)
spriteEntry.insert(0,0)

dewLabel=Label(colddrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10,)
dewEntry.insert(0,0)

frootiLabel=Label(colddrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10,)
frootiEntry.insert(0,0)

cocacolaLabel=Label(colddrinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cocacolaEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10,)
cocacolaEntry.insert(0,0)


#bill
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18,width=53,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


#billmenu
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('arial',14),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10,)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('arial',14),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10,)

colddrinkpriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
colddrinkpriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
colddrinkpriceEntry=Entry(billmenuFrame,font=('arial',14),width=10,bd=5)
colddrinkpriceEntry.grid(row=2,column=1,pady=6,padx=10,)


#billtax

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('arial',14),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10,)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('arial',14),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10,)

colddrinktaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
colddrinktaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
colddrinktaxEntry=Entry(billmenuFrame,font=('arial',14),width=10,bd=5)
colddrinktaxEntry.grid(row=2,column=3,pady=6,padx=10,)

#billbuttons
buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=4)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=4)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=4)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=4)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=4)

################################################################################



root.mainloop()