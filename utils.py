import tkinter as tk


def color_change_hover(event: tk.Event):
    if event.type == "7":
        event.widget["bg"] = "gray"
    if event.type == "8":
        event.widget["bg"] = "SystemButtonFace"
