import functions
import FreeSimpleGUI as sg
import time
import os
import sys


def resource_path(filename):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, filename)

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as f:
        pass


sg.theme("LightYellow")

clock = sg.Text('', key = 'clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button(size=10, image_source=resource_path("add.png"), mouseover_colors="light blue",
                       tooltip="Add Todo", key='Add')
complete_button = sg.Button(image_source=resource_path("complete.png"), tooltip="Complete", key="Complete")

list_box = sg.Listbox(values = functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

exit_button = sg.Button("Exit")

window = sg.Window("To-Do App",
                   layout =[[clock],
                       [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout = 200)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
             try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
             except IndexError:
                 sg.popup("Please select an item first!", font = ("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

window.close()