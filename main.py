from tkinter import *
from tkinter import messagebox
import math


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
PI = math.pi

window = Tk()
window.title('Regular Polygon')
window.configure(padx=50, pady=50, bg='grey')
#Labels
number_of_edges = Label(text='Enter the number of edges:')
number_of_edges.grid(row=1,column=0)

length_of_edges = Label(text='Enter the length of the edge(in centimeters):')
length_of_edges.grid(row=2,column=0)
# Entry
number_of_edges_entry = Entry(width=45)
number_of_edges_entry.grid(row=1, column=1, columnspan=2)
number_of_edges_entry.focus()# positioning the cursor in this entry

length_of_edges_entry = Entry(width=45)
length_of_edges_entry.grid(row=2, column=1, columnspan=2)
length_of_edges_entry.focus()


def solve():
    num_edges = number_of_edges_entry.get()
    if num_edges.isdigit():
        num_edges = int(num_edges)
        if num_edges < 3:
            messagebox.showwarning(title=None,message='Polygon must have at least three edges!')
        else:
            length = float(length_of_edges_entry.get()) * 37.7952755906 # length is now converted in pixel
            alfa = 360/num_edges
            beta = 90 - (alfa/2)
            theta = beta*PI/180
            radius = length/(2*math.sin(alfa*PI/360))
            x0 = CANVAS_WIDTH/2
            y0 = CANVAS_HEIGHT/2
            coord = []
            n = 1
            while n <= num_edges:
                coord.append(x0 + radius*math.cos(theta))
                coord.append(y0 + radius*math.sin(theta))
                theta -= alfa*PI/180
                n += 1
            circumference = round(num_edges*length/37.7952755906, 2)
            area = round(0.5*num_edges*math.sin(alfa*PI/180)*(radius/37.7952755906)**2, 2)
            if coord[1] > CANVAS_HEIGHT:
                messagebox.showinfo(title=None, message='Your polygon edge is to long!')
            else:
                # creating a canvas for showing the result
                canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_WIDTH, bg='black')
                canvas.create_polygon(coord, fill='#b58f5b')
                canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/4,
                                   text="Regular Polygon with {} edges\n\nhave a circumference of {}cm\nand area of {}cm2"
                                   .format( num_edges, circumference, area), fill="white", font='Helvetica 15 bold')
                canvas.grid(row=0, column=1)
    else:
        messagebox.showinfo(title=None, message='The number of edges must be an integer number!')

solve_button = Button(text='show polygon', width=46, command=solve)
solve_button.grid(row=4,column=1,columnspan=2)

window.mainloop()