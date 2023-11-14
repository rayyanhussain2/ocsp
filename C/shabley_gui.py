import tkinter as tk
import ttkbootstrap as ttk
import shabley_shubik as ss
import matplotlib.pyplot as plt
import plotter as pl

#Done
courses = []
window = ttk.Window()
window.title("DM Project")
window.geometry('750x750')
window.resizable(False,False)
window["background"] = "#04364A"
frame_no = 1

states = []
state_name = tk.StringVar()
seats = tk.IntVar(value=None)
new_state_name = tk.StringVar()
new_seats = tk.IntVar(value=None)
actual_name = "";actual_value = 0

list_window_frame = ttk.Frame(master=window, style="TFrame")
list_window_frame.place(x = 0, y = 0, width = 750,height = 700)
list_window_frame.lower()

about_window_frame = ttk.Frame(master=window, style="TFrame")
about_window_frame.place(x = 0, y = 0, width = 750,height = 700)
about_window_frame.lower()

main_window_frame = ttk.Frame(master=window, style="TFrame")
main_window_frame.place(x = 0, y = 0, width = 750,height = 700)


style = ttk.Style()
style.configure("TFrame", background="#04364A")
style.configure("TButton", background="#07597a")
style.configure("TLabel",background = "#04364A",foreground="white")
style.configure("TButton.FinalButton", background="#37ACA4")
total = 0

def toggle_visibility(new_frame,no):
    global frame_no
    main_window_frame.place_forget()
    list_window_frame.place_forget()
    about_window_frame.place_forget()

    if no == 2:
        list_window()

    new_frame.place(x = 0, y = 0, width = 750,height = 700)
    frame_no = no
        

def reset():
    global courses,total
    states.clear()
    total = 0


def add_state():
    global total
    d = dict()
    d["Name"] = state_name.get();state_name.set("")
    d["Seats"] = seats.get();seats.set(0)
    d["Key Player"] = 0
    total += d["Seats"]
    states.append(d)

def modify_details():
    global actual_name,actual_value,states,new_state_name,new_seats
    name = new_state_name.get();new_state_name.set("")
    value = new_seats.get();new_seats.set(0)

    for i in states:
        if i["Name"] == actual_name:
            if (value == 0):
                states.remove(i)
                break
            i["Name"] = name
            i["Seats"] = value
            break
    print(states)

def calculate_shabley_shubik():
    if (total) != 0:
        ss.main_caller(states, total//2+1)
        pl.plotter(plt,states,total)
        plt.show()
    else:
        print("No inputs yet") 


def on_select(event):
    global actual_name, actual_value
    # Get the selected item(s) from the listbox
    selected_index = listbox.curselection()
    if selected_index:
        selected_value = states[selected_index[0]]
    
        if (selected_value):
            actual_name = selected_value["Name"]
            actual_value = selected_value["Seats"]
            entry.delete(0, tk.END) 
            entry.insert(0,actual_name)
            entry2.delete(0, tk.END) 
            entry2.insert(0,actual_value)

def main_window():
    global state_name,seats,seats
    title_label = ttk.Label(master=main_window_frame, text="Shabley Shubik", font="Calibri 30 bold",foreground="white")
    title_label.place(x = 234, y = 33, width = 300,height = 50)
    title_label["background"] = "#04364A"
    #First Input Box for entering couse code
    input_frame = ttk.Frame(master=main_window_frame, style="TFrame")

    input_frame.place(x = 200, y = 125, width = 513,height = 100)

    state_name_label = ttk.Label(master=input_frame, text="Enter name:", font="Calibri 15 bold")
    state_name_label.place(x = 0, y = 0)

    state_name = tk.StringVar()
    entry = ttk.Entry(master=input_frame, textvariable=state_name, background="white")
    entry.place(x = 0, y = 50, width = 300,height = 50)
    #First Input Box for entering credits
    input_frame2 = ttk.Frame(master=main_window_frame)
    input_frame2.place(x = 200, y = 250, width = 750,height = 100)

    seats_label = ttk.Label(master=input_frame2, text="Enter name:", font="Calibri 15 bold")
    seats_label.place(x = 0, y = 0)

    seats = tk.IntVar(value=None)
    entry2 = ttk.Entry(master=input_frame2, textvariable=seats)
    entry2.place(x = 0, y = 50, width = 300,height = 50)

    add_button = ttk.Button(master=main_window_frame, text="Add state", command=add_state)
    add_button.place(x = 260, y = 400, width = 186,height = 56)

    calculate_button = ttk.Button(master=main_window_frame, text="Calculate Shabley Shubik", command=calculate_shabley_shubik)
    calculate_button.place(x = 260, y = 500, width = 186,height = 56)

    reset_button = ttk.Button(master=main_window_frame, text="Reset", command=reset)
    reset_button.place(x = 260, y = 600, width = 186,height = 56)


def list_window():
    global states,listbox,entry,entry2,new_state_name,new_seats,actual_name,actual_value
    # Title label
    title_label = ttk.Label(
        master=list_window_frame,
        text="Listing data",
        font="Calibri 30 bold",
        foreground="white"
    )
    title_label.place(x=280, y=33, width=300, height=50)
    title_label["background"] = "#04364A"

    # Input frame
    input_frame = ttk.Frame(master=list_window_frame, style="TFrame")
    input_frame.place(x=150, y=100, width=450, height=500)

    # Listbox
    listbox = tk.Listbox(input_frame, selectmode=tk.SINGLE,font="Helvetica 20")
    listbox.place(x=0,y=0,height=200,width=400)

    scrollbar = tk.Scrollbar(input_frame, orient="vertical", command=listbox.yview)
    scrollbar.place(x=400, y=0, height=200)
    listbox.config(yscrollcommand=scrollbar.set)
    # Add items to the listbox
    for item in states:
        listbox.insert(tk.END, item["Name"])

    # Bind the listbox selection event to the on_select function
    listbox.bind('<<ListboxSelect>>', on_select)

    options_frame = ttk.Frame(master=list_window_frame, style="TFrame")

    options_frame.place(x = 200, y = 330, width = 513,height = 350)

    state_name_label = ttk.Label(master=options_frame, text="Modify name:", font="Calibri 15 bold")
    state_name_label.place(x = 0, y = 0)

    new_state_name = tk.StringVar()
    entry = ttk.Entry(master=options_frame, textvariable=new_state_name, background="white")
    entry.place(x = 0, y = 50, width = 300,height = 50)

    seats_label = ttk.Label(master=options_frame, text="Modify weight:", font="Calibri 15 bold")
    seats_label.place(x = 0, y = 130)

    new_seats = tk.IntVar(value=None)
    entry2 = ttk.Entry(master=options_frame, textvariable=new_seats)
    entry2.place(x = 0, y = 160, width = 300,height = 50)

    modify_button = ttk.Button(master=options_frame, text="Modify details", command=modify_details)
    modify_button.place(x = 60, y = 250, width = 186,height = 56)
    #First Input Box for entering credits

    # Frame for buttons


input_frame4 = ttk.Frame(master=window)
input_frame4.place(x = 0, y = 700, width = 750,height = 50)

first_button = ttk.Button(master=input_frame4, text="Main window", command = lambda: toggle_visibility(main_window_frame,1))
first_button.place(x = 0, y = 0, width = 750/2,height = 50)

# second_button = ttk.Button(master=input_frame4, text="Listing States", command = lambda: toggle_visibility(list_window_frame,2))
# second_button.place(x = 750/3, y = 0, width = 750/3,height = 50)

third_button = ttk.Button(master=input_frame4, text="List window", command = lambda: toggle_visibility(list_window_frame,2))
third_button.place(x = 750/2, y = 0, width = 750/2,height = 50)
        
list_window()
main_window()

window.mainloop()

