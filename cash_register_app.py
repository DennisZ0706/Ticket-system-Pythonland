import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import datetime
import time
import winsound
import os
from os import supports_bytes_environ
from tkinter import simpledialog
from tkinter import messagebox
import webbrowser

bg_app ='#d4e783'

root = tk.Tk()
root.iconbitmap('Img/Logo2.ico')
root.title('Kassa "Pythonland"')
root.configure(bg=bg_app)
root.geometry('1200x980+300+0')
root.resizable(False, False)

frame1 = Frame(root, width=580, height=680, background=bg_app)
frame2 = Frame(root, width=580, height=680, background=bg_app)
frame3 = Frame(root, width=580, height=680, background=bg_app)
frame4 = Frame(root, width=580, height=680, background=bg_app)
frame5 = Frame(root, width=580, height=680, background=bg_app)
frame6 = Frame(root, width=580, height=680, background=bg_app)
frame7 = Frame(root, width=580, height=680, background=bg_app)
frame8 = Frame(root, width=580, height=680, background=bg_app)

frame1.place(relx=.510, rely=.300)
frame2.place(relx=.510, rely=.300)
frame3.place(relx=.510, rely=.300)
frame4.place(relx=.510, rely=.300)
frame5.place(relx=.510, rely=.300)
frame6.place(relx=.510, rely=.300)
frame7.place(relx=.510, rely=.300)
frame8.place(relx=.510, rely=.300)

#================================= LISTS AND VARIABLES =================================
                                   
# Lists for remembering last scanned ticket

entrance_2 = [0, 0]
parking_2 = [0, 0]
restaurant_2 = [0, 0]
theatre_2 = [0, 0]
facepaint_2 = [0, 0]
icecreamparlor_2 = [0, 0]


# Lists for remembering last 5 scanned tickets

entrance_5 = []
parking_5 = []
restaurant_5 = []
theatre_5 = []
facepaint_5 = []
icecreamparlor_5 = []

entrance = 'Entrance'
parking = 'Parking'
restaurant = 'Restaurant'
theatre = 'Theatre'
facepaint = 'Facepaint'
icecreamparlor = 'Icecreamparlor'

# Directories for writing data in the database

dir_entrance = r'Database/Cash_Register/Entrance'
dir_parking = r'Database/Cash_Register/Parking'
dir_restaurant = r'Database/Cash_Register/Restaurant'
dir_theatre = r'Database/Cash_Register/Theatre'
dir_facepaint = r'Database/Cash_Register/Facepaint'
dir_icecreamparlor = r'Database/Cash_Register/Icecreamparlor'


#==================================== POSITION CAMERA ===================================

camera_x = 30
camera_y = 370

#======================================== IMAGES ========================================
                                          
logo1 = ImageTk.PhotoImage(Image.open('Img/Logo1.jpg'))

image_tickets = ImageTk.PhotoImage(Image.open('Img/Tickets1.jpg'))
image_parking = ImageTk.PhotoImage(Image.open('Img/Parkeren1.jpg'))
image_restaurant = ImageTk.PhotoImage(Image.open('Img/Restaurant1.jpg'))
image_theatre = ImageTk.PhotoImage(Image.open('Img/Theater1.jpg'))
image_facepaint = ImageTk.PhotoImage(Image.open('Img/Schmink1.jpg'))
image_icecreamparlor = ImageTk.PhotoImage(Image.open('Img/IJs1.jpg'))

image_denied = ImageTk.PhotoImage(Image.open('Img/Geen_toegang.jpg'))
image_allowed = ImageTk.PhotoImage(Image.open('Img/Wel_toegang.jpg')) 
         
#================================ FONTS AND TEXT COLORS =================================
                                
#Titles
title1_font = font=('Helvetica', 72, 'bold')
title1_color = 'black'
title1_bg = bg_app

title2_font = font=('Showcard Gothic', 32, '')
title2_color = 'black'
title2_bg = '#9ddc38'

#Text
app_font1 = font=('Helvetica', 12, '')
app_font1_color = 'black'
app_font1_bg = bg_app

#Buttons
button1_font = font=('Helvetica', 16, '')
button1_color = 'black'
button1_bg = bg_app

button2_font = font=('Showcard Gothic', 18, )
button2_color = 'black'
button2_bg = '#9ddc38'

#Dates
date_font = font=('Showcard Gothic', 32, 'bold')
date_color = 'black'
date_bg = 'white'

#Clock
clock_font = font=('Courier', 26, 'bold')
clock_color = '#9ddc38'
clock_bg = 'black'

#Checklist
check1_font = font=('Courier', 16, 'bold')
check1_color = 'green'
check1_bg = 'black'

check2_font = font=('Courier', 12, 'bold')
check2_color = 'green'
check2_bg = 'black'

check3_font = font=('Courier', 10, 'bold')
check3_color = 'green'
check3_bg = 'black'

#Entry
entry_font = font=('Helvetica', 16, 'bold')
entry_color = 'black'
entry_bg = 'white'

#================================== GENERAL FUNCTIONS ==================================
                                    
cap = cv2.VideoCapture(0)

# Function for showing frames

def show_frame(frame):

    frame.tkraise()

# Function to show corresponding image at checkout

def picture(image):

    app_picture.config(image=image)

# Function to show calendar with date

def show_datum(): 

    weekday_now = datetime.datetime.now().strftime('%a')
    day_now = datetime.datetime.now().strftime('%d') 
    month_now = datetime.datetime.now().strftime('%m')
    year_now = datetime.datetime.now().strftime('%y') 

    date_weekday.config(text=weekday_now)
    date_day.config(text=day_now)
    date_month.config(text=month_now)
    date_year.config(text=year_now)

# Function to show clock

def show_clock():

    clock_hour = datetime.datetime.now().strftime('%H')
    clock_min = datetime.datetime.now().strftime('%M')
    clock_sec = datetime.datetime.now().strftime('%S')

    app_clock.config(text=clock_hour + ":" + clock_min + ":" + clock_sec)
    app_clock.after(1000, show_clock)

# Function for scanning using laptop camera.

def scanner():

    cv2image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image = img)
    camera.imgtk = imgtk
    camera.configure(image=imgtk)
    
    success, image = cap.read()
    for scan in decode(image, symbols=[ZBarSymbol.QRCODE]):

        global ticketnumber
        ticketnumber = scan.data.decode('utf-8')

        global scan_hour
        global scan_min
        global scan_sec
        global scan_day
        global scan_month
        global scan_year

        scan_hour = datetime.datetime.now().strftime('%H')
        scan_min = datetime.datetime.now().strftime('%M')
        scan_sec = datetime.datetime.now().strftime('%S')
        scan_day = datetime.datetime.now().strftime('%d')
        scan_month = datetime.datetime.now().strftime('%m')
        scan_year = datetime.datetime.now().strftime('%y')
        
        get_info()

        if r.get() == 1:
            scan_entrance()

        if r.get() == 2:
            scan_parking()

        if r.get() == 3:
            scan_restaurant()

        if r.get() == 4:
            scan_theatre()

        if r.get() == 5:
            scan_facepaint()
        
        if r.get() == 6:
            scan_icecreamparlor()
        
    camera.after(20, scanner)

# Function to retrieve ticket data from database 

def get_info():

    try:

        with open('Database/Tickets/Data/Ticket ' + ticketnumber + '.txt') as content:
            lines = content.read().splitlines()

            global number_toddle
            global number_child
            global number_adult
            global number_senior
            global number_visitors

            number_toddle = int(lines[9])
            number_child = int(lines[11])
            number_adult = int(lines[13])
            number_senior = int(lines[15])
            number_visitors = int(lines[18])

            global number_car
            global number_restaurant
            global number_theatre
            global number_facepaint 
            global number_icecreamparlor
            global time_theatre

            number_car = int(lines[23])
            number_restaurant = int(lines[25])
            number_theatre = int(lines[27])
            number_facepaint = int(lines[29])
            number_icecreamparlor = int(lines[31])
            time_theatre = lines[34]
    
    except FileNotFoundError:
        pass

# Function to check whether the date on the ticket corresponds to the day on which 
# the visitor visits the park. 

def check_date():

    try:
    
        with open('Database/Tickets/Data/Ticket ' + ticketnumber + '.txt', 'r') as f:
                
            file = f.read().splitlines()
            datum = file[2]
                
            if datum == str(scan_day + '/' + scan_month + '/' + scan_year):

                return True
                
            else:

                return False
    
    except FileNotFoundError:
        return "Invalid code"
        

# Function for checking whether the ticket has not yet been used.  

def check_used(dir):

    folderpath = dir
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    
    used_tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            used_tickets.append(info)

    if ticketnumber in used_tickets:
        return True

    else:
        return False

# Function to show image when access is allowed. The picture shows also how many 
# visitors may pass

def acces_number(aantal):
    
    global foto
    foto = ImageTk.PhotoImage(Image.open('Img/Wel_toegang' + str(aantal) + '.jpg')) 
    Acces = Label(root, image = foto)
    Acces.place(x=camera_x, y=camera_y)
    Acces.after(2000, Acces.destroy)

# Feature to show image when access should be denied

def acces_denied():

    denied = Label(root, image=image_denied)
    denied.place(x=camera_x, y=camera_y)
    denied.after(2000, denied.destroy)

# Function to show last 5 scanned tickets.

def show_last5(list, label):
  
    list.append(ticketnumber + "  " + scan_hour + ":" + scan_min + ":" 
                 + scan_sec)

    if len(list) == 6:

        list.pop(0)

    label.delete(0, END)

    for x in list:
        label.insert(0, "Ticket" + x  + '\n') 

# Function to remember last scanned ticket

def remember_last(list):

    list.append(ticketnumber)

    if len(list) == 3:

        list.pop(0)

# Function to show ticket details for the following cash registers:
# entrance, restaurant, theatre, icecream parlor

def show_info1(label): 

    label.delete(0, END)

    if r.get() == 4:

        label.insert(END, "Ticket " + ticketnumber  + '         ' + time_theatre + '\n')

    else:

        label.insert(END, "Ticket " + ticketnumber  + '\n')

    label.insert(END, '\n')
    label.insert(END, "Aantal kleine kinderen: " + str(number_toddle)  + '\n')
    label.insert(END, '\n')
    label.insert(END, "Aantal kinderen: " + str(number_child)  + '\n')
    label.insert(END, '\n')
    label.insert(END, "Aantal volwassenen: " + str(number_adult)  + '\n')
    label.insert(END, '\n')
    label.insert(END, "Aantal senioren: " + str(number_senior)  + '\n')
    label.insert(END, '\n')
    label.insert(END, "Totaal aantal bezoekers: " + str(number_visitors)  + '\n')

# Function to show ticket details for the following cash registers:
# parking, facepaint 

def show_info2(label):

    label.delete(0, END)

    if r.get() == 2:

        label.insert(END, "Ticket " + ticketnumber  + '\n')
        label.insert(END, '\n')
        label.insert(END, "Aantal auto's: " + str(number_car))

    if r.get() == 5:

        label.insert(END, "Ticket " + ticketnumber  + '\n')
        label.insert(END, '\n')
        label.insert(END, "Aantal schminken: " + str(number_facepaint))

# Function to show message if there has not been paid for facility and
# access should be denied.

def show_error1(label):

    label.delete(0, END)

    label.insert(END, "Gebruik faciliteit niet" + '\n') 
    label.insert(END, "bij Ticket inbegrepen")

# Function to show message if ticket has already been used and
# access should be denied

def show_error2(label):

    label.delete(0, END)

    label.insert(END, "Ticket al gebruikt")     

# Function to show message if date on ticket does not match
# with the day on which the visit takes place and access should be denied.

def show_error3(label):

    label.delete(0, END)

    label.insert(END, "Ticket is op deze datum" + '\n') 
    label.insert(END, "niet meer geldig")  

# Function to show message if qr code is invalid.

def show_error4(label):

    label.delete(0, END)

    label.insert(END, "Ongeldige ticket") 

# Function for writing data to the database when visiting
# visiting facility: entrance, restaurant, theatre, icecream parlor

def database_facility(dir):

    with open('Database/Cash_Register/' + dir + '/Ticket ' + ticketnumber + ' ' + scan_day + "_" + 
                scan_month + "_" + scan_year + '.txt', 'w') as file_entrance:

            file_entrance.write("%07d"%int(ticketnumber) + '\n' + '\n')
            file_entrance.write(scan_day + "/" + scan_month + "/" + scan_year + '\n' + '\n')
            file_entrance.write(scan_hour + ":" + scan_min + ":" + scan_sec + '\n' + '\n')
            file_entrance.write(dir + '\n \n')
            file_entrance.write('Aantal kleinkind:' + '\n') 
            file_entrance.write(str(number_toddle) + '\n')
            file_entrance.write('Aantal kind:' + '\n') 
            file_entrance.write(str(number_child) + '\n')
            file_entrance.write('Aantal volwassenen:' + '\n') 
            file_entrance.write(str(number_adult) + '\n')
            file_entrance.write('Aantal senioren:' + '\n') 
            file_entrance.write(str(number_senior) + '\n' + '\n')
            file_entrance.write('Totaal:' + '\n')
            file_entrance.write(str(number_visitors))

# Function for writing data to the database when visiting facility: face painting

def database_facepaint():

    # Calculation of the number of faces painted. It is assumed that a quarter of the
    # small children is a baby and will not have their face painted. It is also assumed
    # that with every ticket the youngest of the group will be painted.  

    average_toddle = int(number_toddle * 0.75)

    if number_facepaint == number_toddle + number_child + number_adult + number_senior:
                facepaint_toddle = number_toddle
                facepaint_child = number_child
                facepaint_adult = number_adult
                facepaint_senior = number_senior

    else:

        if number_toddle == 0:
            facepaint_toddle = 0

        else:
            if number_facepaint <= average_toddle:
                        facepaint_toddle = number_facepaint
                            
            else:
                facepaint_toddle = average_toddle
                
        if number_child == 0 or number_facepaint - facepaint_toddle == 0:
                    facepaint_child = 0
                
        else:
            if (number_facepaint - facepaint_toddle) >= number_child:
                facepaint_child = number_child

            else:
                facepaint_child = number_facepaint - facepaint_toddle

        if number_adult == 0 or number_facepaint - facepaint_toddle - facepaint_child == 0:
                    facepaint_adult = 0

        else:
            if (number_facepaint - facepaint_toddle - facepaint_child) >= number_adult:
                facepaint_adult = number_adult
                    
            else:
                facepaint_adult = number_facepaint - facepaint_toddle - facepaint_child
                
        if  number_senior == 0 or number_facepaint - facepaint_toddle - facepaint_child - facepaint_adult == 0:
                facepaint_senior = 0
                
        else: 
            if (number_facepaint - facepaint_toddle - facepaint_child - facepaint_adult) >= number_senior:
                facepaint_senior = number_senior
                    
            else:
                facepaint_senior = number_facepaint - facepaint_toddle - facepaint_child - facepaint_adult

    with open('Database/Cash_Register/' + facepaint + '/Ticket ' + ticketnumber + ' ' + scan_day + "_" + 
                scan_month + "_" + scan_year + '.txt', 'w') as file_entrance:

            file_entrance.write("%07d"%int(ticketnumber) + '\n' + '\n')
            file_entrance.write(scan_day + "/" + scan_month + "/" + scan_year + '\n' + '\n')
            file_entrance.write(scan_hour + ":" + scan_min + ":" + scan_sec + '\n' + '\n')
            file_entrance.write(facepaint + '\n' + '\n')
            file_entrance.write('Aantal schminken kleinkinderen:' + '\n')
            file_entrance.write(str(facepaint_toddle) + '\n')
            file_entrance.write('Aantal schminken kinderen:' + '\n')
            file_entrance.write(str(facepaint_child) + '\n')
            file_entrance.write('Aantal schminken volwassenen:' + '\n')
            file_entrance.write(str(facepaint_adult) + '\n')
            file_entrance.write('Aantal schminken senioren:' + '\n')
            file_entrance.write(str(facepaint_senior) + '\n' + '\n')
            file_entrance.write('Aantal schminken totaal:' '\n') 
            file_entrance.write(str(number_facepaint) + '\n' + '\n')
            file_entrance.write('Toegang:' + '\n' + '\n')
            file_entrance.write('Aantal kleinkind:' + '\n') 
            file_entrance.write(str(number_toddle) + '\n')
            file_entrance.write('Aantal kind:' + '\n') 
            file_entrance.write(str(number_child) + '\n')
            file_entrance.write('Aantal volwassenen:' + '\n') 
            file_entrance.write(str(number_adult) + '\n')
            file_entrance.write('Aantal senioren:' + '\n') 
            file_entrance.write(str(number_senior) + '\n' + '\n')
            file_entrance.write('Totaal:' + '\n')
            file_entrance.write(str(number_visitors))

# Function for writing data to the database when visiting facility: parking

def database_parking():

    with open('Database/Cash_Register/' + parking + '/Ticket ' + ticketnumber + ' ' + scan_day + "_" + 
                scan_month + "_" + scan_year + '.txt', 'w') as file_entrance:

            file_entrance.write("%07d"%int(ticketnumber) + '\n' + '\n')
            file_entrance.write(scan_day + "/" + scan_month + "/" + scan_year + '\n' + '\n')
            file_entrance.write(scan_hour + ":" + scan_min + ":" + scan_sec + '\n' + '\n')
            file_entrance.write(parking + '\n \n')
            file_entrance.write('Aantal kleinkind:' + '\n') 
            file_entrance.write(str(number_toddle) + '\n')
            file_entrance.write('Aantal kind:' + '\n') 
            file_entrance.write(str(number_child) + '\n')
            file_entrance.write('Aantal volwassenen:' + '\n') 
            file_entrance.write(str(number_adult) + '\n')
            file_entrance.write('Aantal senioren:' + '\n') 
            file_entrance.write(str(number_senior) + '\n' + '\n')
            file_entrance.write('Totaal:' + '\n')
            file_entrance.write(str(number_visitors) + '\n' + '\n')
            file_entrance.write(parking + '\n' + '\n')
            file_entrance.write('Aantal ' + (parking.lower()) + ':' '\n') 
            file_entrance.write(str(number_car) + '\n')

# Function to write data to the database for keep track of the current number of cars 
# at the parking lot.

def database_parkinglot():    

    folderpath = r'Database/Parkinglot'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            
            
            if info == ticketnumber:
                delete = path
        
        f.close()
    
    try:           
        os.remove(delete)

    except UnboundLocalError:
        pass

# Function for showing which checkout is currently in use.

def change_title(checkout):

    scan_title.config(text='Scan ' + checkout)

# Function to welcome visitors with a different time slot than the current time
# if theatre still has seats left. 

def escape_theatre():

    winsound.Beep(1000, 500)
    acces_number(number_theatre)
    show_last5(theatre_5, check_theatre)
    show_info1(info_theatre)
    database_facility(theatre)
    remember_last(theatre_2)
    button_escape.place(x=1500, y=1500)



#================================ FUNCTIONS CHECKOUTS ==================================
                                    
                                     
# Checkout entrance

def scan_entrance():

    if check_date() == "Invalid code":

        acces_denied()
        show_error4(info_entrance)

    elif check_date() == False:

        acces_denied()
        show_error3(info_entrance)
    
    else:

        if check_used(dir_entrance) == True:

            acces_denied()
    
            if entrance_2[1] == ticketnumber:
                pass

            else:
                show_error2(info_entrance)

        else:

            winsound.Beep(1000, 500)
            acces_number(number_visitors)
            show_last5(entrance_5, check_entrance)
            show_info1(info_entrance)
            database_facility(entrance)
            remember_last(entrance_2)
        
# Checkout parkinglot

def scan_parking():

    if check_date() == "Invalid code":

        acces_denied()
        show_error4(info_parking)

    elif check_date() == False:

        acces_denied()
        show_error3(info_parking)
    
    else:


        if number_car == 0:
            
            acces_denied()
            show_error1(info_parking)
            remember_last(parking_2)

        elif check_used(dir_parking) == True:

            acces_denied()
    
            if parking_2[1] == ticketnumber:
                pass

            else:
                show_error2(info_parking)
            
        else:

            winsound.Beep(1000, 500)
            acces_number(number_car)
            show_last5(parking_5, check_parking)
            show_info2(info_parking)
            database_parking()
            database_parkinglot()
            remember_last(parking_2)
   
# Checkout restaurant

def scan_restaurant():

    if check_date() == "Invalid code":

        acces_denied()
        show_error4(info_restaurant)

    elif check_date() == False:

        acces_denied()
        show_error3(info_restaurant)
    
    else:

        if number_restaurant == 0:
            
            acces_denied()
            show_error1(info_restaurant)
            remember_last(restaurant_2)

        elif check_used(dir_restaurant) == True:

            acces_denied()
    
            if restaurant_2[1] == ticketnumber:
                pass

            else:
                show_error2(info_restaurant)
            
        else:

            winsound.Beep(1000, 500)
            acces_number(number_restaurant)
            show_last5(restaurant_5, check_restaurant)
            show_info1(info_restaurant)
            database_facility(restaurant)
            remember_last(restaurant_2)

# Checkout theatre

def scan_theatre():

    entrance_theatre = time_theatre[0:2]

    if check_date() == "Invalid code":

        acces_denied()
        show_error4(info_theatre)
    

    elif check_date() == False:

        acces_denied()
        show_error3(info_theatre)
    
    else:

        if number_theatre == 0:
            
            acces_denied()
            show_error1(info_theatre)
            remember_last(theatre_2)

        elif check_used(dir_theatre) == True:

            acces_denied()
    
            if theatre_2[1] == ticketnumber:
                pass

            else:
                show_error2(info_theatre)
            
        elif (int(entrance_theatre) -1) != int(scan_hour):
            
            acces_denied()

            info_theatre.delete(0, END)
            info_theatre.insert(END, "Ticket niet geldig op dit") 
            info_theatre.insert(END, "tijdstip")

            button_escape.place(x=90, y=480)
    
        else:
        
            winsound.Beep(1000, 500)
            acces_number(number_theatre)
            show_last5(theatre_5, check_theatre)
            show_info1(info_theatre)
            database_facility(theatre)
            remember_last(theatre_2)
            button_escape.place(x=1500, y=1500)                                                                         

# Checkout facepaint

def scan_facepaint():

    if check_date() == "Invalid code":

        acces_denied()
        show_error4(info_facepaint)

    elif check_date() == False:

        acces_denied()
        show_error3(info_facepaint)
    
    else:

        if number_facepaint == 0:
            
            acces_denied()
            show_error1(info_facepaint)
            remember_last(facepaint_2)
        
        elif check_used(dir_facepaint) == True:

            acces_denied()
    
            if facepaint_2[1] == ticketnumber:
                pass

            else:
                show_error2(info_facepaint)

        else:
        
            winsound.Beep(1000, 500)
            acces_number(number_facepaint)
            show_last5(facepaint_5, check_facepaint)
            show_info2(info_facepaint)
            database_facepaint()
            remember_last(facepaint_2)

# Checkout icecreamparlor

def scan_icecreamparlor():

    if check_date() == "Invalid code":

        acces_denied()
        show_error4(info_icecreamparlor)

    elif check_date() == False:

        acces_denied()
        show_error3(info_icecreamparlor)
    
    else:

        if number_icecreamparlor == 0:
            
            acces_denied()
            show_error1(info_icecreamparlor)
            remember_last(icecreamparlor_2)
        
        elif check_used(dir_icecreamparlor) == True:

            acces_denied()
    
            if icecreamparlor_2[1] == ticketnumber:
                pass

            else:
                show_error2(info_icecreamparlor)
        
        else:
        
            winsound.Beep(1000, 500)
            acces_number(number_icecreamparlor)
            show_last5(icecreamparlor_5, check_icecreamparlor)
            show_info1(info_icecreamparlor)
            database_facility(icecreamparlor)
            remember_last(icecreamparlor_2)
    
#================================== FUNCTIONS FRAMES ===================================

# Functions for visual changes when using different cash registers

def checkout_entrance():
    
    picture(image_tickets)
    show_frame(frame1)
    change_title(entrance)
    info_entrance.delete(0, END)

def checkout_parking():

    picture(image_parking)
    show_frame(frame2)
    change_title(parking)
    info_parking.delete(0, END)

def checkout_restaurant():

    picture(image_restaurant)
    show_frame(frame3)
    change_title(restaurant)
    info_restaurant.delete(0, END)


def checkout_theatre():

    picture(image_theatre)
    show_frame(frame4)
    change_title(theatre)
    button_escape.place(x=1500, y=1500)
    info_theatre.delete(0, END)

def checkout_facepaint():

    picture(image_facepaint)
    show_frame(frame5)
    change_title(facepaint)
    info_facepaint.delete(0, END)
    
def checkout_icecreamparlor():

    picture(image_icecreamparlor)
    show_frame(frame6)
    change_title(icecreamparlor)
    info_icecreamparlor.delete(0, END)

# Function to retrieve ticket data from database

def database_data():

    try:
    
        show_frame(frame7)

        check_ticket.delete(0, END)

        number = input_data.get()
        number = int(number)
        number = "%07d"%number

        f = open("Database/Tickets/Data/Ticket " + str(number) + ".txt", "r")

        lines = f.readlines()

        check_ticket.insert(END, 'Ticket ' + lines[0])

        for line in lines[7:19]:
            check_ticket.insert(END, line)
        
        for line in lines[21:36]:
            check_ticket.insert(END, line)
        
        input_data.delete(0,END)
    
    except FileNotFoundError:

        check_ticket.insert(END, "Ticket " + str(number) + " bestaat niet")
        input_data.delete(0,END)
    
    except ValueError:

        check_ticket.insert(END, "Foute invoer")
        input_data.delete(0,END)

# Function to search for tickets by name in the database

def database_naam():
    
    firstname_visitor = input_firstname.get()
    lastname_visitor1 = input_lastname.get()

    if len(firstname_visitor) <= 1 or len(lastname_visitor1) <= 1:
        messagebox.showerror("Geen Invoer",
                                    "Voer een volledige voor- en achternaam in")
        

    elif  not all(x.isalpha() or x.isspace() for x in firstname_visitor):
        messagebox.showerror("Ongeldige Voornaam",
                                    "Gebruik geen cijfer of een ander ongeldig teken")
        
    
    elif  not all(x.isalpha() or x.isspace() for x in lastname_visitor1):
        messagebox.showerror("Ongeldige Achternaam",
                                    "U heeft een cijfer of een ander ongeldig teken ingevoerd")

    else:

        input_firstname.delete(0, END)
        input_lastname.delete(0, END)

        show_frame(frame8)

        firstname_visitor = firstname_visitor.lower()
        firstname_visitor = firstname_visitor.strip()
        firstname_visitor = firstname_visitor.title()

        
        lastname_visitor1 = lastname_visitor1.lower()
        lastname_visitor1 = lastname_visitor1.strip()
        lastname = lastname_visitor1.split()

        last_word = lastname[-1]
        last_word = last_word.title()
        lastname.pop(-1)
        rest = " ".join(lastname)

        lastname_visitor2 = rest + " " + last_word

        if len(lastname) > 0:

            name_visitor = firstname_visitor + " " + lastname_visitor2

        else: 
    
            name_visitor = firstname_visitor + "" + lastname_visitor2

    folderpath = r'Database/Tickets/Name_ticket'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            naam = file[4]
            nummer = file[0]
            
            if naam == name_visitor:
                tickets.append(nummer)
                

    if len(tickets) == 0:
        check_name.delete(0, END)
        check_name.insert(END, "Er bevindt zich geen ticket met")
        check_name.insert(END, '\n')
        check_name.insert(END, "de naam: " + name_visitor)
        check_name.insert(END, '\n')
        check_name.insert(END, "in de Database")



    else: 
        check_name.delete(0, END)
        check_name.insert(END, "Onderstaande tickets staan op")
        check_name.insert(END, '\n')
        check_name.insert(END, "de naam: " + name_visitor)
        check_name.insert(END, '\n')
        check_name.insert(END, "in de Database")
        check_name.insert(END, '\n')

        for ticket in tickets:
            check_name.insert(END, "Ticket " + ticket + '\n')

# Function to retrieve printable PDF when entering ticketnumber.

def print_pdf():

    try:
        number = int(input_print.get())
        number = "%07d"%number
        input_print.delete(END,0)
    
    except ValueError:
        pass

    folderpath = r'Database/Tickets/Data'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            tickets.append(info)

    if number in tickets:

        webbrowser.open_new(r'Database\Tickets\Pdf\Ticket '+ str(number) + '.pdf')

    else:

        check_name.delete(0, END)
        check_name.insert(END, "Er bevindt zich geen ticket met")
        check_name.insert(END, '\n')
        check_name.insert(END, "het nummer: " + str(number))
        check_name.insert(END, '\n')
        check_name.insert(END, "in de Database")

# Function to return to frame of checkout which is currently in use.

def database_close():
    
    if r.get() == 1:
        checkout_entrance()

    if r.get() == 2:
        checkout_parking()

    if r.get() == 3:
        checkout_restaurant()

    if r.get() == 4:
        checkout_theatre()

    if r.get() == 5:
        checkout_facepaint()
        
    if r.get() == 6:
        checkout_icecreamparlor()

# Function to remove visitor names from database the next day after
# visit relevant visitors. Names are therefore only available on the day of the visit.

def delete_names():
    
    time_now = datetime.datetime.now()
    date_now = str(time_now.strftime('%d')) + '/' + str(time_now.strftime('%m')) + '/' + str(time_now.strftime('%y'))

    folderpath = r'Database/Tickets/Name_ticket'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    delete = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            datum_ticket = file[2]
            if datum_ticket != date_now:
                delete.append(path)
        f.close()

    for ticket in delete:
        os.remove(ticket)
 
#==================================== FORMAT ROOT =====================================

app_title = Label(root, text="KASSA", font=title1_font, 
                        bg=title1_bg, fg=title1_color)
app_title.place(x=390, y=30)

date_weekday = Label(root, text="", font=date_font, bg=date_bg, fg=date_color, 
                      borderwidth=2, relief="ridge", width=3)
date_day = Label(root, text="", font=date_font, bg=date_bg, fg=date_color,
                  borderwidth=2, relief="ridge", width=2)
date_month = Label(root, text="", font=date_font, bg=date_bg, fg=date_color,
                    borderwidth=2, relief="ridge", width=2)
date_year = Label(root, text="", font=date_font, bg=date_bg, fg=date_color,
                   borderwidth=2, relief="ridge", width=2)

date_weekday.place(x=30, y=30)
date_day.place(x=140, y=30)
date_month.place(x=216, y=30)
date_year.place(x=292, y=30)

app_clock = Label(root, text="", font=clock_font, bg=clock_bg, fg =clock_color)
app_clock.place(x=90, y=110)

app_picture = Label(root, image=image_tickets, borderwidth=0)
app_picture.place(x=840, y=32)

app_logo = Label(root, image=logo1, borderwidth=0)
app_logo.place(x=980, y=-5) 

r = IntVar()
r.set('1')

button_entrance = Radiobutton(root, text="Toegang", font=button1_font, 
                             bg=button1_bg, fg=button1_color, 
                             variable=r, value=1, command=checkout_entrance)
button_parking = Radiobutton(root, text="Parkeren", font=button1_font, 
                              bg=button1_bg, fg=button1_color,
                              variable=r, value=2, command=checkout_parking)
button_restaurant = Radiobutton(root, text="Restaurant", font=button1_font, 
                                bg=button1_bg, fg=button1_color,
                                variable=r, value=3, command=checkout_restaurant)
button_theatre = Radiobutton(root, text="Theater", font=button1_font, 
                             bg=button1_bg, fg=button1_color,
                             variable=r, value=4, command=checkout_theatre)
button_facepaint = Radiobutton(root, text="Schminken", font=button1_font, 
                               bg=button1_bg, fg=button1_color,
                               variable=r, value=5, command=checkout_facepaint)
button_icecreamparlor = Radiobutton(root, text="IJssalon", font=button1_font, 
                              bg=button1_bg, fg=button1_color,
                              variable=r, value=6, command=checkout_icecreamparlor)

button_entrance.place(x=20, y=200)
button_parking.place(x=220, y=200)
button_restaurant.place(x=420, y=200)
button_theatre.place(x=620, y=200)
button_facepaint.place(x=820, y=200)
button_icecreamparlor.place(x=1020, y=200)

scan_title = Label(root, text="Scan Toegang", font=title2_font, 
                        bg=title2_bg, fg=title2_color, width=14)
scan_title.place(x=34, y=294)

camera = Label(root, width=500, height=460)
camera.place(x=camera_x, y=camera_y)

app_data = Label(root, text="Ticketgegevens opvragen:",
                          font=app_font1, bg=app_font1_bg, fg=app_font1_color)
app_data.place(x=30, y=920)

input_data = Entry(root, width=8, font=entry_font, bg=entry_bg, fg=entry_color)
input_data.place(x=270, y=916)

button_data = Button(root, text="CHECK", font=button2_font, bg=button2_bg,
                         fg=button2_color, command=database_data)
button_data.place(x=406, y=900)

#=================================== FORMAT FRAME1 =====================================

check_entrance = Listbox(frame1, font=check1_font, bg=check1_bg, fg=check1_color,  
                        width=23, height=5)
check_entrance.place(x=90, y=0)

info_entrance = Listbox(frame1, font=check2_font, bg=check2_bg, fg=check2_color,  
                        width=31, height=11)
info_entrance.place(x=90, y=200)

app_firstname1 = Label(frame1, text="Voornaam:",
                          font=app_font1, bg=app_font1_bg, fg=app_font1_color)
app_firstname1.place(x=0, y=605)

app_name = Label(frame1, text="Achternaam:",
                          font=app_font1, bg=app_font1_bg, fg=app_font1_color)
app_name.place(x=0, y=645)

input_firstname = Entry(frame1, width=18, font=entry_font, bg=entry_bg, fg=entry_color)
input_firstname.place(x=140, y=600)

input_lastname = Entry(frame1, width=18, font=entry_font, bg=entry_bg, fg=entry_color)
input_lastname.place(x=140, y=640)

button_name = Button(frame1, text="CHECK", font=button2_font, bg=button2_bg,
                         fg=button2_color, command=database_naam)
button_name.place(x=440, y=605)

#=================================== FORMAT FRAME2 =====================================

check_parking = Listbox(frame2, font=check1_font, bg=check1_bg, fg=check1_color, 
                        width=23, height=5)
check_parking.place(x=90, y=0)

info_parking = Listbox(frame2, font=check2_font, bg=check2_bg, fg=check2_color,  
                        width=31, height=11)
info_parking.place(x=90, y=200)

#=================================== FORMAT FRAME3 =====================================

check_restaurant = Listbox(frame3, font=check1_font, bg=check1_bg, fg=check1_color,  
                        width=23, height=5)
check_restaurant.place(x=90, y=0)

info_restaurant = Listbox(frame3, font=check2_font, bg=check2_bg, fg=check2_color,  
                        width=31, height=11)
info_restaurant.place(x=90, y=200)

#=================================== FORMAT FRAME4 =====================================

check_theatre = Listbox(frame4, font=check1_font, bg=check1_bg, fg=check1_color,  
                        width=23, height=5)
check_theatre.place(x=90, y=0)

info_theatre = Listbox(frame4, font=check2_font, bg=check2_bg, fg=check2_color,  
                        width=31, height=11)
info_theatre.place(x=90, y=200)

button_escape = Button(frame4, text="ESCAPE", font=button2_font, bg=button2_bg,
                         fg=button2_color, command=escape_theatre)

#=================================== FORMAT FRAME5 =====================================

check_facepaint = Listbox(frame5, font=check1_font, bg=check1_bg, fg=check1_color,  
                        width=23, height=5)
check_facepaint.place(x=90, y=0)

info_facepaint = Listbox(frame5, font=check2_font, bg=check2_bg, fg=check2_color,  
                        width=31, height=11)
info_facepaint.place(x=90, y=200)

#=================================== FORMAT FRAME6 =====================================

check_icecreamparlor = Listbox(frame6, font=check1_font, bg=check1_bg, fg=check1_color,  
                        width=23, height=5)
check_icecreamparlor.place(x=90, y=0)

info_icecreamparlor = Listbox(frame6, font=check2_font, bg=check2_bg, fg=check2_color,  
                        width=31, height=11)
info_icecreamparlor.place(x=90, y=200)

#=================================== FORMAT FRAME7 =====================================

button_return = Button(frame7, text ="Close", font=button2_font, bg=button2_bg,
                       fg=button2_color, command=database_close)
button_return.place(x=440, y=605)

check_ticket = Listbox(frame7, font=check3_font, bg=check3_bg, fg=check3_color,  
                        width=37, height=27)
check_ticket.place(x=90, y=0)

#=================================== FORMAT FRAME8 =====================================

button_return2 = Button(frame8, text ="Close", font=button2_font, bg=button2_bg,
                       fg=button2_color, command=database_close)
button_return2.place(x=440, y=605)

check_name = Listbox(frame8, font=check3_font, bg=check3_bg, fg=check3_color,  
                        width=37, height=27)
check_name.place(x=90, y=0)

app_firstname2 = Label(frame8, text="Ticketnummer:",
                          font=app_font1, bg=app_font1_bg, fg=app_font1_color)
app_firstname2.place(x=0, y=625)

input_print = Entry(frame8, width=8, font=entry_font, bg=entry_bg, fg=entry_color)
input_print.place(x=140, y=620)

Button_printen = Button(frame8, text="PRINT", font=button2_font, bg=button2_bg,
                         fg=button2_color, command=print_pdf)
Button_printen.place(x=300, y=605)


show_frame(frame1)
scanner()    
show_datum()
show_clock()
delete_names()

root.mainloop()