import tkinter as tk
import random as rand

# base code from: https://seebass22.github.io/python-desktop-pet-tutorial/2021/05/16/desktop-pet.html

class pet(): 
    def __init__(self):
        # create a window
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.mouse_pressed = False
        self.right = True
        self.down = False
        self.idling = False
        self.idlect = 0
        # placeholder image
        self.img = tk.PhotoImage(file="assets/placeholder.png")

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground="black")

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes("-topmost", True)

        # turn black into transparency
        self.window.wm_attributes("-transparentcolor", "black")

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg="black")
        self.x = 0
        self.y = self.screen_height - 165
        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = 0
        self.y = self.screen_height - 165
        self.window.geometry('128x128+{x}+{y}'.format(x=str(self.x), y=str(self.y)))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.bind("<Return>", lambda e: self.pick_up())
        self.window.bind("<l>", lambda e: self.throw_left())
        self.window.bind("<r>", lambda e: self.throw_right())
        self.update_num = self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        print(self.x, self.screen_width)
        if self.right and not self.down and not self.idling:
            self.x += 1
            if self.x >= self.screen_width-100:
                self.idling = True
                self.right = False
        elif not self.down and not self.idling:
            self.x -= 1
            if self.x <= 0:
                self.idling
                self.right = True
        if self.down: 
            self.y += 1
            if self.y >= self.screen_height - 165: 
                self.y = self.screen_height - 165
                self.down = False
        if self.idling: 
            self.idlect += 1
        if self.idlect > 20:
            self.idling = False

        self.window.geometry('128x128+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)

    def pick_up(self):
        print("enter")
        self.down = True
        self.window.after_cancel(self.update_num)
        self.y = rand.randint(int(self.screen_height/4), 2*int(self.screen_height/4))
        self.window.geometry("128x128+{x}+{y}".format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)

    def throw_left(self):
        print("left")
        self.down = True
        self.window.after_cancel(self.update_num)
        self.x = 0
        self.window.geometry("128x128+{x}+{y}".format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)

    def throw_right(self):
        print("left")
        self.down = True
        self.window.after_cancel(self.update_num)
        self.x = self.screen_width-100
        self.window.geometry("128x128+{x}+{y}".format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)


if __name__ == '__main__':
    pet()
