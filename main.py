import tkinter as tk
import time

# base code from: https://seebass22.github.io/python-desktop-pet-tutorial/2021/05/16/desktop-pet.html

class pet(): 
    def __init__(self):
        # create a window
        self.window = tk.Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.right = True
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

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = 0
        self.window.geometry('128x128+{x}+{y}'.format(x=str(self.x), y=str(self.screen_height-165)))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        print(self.x, self.screen_width)
        if self.right:
            self.x += 1
            if self.x >= self.screen_width: 
                self.right = False
        else: 
            self.x -= 1  
            if self.x <= 0: 
                self.right = True
        self.window.geometry('128x128+{x}+{y}'.format(x=str(self.x), y=str(self.screen_height-165)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(10, self.update)


if __name__ == '__main__':
    pet()
