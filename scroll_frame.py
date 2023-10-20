import tkinter as tk


class ScrollFrame(tk.Frame):
    def __init__(self, master, x=True, y=True, custom_width=0, custom_height=0, **kw):
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        super().__init__(master, **kw)
        self._f = tk.Frame(self)
        if custom_width:
            canvas = tk.Canvas(self._f, width=custom_width, height=custom_height)
        else:
            canvas = tk.Canvas(self._f)
        self._scrollable_frame = tk.Frame(canvas)
        self._scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all"),
            ),
        )
        canvas.create_window(
            0,
            0,
            anchor="nw",
            window=self._scrollable_frame,
        )
        if y:
            self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
            self.scrollbar_y.pack(side=tk.RIGHT, fill="y")
            canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if x:
            self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=canvas.xview)
            self.scrollbar_x.pack(side=tk.BOTTOM, fill="x")
            canvas.configure(xscrollcommand=self.scrollbar_x.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.bind("<MouseWheel>", _on_mousewheel, "+")

    @property
    def f(self):  # 子ウィジェットを作るときは、子ウィジェットのインスタンス生成時、引数masterにこのプロパティを渡すこと．
        return self._scrollable_frame

    def pack(self, **kw):
        self._f.pack()
        super().pack(**kw)
