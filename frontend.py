from tkinter import *
import tkinter
from backend import Database

database = Database("books.db")

class Window(object):
    def __init__(self, window):
        back = tkinter.Frame(master=window, width=500, height=400, bg='white')
        back.grid(row=0, column=0, rowspan=30, columnspan=30)
        window.wm_title("BookStore")
        
        
        self.title_label = Label(window, text="Title").grid(row=0, column=0)
        self.author_label = Label(window, text="Author").grid(row=0, column=2)
        self.year_label = Label(window, text="Year").grid(row=1, column=0)
        self.isbn_label = Label(window, text="ISBN").grid(row=1, column=2)

        self.title_text = StringVar()
        self.title_entry = Entry(window, textvariable=self.title_text)
        self.title_entry.grid(row=0, column=1)

        self.author_text = StringVar()
        self.author_entry = Entry(window, textvariable=self.author_text)
        self.author_entry.grid(row=0, column=3)

        self.year_text = StringVar()
        self.year_entry = Entry(window, textvariable=self.year_text)
        self.year_entry.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.isbn_entry = Entry(window, textvariable=self.isbn_text)
        self.isbn_entry.grid(row=1, column=3)


        self.content_listbox = Listbox(window, width=35, height=6)
        self.content_listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.content_listbox.bind("<<ListboxSelect>>", self.get_selected_row)

        scrollbar = Scrollbar(window)
        scrollbar.grid(row=2, column=2, rowspan=9)

        self.content_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.content_listbox.yview)

        view_all_btn = Button(window, text="View All", width=12, command=self.view_all_command)
        view_all_btn.grid(row=2, column=3)

        search_entry_btn = Button(window, text="Search Entry", width=12, command=self.search_command)
        search_entry_btn.grid(row=3, column=3)

        add_entry_btn = Button(window, text="Add Entry", width=12, command=self.insert_entry_command)
        add_entry_btn.grid(row=4, column=3)

        update_btn = Button(window, text="Update Entry", width=12, command=self.update_entry_command)
        update_btn.grid(row=5, column=3)

        delete_btn = Button(window, text="Delete Entry", width=12, command=self.delete_entry_command)
        delete_btn.grid(row=6, column=3)

        close_btn = Button(window, text="Close Entry", width=12, command=self.quit_command)
        close_btn.grid(row=7, column=3)
        
        
        
    def clear_text_area(self):
        self.content_listbox.delete(0, END)

    def view_all_command(self):
        self.clear_text_area()
        for item in database.view():
            self.content_listbox.insert(END, item)

    def search_command(self):
        self.clear_text_area()
        for item in database.search(title=self.title_text.get(), author=self.author_text.get(), year=self.year_text.get(), isbn=self.isbn_text.get()):
            self.content_listbox.insert(END, item)
            
    def insert_entry_command(self):
        database.insert(title = self.title_text.get(), author = self.author_text.get(), year = self.year_text.get(), isbn = self.isbn_text.get())
        self.view_all_command()
        
    def get_selected_row(self, event):
        try:
            global selected_tuple
            if(len(self.content_listbox.curselection()) > 0):
                index = self.content_listbox.curselection()[0]
                selected_tuple = self.content_listbox.get(index)

                self.title_entry.delete(0, END)
                self.title_entry.insert(END, selected_tuple[1])

                self.author_entry.delete(0, END)
                self.author_entry.insert(END, selected_tuple[2])

                self.year_entry.delete(0, END)
                self.year_entry.insert(END, selected_tuple[3])

                self.isbn_entry.delete(0, END)
                self.isbn_entry.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def delete_entry_command(self):
        if "selected_tuple" in globals():
            self.clear_text_area()
            database.delete(selected_tuple[0])
            self.view_all_command()

    def update_entry_command(self):
        if "selected_tuple" in globals():
            self.clear_text_area()
            database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
            self.view_all_command()

    def quit_command(self):
        MainWindow.destroy()

MainWindow = Tk()
win = Window(MainWindow)
MainWindow.mainloop()