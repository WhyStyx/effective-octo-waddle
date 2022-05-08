
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Order N Deliver")
root.geometry('300x200')
# Frames to separate first window
top_frame = Frame(root, height=200, width=300,)
top_frame.pack(side=TOP)
bot_frame = Frame(root, height=200, width=300,)
bot_frame.pack(side=BOTTOM)

win_title = Label(top_frame, text="Customer Info")
win_title.grid(row=0, column=1, columnspan=4)

# button to select delivery
b_delivery = Button(top_frame, text='Delivery', padx=50, command=lambda: click_delivery())
b_delivery.grid(row=2, column=0, columnspan=3)

# button to select carryout
b_carryout = Button(top_frame, text="Carry Out",  padx=50, command=lambda: click_carryout())
b_carryout.grid(row=2, column=3, columnspan=3)

# second window for ordering
def orderscreen():
    order_screen = Tk()
    order_screen.title("Order menu")
    order_screen.geometry('600x600')
# frames to split window
    top_frame2 = Frame(order_screen, height=100, width=600, bg="black")
    top_frame2.place(x=0, y=0)
    left_frame = Frame(order_screen, height=500, width=300, bg="blue")
    left_frame.place(x=0, y=100)
    right_frame = Frame(order_screen, height=400, width=300, bg="red")
    right_frame.place(x=300, y=100)
    rightbot_frame = Frame(order_screen, height=200, width=300, bg="grey")
    rightbot_frame.place(x=300, y=400)

# Title for frames
    order_title = Label(top_frame2, text="Customer Order")
    order_title.place(x=250, y=35)
    order_left = Label(left_frame, text="Specialty Pizzas")
    order_left.place(x=100, y=5)
    order_right = Label(right_frame, text="Items Ordered")
    order_right.place(x=100, y=5)
    order_ribot =Label(rightbot_frame, text="Total purchase")
    order_ribot.place(x=100, y=5)


# button click for carry out
def click_carryout():
    customer_name = Label(bot_frame, text="enter customer name")
    customer_name.grid(row=0, column=0, columnspan=1)
    name = Entry(bot_frame)
    name.grid(row=0, column=1, columnspan=1)
    customer_phone = Label(bot_frame, text="enter customer phone")
    customer_phone.grid(row=2, column=0, columnspan=1)
    phone = Entry(bot_frame)
    phone.grid(row=2, column=1, columnspan=1)
# submit button for conformation carryout
    def click_submit():
        orderscreen()
        root.destroy()
    b_submit = Button(bot_frame, text='submit info', command=lambda: click_submit())
    b_submit.grid(row=3, columnspan=3)

# button for delivery
def click_delivery():
    customer_name = Label(bot_frame, text="enter customer name")
    customer_name.grid(row=0, column=0, columnspan=1)
    name = Entry(bot_frame)
    name.grid(row=0, column=1, columnspan=1)
    customer_address = Label(bot_frame, text="enter customer address")
    customer_address.grid(row=1, column=0, columnspan=1)
    address = Entry(bot_frame)
    address.grid(row=1, column=1, columnspan=1)
    customer_phone = Label(bot_frame, text="enter customer phone")
    customer_phone.grid(row=2, column=0, columnspan=1)
    phone = Entry(bot_frame)
    phone.grid(row=2, column=1, columnspan=1)

    # gets Entry box inputs stores to use and write to file
    customer_info = name.get() + address.get() + phone.get()

# submit button to confirm delivery
    def click_submit():
        # Writes customer info to file
        customer_data = open("Customer_Data.txt", "a+")
        customer_data.write(customer_info)
        customer_data.close()

        orderscreen()
        root.destroy()

    b_submit = Button(bot_frame, text='submit info', command=lambda: click_submit())
    b_submit.grid(row=3, columnspan=3)

if __name__ == "__main__":

    mainloop()
