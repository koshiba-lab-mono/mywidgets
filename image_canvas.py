from __future__ import annotations

import tkinter as tk

import cv2
import numpy as np
from PIL import Image, ImageTk


class ImageCanvas(tk.Canvas):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.img_id: int | None = None
        self.photo: ImageTk.PhotoImage | None = None
        self.img: np.ndarray | None = None

    def update_img(self, img: np.ndarray, rate: float = 1.0):
        if self.photo is not None:
            self.delete(self.img_id)
        height, width, _ = [int(shape * rate) for shape in img.shape]
        self.img = cv2.resize(img, (width, height))
        self.photo = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)), master=self)
        self.img_id = self.create_image(0, 0, anchor="nw", image=self.photo)
        self["height"], self["width"] = height, width
