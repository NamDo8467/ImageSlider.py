from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Hello")
root.iconbitmap('images/light_bulb.ico')

img1 = ImageTk.PhotoImage(Image.open("images/python.png"))
img2 = ImageTk.PhotoImage(Image.open("images/js.png"))
img3 = ImageTk.PhotoImage(Image.open("images/c#.png"))
img4 = ImageTk.PhotoImage(Image.open("images/java.png"))

image_list = [img1, img2, img3, img4]
my_label = Label(root, image = image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def next(image_number):
    print(image_number)
    global my_label
    global next_button
    global back_button
    global image_list
    if image_number == image_list.__len__():
        image_number = 0
        my_label.grid_forget()
        my_label = Label(root, image=image_list[image_number])
        my_label.grid(row=0, column=0, columnspan=3)

        next_button = Button(root, text="Next", command=lambda: next(image_number + 1))
        back_button = Button(root, text="Back", command=lambda: back(image_number - 1))
        status = Label(root, text=f'Image {image_number+1} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        next_button.grid(row=1, column=2)
        back_button.grid(row=1, column=0)
    else:
        my_label.grid_forget()
        my_label = Label(root, image=image_list[image_number])
        my_label.grid(row=0, column=0, columnspan=3)

        next_button = Button(root, text="Next", command=lambda: next(image_number + 1))
        back_button = Button(root, text="Back", command=lambda: back(image_number - 1))
        status = Label(root, text=f'Image {image_number+1} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        next_button.grid(row=1, column=2)
        back_button.grid(row=1, column=0)


def back(image_number):
    print(image_number)
    global my_label
    global next_button
    global back_button
    global image_list
    if image_number < 0:
        image_number = image_list.__len__()-1
        my_label = Label(root, image=image_list[image_number])
        my_label.grid(row=0, column=0, columnspan=3)

        next_button = Button(root, text="Next", command=lambda: next(image_number + 1))
        back_button = Button(root, text="Back", command=lambda: back(image_number - 1))
        status = Label(root, text=f'Image {image_number+1} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        next_button.grid(row=1, column=2)
        back_button.grid(row=1, column=0)
    else:
        my_label.grid_forget()
        my_label = Label(root, image=image_list[image_number])
        my_label.grid(row=0, column=0, columnspan=3)

        next_button = Button(root, text="Next", command=lambda: next(image_number + 1))
        back_button = Button(root, text="Back", command=lambda: back(image_number - 1))
        status = Label(root, text=f'Image {image_number+1} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W + E)
        next_button.grid(row=1, column=2)
        back_button.grid(row=1, column=0)


next_button = Button(root, text="Next", command=lambda: next(1))
back_button = Button(root, text="Back", command=back, state=DISABLED)
quit_button = Button(root, text="Exit the program", command=root.quit)
status = Label(root, text = f'Image 1 of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)

back_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1, padx=30, pady=10)
next_button.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop()