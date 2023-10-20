from __future__ import annotations

import tkinter as tk
from abc import ABCMeta, abstractmethod

import numpy as np

from .image_canvas import ImageCanvas
from .view_option_selector import ViewOptionSelector


class ScrollImageViewer(tk.LabelFrame, metaclass=ABCMeta):
    def __init__(self, master: tk.Widget, **kw):
        super().__init__(master, **kw)
        self.viewer = ImageCanvas(self)
        self.option = ViewOptionSelector(self, text="option")
        self.viewer.bind("<MouseWheel>", self._viewer_cmd)
        self.index: int = 0
        self._update()
        for w in (self.option, self.viewer):
            w.pack()

    def _viewer_cmd(self, e: tk.Widget) -> None:
        if e.delta > 0:
            if (self.index + self.option.skip) >= self.img_len:
                self.index = self.img_len - 1
            else:
                self.index += self.option.skip
        else:
            if (self.index - self.option.skip) <= 0:
                self.index = 0
            else:
                self.index -= self.option.skip
        self._update()

    def _update(self):
        self.viewer.update_img(self.img)
        self["text"] = str(self.num)

    @property
    def num(self) -> int:
        return self.index + 1

    @property
    @abstractmethod
    def img(self) -> np.ndarray:
        ...

    @property
    @abstractmethod
    def img_len(self) -> int:
        ...
