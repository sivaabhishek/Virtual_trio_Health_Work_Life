from tkinter import *

def blank_screen(a, b):
    import keyboard
    import threading
    import mouse
    import time

    for i in range( 150 ):
        keyboard.block_key( i )

    global executing
    executing = True

    def move_mouse():
        global executing
        while executing:
            mouse.move( 1, 0, absolute=True, duration=0 )

    def stop_infinite_mouse_control():
        global executing
        time.sleep( a )
        executing = False

    threading.Thread( target=move_mouse ).start()
    threading.Thread( target=stop_infinite_mouse_control ).start()

    win = Tk()
    win.after( a * 1000, lambda: win.destroy() )
    win.geometry( "700x350" )

    label = Label( win, text=b, font=('Helvetica 90 bold'), foreground="red3" )
    label.pack()

    win.wm_attributes( '-fullscreen', 'True' )
    win.mainloop()

    return

number_of_tasks = int( input( "Enter the number of tasks for today: " ) )

print( "Enter the task names in priority order and time taken in minutes" )
print( "Example: Task1 10" )
tasks = []

for i in range( number_of_tasks ):
    inp = input().split()
    inp[1] = int( inp[1] )
    tasks.append( inp )

print( tasks )

import datetime
import time
import keyboard


while True:
    time.sleep(1800)
    hr = datetime.datetime.now().time().hour
    mi = datetime.datetime.now().time().minute
    if hr == 9 and mi == 30:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 10 and mi == 5:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 10 and mi == 40:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 11 and mi == 15:
        blank_screen(600,'Please take 10 minute break')
    elif hr == 11 and mi == 55:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 12 and mi == 30:
        blank_screen(3600,"Lunch Break")
    elif hr == 14 and mi == 0:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 14 and mi == 35:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 15 and mi == 10:
        blank_screen(600,'Please take 10 minute break')
    elif hr == 15 and mi == 50:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 16 and mi == 0:
        blank_screen(600,'Please take 10 minute break')
    elif hr == 16 and mi == 40:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 17 and mi == 15:
        blank_screen(1500,'Please take 25 minute break')
    elif hr == 18 and mi == 10:
        blank_screen(300,'Please take 5 minute break')
    elif hr == 18 and mi == 45:
        blank_screen(300,'Please take 5 minute break')
        exit()
    for i in range( 150 ):
        keyboard.unblock_key( i )
