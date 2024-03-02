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
        self.update_num = self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        print(self.x, self.screen_width)
        if self.right and not self.down:
            self.x += 1
            if self.x >= self.screen_width:
                self.right = False
        elif not self.down:
            self.x -= 1
            if self.x <= 0:
                self.right = True

        if self.down: 
            self.y += 1
            if self.y >= self.screen_height - 165: 
                self.y = self.screen_height - 165
                self.down = False
        self.window.geometry('128x128+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)

    def pick_up(self):
        print("enter")
        self.down = True
        self.window.after_cancel(self.update_num)
        #self.x = rand.randint(0, self.screen_width)
        self.y = rand.randint(int(self.screen_height/4), 2*int(self.screen_height/4))
        self.window.geometry("128x128+{x}+{y}".format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)

if __name__ == '__main__':
    pet()
