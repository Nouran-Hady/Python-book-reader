from tkinter import*

window = Tk()
window.geometry("800x700")
window.title('welcome')

# making frames to the buttons
my_frame = Frame(window)
my_frame.pack()

entrylabel = Label(my_frame, height=2, width=20, text="start from page", font=("helvetica", 10, "bold"), relief="flat")
entrylabel.grid(row=0, column=0)
entry = Entry(my_frame, width=6, relief="raised", borderwidth=3)
entry.grid(row=0, column=1)
entry1label = Label(my_frame, height=2, width=10, text="end page", font=("helvetica", 10, "bold"), relief="flat")
entry1label.grid(row=2,column=0)
entry1 = Entry(my_frame, width=6, relief="raised", borderwidth=3)
entry1.grid(row=2, column=1)





label = Label(my_frame, height=5, width=10, text="poems:", font=("helvetica",10, "bold"), relief="flat")
label.grid(row=3, column=0)


# images of the buttons
#tkinter_image=PhotoImage(file=r"#put the image here after rezie it "
                             # r"(50x the aspect ratio of the site that i sent to"
                             # r" you) and change the height and width of the buttons but make them all the same ")

photo = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\william.png")
william_book = Button(my_frame, image=photo  ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("william_shakespeare_2012_1.pdf"))
william_book.grid(row=4, column=0)

photo1 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\maya (2).png")
william_book = Button(my_frame, image=photo1 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("The Complete Collected Poems of Maya Angelou ( PDFDrive ).pdf"))
william_book.grid(row=4, column=1)

photo2 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\emily.png")
william_book = Button(my_frame, image=photo2 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("emily_dickinson_2012_5.pdf"))
william_book.grid(row=4, column=2)

photo3 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\rumi.png")
william_book = Button(my_frame, image=photo3 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("171_rumi-the-book-of-love.pdf"))
william_book.grid(row=4, column=3)

photo4 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\mystical.png")
william_book = Button(my_frame, image=photo4 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("Mystical Poems of Rumi - words cascade ( PDFDrive ).pdf"))
william_book.grid(row=4, column=4)







label1 = Label(my_frame, height=5, width=10, text="novels:", font=("helvetica",10, "bold"), relief="flat")
label1.grid(row=5, column=0)


photo5 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\oliver twist.png")
william_book = Button(my_frame, image=photo5  ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("oliver-twist.pdf"))
william_book.grid(row=6, column=0)

photo6 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\a tale of two cities.png")
william_book = Button(my_frame, image=photo6 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("A Tale of Two Cities ( PDFDrive ).pdf"))
william_book.grid(row=6, column=1)

photo7 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\prisoner of zenda.png")
william_book = Button(my_frame, image=photo7 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("The Prisoner of Zenda ( PDFDrive ).pdf"))
william_book.grid(row=6, column=2)

photo8 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\the monk.png")
william_book = Button(my_frame, image=photo8 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("The Monk Who Sold His Ferrari ( PDFDrive ).pdf"))
william_book.grid(row=6, column=3)

photo9 = PhotoImage(file = r"C:\Users\malsayed\PycharmProjects\church.png")
william_book = Button(my_frame, image=photo9 ,height=215,width=155,
                      relief="raised", borderwidth=3, command=lambda: read("The Triumphant Church, Kenneth Hagin, 433pg.pdf"))
william_book.grid(row=6, column=4)




def read(book):
    pass

window.mainloop()
