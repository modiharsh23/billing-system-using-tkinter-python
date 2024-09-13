from tkinter import *
from tkinter import messagebox
import os
global bill_num
bill_num = 1

#Function Part

def clear_bill():
    text_area.delete(1.0,END)
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    pizza_entry.delete(0,END)
    pizza_entry.insert(0,0)
    burger_entry.delete(0,END)
    burger_entry.insert(0,0)
    sandwich_entry.delete(0,END)
    sandwich_entry.insert(0,0)
    punjabi_entry.delete(0,END)
    punjabi_entry.insert(0,0)
    gujarati_entry.delete(0,END)
    gujarati_entry.insert(0,0)
    chole_entry.delete(0,END)
    chole_entry.insert(0,0)
    manchurian_entry.delete(0,END)
    manchurian_entry.insert(0,0)
    noodle_entry.delete(0,END)
    noodle_entry.insert(0,0)
    rice_entry.delete(0,END)
    rice_entry.insert(0,0)

    fast_foods_entry.delete(0,END)
    fast_foods_entry.insert(0,f'0 Rs')
    fast_foods_tax_entry.delete(0,END)
    fast_foods_tax_entry.insert(0,f'0 Rs')
    fix_lunches_entry.delete(0,END)
    fix_lunches_entry.insert(0,f'0 Rs')
    fix_lunches_tax_entry.delete(0,END)
    fix_lunches_tax_entry.insert(0,f'0 Rs')
    chinese_entry.delete(0,END)
    chinese_entry.insert(0,f'0 Rs')
    chinese_tax_entry.delete(0,END)
    chinese_tax_entry.insert(0,f'0 Rs')

    messagebox.showinfo('Success',f'Bill cleared')        

if not os.path.exists('bills'):
      os.mkdir('bills')

def print_bill():
    messagebox.showinfo('Success',f'Bill Printed')

def save_bill():
    global bill_num
    global bill_content

    saveresult=messagebox.askyesno('confirm','You wnat to save the Bill ?')
    if saveresult:
            bill_content = text_area.get(1.0,END)
            file=open(f'bills/ {bill_num}.txt','w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo('Success',f'Bill {bill_num} Saved Succesfully')
            bill_num=1

def bill_area():
    if name_entry.get()=='' or phone_entry.get()=='':
        messagebox.showerror('Error','Customer Details Required')
    elif fast_foods_entry.get()=='' and fix_lunches_entry.get()=='' and chinese_entry.get()=='':
        messagebox.showerror('Error','Enter Product Quantity')
    elif fast_foods_entry.get()=='0 Rs' and fix_lunches_entry.get()=='0 Rs' and chinese_entry.get()=='0 Rs':
        messagebox.showerror('Error','Enter Product Quantity')
    else:
            text_area.delete(1.0,END)

            text_area.insert(END,"\t\t\tWELCOME\n\n")
            text_area.insert(END,f' Bill Number : {bill_num}\n')
            text_area.insert(END,f' Customer Name : {name_entry.get()}\n')
            text_area.insert(END,f' Customer Phone No. : {phone_entry.get()}\n')
            text_area.insert(END,'-------------------------------------------------------\n')
            text_area.insert(END,' Product\t\t\t\tQuantity\t\tPrice\n')
            text_area.insert(END,'-------------------------------------------------------\n')
            if pizza_entry.get()!='0':
                text_area.insert(END,f' Pizza \t\t\t\t  {pizza_entry.get()} \t\t{pizzaval} Rs\n')
            if burger_entry.get()!='0':
                text_area.insert(END,f' Burger \t\t\t\t  {burger_entry.get()} \t\t{burgerval} Rs\n')
            if sandwich_entry.get()!='0':
                text_area.insert(END,f' Sandwich \t\t\t\t  {sandwich_entry.get()} \t\t{sandwichval} Rs\n')

            if punjabi_entry.get()!='0':
                text_area.insert(END,f' Punjabi Fix \t\t\t\t  {punjabi_entry.get()} \t\t{punjabival} Rs\n')
            if gujarati_entry.get()!='0':
                text_area.insert(END,f' Gujarati Fix \t\t\t\t  {gujarati_entry.get()} \t\t{gujaratival} Rs\n')
            if chole_entry.get()!='0':
                text_area.insert(END,f' Chole \t\t\t\t  {chole_entry.get()} \t\t{choleval} Rs\n')

            if manchurian_entry.get()!='0':
                text_area.insert(END,f' Manchurian \t\t\t\t  {manchurian_entry.get()} \t\t{manchurianval} Rs\n')
            if noodle_entry.get()!='0':
                text_area.insert(END,f' Noodles \t\t\t\t  {noodle_entry.get()} \t\t{noodleval} Rs\n')
            if rice_entry.get()!='0':
                text_area.insert(END,f' Rice \t\t\t\t  {rice_entry.get()} \t\t{riceval} Rs\n')
            
            text_area.insert(END,'-------------------------------------------------------\n')

            if fast_foods_tax_entry.get()!='0.0 Rs':
                text_area.insert(END,f' Fast Food Tax : {fast_foods_tax_entry.get()}\n')
            if fix_lunches_tax_entry.get()!='0.0 Rs':
                text_area.insert(END,f' Fix Lunches Tax : {fix_lunches_tax_entry.get()}\n')
            if chinese_tax_entry.get()!='0.0 Rs':
                text_area.insert(END,f' Chinese Tax : {chinese_tax_entry.get()}\n')
            
            text_area.insert(END,'-------------------------------------------------------\n')

            text_area.insert(END,f'\n\t\t\t\t\tTotal : {totalbill}\n')

            text_area.insert(END,'-------------------------------------------------------\n')

            save_bill()
        

def total():
    global pizzaval,burgerval,sandwichval,punjabival,gujaratival,choleval,manchurianval,noodleval,riceval,totalbill

    #fastfoods cal
    pizzaval=int(pizza_entry.get())*90
    burgerval=int(burger_entry.get())*50
    sandwichval=int(sandwich_entry.get())*75

    total_fastfood_val=pizzaval+burgerval+sandwichval
    fast_foods_entry.delete(0,END)
    fast_foods_entry.insert(0,f'{total_fastfood_val} Rs')

    total_fastfood_tax=total_fastfood_val*0.12
    fast_foods_tax_entry.delete(0,END)
    fast_foods_tax_entry.insert(0,f'{total_fastfood_tax} Rs')

    #fixlunches cal
    punjabival=int(punjabi_entry.get())*120
    gujaratival=int(gujarati_entry.get())*100
    choleval=int(chole_entry.get())*60

    total_fixlunch_val=punjabival+gujaratival+choleval
    fix_lunches_entry.delete(0,END)
    fix_lunches_entry.insert(0,f'{total_fixlunch_val} Rs')

    total_fixlunch_tax=total_fixlunch_val*.05
    fix_lunches_tax_entry.delete(0,END)
    fix_lunches_tax_entry.insert(0,f'{total_fixlunch_tax} Rs')

    #chinese cal
    manchurianval=int(manchurian_entry.get())*90
    noodleval=int(noodle_entry.get())*80
    riceval=int(rice_entry.get())*70

    total_chinese_val=manchurianval+noodleval+riceval
    chinese_entry.delete(0,END)
    chinese_entry.insert(0,f'{total_chinese_val} Rs')

    total_chinese_tax=total_chinese_val*.09
    chinese_tax_entry.delete(0,END)
    chinese_tax_entry.insert(0,f'{total_chinese_tax} Rs')

    totalbill=total_fastfood_val+total_fastfood_tax+total_fixlunch_val+total_fixlunch_tax+total_chinese_val+total_chinese_tax
    
#GUI part

root=Tk()
root.title('Retail billing system')
root.geometry('1270x685')
root.iconbitmap('C:\HARSH PROGRAMING\PYTHON\Bill\ico.ico')
headinglabel=Label(root,text='Billing System',font=('Times new roman',20,'bold'),bg='gray20',fg='white',bd=10,relief=RAISED)
headinglabel.pack(fill=X)

# customer details

customer_details_frame=LabelFrame(root,text='Customer Details',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=10,relief=RAISED)
customer_details_frame.pack(fill=X,pady=5)

name_label=Label(customer_details_frame,text='Name :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=10)
name_label.grid(row=0,column=0)

name_entry=Entry(customer_details_frame,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE)
name_entry.grid(row=0,column=1,padx=10,pady=3)

phone_label=Label(customer_details_frame,text='Phone :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=10)
phone_label.grid(row=0,column=2)

phone_entry=Entry(customer_details_frame,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE)
phone_entry.grid(row=0,column=3,padx=10,pady=3)

# products

products_frame=Frame(root)
products_frame.pack()

# fast foods

fast_foods=LabelFrame(products_frame,text='Fast Foods',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=10,)
fast_foods.grid(row=0,column=0)

pizza_label=Label(fast_foods,text='Pizza :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
pizza_label.grid(row=0,column=0)

pizza_entry=Entry(fast_foods,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
pizza_entry.grid(row=0,column=1,padx=10,pady=3)
pizza_entry.insert(0,0)

burger_label=Label(fast_foods,text='Burger :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
burger_label.grid(row=1,column=0)

burger_entry=Entry(fast_foods,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
burger_entry.grid(row=1,column=1,padx=10,pady=3)
burger_entry.insert(0,0)

sandwich_label=Label(fast_foods,text='Sandwich :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
sandwich_label.grid(row=2,column=0)

sandwich_entry=Entry(fast_foods,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
sandwich_entry.grid(row=2,column=1,padx=10,pady=3)
sandwich_entry.insert(0,0)

# fix lunches

fix_lunches=LabelFrame(products_frame,text='Fix Lunch',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=10)
fix_lunches.grid(row=0,column=1)

punjabi_label=Label(fix_lunches,text='Punjabi :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
punjabi_label.grid(row=0,column=0)

punjabi_entry=Entry(fix_lunches,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
punjabi_entry.grid(row=0,column=1,padx=10,pady=3)
punjabi_entry.insert(0,0)

gujarati_label=Label(fix_lunches,text='Gujarati :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
gujarati_label.grid(row=1,column=0)

gujarati_entry=Entry(fix_lunches,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
gujarati_entry.grid(row=1,column=1,padx=10,pady=3)
gujarati_entry.insert(0,0)

chole_label=Label(fix_lunches,text='Chole :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
chole_label.grid(row=2,column=0)

chole_entry=Entry(fix_lunches,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
chole_entry.grid(row=2,column=1,padx=10,pady=3)
chole_entry.insert(0,0)

# chinese 

chinese_foods=LabelFrame(products_frame,text='Chinese',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=10)
chinese_foods.grid(row=0,column=2)

manchurian_label=Label(chinese_foods,text='Manchurian :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
manchurian_label.grid(row=0,column=0)

manchurian_entry=Entry(chinese_foods,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
manchurian_entry.grid(row=0,column=1,padx=10,pady=3)
manchurian_entry.insert(0,0)

noodle_label=Label(chinese_foods,text='Noodles :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
noodle_label.grid(row=1,column=0)

noodle_entry=Entry(chinese_foods,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
noodle_entry.grid(row=1,column=1,padx=10,pady=3)
noodle_entry.insert(0,0)

rice_label=Label(chinese_foods,text='Rice :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
rice_label.grid(row=2,column=0)

rice_entry=Entry(chinese_foods,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
rice_entry.grid(row=2,column=1,padx=10,pady=3)
rice_entry.insert(0,0)

# text area 

bill_frame=Frame(products_frame,padx=10,bd=2,relief= GROOVE)
bill_frame.grid(row=0,column=3)

bill_area_label=Label(bill_frame,text='Bill Area',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=2,relief= GROOVE)
bill_area_label.pack(fill=X)

bill_scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
bill_scrollbar.pack(side=RIGHT,fill=Y)

text_area=Text(bill_frame,height=22,width=55,yscrollcommand=bill_scrollbar.set)
text_area.pack()
bill_scrollbar.config(command=text_area.yview)

# bill menu 

bill_menu=LabelFrame(root,text='Bill menu',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
bill_menu.pack()

fast_foods_price=Label(bill_menu,text='Fast foods :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
fast_foods_price.grid(row=0,column=0)

fast_foods_entry=Entry(bill_menu,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
fast_foods_entry.grid(row=0,column=1,padx=10,pady=3)

fix_lunches_price=Label(bill_menu,text='Fix Lunches :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
fix_lunches_price.grid(row=1,column=0)

fix_lunches_entry=Entry(bill_menu,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
fix_lunches_entry.grid(row=1,column=1,padx=10,pady=3)

chinese_price=Label(bill_menu,text='Chinese :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
chinese_price.grid(row=2,column=0)

chinese_entry=Entry(bill_menu,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
chinese_entry.grid(row=2,column=1,padx=10,pady=3)

fast_foods_tax=Label(bill_menu,text='Fast foods Tax :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
fast_foods_tax.grid(row=0,column=3)

fast_foods_tax_entry=Entry(bill_menu,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
fast_foods_tax_entry.grid(row=0,column=4,padx=10,pady=3)

fix_lunches_tax=Label(bill_menu,text='Fix Lunches Tax :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
fix_lunches_tax.grid(row=1,column=3)

fix_lunches_tax_entry=Entry(bill_menu,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
fix_lunches_tax_entry.grid(row=1,column=4,padx=10,pady=3)

chinese_tax=Label(bill_menu,text='Chinese Tax :',font=('Times new roman',15,'bold'),bg='gray20',fg='white',bd=7)
chinese_tax.grid(row=2,column=3)

chinese_tax_entry=Entry(bill_menu,font=('Times new roman',15,),bg='white',fg='gray20',bd=2,relief= GROOVE,width=10)
chinese_tax_entry.grid(row=2,column=4,padx=10,pady=3)

# button frame 

button_frame=Frame(bill_menu,bd=8,relief=RAISED,bg='white')
button_frame.grid(row=0,column=5,rowspan=3) 

total_button=Button(button_frame,text='Total',font=('times new roman',15,'bold'),fg='black',bg='gray20',bd=2,width=8,relief= RAISED,command=total)
total_button.grid(row=0,column=0,pady=25,padx=15)

bill_button=Button(button_frame,text='Bill',font=('times new roman',15,'bold'),fg='black',bg='gray20',bd=2,width=8,relief= RAISED,command=bill_area)
bill_button.grid(row=0,column=1,pady=25,padx=15)

print_button=Button(button_frame,text='Print',font=('times new roman',15,'bold'),fg='black',bg='gray20',bd=2,width=8,relief= RAISED,command=print_bill)
print_button.grid(row=0,column=3,pady=25,padx=15)

clear_button=Button(button_frame,text='Clear',font=('times new roman',15,'bold'),fg='black',bg='gray20',bd=2,width=8,relief= RAISED,command=clear_bill)
clear_button.grid(row=0,column=4,pady=25,padx=15)

root.update()
win_width = root.winfo_width()
win_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

win_x = int((screen_width/2) - (win_width/2))
win_y = int((screen_height/2) - (win_height/2))

root.geometry(f"{win_width}x{win_height}+{win_x}+{win_y}")

root.mainloop()