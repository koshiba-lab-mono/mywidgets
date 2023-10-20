import tkinter as tk


class ViewOptionSelector(tk.LabelFrame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master
        self.skip: int = 1
        self._create_widget()

    def _create_widget(self) -> None:
        def jump_cmd(e: tk.Event):
            self.master.index = int(jump_entry.get()) - 1
            self.master._update()

        def skip_cmd(e: tk.Event):
            self.skip = int(skip_entry.get())

        jump_area = tk.Frame(self)
        tk.Label(jump_area, text=f"jump (1~{self.master.img_len})").pack()
        jump_entry = tk.Entry(jump_area, justify="center")
        jump_entry.bind("<Return>", jump_cmd)
        skip_area = tk.Frame(self)
        tk.Label(skip_area, text="skip").pack()
        skip_entry = tk.Entry(skip_area, justify="center")
        skip_entry.bind("<Return>", skip_cmd)
        for w in (jump_entry, skip_entry):
            (w.insert(0, str(1)), w.pack())
        for w in (jump_area, skip_area):
            w.pack(side=tk.LEFT)
