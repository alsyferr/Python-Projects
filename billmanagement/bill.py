from tkinter import *

root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')

root.iconbitmap('bill.ico')

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

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
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

facecreamLabel=Label(cometicsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)

facewashLabel=Label(cometicsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10,)

hairsprayLabel=Label(cometicsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10,)

hairgelLabel=Label(cometicsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10,)

BodylotionLabel=Label(cometicsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
BodylotionEntry=Entry(cometicsFrame,font=('arial',15),width=10,bd=5)
BodylotionEntry.grid(row=5,column=1,pady=9,padx=10,)


#products2 

GroceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
GroceryFrame.grid(row=0,column=1)

riceLabel=Label(GroceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)

oilLabel=Label(GroceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)

daalLabel=Label(GroceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10,)

wheatLabel=Label(GroceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10,)

sugarLabel=Label(GroceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10,)

teaLabel=Label(GroceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(GroceryFrame,font=('arial',15),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,)


#products3 

colddrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=8,relief=GROOVE)
colddrinksFrame.grid(row=0,column=2)

maazaLabel=Label(colddrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)

pepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)

spriteLabel=Label(colddrinksFrame,text='sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10,)

dewLabel=Label(colddrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10,)

frootiLabel=Label(colddrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10,)

cocacolaLabel=Label(colddrinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cocacolaEntry=Entry(colddrinksFrame,font=('arial',15),width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10,)


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

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
totalButton.grid(row=0,column=0,pady=20,padx=4)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
billButton.grid(row=0,column=1,pady=20,padx=4)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=4)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=4)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=4)

################################################################################



root.mainloop()