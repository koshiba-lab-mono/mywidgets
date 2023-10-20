import tkinter as tk
from typing import Sequence

import numpy as np

from .scroll_image_viewer import ScrollImageViewer


class CompletedLoadingViewer(ScrollImageViewer):
    def __init__(self, master: tk.Widget, imgs: Sequence[np.ndarray], **kw):
        self.imgs: Sequence[np.ndarray] = imgs
        super().__init__(master, **kw)

    @property
    def img(self) -> np.ndarray:
        return self.imgs[self.index]

    @property
    def img_len(self) -> int:
        return len(self.imgs)
