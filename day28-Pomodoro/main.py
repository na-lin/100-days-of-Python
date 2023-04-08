from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
# f7f5dd
YELLOW = "#FFFDA2"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.05
reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # global timer ,don't have this line is ok, it's global scope
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="25:00")
    timer_label.config(text="Timer")
    checkmarks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(sec):
    count_mins = math.floor(sec / 60)
    # why not use int(float) to omit decimal part
    count_secs = sec % 60
    # use if statement to show timer as  5:00
    # use dynamic typing to show 1:00 instead if else statment , so just use one canvas.textconfig
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    if count_mins < 10:
        count_mins = f"0{count_mins}"

    # if sec % 60 == 0:
    #     # when sec < 10 . show like 1:9 , not 1:09 until 0:00
    #     canvas.itemconfig(time_text,text=f"{count_mins}:0{count_secs}")
    # else:
    canvas.itemconfig(time_text, text=f"{count_mins}:{count_secs}")

    if sec > 0:
        global timer
        timer = window.after(1000, count_down, sec - 1)
    else:  # sec == 0
        # global reps,marks
        # if reps % 2 != 0 :
        #     marks = marks + "✓"
        # checkmarks_label.config(text=marks)
        # start_count()

        global reps
        # TODO: add checkbox when one work time finish -- not don, have bug here
        work_sessions = math.floor(reps + 1 / 2)
        marks = ""
        print(work_sessions)
        if work_sessions % 2 == 0:
            for _ in range(work_sessions):
                marks += "✓"
            checkmarks_label.config(text=marks)

        # TODO: stop automic count , when one count end, change time_label and click start to start next count
        if (reps + 1) % 8 == 0:
            timer_label.config(text="Break", fg=RED)
        elif (reps + 1) % 2 == 0:
            timer_label.config(text="Break",fg=PINK)
        else:
            timer_label.config(text="Work",fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    # 25  minutes
    global reps
    reps += 1
    # or use reps % 2 , reps % 8 to figure out reps
    # error when reps > 8 , not good for user interface
    # if reps in (1, 3, 5, 7):
    #     time = WORK_MIN * 60
    # elif reps in (2, 4, 6):
    #     time = SHORT_BREAK_MIN * 60
    # elif reps == 8:
    #     time = LONG_BREAK_MIN * 60
    work_sessions = math.floor(reps / 2)
    marks = ""
    for _ in range(work_sessions):
        marks += "✓"
    checkmarks_label.config(text=marks)

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize(width=300, height=250)
# timer_label have specific width , when change its text when not effect other widget position
# window.resizable(False, False)
# window.geometry("500x480")
window.config(padx=100, pady=50, bg=YELLOW)

# TODO: canves image and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="25:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=1, column=1)

# TODO: window label: Timer, checkmark
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"), width=5)
timer_label.grid(row=0, column=1)

checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
checkmarks_label.grid(row=3, column=1)

# TODO: window button: Start, Reset
start_button = Button(text="Start", bg="white", highlightthickness=0, command=start_count)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
