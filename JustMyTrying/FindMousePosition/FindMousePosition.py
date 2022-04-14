import pyautogui as pg
import tkinter as tk
import keyboard
import time

# узнать координаты
'''
start_key = input( 'Клавиша запуска: ' )
stop_key = input( 'Клавиша остановки: ' )

while True:
    if key.is_pressed( start_key ):
        tm.sleep(0.2)
        print(pg.position())
            
    if key.is_pressed( stop_key ):
        print('thanks')
        break
'''

WIDTH, HEIGHT = pg.size()  # Get the size of the primary monitor.
print("Size window:", WIDTH, HEIGHT, "\n")

# pg.alert(text = 'To use, press: "Ctrl"', title = 'Position of mouse', button = 'OK')

root = tk.Tk()
root.title('Location mouse')
s = "Size window: " + str(WIDTH) + " " + str(HEIGHT) + "\n" + "Press: 'Ctrl'"
label = tk.Label(root, font=('Ubuntu', 30), text=s)
label.pack()
mouseX0 = -1
mouseY0 = -1
while True:
    if keyboard.is_pressed('Esc'):
        break
    if keyboard.is_pressed('Ctrl'):
        mouseX, mouseY = pg.position()  # Get the XY position of the mouse.
        if mouseX0 == -1 and mouseY0 == -1:
            s = "Location mouse: " + str(mouseX) + " " + str(mouseY)
            print("Location mouse:", mouseX, mouseY)
            print("-" * 20)
            mouseX0 = mouseX
            mouseY0 = mouseY
            label.config(text=s)
        else:
            s = "Location mouse: " + str(mouseX) + " " + str(mouseY) + "\n"
            s += "Recently location mouse: " + str(mouseX0) + " " + str(mouseY0)
            s += "\n" + "Distantion: " + str(abs(mouseX - mouseX0)) + " " + str(abs(mouseY - mouseY0))
            print("Location mouse:", mouseX, mouseY)
            print("Recently location mouse:", mouseX0, mouseY0)
            print("Distantion:", abs(mouseX - mouseX0), abs(mouseY - mouseY0))
            print("-" * 20)
            mouseX0 = mouseX
            mouseY0 = mouseY
            label.config(text=s)

        time.sleep(0.25)

    try:
        root.update()
    except:
        break

root.mainloop()
print("\n------> Done")