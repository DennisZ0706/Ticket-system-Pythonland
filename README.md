# Ticket system Pythonland

## The App

Complete ticket system for Pythonland with a ticket application, a cash register application and a database application. The ticket application allows visitors to create their own tickets at ticket machines at the entrance of the park. With the cash register application, these tickets can then be scanned by cashier staff at all cash registers in the park. With the database application all kinds of data can be retrieved from the database.

The ticket application guides the visitor through the ordering process. With arrows and checkboxes visitors and extra facilities can be added to the ticket. When the ticket is ready, a printable PDF of the E-ticket will be made.

All cash registers of the park have been implemented in the cash register application. A cash register can be selected by clicking the radio button of the cash register. When a visitor has lost a ticket, the application can retrieve the ticket from the database based on the name. Ticket data can also be requested from the database.

When a ticket is scanned the data will be added to the database. With the database application all kinds of visitor numbers can be retrieved from the database. Both per arrangement and in total. And both by date and total. It is also possible to request a report with all visitor numbers over a certain period.


## Libraries used

* tkinter               
* PIL, ImageTK Image
* datetime
* qrcode
* fpdf
* webbrowser
* os 
* calendar
* cv2
* winsound
* pyzbar


## Learned skills

* Build an E-ticket in pdf
* Show a pdf with webbrowser
* Work with cv2 and pyzbar to scan qr codes
* Learn filehandling, write and read files
* Build and design a database
* Work with calendars and datepickers
* Work with os to retrieve data from a database  

<br>

* Making a moscow analysis
* Creating a manual
* Basics of Git and Github
* A deeper understanding of testing applications


## How it works

**ticket_app**

The ordering process is started by clicking on the "Tickets Bestellen" button. By clicking on the arrows, visitors can be added to the ticket (per age category). Additional facilities can be added by checking the checkboxes. When a step has been completed, visitors can press "Verder". If they want to go back, they can click "Terug". After the last step and visitors have entered their name they can press on "Betalen" to pay and get the E-ticket.

**cash_register_app**

Tickets can be scanned by holding the QR-code in front of the camera. Info about the scanned ticket will dissapear at the black screens. When a ticket has been successfully scanned, a green image will appear in the camera screen with the number of visitors that are allowed to enter. When the ticket is invalid a red cross appears in the camera screen. By entering the ticket number in the input field at the bottom left, the ticket data of the entered ticket can be requested from the database. When a visitor has lost his ticket, his ticket can be retrieved from the database by entering his name in in the input fields at the bottom right. 

**database_app**

By clicking on the various cash registers at the top, data can be seen about how many visitors have visited each facility. By clicking on a date at the top of the calendar and clicking on "Date" you can also retrieve visitor numbers per date from a specific cash register. A report with all visitor numbers of all cash registers over a certain period of time can be requested by entering 2 dates at the top left and clicking on "Rapport". At the cash register at the entrance is also shown what the waiting time at the gate is. And at the cash register of the parkinglot is also shown how many cars are on the parkinglot. 


## Preview

**ticket_app**

![screenshot_ticket_start](Showcase/screenshot_ticket_start.png?raw=true "Start screen")

![screenshot_ticket_input_persons](Showcase/screenshot_ticket_input_persons.png?raw=true "Fill in persons")

![screenshot_ticket_eticket](Showcase/screenshot_ticket_eticket.png?raw=true "E-ticket")

**cash_register_app**

![screenshot_cash_acces](Showcase/screenshot_cash_acces.png?raw=true "Acces allowed")

![screenshot_cash_denied](Showcase/screenshot_cash_denied.png?raw=true "Acces denied")

![screenshot_cash_ticketdata](Showcase/screenshot_cash_ticketdata.png?raw=true "Get ticket data")

![screenshot_cash_name](Showcase/screenshot_cash_name.png?raw=true "Search ticket with name")

**database_app**

![screenshot_data_total](Showcase/screenshot_data_total.png?raw=true "Get data total")

![screenshot_data_date](Showcase/screenshot_data_date.png?raw=true "Get data date")

![screenshot_data_report](Showcase/screenshot_data_report.png?raw=true "Get report")
