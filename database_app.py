from calendar import month
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
from tkcalendar import *
import datetime
from datetime import timedelta
import tkcalendar
from tkinter import messagebox
from fpdf import FPDF
import webbrowser

bg_app ='#d4e783'

root = tk.Tk()
root.iconbitmap('Img/Logo2.ico')
root.title('Database "Pythonland"')
root.configure(bg=bg_app)
root.geometry('1400x980+150+0')
root.resizable(False, False)

frame1 = Frame(root, width=340, height=700, background=bg_app)
frame2 = Frame(root, width=340, height=700, background=bg_app)
frame3 = Frame(root, width=340, height=700, background=bg_app)
frame4 = Frame(root, width=340, height=700, background=bg_app)
frame5 = Frame(root, width=340, height=700, background=bg_app)
frame6 = Frame(root, width=340, height=700, background=bg_app)
frame7 = Frame(root, width=290, height=80, background=bg_app)
frame8 = Frame(root, width=290, height=80, background=bg_app)
frame9 = Frame(root, width=290, height=80, background=bg_app)
frame10 = Frame(root, width=290, height=80, background=bg_app)
frame11 = Frame(root, width=290, height=80, background=bg_app)
frame12 = Frame(root, width=290, height=80, background=bg_app)
frame13 = Frame(root, width=290, height=268, background=bg_app)
frame14 = Frame(root, width=290, height=268, background=bg_app)

frame1.place(x=0, y=270)
frame2.place(x=0, y=270)
frame3.place(x=0, y=270)
frame4.place(x=0, y=270)
frame5.place(x=0, y=270)
frame6.place(x=0, y=270)
frame7.place(x=1080, y=266)
frame8.place(x=1080, y=266)
frame9.place(x=1080, y=266)
frame10.place(x=1080, y=266)
frame11.place(x=1080, y=266)
frame12.place(x=1080, y=266)
frame13.place(x=1080, y=350)
frame14.place(x=1080, y=708)

#===================================== VARIABLES =======================================

# Directories for retrieving data from the database

entrance = r'Database/Cash_Register/Entrance'
parking = r'Database/Cash_Register/Parking'
restaurant = r'Database/Cash_Register/Restaurant'
theatre = r'Database/Cash_Register/Theatre'
facepaint = r'Database/Cash_Register/Facepaint'
icecreamparlor = r'Database/Cash_Register/Icecreamparlor'
parkinglot = r'Database/Parkinglot'

# Text line variables to get corresponding info from text file from database.

toddle = 9
child = 11
adult = 13
senior = 15
total = 18
car = 3

year_now = int(datetime.datetime.now().strftime('%Y'))
month_now = int(datetime.datetime.now().strftime('%m'))
day_now = int(datetime.datetime.now().strftime('%d'))

timeslot9_10 = 9
timeslot10_11= 10
timeslot11_12= 11
timeslot12_13= 12
timeslot13_14= 13
timeslot14_15= 14
timeslot15_16= 15
timeslot16_17= 16
timeslot17_18 = 17

#======================================== IMAGES ========================================
                                             
logo1 = ImageTk.PhotoImage(Image.open('Img/Logo1.jpg'))

image_tickets = ImageTk.PhotoImage(Image.open('Img/Tickets1.jpg'))
image_parking = ImageTk.PhotoImage(Image.open('Img/Parkeren1.jpg'))
image_restaurant = ImageTk.PhotoImage(Image.open('Img/Restaurant1.jpg'))
image_theatre = ImageTk.PhotoImage(Image.open('Img/Theater1.jpg'))
image_facepaint = ImageTk.PhotoImage(Image.open('Img/Schmink1.jpg'))
image_icecreamparlor = ImageTk.PhotoImage(Image.open('Img/IJs1.jpg'))

#================================ FONTS AND TEXT COLORS =================================
                                  
#Titles
title1_font = font=('Helvetica', 56, 'bold')
title1_color = 'black'
title1_bg = bg_app

title2_font = font=('Helvetica', 26, 'bold')
title2_color = 'black'
title2_bg = bg_app

#Text
app1_font = font=('Helvetica', 12, '')
app1_color = 'black'
app1_bg = bg_app

app2_font = font=('Helvetica', 12, 'bold')
app2_color = 'black'
app2_bg = bg_app

app3_font = font=('Helvetica', 10, 'bold')
app3_color = 'black'
app3_bg = bg_app

#Buttons
button1_font = font=('Helvetica', 16, '')
button1_color = 'black'
button1_bg = bg_app

button2_font = font=('Showcard Gothic', 20, )
button2_color = 'black'
button2_bg = '#9ddc38'

#Checklist
check1_font = font=('Courier', 16, 'bold')
check1_color = 'lightgreen'
check1_bg = 'black'

check2_font = font=('Courier', 12, 'bold')
check2_color = 'lightgreen'
check2_bg = 'black'

check3_font = font=('Courier', 12, 'bold')
check3_color = 'green'
check3_bg = 'black'

check4_font = font=('Courier', 24, 'bold')
check4_color = 'red'
check4_bg = 'black'

#Entry
entry_font = font=('Helvetica', 28, '')
entry_color = 'lightgreen'
entry_bg = 'black'

#===================================== COÖRDINATEs ======================================

# column numbers
root_x1 = 340
# column % total
root_x2 = 540
# column % facility
root_x3 = 680
# column description time slot
root_x4 = 800
# column numbers time slot
root_x5 = 940

# textlines frames 
frame_y1 = 0
frame_y2 = 94
frame_y3 = 134
frame_y4 = 174
frame_y5 = 214
frame_y6 = 254
frame_y7 = 294

frame_y8 = 360
frame_y9 = 454
frame_y10 = 494
frame_y11 = 534
frame_y12 = 574
frame_y13 = 614
frame_y14 = 654
frame_y15 = 0
frame_y16 = 30

# column frames
frame_x1 = 10
frame_x2 = 60

#================================== FUNCTIONS NUMBERS ===================================
                                    
# Calculation of number of tickets per facility (or total = entry)

def tickets(facility):

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            tickets.append(info)


    return (len(tickets))

# Calculation of number of visitors per category per facility (or total = total and access)

def visitors(facility, category):

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = int(file[category])
            tickets.append(info)

    return (sum(tickets))

# BY DATE

# Calculation of number of tickets per facility on date (or total = dir_access)

def tickets_date(facility, selection):

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            date = file[2]
            if date == str(selection):
                tickets.append(info)
                
            
    return (len(tickets))

# Calculation of visitors per category per facility per date
# (or total = access and dir_access)

def visitors_date(facility, category, selection):

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = int(file[category])
            date = file[2]
            if date == selection:
                tickets.append(info)

    return (sum(tickets))

# Calculation of number of visitors per facility per time slot 

def timeslot(facility, timeslot):

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = int(file[18])
            time = (file[4])
            time = int(time[0:2])

            if time == timeslot:
                tickets.append(info)

    return (sum(tickets))

# Calculation of number of visitors per facility per time slot per date
   
def timeslot_date(facility, timeslot, selection):

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = int(file[18])
            date = file[2]
            time = (file[4])
            time = int(time[0:2])

            if time == timeslot and date == selection:
                tickets.append(info)

    return (sum(tickets))

# Function to show tickets in list per facility

def list_tickets(facility):
    
    total_list.delete(0, END)

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            time = file[4]
            total_list.insert(END, 'Ticket ' + info + '    ' + time)

# Function to show tickets in list per facility per date

def list_tickets_date(facility, selection):

    date_list.delete(0, END)

    folderpath = facility
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = file[0]
            date = file[2]
            time = file[4]
            if date == str(selection):
                date_list.insert(END, 'Ticket ' + info + '    ' + time)
                
    return (len(tickets))

#================================== GENERAL FUNCTIONS ==================================

# Function to change frames

def show_frame(frame):

    frame.tkraise()
    clear_date()

# Function for showing corresponding image at checkout data

def picture(image):

    app_picture.config(image=image)

# Function to delete content listboxes to show info total

def clear_total():

    for entry in (entry1_total, entry2_total, entry3_total, entry4_total, 
                  entry5_total, entry6_total, entry7_total, entry8_total,
                  entry9_total, entry10_total, entry11_total, entry12_total,
                  entry13_total, entry14_total, entry15_total, entry16_total,
                  entry17_total, entry18_total):

        entry.delete(0,END)   

# Function to delete content listboxes to show info by date

def clear_date():

    for entry in (entry1_date, entry2_date, entry3_date, entry4_date, 
                  entry5_date, entry6_date, entry7_date, entry8_date,
                  entry9_date, entry10_date, entry11_date, entry12_date,
                  entry13_date, entry14_date, entry15_date, entry16_date,
                  entry17_date, entry18_date):
        
        entry.delete(0,END)

    for label in (entrance8, parking8, restaurant8, theatre8, icecreamparlor8):

        label.config(text='Datum')

# Function to delete content listboxes to show info timeslot

def clear_timeslot():

    for entry in (entry1_time, entry2_time, entry3_time, entry4_time, 
                  entry5_time, entry6_time, entry7_time, entry8_time,
                  entry9_time):

        entry.delete(0,END)  

# Function to delete content listboxes to show info timeslot by date

def clear_timeslot_date():

    for entry in (entry10_time, entry11_time, entry12_time, entry13_time, 
                  entry14_time, entry15_time, entry16_time, entry17_time, 
                  entry18_time):

        entry.delete(0,END)  

# Function to show data total + calculate percentages of total and facility

def data_total(facility):

    entry1_total.insert(END, tickets(facility))
    entry2_total.insert(END, visitors(facility, total))
    entry3_total.insert(END, visitors(facility, toddle))
    entry4_total.insert(END, visitors(facility, child))
    entry5_total.insert(END, visitors(facility, adult))
    entry6_total.insert(END, visitors(facility, senior))
    
    entry7_total.insert(END, "{:.0f}".format(tickets(facility)/tickets(entrance) 
                         *100) + '%')
    entry8_total.insert(END, "{:.0f}".format(visitors(facility, total)/
                         visitors(entrance, total) *100) + '%')
    entry9_total.insert(END, "{:.0f}".format(visitors(facility, toddle)/
                         visitors(entrance, toddle) *100) + '%')
    entry10_total.insert(END, "{:.0f}".format(visitors(facility, child)/
                         visitors(entrance, child) *100) + '%')
    entry11_total.insert(END, "{:.0f}".format(visitors(facility, adult)/
                         visitors(entrance, adult) *100) + '%')
    entry12_total.insert(END, "{:.0f}".format(visitors(facility, senior)/
                         visitors(entrance, senior) *100) + '%')
    
    entry13_total.insert(END, "{:.0f}".format(tickets(facility)/tickets(facility) 
                         *100) + '%')
    entry14_total.insert(END, "{:.0f}".format(visitors(facility, total)/
                         visitors(facility, total) *100) + '%')
    entry15_total.insert(END, "{:.0f}".format(visitors(facility, toddle)/
                         visitors(facility, total) *100) + '%')
    entry16_total.insert(END, "{:.0f}".format(visitors(facility, child)/
                         visitors(facility, total) *100) + '%')
    entry17_total.insert(END, "{:.0f}".format(visitors(facility, adult)/
                         visitors(facility, total) *100) + '%')
    entry18_total.insert(END, "{:.0f}".format(visitors(facility, senior)/
                         visitors(facility, total) *100) + '%')

    entry1_time.insert(END, timeslot(facility, timeslot9_10))
    entry2_time.insert(END, timeslot(facility, timeslot10_11))
    entry3_time.insert(END, timeslot(facility, timeslot11_12))
    entry4_time.insert(END, timeslot(facility, timeslot12_13))
    entry5_time.insert(END, timeslot(facility, timeslot13_14))
    entry6_time.insert(END, timeslot(facility, timeslot14_15))
    entry7_time.insert(END, timeslot(facility, timeslot15_16))
    entry8_time.insert(END, timeslot(facility, timeslot16_17))
    entry9_time.insert(END, timeslot(facility, timeslot17_18))

# Function to show data by date + calculate percentages of total and facility
# per date

def data_date(facility, date):

    entry1_date.insert(END, tickets_date(facility, date))
    entry2_date.insert(END, visitors_date(facility, total, date))
    entry3_date.insert(END, visitors_date(facility, toddle, date))
    entry4_date.insert(END, visitors_date(facility, child, date))
    entry5_date.insert(END, visitors_date(facility, adult, date))
    entry6_date.insert(END, visitors_date(facility, senior, date))
   
    entry7_date.insert(END, "{:.0f}".format(tickets_date(facility, date)/
                        tickets_date(entrance, date) *100) + '%')
    entry8_date.insert(END, "{:.0f}".format(visitors_date(facility, total, date)/
                         visitors_date(entrance, total, date) *100) + '%')
    entry9_date.insert(END, "{:.0f}".format(visitors_date(facility, toddle, date)/
                         visitors_date(entrance, toddle, date) *100) + '%')
    entry10_date.insert(END, "{:.0f}".format(visitors_date(facility, child, date)/
                         visitors_date(entrance, child, date) *100) + '%')
    entry11_date.insert(END, "{:.0f}".format(visitors_date(facility, adult, date)/
                         visitors_date(entrance, adult, date) *100) + '%')
    entry12_date.insert(END, "{:.0f}".format(visitors_date(facility, senior, date)/
                         visitors_date(entrance, senior, date) *100) + '%')
    
    entry13_date.insert(END, "{:.0f}".format(tickets_date(facility, date)/
                          tickets_date(facility, date) *100) + '%')
    entry14_date.insert(END, "{:.0f}".format(visitors_date(facility, total, date)/
                         visitors_date(facility, total, date) *100) + '%')
    entry15_date.insert(END, "{:.0f}".format(visitors_date(facility, toddle, date)/
                         visitors_date(facility, total, date) *100) + '%')
    entry16_date.insert(END, "{:.0f}".format(visitors_date(facility, child, date)/
                         visitors_date(facility, total, date) *100) + '%')
    entry17_date.insert(END, "{:.0f}".format(visitors_date(facility, adult, date)/
                         visitors_date(facility, total, date) *100) + '%')
    entry18_date.insert(END, "{:.0f}".format(visitors_date(facility, senior, date)/
                         visitors_date(facility, total, date) *100) + '%')

    entry10_time.insert(END, timeslot_date(facility, timeslot9_10, date))
    entry11_time.insert(END, timeslot_date(facility, timeslot10_11, date))
    entry12_time.insert(END, timeslot_date(facility, timeslot11_12, date))
    entry13_time.insert(END, timeslot_date(facility, timeslot12_13, date))
    entry14_time.insert(END, timeslot_date(facility, timeslot13_14, date))
    entry15_time.insert(END, timeslot_date(facility, timeslot14_15, date))
    entry16_time.insert(END, timeslot_date(facility, timeslot15_16, date))
    entry17_time.insert(END, timeslot_date(facility, timeslot16_17, date))
    entry18_time.insert(END, timeslot_date(facility, timeslot17_18, date))

#============================ SPECIFIC FUNCTIONS FRAMES ================================
                              
# Function to retrieve current number of cars in parking lot

def data_parkinglot():

    folderpath = r'Database/Parkinglot'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    tickets = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            info = int(file[3])
            tickets.append(info)

    parkinglot_list.delete(0, END)
    parkinglot_list.insert(END, sum(tickets))

# Function to calculate and display average waiting time. The time between creating
# the ticket and entering the park

def data_waiting_time():

    folderpath = r'Database/Tickets/Data'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    min_ordering = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            time1 = (file[4])
            hours1 = int(time1[0:2])
            minutes1 = (hours1 * 60) + int(time1[3:5])
            
            min_ordering.append(minutes1)

    total_ordering = sum(min_ordering)
    tickets = len(min_ordering)

    folderpath = r'Database/Cash_Register/Entrance'
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

    min_entrance = []

    for path in filepaths:
        with open(path, 'r') as f:
            file = f.read().splitlines()
            time2 = (file[4])
            hours2 = int(time2[0:2])
            minutes2 = (hours2 * 60) + int(time2[3:5])
            
            min_entrance.append(minutes2)

    total_entrance = sum(min_entrance)

    average_time = (total_entrance - total_ordering)/tickets
    average_time = int(average_time)


    entrance_list.delete(0, END)
    entrance_list.insert(0, average_time)

#================================== FUNCTIONS FRAMES ===================================

# Function to show data checkout entrance

def data_entrance():

    clear_total()
    clear_timeslot()
    clear_timeslot_date()
    data_total(entrance)
    data_waiting_time()
    list_tickets(entrance)
    picture(image_tickets)
    show_frame(frame1)
    show_frame(frame7)
    date_list.delete(0, END)
    description_2c.config(text="Toegang")
    description_4c.config(text="Toegang")
    entrance8.config(text='Datum')
    description_3d.config(text="op datum")
    description_4d.config(text="op datum")
    description_6b.config(text= "op datum")

# Function to show data checkout parking

def data_parking():

    clear_total()
    clear_timeslot()
    clear_timeslot_date()
    data_total(parking)
    list_tickets(parking)
    picture(image_parking)
    show_frame(frame2)
    show_frame(frame8)
    date_list.delete(0, END)
    description_2c.config(text="Parkeren")
    description_4c.config(text="Parkeren")
    parking8.config(text='Datum')
    description_3d.config(text="op datum")
    description_4d.config(text="op datum")
    description_6b.config(text= "op datum")

    parkinglot_list.insert(END, visitors(parkinglot, car)) 
    

# Function to show data checkout restaurant

def data_restaurant():

    clear_total()
    clear_timeslot()
    clear_timeslot_date()
    data_total(restaurant)
    list_tickets(restaurant)
    picture(image_restaurant)
    show_frame(frame3)
    show_frame(frame9)
    date_list.delete(0, END)
    description_2c.config(text="Restaurant")
    description_4c.config(text="Restaurant")
    restaurant8.config(text='Datum')
    description_3d.config(text="op datum")
    description_4d.config(text="op datum")
    description_6b.config(text= "op datum")

# Function to show data checkout theatre

def data_theatre():

    clear_total()
    clear_timeslot()
    clear_timeslot_date()
    data_total(theatre)
    list_tickets(theatre)
    picture(image_theatre)
    show_frame(frame4)
    show_frame(frame10)
    date_list.delete(0, END)
    description_2c.config(text="Theater")
    description_4c.config(text="Theater")
    theatre8.config(text='Datum')
    description_3d.config(text="op datum")
    description_4d.config(text="op datum")
    description_6b.config(text= "op datum")

# Function to show data checkout facepaint

def data_facepaint():

    clear_total()
    clear_timeslot()
    clear_timeslot_date()
    data_total(facepaint)
    list_tickets(facepaint)
    picture(image_facepaint)
    show_frame(frame5)
    show_frame(frame11)
    date_list.delete(0, END)
    description_2c.config(text="Schminken")
    description_4c.config(text="Schminken")
    facepaint8.config(text='Datum')
    description_3d.config(text="op datum")
    description_4d.config(text="op datum")
    description_6b.config(text= "op datum")
    
# Function to show data checkout icecreamparlor

def data_icecreamparlor():

    clear_total()
    clear_timeslot()
    clear_timeslot_date()
    data_total(icecreamparlor)
    list_tickets(icecreamparlor)
    picture(image_icecreamparlor)
    show_frame(frame6)
    show_frame(frame12)
    date_list.delete(0, END)
    description_2c.config(text="Ijssalon")
    description_4c.config(text="Ijssalon")
    icecreamparlor8.config(text='Datum')
    description_3d.config(text="op datum")
    description_4d.config(text="op datum")
    description_6b.config(text= "op datum")

    icecreamparlor_list.delete(0, END)
    icecreamparlor_list.insert(0, '{:.2f}'.format((tickets(icecreamparlor) * 5)/visitors(icecreamparlor, total)).replace(".", ","))

# Function to show dates of selected date on the calendar

def date():

    date = str((calender.get_date()))
    clear_date()
    clear_timeslot_date()

    description_3d.config(text=date)
    description_4d.config(text=date)
    description_6b.config(text=date)

    for label in (entrance8, parking8, restaurant8, theatre8, facepaint8, icecreamparlor8):

        label.config(text='Datum  ' + date)

    if r.get() == 1:
        
        try:
            data_date(entrance, date)

        except ZeroDivisionError:
            pass
        
        list_tickets_date(entrance, date)
    
    
    if r.get() == 2:
        
        try:
            data_date(parking, date)
            

        except ZeroDivisionError:
            pass
        
        list_tickets_date(parking, date)
        

    if r.get() == 3:
        
        try:
            data_date(restaurant, date)

        except ZeroDivisionError:
            pass

        list_tickets_date(restaurant, date)
    
    if r.get() == 4:
        
        try:
            data_date(theatre, date)

        except ZeroDivisionError:
            pass

        list_tickets_date(theatre, date)
    
    if r.get() == 5:
        
        try:
            data_date(facepaint, date)

        except ZeroDivisionError:
            pass
        
        list_tickets_date(facepaint, date)
    
    if r.get() == 6:
        
        try:
            data_date(icecreamparlor, date)

        except ZeroDivisionError:
            pass
        
        list_tickets_date(icecreamparlor, date)   

# Function to create a report from user-entered Data 

def report():

    # List to store days to be included in the report

    dates= []

    # Lists for saving data of all examined days

    tickets_entrance_total = []
    tickets_parking_total = []
    tickets_restaurant_total = []
    tickets_theatre_total = []
    tickets_facepaint_total = []
    tickets_icecreamparlor_total = []

    visitors_entrance_total = []
    toddle_entrance_total = []
    child_entrance_total = []
    adult_entrance_total = []
    senior_entrance_total = []
    
    visitors_parking_total = []
    toddle_parking_total = []
    child_parking_total = []
    adult_parking_total = []
    senior_parking_total = []
    
    visitors_restaurant_total = []
    toddle_restaurant_total = []
    child_restaurant_total = []
    adult_restaurant_total = []
    senior_restaurant_total = []
    
    visitors_theatre_total = []
    toddle_theatre_total = []
    child_theatre_total = []
    adult_theatre_total = []
    senior_theatre_total = []
    
    visitors_facepaint_total = []
    toddle_facepaint_total = []
    child_facepaint_total = []
    adult_facepaint_total = []
    senior_facepaint_total = []
    
    visitors_icecreamparlor_total = []
    toddle_icecreamparlor_total = []
    child_icecreamparlor_total = []
    adult_icecreamparlor_total = []
    senior_icecreamparlor_total = []

    entrance_9_10_total = []
    entrance_10_11_total = []
    entrance_11_12_total = []
    entrance_12_13_total = []
    entrance_13_14_total = []
    entrance_14_15_total = []
    entrance_15_16_total = []
    entrance_16_17_total = []
    entrance_17_18_total = []

    parking_9_10_total = []
    parking_10_11_total = []
    parking_11_12_total = []
    parking_12_13_total = []
    parking_13_14_total = []
    parking_14_15_total = []
    parking_15_16_total = []
    parking_16_17_total = []
    parking_17_18_total = []

    restaurant_9_10_total = []
    restaurant_10_11_total = []
    restaurant_11_12_total = []
    restaurant_12_13_total = []
    restaurant_13_14_total = []
    restaurant_14_15_total = []
    restaurant_15_16_total = []
    restaurant_16_17_total = []
    restaurant_17_18_total = []

    theatre_9_10_total = []
    theatre_10_11_total = []
    theatre_11_12_total = []
    theatre_12_13_total = []
    theatre_13_14_total = []
    theatre_14_15_total = []
    theatre_15_16_total = []
    theatre_16_17_total = []
    theatre_17_18_total = []

    facepaint_9_10_total = []
    facepaint_10_11_total = []
    facepaint_11_12_total = []
    facepaint_12_13_total = []
    facepaint_13_14_total = []
    facepaint_14_15_total = []
    facepaint_15_16_total = []
    facepaint_16_17_total = []
    facepaint_17_18_total = []

    icecreamparlor_9_10_total = []
    icecreamparlor_10_11_total = []
    icecreamparlor_11_12_total = []
    icecreamparlor_12_13_total = []
    icecreamparlor_13_14_total = []
    icecreamparlor_14_15_total = []
    icecreamparlor_15_16_total = []
    icecreamparlor_16_17_total = []
    icecreamparlor_17_18_total = []

    # Function to save days between dates entered by user 

    diff = (date_2.get_date()-date_1.get_date()).days
    for i in range(diff+1):
        day = date_1.get_date() + timedelta(days=i)
        dates.append(day)
    if dates:
       dates = [x.strftime('%d/%m/%y') for x in dates] 
    else:
        messagebox.showerror("Foute invoer",
                                    "Kies als tweede datum een datum die "
                                    "later is dan de eerste datum")

    # Retrieve all necessary data from the database

    for date in dates:

        tickets_entrance = tickets_date(entrance, date)
        tickets_entrance_total.append(tickets_entrance)
        tickets_parking = tickets_date(parking, date)
        tickets_parking_total.append(tickets_parking)
        tickets_restaurant = tickets_date(restaurant, date)
        tickets_restaurant_total.append(tickets_restaurant)
        tickets_theatre = tickets_date(theatre, date)
        tickets_theatre_total.append(tickets_theatre)
        tickets_facepaint = tickets_date(facepaint, date)
        tickets_facepaint_total.append(tickets_facepaint)
        tickets_icecreamparlor = tickets_date(icecreamparlor, date)
        tickets_icecreamparlor_total.append(tickets_icecreamparlor)

        visitors_entrance = visitors_date(entrance, total, date)
        visitors_entrance_total.append(visitors_entrance)   
        toddle_entrance = visitors_date(entrance, toddle, date)
        toddle_entrance_total.append(toddle_entrance)
        child_entrance = visitors_date(entrance, child, date)
        child_entrance_total.append(child_entrance)
        adult_entrance = visitors_date(entrance, adult, date)
        adult_entrance_total.append(adult_entrance)
        senior_entrance = visitors_date(entrance, senior, date)
        senior_entrance_total.append(senior_entrance)

        visitors_parking = visitors_date(parking, total, date)
        visitors_parking_total.append(visitors_parking)
        toddle_parking = visitors_date(parking, toddle, date)
        toddle_parking_total.append(toddle_parking)
        child_parking = visitors_date(parking, child, date)
        child_parking_total.append(child_parking)
        adult_parking = visitors_date(parking, adult, date)
        adult_parking_total.append(adult_parking)
        senior_parking = visitors_date(parking, senior, date)
        senior_parking_total.append(senior_parking)

        visitors_restaurant = visitors_date(restaurant, total, date)
        visitors_restaurant_total.append(visitors_restaurant)
        toddle_restaurant = visitors_date(restaurant, toddle, date)
        toddle_restaurant_total.append(toddle_restaurant)
        child_restaurant = visitors_date(restaurant, child, date)
        child_restaurant_total.append(child_restaurant)
        adult_restaurant = visitors_date(restaurant, adult, date)
        adult_restaurant_total.append(adult_restaurant)
        senior_restaurant = visitors_date(restaurant, senior, date)
        senior_restaurant_total.append(senior_restaurant)

        visitors_theatre = visitors_date(theatre, total, date)
        visitors_theatre_total.append(visitors_theatre)
        toddle_theatre = visitors_date(theatre, toddle, date)
        toddle_theatre_total.append(toddle_theatre)
        child_theatre = visitors_date(theatre, child, date)
        child_theatre_total.append(child_theatre)
        adult_theatre = visitors_date(theatre, adult, date)
        adult_theatre_total.append(adult_theatre)
        senior_theatre = visitors_date(theatre, senior, date)
        senior_theatre_total.append(senior_theatre)

        visitors_facepaint = visitors_date(facepaint, total, date)
        visitors_facepaint_total.append(visitors_facepaint)
        toddle_facepaint = visitors_date(facepaint, toddle, date)
        toddle_facepaint_total.append(toddle_facepaint)
        child_facepaint = visitors_date(facepaint, child, date)
        child_facepaint_total.append(child_facepaint)
        adult_facepaint = visitors_date(facepaint, adult, date)
        adult_facepaint_total.append(adult_facepaint)
        senior_facepaint = visitors_date(facepaint, senior, date)
        senior_facepaint_total.append(senior_facepaint)

        visitors_icecreamparlor = visitors_date(icecreamparlor, total, date)
        visitors_icecreamparlor_total.append(visitors_icecreamparlor)
        toddle_icecreamparlor = visitors_date(icecreamparlor, toddle, date)
        toddle_icecreamparlor_total.append(toddle_icecreamparlor)
        child_icecreamparlor = visitors_date(icecreamparlor, child, date)
        child_icecreamparlor_total.append(child_icecreamparlor)
        adult_icecreamparlor = visitors_date(icecreamparlor, adult, date)
        adult_icecreamparlor_total.append(adult_icecreamparlor)
        senior_icecreamparlor = visitors_date(icecreamparlor, senior, date)
        senior_icecreamparlor_total.append(senior_icecreamparlor)
        
        entrance_9_10 = timeslot_date(entrance, timeslot9_10, date)
        entrance_9_10_total.append(entrance_9_10)
        entrance_10_11 = timeslot_date(entrance, timeslot10_11, date)
        entrance_10_11_total.append(entrance_10_11)
        entrance_11_12 = timeslot_date(entrance, timeslot11_12, date)
        entrance_11_12_total.append(entrance_11_12)
        entrance_12_13 = timeslot_date(entrance, timeslot12_13, date)
        entrance_12_13_total.append(entrance_12_13)
        entrance_13_14 = timeslot_date(entrance, timeslot13_14, date)
        entrance_13_14_total.append(entrance_13_14)
        entrance_14_15 = timeslot_date(entrance, timeslot14_15, date)
        entrance_14_15_total.append(entrance_14_15)
        entrance_15_16 = timeslot_date(entrance, timeslot15_16, date)
        entrance_15_16_total.append(entrance_15_16)
        entrance_16_17 = timeslot_date(entrance, timeslot16_17, date)
        entrance_16_17_total.append(entrance_16_17)
        entrance_17_18 = timeslot_date(entrance, timeslot17_18, date)
        entrance_17_18_total.append(entrance_17_18)

        parking_9_10 = timeslot_date(parking, timeslot9_10, date)
        parking_9_10_total.append(parking_9_10)
        parking_10_11 = timeslot_date(parking, timeslot10_11, date)
        parking_10_11_total.append(parking_10_11)
        parking_11_12 = timeslot_date(parking, timeslot11_12, date)
        parking_11_12_total.append(parking_11_12)
        parking_12_13 = timeslot_date(parking, timeslot12_13, date)
        parking_12_13_total.append(parking_12_13)
        parking_13_14 = timeslot_date(parking, timeslot13_14, date)
        parking_13_14_total.append(parking_13_14)
        parking_14_15 = timeslot_date(parking, timeslot14_15, date)
        parking_14_15_total.append(parking_14_15)
        parking_15_16 = timeslot_date(parking, timeslot15_16, date)
        parking_15_16_total.append(parking_15_16)
        parking_16_17 = timeslot_date(parking, timeslot16_17, date)
        parking_16_17_total.append(parking_16_17)
        parking_17_18 = timeslot_date(parking, timeslot17_18, date)
        parking_17_18_total.append(parking_17_18)

        restaurant_9_10 = timeslot_date(restaurant, timeslot9_10, date)
        restaurant_9_10_total.append(restaurant_9_10)
        restaurant_10_11 = timeslot_date(restaurant, timeslot10_11, date)
        restaurant_10_11_total.append(restaurant_10_11)
        restaurant_11_12 = timeslot_date(restaurant, timeslot11_12, date)
        restaurant_11_12_total.append(restaurant_11_12)
        restaurant_12_13 = timeslot_date(restaurant, timeslot12_13, date)
        restaurant_12_13_total.append(restaurant_12_13)
        restaurant_13_14 = timeslot_date(restaurant, timeslot13_14, date)
        restaurant_13_14_total.append(restaurant_13_14)
        restaurant_14_15 = timeslot_date(restaurant, timeslot14_15, date)
        restaurant_14_15_total.append(restaurant_14_15)
        restaurant_15_16 = timeslot_date(restaurant, timeslot15_16, date)
        restaurant_15_16_total.append(restaurant_15_16)
        restaurant_16_17 = timeslot_date(restaurant, timeslot16_17, date)
        restaurant_16_17_total.append(restaurant_16_17)
        restaurant_17_18 = timeslot_date(restaurant, timeslot17_18, date)
        restaurant_17_18_total.append(restaurant_17_18)

        theatre_9_10 = timeslot_date(theatre, timeslot9_10, date)
        theatre_9_10_total.append(theatre_9_10)
        theatre_10_11 = timeslot_date(theatre, timeslot10_11, date)
        theatre_10_11_total.append(theatre_10_11)
        theatre_11_12 = timeslot_date(theatre, timeslot11_12, date)
        theatre_11_12_total.append(theatre_11_12)
        theatre_12_13 = timeslot_date(theatre, timeslot12_13, date)
        theatre_12_13_total.append(theatre_12_13)
        theatre_13_14 = timeslot_date(theatre, timeslot13_14, date)
        theatre_13_14_total.append(theatre_13_14)
        theatre_14_15 = timeslot_date(theatre, timeslot14_15, date)
        theatre_14_15_total.append(theatre_14_15)
        theatre_15_16 = timeslot_date(theatre, timeslot15_16, date)
        theatre_15_16_total.append(theatre_15_16)
        theatre_16_17 = timeslot_date(theatre, timeslot16_17, date)
        theatre_16_17_total.append(theatre_16_17)
        theatre_17_18 = timeslot_date(theatre, timeslot17_18, date)
        theatre_17_18_total.append(theatre_17_18)

        facepaint_9_10 = timeslot_date(facepaint, timeslot9_10, date)
        facepaint_9_10_total.append(facepaint_9_10)
        facepaint_10_11 = timeslot_date(facepaint, timeslot10_11, date)
        facepaint_10_11_total.append(facepaint_10_11)
        facepaint_11_12 = timeslot_date(facepaint, timeslot11_12, date)
        facepaint_11_12_total.append(facepaint_11_12)
        facepaint_12_13 = timeslot_date(facepaint, timeslot12_13, date)
        facepaint_12_13_total.append(facepaint_12_13)
        facepaint_13_14 = timeslot_date(facepaint, timeslot13_14, date)
        facepaint_13_14_total.append(facepaint_13_14)
        facepaint_14_15 = timeslot_date(facepaint, timeslot14_15, date)
        facepaint_14_15_total.append(facepaint_14_15)
        facepaint_15_16 = timeslot_date(facepaint, timeslot15_16, date)
        facepaint_15_16_total.append(facepaint_15_16)
        facepaint_16_17 = timeslot_date(facepaint, timeslot16_17, date)
        facepaint_16_17_total.append(facepaint_16_17)
        facepaint_17_18 = timeslot_date(facepaint, timeslot17_18, date)
        facepaint_17_18_total.append(facepaint_17_18)

        icecreamparlor_9_10 = timeslot_date(icecreamparlor, timeslot9_10, date)
        icecreamparlor_9_10_total.append(icecreamparlor_9_10)
        icecreamparlor_10_11 = timeslot_date(icecreamparlor, timeslot10_11, date)
        icecreamparlor_10_11_total.append(icecreamparlor_10_11)
        icecreamparlor_11_12 = timeslot_date(icecreamparlor, timeslot11_12, date)
        icecreamparlor_11_12_total.append(icecreamparlor_11_12)
        icecreamparlor_12_13 = timeslot_date(icecreamparlor, timeslot12_13, date)
        icecreamparlor_12_13_total.append(icecreamparlor_12_13)
        icecreamparlor_13_14 = timeslot_date(icecreamparlor, timeslot13_14, date)
        icecreamparlor_13_14_total.append(icecreamparlor_13_14)
        icecreamparlor_14_15 = timeslot_date(icecreamparlor, timeslot14_15, date)
        icecreamparlor_14_15_total.append(icecreamparlor_14_15)
        icecreamparlor_15_16 = timeslot_date(icecreamparlor, timeslot15_16, date)
        icecreamparlor_15_16_total.append(icecreamparlor_15_16)
        icecreamparlor_16_17 = timeslot_date(icecreamparlor, timeslot16_17, date)
        icecreamparlor_16_17_total.append(icecreamparlor_16_17)
        icecreamparlor_17_18 = timeslot_date(icecreamparlor, timeslot17_18, date)
        icecreamparlor_17_18_total.append(icecreamparlor_17_18)

    # Calculate average number of visitors per ticket and percentages use facilities

    try:
        number_entrance = "{:.0f}".format(sum(visitors_entrance_total)/(sum(tickets_entrance_total)))
        percent_parking = "{:.0f}".format(100 * (sum(visitors_parking_total)/(sum(visitors_entrance_total))))
        percent_restaurant = "{:.0f}".format(100 * (sum(visitors_restaurant_total)/(sum(visitors_entrance_total))))
        percent_theatre = "{:.0f}".format(100 * (sum(visitors_theatre_total)/(sum(visitors_entrance_total))))
        percent_facepaint = "{:.0f}".format(100 * (sum(visitors_facepaint_total)/(sum(visitors_entrance_total))))
        percent_icecreamparlor = "{:.0f}".format(100 * (sum(visitors_icecreamparlor_total)/(sum(visitors_entrance_total))))
  
    except ZeroDivisionError:
        number_entrance = 0
        percent_parking = 0
        percent_restaurant = 0
        percent_theatre = 0
        percent_facepaint = 0
        percent_icecreamparlor = 0
        
    # Formatting and displaying the report in a PDF
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    
    pdf.set_font('Helvetica', 'B', 42)
    pdf.cell(77, 10, "Rapport")

    pdf.set_font('Helvetica', 'I', 20)
    pdf.cell(40, 2, str(date_1.get_date().strftime('%d/%m/%Y')), ln=1)
    pdf.cell(0, 6, "-", align='C', ln=1)
    pdf.cell(0, 4, str(date_2.get_date().strftime('%d/%m/%Y')), align='C' , ln=1)
    
    pdf.image('Img/Logo_wit.jpg', 160, -5, 36, 36)

    pdf.line(10, 27, 200, 27)
    
    pdf.set_font('', '', 20)
    pdf.cell(0, 9, "", ln=1)
    pdf.set_font('Helvetica', '', 20)
    pdf.cell(65, 6, "Kassa Entree")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, "Tickets")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, str(sum(tickets_entrance_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers   9:00 - 10:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(entrance_9_10_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 10:00 - 11:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(entrance_10_11_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(90, 2, "Totaal Bezoekers")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 2, str(sum(visitors_entrance_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 11:00 - 12:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(entrance_11_12_total)), ln=1) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kleinkind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(toddle_entrance_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 12:00 - 13:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(entrance_12_13_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(child_entrance_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 13:00 - 14:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(entrance_13_14_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Volwassen")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(adult_entrance_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 14:00 - 15:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(entrance_14_15_total)), ln=1)  
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Senior")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(senior_entrance_total))) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 15:00 - 16:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(entrance_15_16_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 16:00 - 17:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(entrance_16_17_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(90, 4, "Gemiddeld aantal bezoekers per Ticket")
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(25, 4, str(number_entrance)) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 17:00 - 18:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(entrance_17_18_total)), ln=1)
    
    pdf.set_font('', '', 20)
    pdf.cell(0, 6, "", ln=1)
    pdf.set_font('Helvetica', '', 20)
    pdf.cell(65, 6, "Kassa Parkeren")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, "Tickets")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, str(sum(tickets_parking_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers   9:00 - 10:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(parking_9_10_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 10:00 - 11:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(parking_10_11_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(90, 2, "Totaal Bezoekers")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 2, str(sum(visitors_parking_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 11:00 - 12:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(parking_11_12_total)), ln=1) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kleinkind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(toddle_parking_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 12:00 - 13:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(parking_12_13_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(child_parking_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 13:00 - 14:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(parking_13_14_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Volwassen")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(adult_parking_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 14:00 - 15:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(parking_14_15_total)), ln=1)  
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Senior")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(senior_parking_total))) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 15:00 - 16:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(parking_15_16_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 16:00 - 17:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(parking_16_17_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(90, 4, "% Bezoekers dat parkeerterrein gebruikt")
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(25, 4, str(percent_parking) + "%") 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 17:00 - 18:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(parking_17_18_total)), ln=1)
    
    pdf.set_font('', '', 18)
    pdf.cell(0, 6, "", ln=1)
    pdf.set_font('Helvetica', '', 20)
    pdf.cell(65, 6, "Kassa Restaurant")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, "Tickets")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, str(sum(tickets_restaurant_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers   9:00 - 10:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(restaurant_9_10_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 10:00 - 11:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(restaurant_10_11_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(90, 2, "Totaal Bezoekers")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 2, str(sum(visitors_restaurant_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 11:00 - 12:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(restaurant_11_12_total)), ln=1) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kleinkind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(toddle_restaurant_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 12:00 - 13:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(restaurant_12_13_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(child_restaurant_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 13:00 - 14:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(restaurant_13_14_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Volwassen")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(adult_restaurant_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 14:00 - 15:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(restaurant_14_15_total)), ln=1)  
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Senior")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(senior_restaurant_total))) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 15:00 - 16:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(restaurant_15_16_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 16:00 - 17:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(restaurant_16_17_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(90, 4, "% Bezoekers dat Restaurant bezoekt")
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(25, 4, str(percent_restaurant) + "%") 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 17:00 - 18:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(restaurant_17_18_total)), ln=1)

    pdf.set_font('', '', 18)
    pdf.cell(0, 6, "", ln=1)
    pdf.set_font('Helvetica', '', 20)
    pdf.cell(65, 6, "Kassa 3D-theater")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, "Tickets")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, str(sum(tickets_theatre_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers   9:00 - 10:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(theatre_9_10_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 10:00 - 11:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(theatre_10_11_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(90, 2, "Totaal Bezoekers")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 2, str(sum(visitors_theatre_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 11:00 - 12:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(theatre_11_12_total)), ln=1) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kleinkind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(toddle_theatre_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 12:00 - 13:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(theatre_12_13_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(child_theatre_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 13:00 - 14:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(theatre_13_14_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Volwassen")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(adult_theatre_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 14:00 - 15:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(theatre_14_15_total)), ln=1)  
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Senior")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(senior_theatre_total))) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 15:00 - 16:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(theatre_15_16_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 16:00 - 17:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(theatre_16_17_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(90, 4, "% Bezoekers dat 3D-theater bezoekt")
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(25, 4, str(percent_theatre) + "%") 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 17:00 - 18:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(theatre_17_18_total)), ln=1)

    pdf.set_font('', '', 18)
    pdf.cell(0, 6, "", ln=1)
    pdf.set_font('Helvetica', '', 20)
    pdf.cell(65, 6, "Kassa schminken")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, "Tickets")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, str(sum(tickets_facepaint_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers   9:00 - 10:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(facepaint_9_10_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 10:00 - 11:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(facepaint_10_11_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(90, 2, "Totaal Bezoekers")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 2, str(sum(visitors_facepaint_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 11:00 - 12:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(facepaint_11_12_total)), ln=1) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kleinkind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(toddle_facepaint_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 12:00 - 13:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(facepaint_12_13_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(child_facepaint_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 13:00 - 14:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(facepaint_13_14_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Volwassen")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(adult_facepaint_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 14:00 - 15:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(facepaint_14_15_total)), ln=1)  
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Senior")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(senior_facepaint_total))) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 15:00 - 16:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(facepaint_15_16_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 16:00 - 17:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(facepaint_16_17_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(90, 4, "% Bezoekers dat Schminken bezoekt")
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(25, 4, str(percent_facepaint) + "%") 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 17:00 - 18:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(facepaint_17_18_total)), ln=1)

    pdf.set_font('', '', 18)
    pdf.cell(0, 6, "", ln=1)
    pdf.set_font('Helvetica', '', 20)
    pdf.cell(65, 6, "Kassa ijssalon")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, "Tickets")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 7, str(sum(tickets_icecreamparlor_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers   9:00 - 10:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(icecreamparlor_9_10_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 10:00 - 11:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(icecreamparlor_10_11_total)), ln=1)
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(90, 2, "Totaal Bezoekers")
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(25, 2, str(sum(visitors_icecreamparlor_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 11:00 - 12:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(icecreamparlor_11_12_total)), ln=1) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kleinkind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(toddle_icecreamparlor_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 12:00 - 13:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(icecreamparlor_12_13_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Kind")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(child_icecreamparlor_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 13:00 - 14:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 4, str(sum(icecreamparlor_13_14_total)), ln=1)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Volwassen")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(adult_icecreamparlor_total)))
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 14:00 - 15:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(icecreamparlor_14_15_total)), ln=1)  
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(90, 4, "Aantal Senior")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(25, 4, str(sum(senior_icecreamparlor_total))) 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 15:00 - 16:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(icecreamparlor_15_16_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(115, 4, "")
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 16:00 - 17:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(icecreamparlor_16_17_total)), ln=1)  
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(90, 4, "% Bezoekers dat Ijssalon bezoekt")
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(25, 4, str(percent_icecreamparlor) + "%") 
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(50, 4, "Bezoekers 17:00 - 18:00")
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(30, 4, str(sum(icecreamparlor_17_18_total)), ln=1)

    pdf.output('Database/Reports/Rapport '+ str(date_1.get_date()) + ' - ' + str(date_2.get_date()) + '.pdf')

    webbrowser.open_new(r'Database\Reports\Rapport '+ str(date_1.get_date()) + ' - ' + str(date_2.get_date()) + '.pdf')
                                    
#==================================== FORMAT ROOT =====================================

app_title = Label(root, text="Database", font=title1_font, 
                        bg=title1_bg, fg=title1_color)
app_title.place(x=10, y=30)

button_report = Button(root, text="RAPPORT", font=button2_font, bg=button2_bg,
                      fg=button2_color, command=report)
button_report.place(x=40, y=140)

date_1 = tkcalendar.DateEntry(root)
date_2 = tkcalendar.DateEntry(root)

date_1.place(x=300, y=140)
date_2.place(x=300, y=180)

calender = Calendar(root, selectmode='day', year=year_now, month=month_now, day=day_now, 
                    date_pattern='dd/mm/yy') 
calender.place(x=560, y=10)

app_picture = Label(root, image=image_tickets, borderwidth=0)
app_picture.place(x=1040, y=32)

app_logo = Label(root, image=logo1, borderwidth=0)
app_logo.place(x=1180, y=-5) 

r = IntVar()
r.set('1')

button_entrance = Radiobutton(root, text="Toegang", font=button1_font, 
                             bg=button1_bg, fg=button1_color, 
                             variable=r, value=1, command=data_entrance)
button_parking = Radiobutton(root, text="Parkeren", font=button1_font, 
                              bg=button1_bg, fg=button1_color,
                              variable=r, value=2, command=data_parking)
button_restaurant = Radiobutton(root, text="Restaurant", font=button1_font, 
                                bg=button1_bg, fg=button1_color,
                                variable=r, value=3, command=data_restaurant)
button_theatre = Radiobutton(root, text="Theater", font=button1_font, 
                             bg=button1_bg, fg=button1_color,
                             variable=r, value=4, command=data_theatre)
button_facepaint = Radiobutton(root, text="Schminken", font=button1_font, 
                               bg=button1_bg, fg=button1_color,
                               variable=r, value=5, command=data_facepaint)
button_icecreamparlor = Radiobutton(root, text="IJssalon", font=button1_font, 
                              bg=button1_bg, fg=button1_color,
                              variable=r, value=6, command=data_icecreamparlor)

button_entrance.place(x=50, y=220)
button_parking.place(x=280, y=220)
button_restaurant.place(x=510, y=220)
button_theatre.place(x=740, y=220)
button_facepaint.place(x=970, y=220)
button_icecreamparlor.place(x=1200, y=220)

button_date = Button(root, text="DATUM", font=button2_font, bg=button2_bg,
                      fg=button2_color, command=date)
button_date.place(x=1140, y=625)

entry1_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1,)
entry2_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry3_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry4_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry5_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry6_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry7_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry8_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry9_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry10_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry11_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry12_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry13_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry14_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry15_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                       width=4, height=1)
entry16_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry17_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry18_total = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)

entry1_total.place(x=root_x1, y=364)
entry2_total.place(x=root_x1, y=404)
entry3_total.place(x=root_x1, y=444)
entry4_total.place(x=root_x1, y=484)
entry5_total.place(x=root_x1, y=524)
entry6_total.place(x=root_x1, y=564)
entry7_total.place(x=root_x2, y=364)
entry8_total.place(x=root_x2, y=404)
entry9_total.place(x=root_x2, y=444)
entry10_total.place(x=root_x2, y=484)
entry11_total.place(x=root_x2, y=524)
entry12_total.place(x=root_x2, y=564)
entry13_total.place(x=root_x3, y=364)
entry14_total.place(x=root_x3, y=404)
entry15_total.place(x=root_x3, y=444)
entry16_total.place(x=root_x3, y=484)
entry17_total.place(x=root_x3, y=524)
entry18_total.place(x=root_x3, y=564)

entry1_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1,)
entry2_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry3_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry4_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry5_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry6_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=8, height=1)
entry7_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry8_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry9_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry10_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry11_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry12_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry13_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry14_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                       width=4, height=1)
entry15_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry16_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry17_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)
entry18_date = Listbox(root, font=check1_font, bg=check1_bg, fg=check1_color,
                        width=4, height=1)

entry1_date.place(x=root_x1, y=722)
entry2_date.place(x=root_x1, y=762)
entry3_date.place(x=root_x1, y=802)
entry4_date.place(x=root_x1, y=842)
entry5_date.place(x=root_x1, y=882)
entry6_date.place(x=root_x1, y=922)
entry7_date.place(x=root_x2, y=722)
entry8_date.place(x=root_x2, y=762)
entry9_date.place(x=root_x2, y=802)
entry10_date.place(x=root_x2, y=842)
entry11_date.place(x=root_x2, y=882)
entry12_date.place(x=root_x2, y=922)
entry13_date.place(x=root_x3, y=722)
entry14_date.place(x=root_x3, y=762)
entry15_date.place(x=root_x3, y=802)
entry16_date.place(x=root_x3, y=842)
entry17_date.place(x=root_x3, y=882)
entry18_date.place(x=root_x3, y=922)

entry1_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1,)
entry2_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry3_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry4_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry5_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry6_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                       width=10, height=1)
entry7_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry8_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry9_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry10_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry11_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry12_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry13_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry14_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry15_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry16_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry17_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)
entry18_time = Listbox(root, font=check2_font, bg=check2_bg, fg=check2_color,
                        width=10, height=1)

entry1_time.place(x=root_x5, y=350)
entry2_time.place(x=root_x5, y=380)
entry3_time.place(x=root_x5, y=410)
entry4_time.place(x=root_x5, y=440)
entry5_time.place(x=root_x5, y=470)
entry6_time.place(x=root_x5, y=500)
entry7_time.place(x=root_x5, y=530)
entry8_time.place(x=root_x5, y=560)
entry9_time.place(x=root_x5, y=590)
entry10_time.place(x=root_x5, y=708)
entry11_time.place(x=root_x5, y=738)
entry12_time.place(x=root_x5, y=768)
entry13_time.place(x=root_x5, y=798)
entry14_time.place(x=root_x5, y=828)
entry15_time.place(x=root_x5, y=858)
entry16_time.place(x=root_x5, y=888)
entry17_time.place(x=root_x5, y=918)
entry18_time.place(x=root_x5, y=948)

description_1a = Label(root, text='% van totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_1b = Label(root, text='bezoekers', font=app3_font, bg=app3_bg, fg=app3_color)
description_1c = Label(root, text='Pythonland', font=app3_font, bg=app3_bg, fg=app3_color)
description_1d = Label(root, text='totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_2a = Label(root, text='% van totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_2b = Label(root, text='bezoekers', font=app3_font, bg=app3_bg, fg=app3_color)
description_2c = Label(root, text='Toegang', font=app3_font, bg=app3_bg, fg=app3_color)
description_2d = Label(root, text='totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_3a = Label(root, text='% van totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_3b = Label(root, text='bezoekers', font=app3_font, bg=app3_bg, fg=app3_color)
description_3c = Label(root, text='Pythonland', font=app3_font, bg=app3_bg, fg=app3_color)
description_3d = Label(root, text='op datum', font=app3_font, bg=app3_bg, fg=app3_color)
description_4a = Label(root, text='% van totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_4b = Label(root, text='bezoekers', font=app3_font, bg=app3_bg, fg=app3_color)
description_4c = Label(root, text='Toegang', font=app3_font, bg=app3_bg, fg=app3_color)
description_4d = Label(root, text='op datum', font=app3_font, bg=app3_bg, fg=app3_color)
description_5a = Label(root, text='Bezoekers kassa per tijdslot', font=app3_font, bg=app3_bg, fg=app3_color)
description_5b = Label(root, text='totaal', font=app3_font, bg=app3_bg, fg=app3_color)
description_6a = Label(root, text='Bezoekers kassa per tijdslot', font=app3_font, bg=app3_bg, fg=app3_color)
description_6b = Label(root, text='op datum', font=app3_font, bg=app3_bg, fg=app3_color)
description_7 = Label(root, text="9:00 - 10:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_8 = Label(root, text="10:00 - 11:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_9 = Label(root, text="11:00 - 12:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_10 = Label(root, text="12:00 - 13:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_11 = Label(root, text="13:00 - 14:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_12 = Label(root, text="14:00 - 15:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_13 = Label(root, text="15:00 - 16:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_14 = Label(root, text="16:00 - 17:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_15 = Label(root, text="17:00 - 18:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_16 = Label(root, text="9:00 - 10:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_17 = Label(root, text="10:00 - 11:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_18 = Label(root, text="11:00 - 12:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_19 = Label(root, text="12:00 - 13:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_20 = Label(root, text="13:00 - 14:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_21 = Label(root, text="14:00 - 15:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_22 = Label(root, text="15:00 - 16:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_23 = Label(root, text="16:00 - 17:00", font=app2_font, bg=app2_bg, fg=app2_color)
description_24 = Label(root, text="17:00 - 18:00", font=app2_font, bg=app2_bg, fg=app2_color)


description_1a.place(x=520, y=270)
description_1b.place(x=530, y=292)
description_1c.place(x=527, y=314)
description_1d.place(x=548, y=336)
description_2a.place(x=662, y=270)
description_2b.place(x=672, y=292)
description_2c.place(x=674, y=314)
description_2d.place(x=686, y=336)
description_3a.place(x=520, y=628)
description_3b.place(x=530, y=650)
description_3c.place(x=527, y=672)
description_3d.place(x=538, y=694)
description_4a.place(x=662, y=628)
description_4b.place(x=672, y=650)
description_4c.place(x=674, y=672)
description_4d.place(x=677, y=694)
description_5a.place(x=800, y=270)
description_5b.place(x=800, y=292)
description_6a.place(x=800, y=628)
description_6b.place(x=800, y=650)
description_7.place(x=(root_x4 + 11), y=350)
description_8.place(x=root_x4, y=380)
description_9.place(x=root_x4, y=410)
description_10.place(x=root_x4, y=440)
description_11.place(x=root_x4, y=470)
description_12.place(x=root_x4, y=500)
description_13.place(x=root_x4, y=530)
description_14.place(x=root_x4, y=560)
description_15.place(x=root_x4, y=590)
description_16.place(x=(root_x4 + 11), y=708)
description_17.place(x=root_x4, y=738)
description_18.place(x=root_x4, y=768)
description_19.place(x=root_x4, y=798)
description_20.place(x=root_x4, y=828)
description_21.place(x=root_x4, y=858)
description_22.place(x=root_x4, y=888)
description_23.place(x=root_x4, y=918)
description_24.place(x=root_x4, y=948)

scrollbar1 = Scrollbar(frame13, orient="vertical")
scrollbar1.pack(side=RIGHT, fill=Y)

scrollbar2 = Scrollbar(frame14, orient="vertical")
scrollbar2.pack(side=RIGHT, fill=Y)

total_list = Listbox(frame13, font=check3_font, bg=check3_bg, fg=check3_color,  
                        width=24, height=11, yscrollcommand=scrollbar1.set)
total_list.pack(expand=True, fill=Y)

date_list = Listbox(frame14, font=check3_font, bg=check3_bg, fg=check3_color,  
                        width=24, height=11, yscrollcommand=scrollbar2.set)
date_list.pack(expand=True, fill=Y)

scrollbar1.config(command=total_list.yview)
scrollbar2.config(command=date_list.yview)

#=================================== FORMAT FRAME1 ====================================

entrance1 = Label(frame1, text = "Totaal", font=title2_font, 
                        bg=title2_bg, fg=title2_color)
entrance2 = Label(frame1, text = "Aantal tickets", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance3 = Label(frame1, text = "Aantal bezoekers", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance4 = Label(frame1, text = "Aantal kleine kinderen", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance5 = Label(frame1, text = "Aantal kinderen", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance6 = Label(frame1, text = "Aantal volwassenen", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance7 = Label(frame1, text = "Aantal senioren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

entrance1.place(x=frame_x1, y=frame_y1)
entrance2.place(x=frame_x1, y=frame_y2)
entrance3.place(x=frame_x1, y=frame_y3)
entrance4.place(x=frame_x1, y=frame_y4)
entrance5.place(x=frame_x1, y=frame_y5)
entrance6.place(x=frame_x1, y=frame_y6)
entrance7.place(x=frame_x1, y=frame_y7)


entrance8 = Label(frame1, text = "Datum", font=title2_font, 
                       bg=title2_bg, fg=title2_color)
entrance9 = Label(frame1, text = "Aantal tickets", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance10 = Label(frame1, text = "Aantal bezoekers", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance11 = Label(frame1, text = "Aantal kleine kinderen", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance12 = Label(frame1, text = "Aantal kinderen", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance13 = Label(frame1, text = "Aantal volwassenen", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance14 = Label(frame1, text = "Aantal senioren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

entrance8.place(x=frame_x1, y=frame_y8)
entrance9.place(x=frame_x1, y=frame_y9)
entrance10.place(x=frame_x1, y=frame_y10)
entrance11.place(x=frame_x1, y=frame_y11)
entrance12.place(x=frame_x1, y=frame_y12)
entrance13.place(x=frame_x1, y=frame_y13)
entrance14.place(x=frame_x1, y=frame_y14)

entrance15 = Label(frame7, text = "Gemiddelde wachttijd in minuten:", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
entrance15.place(x=0, y=frame_y15)

entrance_list = Listbox(frame7, font=check4_font, bg=check4_bg, fg=check4_color,  
                        width=6, height=1)
entrance_list.place(x=frame_x2, y=frame_y16)

#=================================== FORMAT FRAME2 =====================================

parking1 = Label(frame2, text = "Totaal", font=title2_font, 
                        bg=title2_bg, fg=title2_color)
parking2 = Label(frame2, text = "Aantal tickets parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking3 = Label(frame2, text = "Aantal bezoekers parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking4 = Label(frame2, text = "Aantal kleine kinderen parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking5 = Label(frame2, text = "Aantal kinderen parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking6 = Label(frame2, text = "Aantal volwassenen parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking7 = Label(frame2, text = "Aantal senioren parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

parking1.place(x=frame_x1, y=frame_y1)
parking2.place(x=frame_x1, y=frame_y2)
parking3.place(x=frame_x1, y=frame_y3)
parking4.place(x=frame_x1, y=frame_y4)
parking5.place(x=frame_x1, y=frame_y5)
parking6.place(x=frame_x1, y=frame_y6)
parking7.place(x=frame_x1, y=frame_y7)

parking8 = Label(frame2, text = "Datum", font=title2_font, 
                       bg=title2_bg, fg=title2_color)
parking9 = Label(frame2, text = "Aantal tickets parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking10 = Label(frame2, text = "Aantal bezoekers parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking11 = Label(frame2, text = "Aantal kleine kinderen parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking12 = Label(frame2, text = "Aantal kinderen parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking13 = Label(frame2, text = "Aantal volwassenen parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking14 = Label(frame2, text = "Aantal senioren parkeren", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

parking8.place(x=frame_x1, y=frame_y8)
parking9.place(x=frame_x1, y=frame_y9)
parking10.place(x=frame_x1, y=frame_y10)
parking11.place(x=frame_x1, y=frame_y11)
parking12.place(x=frame_x1, y=frame_y12)
parking13.place(x=frame_x1, y=frame_y13)
parking14.place(x=frame_x1, y=frame_y14)

parking15 = Label(frame8, text = "Aantal auto's op parkeerterrein:", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking15.place(x=0, y=frame_y15)

parkinglot_list = Listbox(frame8, font=check4_font, bg=check4_bg, fg=check4_color,  
                        width=6, height=1)
parkinglot_list.place(x=frame_x2, y=frame_y16)

#=================================== FORMAT FRAME3 =====================================

restaurant1 = Label(frame3, text = "Totaal", font=title2_font, 
                        bg=title2_bg, fg=title2_color)
restaurant2 = Label(frame3, text = "Aantal tickets restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant3 = Label(frame3, text = "Aantal bezoekers restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant4 = Label(frame3, text = "Aantal kleine kinderen restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant5 = Label(frame3, text = "Aantal kinderen restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant6 = Label(frame3, text = "Aantal volwassenen restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant7 = Label(frame3, text = "Aantal senioren restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

restaurant1.place(x=frame_x1, y=frame_y1)
restaurant2.place(x=frame_x1, y=frame_y2)
restaurant3.place(x=frame_x1, y=frame_y3)
restaurant4.place(x=frame_x1, y=frame_y4)
restaurant5.place(x=frame_x1, y=frame_y5)
restaurant6.place(x=frame_x1, y=frame_y6)
restaurant7.place(x=frame_x1, y=frame_y7)

restaurant8 = Label(frame3, text = "Datum", font=title2_font, 
                      bg=title2_bg, fg=title2_color)
restaurant9 = Label(frame3, text = "Aantal tickets restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant10 = Label(frame3, text = "Aantal bezoekers restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant11 = Label(frame3, text = "Aantal kleine kinderen restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant12 = Label(frame3, text = "Aantal kinderen restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant13 = Label(frame3, text = "Aantal volwassenen restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
restaurant14 = Label(frame3, text = "Aantal senioren restaurant", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

restaurant8.place(x=frame_x1, y=frame_y8)
restaurant9.place(x=frame_x1, y=frame_y9)
restaurant10.place(x=frame_x1, y=frame_y10)
restaurant11.place(x=frame_x1, y=frame_y11)
restaurant12.place(x=frame_x1, y=frame_y12)
restaurant13.place(x=frame_x1, y=frame_y13)
restaurant14.place(x=frame_x1, y=frame_y14)

#=================================== FORMAT FRAME4 =====================================

theatre1 = Label(frame4, text = "Totaal", font=title2_font, 
                        bg=title2_bg, fg=title2_color)
theatre2 = Label(frame4, text = "Aantal tickets theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre3 = Label(frame4, text = "Aantal bezoekers theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre4 = Label(frame4, text = "Aantal kleine kinderen theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre5 = Label(frame4, text = "Aantal kinderen theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre6 = Label(frame4, text = "Aantal volwassenen theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre7 = Label(frame4, text = "Aantal senioren theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

theatre1.place(x=frame_x1, y=frame_y1)
theatre2.place(x=frame_x1, y=frame_y2)
theatre3.place(x=frame_x1, y=frame_y3)
theatre4.place(x=frame_x1, y=frame_y4)
theatre5.place(x=frame_x1, y=frame_y5)
theatre6.place(x=frame_x1, y=frame_y6)
theatre7.place(x=frame_x1, y=frame_y7)

theatre8 = Label(frame4, text = "Datum", font=title2_font, 
                       bg=title2_bg, fg=title2_color)
theatre9 = Label(frame4, text = "Aantal tickets theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre10 = Label(frame4, text = "Aantal bezoekers theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre11 = Label(frame4, text = "Aantal kleine kinderen theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre12 = Label(frame4, text = "Aantal kinderen theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre13 = Label(frame4, text = "Aantal volwassenen theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
theatre14 = Label(frame4, text = "Aantal senioren theater", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

theatre8.place(x=frame_x1, y=frame_y8)
theatre9.place(x=frame_x1, y=frame_y9)
theatre10.place(x=frame_x1, y=frame_y10)
theatre11.place(x=frame_x1, y=frame_y11)
theatre12.place(x=frame_x1, y=frame_y12)
theatre13.place(x=frame_x1, y=frame_y13)
theatre14.place(x=frame_x1, y=frame_y14)

#=================================== FORMAT FRAME5 =====================================

facepaint1 = Label(frame5, text = "Totaal", font=title2_font, 
                        bg=title2_bg, fg=title2_color)
facepaint2 = Label(frame5, text = "Aantal tickets schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint3 = Label(frame5, text = "Aantal bezoekers schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint4 = Label(frame5, text = "Aantal kleine kinderen schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint5 = Label(frame5, text = "Aantal kinderen schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint6 = Label(frame5, text = "Aantal volwassenen schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint7 = Label(frame5, text = "Aantal senioren schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

facepaint1.place(x=frame_x1, y=frame_y1)
facepaint2.place(x=frame_x1, y=frame_y2)
facepaint3.place(x=frame_x1, y=frame_y3)
facepaint4.place(x=frame_x1, y=frame_y4)
facepaint5.place(x=frame_x1, y=frame_y5)
facepaint6.place(x=frame_x1, y=frame_y6)
facepaint7.place(x=frame_x1, y=frame_y7)

facepaint8 = Label(frame5, text = "Datum", font=title2_font, 
                       bg=title2_bg, fg=title2_color)
facepaint9 = Label(frame5, text = "Aantal tickets schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint10 = Label(frame5, text = "Aantal bezoekers schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint11 = Label(frame5, text = "Aantal kleine kinderen schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint12 = Label(frame5, text = "Aantal kinderen schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint13 = Label(frame5, text = "Aantal volwassenen schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
facepaint14 = Label(frame5, text = "Aantal senioren schminken", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

facepaint8.place(x=frame_x1, y=frame_y8)
facepaint9.place(x=frame_x1, y=frame_y9)
facepaint10.place(x=frame_x1, y=frame_y10)
facepaint11.place(x=frame_x1, y=frame_y11)
facepaint12.place(x=frame_x1, y=frame_y12)
facepaint13.place(x=frame_x1, y=frame_y13)
facepaint14.place(x=frame_x1, y=frame_y14)

#=================================== FORMAT FRAME6 =====================================

icecreamparlor1 = Label(frame6, text = "Totaal", font=title2_font, 
                        bg=title2_bg, fg=title2_color)
icecreamparlor2 = Label(frame6, text = "Aantal tickets ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor3 = Label(frame6, text = "Aantal bezoekers ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor4 = Label(frame6, text = "Aantal kleine kinderen ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor5 = Label(frame6, text = "Aantal kinderen ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor6 = Label(frame6, text = "Aantal volwassenen ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor7 = Label(frame6, text = "Aantal senioren ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

icecreamparlor1.place(x=frame_x1, y=frame_y1)
icecreamparlor2.place(x=frame_x1, y=frame_y2)
icecreamparlor3.place(x=frame_x1, y=frame_y3)
icecreamparlor4.place(x=frame_x1, y=frame_y4)
icecreamparlor5.place(x=frame_x1, y=frame_y5)
icecreamparlor6.place(x=frame_x1, y=frame_y6)
icecreamparlor7.place(x=frame_x1, y=frame_y7)

icecreamparlor8 = Label(frame6, text = "Datum", font=title2_font, 
                       bg=title2_bg, fg=title2_color)
icecreamparlor9 = Label(frame6, text = "Aantal tickets ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor10 = Label(frame6, text = "Aantal bezoekers ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor11 = Label(frame6, text = "Aantal kleine kinderen ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor12 = Label(frame6, text = "Aantal kinderen ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor13 = Label(frame6, text = "Aantal volwassenen ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
icecreamparlor14 = Label(frame6, text = "Aantal senioren ijssalon", font=app1_font, 
                        bg=app1_bg, fg=app1_color)

icecreamparlor8.place(x=frame_x1, y=frame_y8)
icecreamparlor9.place(x=frame_x1, y=frame_y9)
icecreamparlor10.place(x=frame_x1, y=frame_y10)
icecreamparlor11.place(x=frame_x1, y=frame_y11)
icecreamparlor12.place(x=frame_x1, y=frame_y12)
icecreamparlor13.place(x=frame_x1, y=frame_y13)
icecreamparlor14.place(x=frame_x1, y=frame_y14)

parking15 = Label(frame12, text = "Donatie per weggegeven ijsje:", font=app1_font, 
                        bg=app1_bg, fg=app1_color)
parking15.place(x=0, y=frame_y15)

icecreamparlor_list = Listbox(frame12, font=check4_font, bg=check4_bg, fg=check4_color,  
                        width=6, height=1)
icecreamparlor_list.place(x=frame_x2, y=frame_y16)

data_entrance()
data_waiting_time()

root.mainloop()