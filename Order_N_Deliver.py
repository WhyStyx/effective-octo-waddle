"""
Program Name: Order N Deliver
Author: Tyke Anfield
Date 5/11/2022
Purpose: Gui to simulate a pizza ordering app
"""
from tkinter import *
import sqlite3
from PIL import ImageTk,Image

root = Tk()
root.title("Order N Deliver")
root.geometry('450x400+600+300')

my_menu = Menu(root)
root.config(menu=my_menu)

# Frames to separate first window
top_frame = Frame(root, height=200, width=450)
top_frame.place(x=0, y=0)
bot_frame = Frame(root, height=200, width=450)
bot_frame.place(x=10, y=120)

win_title = Label(top_frame, text="Customer Info")
win_title.place(x=170, y=40)

# button to select delivery
b_delivery = Button(top_frame, text='Delivery', padx=30, command=lambda: click_delivery())
b_delivery.place(x=95, y=80)

# button to select carryout
b_carryout = Button(top_frame, text="Carry Out",  padx=30, command=lambda: click_carryout())
b_carryout.place(x=220, y=80)

'''
file_menu = Menu(my_menu)
my_menu.add_cascade(Label='exit', menu=file_menu)
file_menu.add_command(Label='exit', commmand=lambda: root.quit)
'''

# Button to exit program
btn_quit = Button(top_frame, text='Exit Program', command=lambda: root.quit())
btn_quit.place(x=10, y=10)


# button click for carry out
def click_carryout():
    CustomerData()


def click_delivery():
    CustomerData()

# ===============================================Ordering_Screen========================================================

# Window to take and output order
def OrderingScreen():
    global Pepperoni
    global supreme_pizza
    global meats
    global veggie
    global buff_chicken
    global taco_pizza

    # second window for ordering
    order_screen = Toplevel()
    order_screen.title("Order menu")
    order_screen.geometry('600x600+425+125')

    # frames to split window
    top_frame2 = Frame(order_screen, height=100, width=600, bg="black")
    top_frame2.place(x=0, y=0)
    left_frame = Frame(order_screen, height=300, width=600, bg="blue")
    left_frame.place(x=0, y=100)
    right_frame = Frame(order_screen, height=200, width=300, bg="red")
    right_frame.place(x=0, y=400)
    rightbot_frame = Frame(order_screen, height=200, width=300, bg="grey")
    rightbot_frame.place(x=300, y=400)

    # Title for frames
    order_title = Label(top_frame2, text="Customer Order")
    order_title.place(x=250, y=20)
    order_left = Label(left_frame, text="Specialty Pizzas")
    order_left.place(x=250, y=0)
    order_right = Label(right_frame, text="Items Ordered")
    order_right.place(x=105, y=5)
    order_ribot =Label(rightbot_frame, text="Total purchase")
    order_ribot.place(x=100, y=5)

    # Pizza Images
    Pepperoni = ImageTk.PhotoImage(Image.open("Images/Pepperoni_Pizza.png"))
    img_label = Label(left_frame, image=Pepperoni)
    img_label.place(x=100, y=75)
    supreme_pizza = ImageTk.PhotoImage(Image.open("Images/Supreme_Pizza.png"))
    img_label = Label(left_frame, image=supreme_pizza)
    img_label.place(x=250, y=75)
    meats = ImageTk.PhotoImage(Image.open("Images/Meats _Pizza.png"))
    img_label = Label(left_frame, image=meats)
    img_label.place(x=400, y=75)
    veggie = ImageTk.PhotoImage(Image.open("Images/Viggie_Pizza.bmp"))
    img_label = Label(left_frame, image=veggie)
    img_label.place(x=100, y=205)
    buff_chicken = ImageTk.PhotoImage(Image.open("Images/Buffalo_Chicken_Pizza.png"))
    img_label = Label(left_frame, image=buff_chicken)
    img_label.place(x=250, y=205)
    taco_pizza = ImageTk.PhotoImage(Image.open("Images/Taco_Pizza.bmp"))
    img_label = Label(left_frame, image=taco_pizza)
    img_label.place(x=400, y=205)

    # pizza Labels
    pepperoni_title = Label(left_frame, text="Pepperoni Pizza: $8")
    pepperoni_title.place(x=90, y=45)
    supreme_pizza_title = Label(left_frame, text="Supreme Pizza: $12")
    supreme_pizza_title.place(x=230, y=45)
    meats_title = Label(left_frame, text="Meats Pizza: $12")
    meats_title.place(x=390, y=45)
    veggie_title = Label(left_frame, text="Veggie Pizza: $10")
    veggie_title.place(x=90, y=180)
    buff_chicken_title = Label(left_frame, text="Buffalo Chicken Pizza: $12")
    buff_chicken_title.place(x=230, y=180)
    taco_pizza_title = Label(left_frame, text="Taco Pizza: $10")
    taco_pizza_title.place(x=390, y=180)


    # Add Pizzas
    pep_spin = Button(left_frame, text="+")
    pep_spin.place(x=100, y=135)
    supreme_spin = Button(left_frame, text="+")
    supreme_spin.place(x=250, y=135)
    meats_spin = Button(left_frame, text="+")
    meats_spin.place(x=400, y=135)
    veggie_spin = Button(left_frame, text="+")
    veggie_spin.place(x=100, y=265)
    buff_chicken_spin = Button(left_frame, text="+")
    buff_chicken_spin.place(x=250, y=265)
    taco_spin = Button(left_frame, text="+")
    taco_spin.place(x=400, y=265)

    # Subtract Pizza
    pep_spin = Button(left_frame, text="-")
    pep_spin.place(x=150, y=135)
    supreme_spin = Button(left_frame, text="-")
    supreme_spin.place(x=300, y=135)
    meats_spin = Button(left_frame, text="-")
    meats_spin.place(x=450, y=135)
    veggie_spin = Button(left_frame, text="-")
    veggie_spin.place(x=150, y=265)
    buff_chicken_spin = Button(left_frame, text="-")
    buff_chicken_spin.place(x=300, y=265)
    taco_spin = Button(left_frame, text="-")
    taco_spin.place(x=450, y=265)

    def add_pizza():
        return

    def sub_pizza():
        return

    btn = Button(right_frame, text='submit', command=lambda: add_pizza())
    btn.place(x=125, y=150)

    total = Label(right_frame, text='')
    total.place(x=20, y=20)


    # Quit button
    btn_quit2 = Button(top_frame2, text='Exit Program', command=lambda: root.quit())
    btn_quit2.place(x=10, y=10)

    def close():
        order_screen.destroy()
    back_btn = Button(top_frame2, text='Back to first screen', command=lambda: close())
    back_btn.place(x=10, y=50)


# =================================================Order_Database=======================================================


class CustomerData:

    def __init__(self):
        # Database
        self.conn = sqlite3.connect('address_book.db')
        # Create cursor
        self.c = self.conn.cursor()

        # Create table
        '''
        c.execute("""CREATE TABLE addresses(
                first_name text, 
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer,
                phone_number integer
                )""")
        '''
        def click_submit():
            # Create a database or connect to one
            self.conn = sqlite3.connect('address_book.db')
            # Create cursor
            self.c = self.conn.cursor()

            # Insert into Table
            self.c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode, :phone)",
                      {
                          'f_name': self.f_name.get(),
                          'l_name': self.l_name.get(),
                          'address': self.address.get(),
                          'city': self.city.get(),
                          'state': self.state.get(),
                          'zipcode': self.zipcode.get(),
                          'phone': self.phone.get()
                      })

            # Commit Changes
            self.conn.commit()

            # Close Connections
            self.conn.close()


            # Clear the Text Boxes
            self.f_name.delete(0, END)
            self.l_name.delete(0, END)
            self.address.delete(0, END)
            self.city.delete(0, END)
            self.state.delete(0, END)
            self.zipcode.delete(0, END)
            self.phone.delete(0, END)

        def query():
            OrderingScreen()


        # Create text boxes
        self.f_name = Entry(bot_frame, width=30)
        self.f_name.grid(row=0, column=1)
        self.l_name = Entry(bot_frame, width=30)
        self.l_name.grid(row=1, column=1)
        self.address = Entry(bot_frame, width=30)
        self.address.grid(row=2, column=1)
        self.city = Entry(bot_frame, width=30)
        self.city.grid(row=3, column=1)
        self.state = Entry(bot_frame, width=30)
        self.state.grid(row=4, column=1)
        self.zipcode = Entry(bot_frame, width=30)
        self.zipcode.grid(row=5, column=1)
        self.phone = Entry(bot_frame, width=30)
        self.phone.grid(row=6, column=1)

        # Create Text Box Labels
        self.f_name_label = Label(bot_frame, text="Enter first name")
        self.f_name_label.grid(row=0, column=0)
        self.l_name_label = Label(bot_frame, text="Enter last name")
        self.l_name_label.grid(row=1, column=0)
        self.address_label = Label(bot_frame, text="Enter address")
        self.address_label.grid(row=2, column=0)
        self.city_label = Label(bot_frame, text="Enter city")
        self.city_label.grid(row=3, column=0)
        self.state_label = Label(bot_frame, text="Enter state")
        self.state_label.grid(row=4, column=0)
        self.zipcode_label = Label(bot_frame, text="Enter zipcode")
        self.zipcode_label.grid(row=5, column=0)
        self.phone_label = Label(bot_frame, text="enter phone number")
        self.phone_label.grid(row=6, column=0)


        # Create Submit button
        self.b_submit = Button(bot_frame, text='submit info', command=lambda: click_submit())
        self.b_submit.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create Query button
        self.query_btn = Button(bot_frame, text='Continue to next screen', command=lambda: query())
        self.query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        # Commit Changes
        self.conn.commit()

        # Close Connections
        self.conn.close()

# ======================================================================================================================


if __name__ == "__main__":

    mainloop()


