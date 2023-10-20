from __future__ import annotations

import tkinter as tk
from typing import Callable

import cv2
import numpy as np

from .image_canvas import ImageCanvas


class ImageExtractor(tk.Tk):
    def __init__(self, image: np.ndarray, **kw):
        super().__init__(**kw)
        self.origin_img: np.ndarray = image
        height, width, _ = image.shape
        self.viewer: ImageCanvas = ImageCanvas(self, width=width, height=height)
        self.viewer.update_img(image)
        self.viewer.bind("<1>", lambda e: self._send_two_cor(e, self._extract_img))
        self.viewer.pack()
        self.subviewer: ImageCanvas = ImageCanvas(self)
        self.subviewer.pack()
        self.result: np.ndarray | None = None

    def _send_two_cor(
        self,
        e: tk.Event,
        send_func: Callable[[tuple[int, int]], None],
        *,
        __clicked_cor: list[None | int] = [None],
    ):
        if __clicked_cor[0] is None:
            __clicked_cor[0] = (e.x, e.y)
        else:
            second_clicked_cor = (e.x, e.y)
            if __clicked_cor[0] == second_clicked_cor:
                return
            send_func(__clicked_cor[0], second_clicked_cor)
            __clicked_cor[0] = None

    def _extract_img(self, cor_1: tuple[int, int], cor_2: tuple[int, int]):
        xmin, ymin = cor_1
        xmax, ymax = cor_2
        if xmin > xmax:
            xmin, xmax = xmax, xmin
        if ymin > ymax:
            ymin, ymax = ymax, ymin
        img_copy = self.origin_img.copy()
        visualized_img = cv2.rectangle(img_copy, cor_1, cor_2, (0, 0, 0), 3)
        self.viewer.update_img(visualized_img)
        extracted_img = self.origin_img[ymin:ymax, xmin:xmax]
        self.subviewer.update_img(extracted_img)
        self.subviewer["height"], self.subviewer["width"], _ = extracted_img.shape
        if self.result is None:
            tk.Button(self, text="完了", command=self.destroy).pack()
        self.result = extracted_img
