import tkinter as tk
from tkinter import *
from threading import Thread
from custom_modules.index import window_location_handler, save_and_exit_window, cls, log, be


class main(tk.Tk):
    __main_frame_title = "MWM"
    __main_title = "Main Window With Menu"

    def __init__(this):
        super().__init__()
        cls()
        h_scroller = tk.Scrollbar(orient="horizontal")
        this.minsize(650, 500)
        this.maxsize(650, 500)
        this.title(this.__main_title.title())
        this.parent = this

        this.parent.option_add('*tearOff', FALSE)
        window_location_handler(this)

        this.content = Frame(this)
        this.content.grid(column=1, row=1, columnspan=4)

        this.search_entry_var = tk.StringVar()

        this.search_frame = tk.LabelFrame(
            this.content, text=this.__main_frame_title.upper())

        this.search_entry = Entry(this.search_frame, xscrollcommand=h_scroller.set,
                                  width=58, textvariable=this.search_entry_var, font=(
                                      "Helvetica", 12, 'normal'))

        this.search_button = Button(this.search_frame, text="Search",
                                    font=("Helvetica", 12, 'bold'))
        be(this.search_button, 'ButtonRelease', this.search_button_handler)
        be(this.search_button, 'KeyRelease', this.button_keyrelease_handler)

        this.build_menu()

    def build_menu(this):
        win = this.parent
        menubar = Menu(win)
        win['menu'] = menubar

        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_edit, label='Edit')

        menu_file.add_command(label='Close', command=this.closeFile)

    def build_interface(this):
        this.search_frame.grid(padx=6, pady=2, column=1, row=1)
        # Textfield
        this.search_entry.grid(ipady=5, pady=5, padx=5, column=1, row=1)
        # Button
        this.search_button.grid(padx=5, ipady=1, column=2, row=1)

    def create_gui(this):
        this.build_interface()
        this.mainloop()

    def search_button_handler(this, event):
        search_term = this.search_entry_var.get()
        this.handling(search_term)

    def button_keyrelease_handler(this, event):
        try:
            if event.keysym == 'space' or event.keycode == 65:
                search_term = this.search_entry_var.get()
                this.handling(search_term)
        except UnboundLocalError as ule:
            return

    def show_results_thread(this, arg=None):
        results_thread = Thread(target=this.show_results, args=(arg,))
        results_thread.start()
        results_thread = None

    def show_results(this, arg=None):
        frame = Frame(this.parent)
        frame.grid(column=1, row=2, ipady=10)

        control_frame = Frame(frame)
        control_frame.grid(column=1, columnspan=4, row=4, pady=10, padx=10)

        def remove_frame(event):
            frame.destroy()

        button_remove = Button(control_frame, text="Destroy",
                               font=("Helvetica", 12, 'bold'))
        button_remove.grid(column=1, row=1, ipady=5, ipadx=5)
        button_remove.bind('<ButtonRelease>', remove_frame)

        entry_title_var = StringVar()
        entry_name_var = StringVar()
        entry_email_var = StringVar()

        lbl_title = Label(frame, text="title".title(), font=(
            "Helvetica", 12, 'bold'))
        lbl_title.grid(column=1, row=1, padx=5)

        entry_title = Entry(frame, textvariable=entry_title_var, width=45)
        entry_title.grid(column=2, row=1, ipady=5)

        lbl_name = Label(frame, text="name".title(), font=(
            "Helvetica", 12, 'bold'))
        lbl_name.grid(column=1, row=2, padx=5)

        entry_name = Entry(frame, textvariable=entry_name_var, width=45)
        entry_name.grid(column=2, row=2, ipady=5)

        lbl_email = Label(frame, text="email".title(), font=(
            "Helvetica", 12, 'bold'))
        lbl_email.grid(column=1, row=3, padx=5)

        entry_email = Entry(frame, textvariable=entry_email_var, width=45)
        entry_email.grid(column=2, row=3, ipady=5)

        this.parent.update()

    def handling(this, search_term):
        if search_term:
            log('Input Value: {}'.format(search_term))
            this.search_entry_var.set('')
        else:
            log('No input')

    def closeFile(this):
        log('\t\tClose menu item selected')
        save_and_exit_window(this)
