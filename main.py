import time
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
        self.window.bind("<B1-Motion>", lambda e: self.move_window(e))
        self.window.bind("<ButtonRelease-1>", lambda e: self.release())
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
                self.idling = True
                self.right = True
        if self.down: 
            self.y += 1
            if self.y >= self.screen_height - 165: 
                self.y = self.screen_height - 165
                self.down = False
        if self.idling: 
            self.idlect += 1

        if self.idlect > 100:
            self.idling = False
            self.idlect = 0

        self.window.geometry('128x128+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.update_num = self.window.after(10, self.update)

    def move_window(self, event):
        self.window.geometry(f"+{event.x_root}+{event.y_root}")
        self.window.after_cancel(self.update_num)

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

    def drag(self, event):
        print("left", event)
        self.window.after_cancel(self.update_num)
        self.x = event.x
        self.y = event.y
        self.idling = True
        # self.update_num = self.window.after(10, self.update)

    def release(self):
        self.window.after_cancel(self.update_num)
        self.x = self.window.winfo_x()
        self.y = self.window.winfo_y()
        self.window.geometry("128x128+{x}+{y}".format(x=str(self.x), y=str(self.y)))

        print("release")

        if self.y >= self.screen_height - 165:
            self.y = self.screen_height - 165
            self.down = False
        else: 
            self.down = True
        print('releaseeeeeeeeeeeeeeee')
        self.update_num = self.window.after(10, self.update)

    def widget_drag_free_bind(self):
        """Bind any widget or Tk master object with free drag"""
        x, y = 0, 0
        def mouse_motion(event):
            global x, y
            # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
            offset_x, offset_y = event.x - x, event.y - y
            new_x = self.window.winfo_x() + offset_x
            new_y = self.window.winfo_y() + offset_y
            new_geometry = f"+{new_x}+{new_y}"
            self.window.geometry(new_geometry)

        def mouse_press(event):
            global x, y
            count = time.time()
            x, y = event.x, event.y
            self.window.after_cancel(self.update_num)

        self.window.bind("<B1-Motion>", mouse_motion)  # Hold the left mouse button and drag events
        self.window.bind("<Button-1>", mouse_press)  # The left mouse button press event, long calculate by only once


if __name__ == '__main__':
    pet()
