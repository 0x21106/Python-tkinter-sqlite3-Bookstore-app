from tkinter import *
import tkinter
import backend

MainWindow = Tk()
back = tkinter.Frame(master=MainWindow, width=500, height=400, bg='white')
back.grid(row=0, column=0, rowspan=30, columnspan=30)
MainWindow.wm_title("BookStore")

def clear_text_area():
    content_listbox.delete(0, END)

def view_all_command():
    clear_text_area()
    for item in backend.view():
        content_listbox.insert(END, item)

def search_command():
    clear_text_area()
    for item in backend.search(title=title_text.get(), author=author_text.get(), year=year_text.get(), isbn=isbn_text.get()):
        content_listbox.insert(END, item)
        
def insert_entry_command():
    backend.insert(title = title_text.get(), author = author_text.get(), year = year_text.get(), isbn = isbn_text.get())
    view_all_command()
    
def get_selected_row(event):
    try:
        global selected_tuple
        if(len(content_listbox.curselection()) > 0):
            index = content_listbox.curselection()[0]
            selected_tuple = content_listbox.get(index)

            title_entry.delete(0, END)
            title_entry.insert(END, selected_tuple[1])

            author_entry.delete(0, END)
            author_entry.insert(END, selected_tuple[2])

            year_entry.delete(0, END)
            year_entry.insert(END, selected_tuple[3])

            isbn_entry.delete(0, END)
            isbn_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass

def delete_entry_command():
    if "selected_tuple" in globals():
        clear_text_area()
        backend.delete(selected_tuple[0])
        view_all_command()

def update_entry_command():
    if "selected_tuple" in globals():
        clear_text_area()
        backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_all_command()

def quit_command():
    MainWindow.destroy()

title_label = Label(MainWindow, text="Title").grid(row=0, column=0)
author_label = Label(MainWindow, text="Author").grid(row=0, column=2)
year_label = Label(MainWindow, text="Year").grid(row=1, column=0)
isbn_label = Label(MainWindow, text="ISBN").grid(row=1, column=2)

title_text = StringVar()
title_entry = Entry(MainWindow, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(MainWindow, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(MainWindow, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(MainWindow, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)


content_listbox = Listbox(MainWindow, width=35, height=6)
content_listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
content_listbox.bind("<<ListboxSelect>>", get_selected_row)

scrollbar = Scrollbar(MainWindow)
scrollbar.grid(row=2, column=2, rowspan=9)

content_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=content_listbox.yview)

view_all_btn = Button(MainWindow, text="View All", width=12, command=view_all_command)
view_all_btn.grid(row=2, column=3)

search_entry_btn = Button(MainWindow, text="Search Entry", width=12, command=search_command)
search_entry_btn.grid(row=3, column=3)

add_entry_btn = Button(MainWindow, text="Add Entry", width=12, command=insert_entry_command)
add_entry_btn.grid(row=4, column=3)

update_btn = Button(MainWindow, text="Update Entry", width=12, command=update_entry_command)
update_btn.grid(row=5, column=3)

delete_btn = Button(MainWindow, text="Delete Entry", width=12, command=delete_entry_command)
delete_btn.grid(row=6, column=3)

close_btn = Button(MainWindow, text="Close Entry", width=12, command=quit_command)
close_btn.grid(row=7, column=3)

MainWindow.mainloop()