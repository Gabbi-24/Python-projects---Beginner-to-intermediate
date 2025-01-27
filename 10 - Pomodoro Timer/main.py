from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#FF4545"
GREEN = "#526E48"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle = 0
check_mark_str = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global check_mark_str
    global cycle

    window.after_cancel(timer)
    check_mark_str = ""
    cycle = 0
    canvas.itemconfig(timer_text, text="00:00")
    heading_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():   # This will be the command for the start button
    global cycle
    global check_mark_str
    cycle += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if cycle in [1, 3, 5, 7]:
        count_down(work_sec)
        heading_label.config(text="Work", fg=GREEN)

    elif cycle in [2, 4, 6]:
        count_down(short_break_sec)
        check_mark_str += "✔"
        heading_label.config(text="Break", fg=PINK)
        check_mark_label.config(text=check_mark_str)

    elif cycle == 8:
        count_down(long_break_sec)
        check_mark_str += "✔"
        heading_label.config(text="Break", fg=RED)
        check_mark_label.config(text=check_mark_str)

    else:
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):      # Is called in the start_timer func
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:   # Don't want negative numbers, it must stop at 0
        global timer
        timer = window.after(1000, count_down, count-1)  # .after(time in ms, function name, any amount of arg to be passed into function)
    else:   # If it is zero, then we want it to run the start_time() func again
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
##### Create window object #####
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)   # Use bg to change background colour

## Get widow to update and call a function every specific number of milliseconds
#-- Call it inside the function defined above
# window.after(1000, count_down, 1)   # .after(time in ms, function name, any amount of arg to be passed into function)


##### Add image to window #####
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # See image for its size
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)    # x-pos, y-pos to get the image in the centre of canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1,row=1)


##### Add other UI components #####
#-- Heading
heading_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"),bg=YELLOW , fg=GREEN)
heading_label.grid(column=1, row=0)

#-- Start button
start_button = Button(text="Start", font=(FONT_NAME,12), command=start_timer)
start_button.grid(column=0, row=2)

#-- Reset button
reset_button = Button(text="Reset", font=(FONT_NAME,12), command=reset_timer)
reset_button.grid(column=2, row=2)

#-- Check mark label
check_mark_label = Label(text=check_mark_str, font=(FONT_NAME, 16), bg=YELLOW , fg=GREEN)
check_mark_label.grid(column=1, row=3)









window.mainloop()




