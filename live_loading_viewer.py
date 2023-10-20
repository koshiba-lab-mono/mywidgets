from __future__ import annotations

import tkinter as tk
from typing import Callable, Sequence

import cv2
import numpy as np

from .scroll_image_viewer import ScrollImageViewer


class LiveLoadingViewer(ScrollImageViewer):
    def __init__(
        self,
        master: tk.Widget,
        img_paths: Sequence[str],
        add_drawing_func: None | Callable[[np.ndarray, int], np.ndarray] = None,
        **kw,
    ):
        self.img_paths: Sequence[str] = img_paths
        self.add_drawing_func: None | Callable[[np.ndarray, int], np.ndarray] = add_drawing_func
        super().__init__(master, **kw)

    @property
    def img(self) -> np.ndarray:
        if self.add_drawing_func is None:
            return cv2.imread(self.img_paths[self.index])
        else:
            return self.add_drawing_func(cv2.imread(self.img_paths[self.index]), self.index)

    @property
    def img_len(self) -> int:
        return len(self.img_paths)
