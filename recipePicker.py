import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

bg_Colour = "#721616"

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()



def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables)-1)

    #get ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()
    
    # print(ingredients)
    # print(table_name)
    connection.close
    return table_name, table_records


def pre_proccess(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])
    print(title)

    ingredients = []

    #ingredients
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)
    
    return title, ingredients    



    

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    #frame 1 widgets
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_Colour)
    logo_widget.image = logo_img
    logo_widget.pack()
    tk.Label(frame1, text = "Ready for your random recipe???", bg=bg_Colour,fg="white", font=("TkMenuFont", 14)).pack()
    tk.Button(frame1, text = "Start", font=("TkMenuFont", 20), bg="#721616", fg="white", cursor="hand2", activebackground="#ffffff", activeforeground=bg_Colour, command=lambda:load_frame2()).pack(pady=40,)




def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_proccess(table_name, table_records)
    #frame 2 widgets
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_Colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=30)
    tk.Label(frame2, text = title, bg=bg_Colour,fg="white", font=("TkHeadingFont", 18)).pack(pady=18)

    for i in ingredients:
        tk.Label(frame2, text = i, bg=bg_Colour,fg="white", font=("TkMenuFont", 13)).pack(pady=4)

    tk.Button(frame2, text = "Back", font=("TkMenuFont", 20), bg=bg_Colour, fg="white", cursor="hand2", activebackground="#ffffff", activeforeground=bg_Colour, command=lambda:load_frame1()).pack(pady=40)

    # print("How does it look?")

# initiallize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

#for size
# x = root.winfo_screenwidth() // 2
# y = int(root.winfo_screenheight() * 0.1)
# root.geometry('500x600+' + str(x) + 'x' + str(y))


frame1 = tk.Frame(root, width=500, height=600, bg=bg_Colour)
frame2 = tk.Frame(root, bg=bg_Colour)


for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky = "nesw")



load_frame1()
# run app
root.mainloop()
