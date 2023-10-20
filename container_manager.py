from __future__ import annotations

import tkinter as tk
from abc import ABCMeta, abstractmethod
from typing import Callable, Container, Sequence, TypeVar

Value = TypeVar("Value")


class ContainerManager(tk.LabelFrame, metaclass=ABCMeta):  # 抽象クラス
    def __init__(
        self,
        master,
        contents: Container[Value],
        receive_content_func: Callable[[tk.Event, Value], None],
        side: str = "top",
        **kw,
    ):
        """
        receive_content_funcに与えられる引数はイベントとcontents内の要素.
        継承先の_create_content_widget内で作成したウィジェットのバインド時に設定する.
        """
        super().__init__(master, **kw)
        self.contents: Container[Value] = contents
        self.receive_content_func: Callable[[Value], None] = receive_content_func
        self.side: str = side
        self.update()

    def update(
        self,
    ):  # クラスの外側やreceive_content_func内でcontentsを更新したときはこのメソッドを呼ぶとウィジェットが更新される
        for widget in self.winfo_children():
            widget.destroy()
        for content in self.contents:
            frame = tk.Frame(self)
            self._create_content_widget(frame, content)
            frame.pack(side=self.side)

    @abstractmethod
    def _create_content_widget(self, frame: tk.Frame, content: Value) -> None:
        ...  # リストの中の表示するコンテンツの説明や操作ボタンをこの抽象メソッドで決める．
