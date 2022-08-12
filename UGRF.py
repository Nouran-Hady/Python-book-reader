# from tkinter import*
# import pyttsx3, PyPDF2
# from tkinter import messagebox, filedialog
#
# window = Tk()
# window.geometry("900x800")
# window.title('AUDIO BOOK')
# window.iconbitmap("icon.ico")
# window.configure(bg='#ffd6ba')
#
# # making frames to the buttons
# my_frame = Frame(window)
# my_frame.pack()
#
#
# entrylabel = Label(my_frame, height=2, width=20, text="start from page", font=("helvetica", 10, "bold"), relief="flat")
# entrylabel.grid(row=0, column=0)
# entry = Entry(my_frame, width=6, relief="raised", borderwidth=3)
# entry.grid(row=0, column=1)
# entry1label = Label(my_frame, height=2, width=10, text="end page", font=("helvetica", 10, "bold"), relief="flat")
# entry1label.grid(row=2,column=0)
# entry1 = Entry(my_frame, width=6, relief="raised", borderwidth=3)
# entry1.grid(row=2, column=1)
#
# # x = int(entry.get())
# # y = int(entry1.get())
#
#
#
# label = Label(my_frame, height=5, width=10, text="poems:", font=("helvetica",10, "bold"), relief="flat")
# label.grid(row=3, column=0)
#
# photo = PhotoImage(file = r"william.png")
# william_book = Button(my_frame, image=photo  ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("william_shakespeare_2012_1.pdf"))
# william_book.grid(row=4, column=0)
#
# photo1 = PhotoImage(file = r"walt.png")
# william_book = Button(my_frame, image=photo1 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("Leaves of Grass.pdf"))
# william_book.grid(row=4, column=1)
#
# photo2 = PhotoImage(file = r"living in the light.png")
# william_book = Button(my_frame, image=photo2 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("Living in the Light- A guide to personal transformation ( PDFDrive ).pdf"))
# william_book.grid(row=4, column=2)
#
# photo3 = PhotoImage(file = r"rumi.png")
# william_book = Button(my_frame, image=photo3 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("171_rumi-the-book-of-love.pdf"))
# william_book.grid(row=4, column=3)
#
# photo4 = PhotoImage(file = r"mystical.png")
# william_book = Button(my_frame, image=photo4 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("Mystical Poems of Rumi - words cascade ( PDFDrive ).pdf"))
# william_book.grid(row=4, column=4)
#
#
# label1 = Label(my_frame, height=2, width=10, text="novels:", font=("helvetica",10, "bold"), relief="flat")
# label1.grid(row=5, column=0)
#
#
# photo5 = PhotoImage(file = r"oliver twist.png")
# william_book = Button(my_frame, image=photo5 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("oliver-twist.pdf"))
# william_book.grid(row=6, column=0)
#
# photo6 = PhotoImage(file = r"a tale of two cities.png")
# william_book = Button(my_frame, image=photo6 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("A Tale of Two Cities ( PDFDrive ).pdf"))
# william_book.grid(row=6, column=1)
#
# photo7 = PhotoImage(file = r"prisoner of zenda.png")
# william_book = Button(my_frame, image=photo7 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("The Prisoner of Zenda ( PDFDrive ).pdf"))
# william_book.grid(row=6, column=2)
#
# photo8 = PhotoImage(file = r"the monk.png")
# william_book = Button(my_frame, image=photo8 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("The Monk Who Sold His Ferrari ( PDFDrive ).pdf"))
# william_book.grid(row=6, column=3)
#
# photo9 = PhotoImage(file = r"church.png")
# william_book = Button(my_frame, image=photo9 ,height=215,width=155,
#                       relief="raised", borderwidth=3, command=lambda: page2func("The Triumphant Church, Kenneth Hagin, 433pg.pdf"))
# william_book.grid(row=6, column=4)
#
# stop = Button(text="quit", height=6, width=5, bg='#ffd6ba',
#                           relief="raised", borderwidth=3, command=lambda: window.quit())
# stop.pack()
#
# def page2func(book):
#         # to open the pdf
#         book1 = open(book, "rb")
#         engine = pyttsx3.init(driverName='sapi5')
#         engine.getProperty("rate")
#         engine.setProperty("rate", 0)
#
#         # to make sure it is encrypted
#         input = PyPDF2.PdfFileReader(book1)
#
#         if input.isEncrypted:
#             input.decrypt('')
#
#         try:
#             x = int(entry.get())
#             y = int(entry1.get())
#
#             bookexe = ""
#             for i in range(x, y + 1):
#                 page = input.getPage(x)
#                 text = page.extractText()
#                 bookexe = bookexe + text
#             engine.say(bookexe)
#             engine.runAndWait()
#         except:
#             messagebox.showinfo("missing page number", "enter page numbers")
#
# def add_book_function():
#     boook=filedialog.askopenfilename(initialdir="Downloads",title="choose a book you want", defaultextension=(("pdf files","*.pdf")))
#     yourbook = Button(text="your book", height=6, width=5, bg='blue',
#                   relief="raised", borderwidth=3, command=lambda: page2func(boook))
#     yourbook.pack(side=LEFT)
#
#
# newbook=Menu(window)
# window.config(menu=newbook)
# addbook=Menu(newbook)
# newbook.add_cascade(label="add books",menu=addbook)
# addbook.add_command(label="add book",command=add_book_function)
#
# window.mainloop()
string = 'abcd'

print(string.upper())