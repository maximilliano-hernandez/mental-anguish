# Max Hernandez, Final Project, CIS 345, !0:30, T Th
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from functools import wraps
from QuestionsClass import *
from difflib import *
from random import randint

window = Tk()
window.geometry('800x800')
window.minsize(width=800, height=800)

data = []
questions_list = []
game_list = []
count = 0
edit = FALSE
question_count = 0
q_index = 0

# STRINGVARS
question_number = StringVar
points = StringVar()
question_text_var = StringVar()
answer_1 = StringVar()
answer_2 = StringVar()
answer_3 = StringVar()
answer_4 = StringVar()
correct_answer = StringVar()
posfeedback = StringVar()
negfeedback = StringVar()
search_questions_edit_text = StringVar()
add_question_success_text = StringVar()


#random needed variables
edit_question_number = 0

# FRAME CREATION
main_menu_frame = Frame(window, relief=GROOVE, borderwidth=1)
questions_management_frame = Frame(window, relief=GROOVE, borderwidth=1)
questions_management_header = Frame(questions_management_frame)
questions_management_body = Frame(questions_management_frame)
view_questions_textbox_manage = Text(questions_management_frame)
questions_management_button_frame = Frame(questions_management_header)
add_edit_questions_frame = Frame(questions_management_header)
search_questions_edit_frame = Frame()
# FRAME PLACEMENT
questions_management_header.pack(side=TOP)
questions_management_body.pack(side=TOP, pady=20, padx=20, fill=X)
view_questions_textbox_manage.pack(expand=1, fill=BOTH, side='bottom')
questions_management_body.grid_columnconfigure(index=1, weight=1)
add_edit_questions_frame.pack(side='left', padx=20, ipadx=40)
questions_management_button_frame.pack(side='right', padx=20, ipadx=40)

# main_menu_frame widget creation
navigation_frame = Frame(main_menu_frame)
play_game_button = Button(navigation_frame, text="Play Game")
question_management_btn = Button(navigation_frame, text="Question Management")
view_questions_textbox_main = Text(main_menu_frame)
search_main = Frame(main_menu_frame)
search_label_main = Label(search_main, text="Search any part of question in the box to the right")
search_box_main = Entry(search_main)
# main_menu_frame widget placement
navigation_frame.pack(side='top', fill=BOTH, expand=1)
play_game_button.pack(expand=1, fill=BOTH, side='left')
question_management_btn.pack(expand=1, fill=BOTH, side='left')
search_label_main.pack(side=LEFT)
search_box_main.pack(side=RIGHT, fill=X, expand=1)
search_main.pack(side=TOP, fill=X)
view_questions_textbox_main.pack(expand=1, fill=BOTH, side='bottom')



# questions_management_frame widget creation
points_label = Label(questions_management_body, text="Point Value: ")
question_text_label = Label(questions_management_body, text="Question: ")
answer_1_label = Label(questions_management_body, text="Answer 1: ")
answer_2_label = Label(questions_management_body, text="Answer 2: ")
answer_3_label = Label(questions_management_body, text="Answer 3: ")
answer_4_label = Label(questions_management_body, text="Answer 4: ")
correct_answer_label = Label(questions_management_body, text="Correct Answer: ")
posfeedback_label = Label(questions_management_body, text="Positive Feedback: ")
negfeedback_label = Label(questions_management_body, text="Negative Feedback: ")
points_entry = Entry(questions_management_body, textvariable=points)
question_text_entry = Entry(questions_management_body, textvariable=question_text_var)
answer_1_entry = Entry(questions_management_body, textvariable=answer_1)
answer_2_entry = Entry(questions_management_body, textvariable=answer_2)
answer_3_entry = Entry(questions_management_body, textvariable=answer_3)
answer_4_entry = Entry(questions_management_body, textvariable=answer_4)
correct_answer_entry = Entry(questions_management_body, textvariable=correct_answer)
posfeedback_entry = Entry(questions_management_body, textvariable=posfeedback)
negfeedback_entry = Entry(questions_management_body, textvariable=negfeedback)
# questions_management_frame widget placement
points_label.grid(sticky=N+S+W+E, row=2, column=0)
question_text_label.grid(sticky=N+S+W+E, row=3, column=0)
answer_1_label.grid(sticky=N+S+W+E, row=4, column=0)
answer_2_label.grid(sticky=N+S+W+E, row=5, column=0)
answer_3_label.grid(sticky=N+S+W+E, row=6, column=0)
answer_4_label.grid(sticky=N+S+W+E, row=7, column=0)
correct_answer_label.grid(sticky=N+S+W+E, row=8, column=0)
posfeedback_label.grid(sticky=N+S+W+E, row=9, column=0)
negfeedback_label.grid(sticky=N+S+W+E, row=10, column=0)
points_entry.grid(sticky=N+S+W+E, row=2, column=1)
question_text_entry.grid(sticky=N+S+W+E, row=3, column=1)
answer_1_entry.grid(sticky=N+S+W+E, row=4, column=1)
answer_2_entry.grid(sticky=N+S+W+E, row=5, column=1)
answer_3_entry.grid(sticky=N+S+W+E, row=6, column=1)
answer_4_entry.grid(sticky=N+S+W+E, row=7, column=1)
correct_answer_entry.grid(sticky=N+S+W+E, row=8, column=1)
posfeedback_entry.grid(sticky=N+S+W+E, row=9, column=1)
negfeedback_entry.grid(sticky=N+S+W+E, row=10, column=1)



# questions_management_button_frame widget creation
add_questions_submit_btn = Button(questions_management_button_frame, text="Submit Question")
add_questions_reset_btn = Button(questions_management_button_frame, text="Reset")
home_btn = Button(questions_management_button_frame, text="Return Home")
add_question_success_label = Label(questions_management_button_frame, textvariable=add_question_success_text)
# questions_management_button_frame widget placement
add_question_success_label.pack(expand=1, fill=BOTH)
add_questions_submit_btn.pack(expand=1, fill=BOTH)
add_questions_reset_btn.pack(expand=1, fill=BOTH)
home_btn.pack()
search_manage = Frame(questions_management_frame)
search_label_manage = Label(search_manage, text="Search any part of question in the box to the right")
search_box_manage = Entry(search_manage)
search_label_manage.pack(side=LEFT)
search_box_manage.pack(side=RIGHT, fill=BOTH, expand=1)
search_manage.pack(side=TOP, fill=BOTH)
view_questions_textbox_manage.pack(expand=1, fill=BOTH, side='bottom')



#add_edit_questions_frame widget creation
question_management_indicator_label = Label(questions_management_header, text="Currently Adding Questions")
add_questions_btn = Button(add_edit_questions_frame, text="Add Questions", state=DISABLED)
edit_questions_btn = Button(add_edit_questions_frame, text="Edit Questions", state=NORMAL)
delete_questions_btn = Button(add_edit_questions_frame, text="Delete Current Question", state=DISABLED, bg='maroon')
edit_questions_search_frame = Frame(questions_management_header)
edit_questions_search_label = Label(edit_questions_search_frame, text="Enter Number of Question you wish to edit")
edit_questions_search_entry = Entry(edit_questions_search_frame, textvariable=search_questions_edit_text, justify=RIGHT)
edit_questions_search_submit = Button(edit_questions_search_frame, text="Submit")
# add_edit_questions_frame packing
question_management_indicator_label.pack(side=TOP)
add_questions_btn.pack(side=TOP)
edit_questions_btn.pack(side=TOP)
delete_questions_btn.pack(side=TOP)
edit_questions_search_label.pack(side=TOP, fill=BOTH)
edit_questions_search_entry.pack(fill=BOTH)
edit_questions_search_submit.pack(fill=BOTH)

# search_questions_edit
search_questions_edit_label = Label(search_questions_edit_frame, text="Enter Number of Question you would like to edit")
search_questions_edit_entry = Entry(textvariable=search_questions_edit_text)
search_questions_edit_btn = Button(search_questions_edit_frame, text="Edit Question")



# GAME WIDGETS AND FRAMES
game_frame = Frame(window, relief=GROOVE, borderwidth=1 )
question_area = Frame(game_frame, relief=GROOVE, borderwidth=1)
question_display = Label(question_area, textvariable=question_text_var, relief=GROOVE, borderwidth=1,
                         font=("Helvetica",20))
answer_area = Frame(game_frame)
left_answers = Frame(answer_area)
upper_left_answer = Button(left_answers, textvariable=answer_1, font=("Helvetica", 20))
lower_left_answer = Button(left_answers, textvariable=answer_2, font=("Helvetica", 20))
right_answers = Frame(answer_area)
upper_right_answer = Button(right_answers, textvariable=answer_3, font=("Helvetica", 20))
lower_right_answer = Button(right_answers, textvariable=answer_4, font=("Helvetica", 20))
question_display.pack(fill=BOTH, expand=1)
question_area.pack(side=TOP, expand=1, fill=BOTH)
answer_area.pack(side=BOTTOM, expand=1, fill=BOTH)
upper_left_answer.pack(side=TOP, expand=1, fill=BOTH)
lower_left_answer.pack(side=BOTTOM, expand=1, fill=BOTH)
upper_right_answer.pack(side=TOP, expand=1, fill=BOTH)
lower_right_answer.pack(side=BOTTOM, expand=1, fill=BOTH)
left_answers.pack(side=LEFT, expand=1, fill=BOTH)
right_answers.pack(side=RIGHT, expand=1, fill=BOTH)




def delete_question():
    global edit_question_number, questions_list
    print(edit_question_number)
    count = 1
    check = messagebox.askyesno(message="Do you wish to delete this question?")
    if check == YES:
        del questions_list[edit_question_number-1]
        for q in questions_list:
            q.question_number = count
            count += 1

    question_list_display()


# new screen function
def new_screen(frame):
    def wrapper():
        main_menu_frame.pack_forget()
        questions_management_frame.pack_forget()
        search_questions_edit_frame.pack_forget()
        game_frame.pack_forget()
        if frame == main_menu_frame or questions_management_frame:
            question_list_display()
        frame.pack(expand=1, fill='both', padx=10, pady=10)
    return wrapper()


def start_game():
    """Begins and plays a 1 player game of Mental Anguish"""
    global game_list

    new_screen(game_frame)
    x = 0

    while x < 3:
        upper = len(questions_list)-1
        y = randint(0, upper)
        game_list.append(questions_list[y])
        x += 1

    next_question()

    upper_left_answer.config(command=lambda: check_answer(answer_1.get()))
    upper_right_answer.config(command=lambda: check_answer(answer_3.get()))
    lower_left_answer.config(command=lambda: check_answer(answer_2.get()))
    lower_right_answer.config(command=lambda: check_answer(answer_4.get()))


def question_counter():
    global question_count

    question_count = 0
    print(question_count)
    while question_count < 3:
        print("hello")
        yield question_count
        print("there")
        question_count += 1

question_gen = question_counter()

def next_question():
    global question_count, q_index, question_gen

    q_index = next(question_gen)
    question_text_var.set(game_list[q_index].question_text)
    answer_1.set(game_list[q_index].answer_bank[0])
    answer_2.set(game_list[q_index].answer_bank[1])
    answer_3.set(game_list[q_index].answer_bank[2])
    answer_4.set(game_list[q_index].answer_bank[3])


def check_answer(chosen_answer):
    global question_count, game_list, q_index

    if chosen_answer == game_list[q_index].answer:
        print("Yay")
    else:
        print("Boo")

    next_question()


def populate_edit_question():
    global question_number, points, question_text_var, answer_1, answer_2, answer_3, answer_4, correct_answer, \
        posfeedback, negfeedback, edit_question_number

    try:
        edit_question_number = int(search_questions_edit_text.get())
        question_index = edit_question_number - 1
        question_to_edit = questions_list[question_index]
        # question_number.set(question_to_edit.question_number)
        points.set(question_to_edit.points)
        question_text_var.set(str(question_to_edit.question_text))
        answer_1.set(question_to_edit.answer_bank[0])
        answer_2.set(question_to_edit.answer_bank[1])
        answer_3.set(question_to_edit.answer_bank[2])
        answer_4.set(question_to_edit.answer_bank[3])
        correct_answer.set(question_to_edit.answer)
        posfeedback.set(question_to_edit.posfeedback)
        negfeedback.set(question_to_edit.negfeedback)

    except IndexError:
        messagebox.showwarning(message="Please Enter a valid Question Number")
    except ValueError:
        messagebox.showwarning(message="Please Enter a valid Question Number")


def reset_add_question():
    """Resets the add_question form"""
    points.set("")
    question_text_var.set("")
    answer_1.set("")
    answer_2.set("")
    answer_3.set("")
    answer_4.set("")
    correct_answer.set("")
    posfeedback.set("")
    negfeedback.set("")
    add_question_success_text.set('')
    search_questions_edit_text.set('')


# TODO Need to condense
def question_search_main(event):
    search_term_main = search_box_main.get()
    search_term_manage = search_box_manage.get()
    results_list = []

    for question in questions_list:
        if question.__str__().lower().__contains__(search_term_main.lower()):
            results_list.append(question)


    view_questions_textbox_main.config(state=NORMAL)
    view_questions_textbox_main.delete(1.0, END)
    for ques in results_list:
        view_questions_textbox_main.insert(END, ques)
    view_questions_textbox_main.config(state=DISABLED)


def question_search_manage(event):
    search_term_manage = search_box_manage.get()
    results_list = []

    for question in questions_list:
        if question.__str__().lower().__contains__(search_term_manage.lower()):
            results_list.append(question)

    view_questions_textbox_manage.config(state=NORMAL)
    view_questions_textbox_manage.delete(1.0, END)
    for ques in results_list:
        view_questions_textbox_manage.insert(END, ques)
    view_questions_textbox_manage.config(state=DISABLED)


def question_list_display():
    view_questions_textbox_main.config(state=NORMAL)
    view_questions_textbox_main.delete(1.0, END)
    for ques in questions_list:
        view_questions_textbox_main.insert(END, ques)
    view_questions_textbox_main.config(state=DISABLED)

    view_questions_textbox_manage.config(state=NORMAL)
    view_questions_textbox_manage.delete(1.0, END)
    for ques in questions_list:
        view_questions_textbox_manage.insert(END, ques)
    view_questions_textbox_manage.config(state=DISABLED)


def submit_question():
    """Allows user to submit questions into the question bank. Formats into JSON, clears Entry forms"""
    global points_entry, question_text_entry, answer_1_entry, answer_2_entry, answer_3_entry, answer_4_entry,\
        correct_answer_entry, posfeedback_entry, negfeedback_entry, data, add_questions_btn, edit_questions_btn,\
        question_management_indicator_label, edit, edit_question_number

    global question_text_var, answer_1, answer_2, answer_3, answer_4, \
        correct_answer, posfeedback, negfeedback, add_question_success_text

    global search_questions_edit_text

    new_question = Question()
    new_question.question_number = len(questions_list)+1
    new_question.points = points_entry.get()
    new_question.question_text = question_text_entry.get()
    new_question.answer_bank = [answer_1_entry.get(), answer_2_entry.get(), answer_3_entry.get(), answer_4_entry.get()]
    new_question.answer = correct_answer_entry.get()
    new_question.posfeedback = posfeedback_entry.get()
    new_question.negfeedback = negfeedback_entry.get()

    if edit == FALSE:
        questions_list.append(new_question)
        add_question_success_text.set('Question Added Successfully')

    else:
        new_question.question_number = edit_question_number
        questions_list[edit_question_number-1] = new_question
        add_question_success_text.set('Question Edited Successfully')

    points.set('')
    question_text_var.set('')
    answer_1.set('')
    answer_2.set('')
    answer_3.set('')
    answer_4.set('')
    correct_answer.set('')
    posfeedback.set('')
    negfeedback.set('')

    question_list_display()


def question_management_toggle():
    global add_questions_btn, edit_questions_btn, edit

    if add_questions_btn['state'] == NORMAL:
        add_questions_btn['state'] = DISABLED
        edit_questions_btn['state'] = NORMAL
        delete_questions_btn['state'] = DISABLED
        question_management_indicator_label.config(text='Currently Adding Questions')
        edit_questions_search_frame.pack_forget()
        edit = FALSE

    else:
        edit_questions_btn['state'] = DISABLED
        add_questions_btn['state'] = NORMAL
        delete_questions_btn['state'] = NORMAL
        question_management_indicator_label.config(text="Currently Editing Questions")
        edit_questions_search_frame.pack(side=BOTTOM)
        edit = TRUE


# COMMAND CONFIGURATION
play_game_button.config(command='open_question_list')
question_management_btn.config(command=lambda: new_screen(questions_management_frame))
search_questions_edit_btn.config(command=populate_edit_question)
add_questions_submit_btn.config(command=submit_question)
add_questions_reset_btn.config(command=reset_add_question)
home_btn.config(command=lambda: new_screen(main_menu_frame))
edit_questions_search_submit.config(command=populate_edit_question)
add_questions_btn.config(command=question_management_toggle)
edit_questions_btn.config(command=question_management_toggle)
delete_questions_btn.config(command=delete_question)
search_box_main.bind("<Key>", question_search_main)
search_box_manage.bind("<Key>", question_search_manage)
play_game_button.config(command=start_game)



with open('question_bank_experimental.json') as file:
    data = json.load(file)

# populates questions_list
for q in data:
    question = Question()
    question.question_number = q["Question Number"]
    question.points = q["Points"]
    question.question_text = q["Question"]
    question.answer_bank = [q["Answer 1"], q["Answer 2"], q["Answer 3"], q["Answer 4"]]
    question.answer = q["Correct Answer"]
    question.posfeedback = q["posfeedback"]
    question.negfeedback = q["negfeedback"]
    questions_list.append(question)

# runs program
new_screen(main_menu_frame)
window.mainloop()
new_file = []

# takes in-application question list and writes it to the json
count = 1
for q in questions_list:
    new_file.append(
        {
            "Question Number": count,
            "Points": q.points,
            "Question": q.question_text,
            "Answer 1": q.answer_bank[0],
            "Answer 2": q.answer_bank[1],
            "Answer 3": q.answer_bank[2],
            "Answer 4": q.answer_bank[3],
            "Correct Answer": q.answer,
            "posfeedback": q.posfeedback,
            "negfeedback": q.negfeedback
        }
    )

    count += 1

with open('question_bank_experimental.json', 'w') as file:
    json.dump(new_file, file)
