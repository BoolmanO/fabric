import gi
from typing import Literal
from fabric.widgets.widget import Widget

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Entry(Gtk.Entry, Widget):
    def __init__(
        self,
        text: str | None = None,
        placeholder_text: str | None = None,
        editable: bool = True,
        characters_visible: bool = True,
        max_length: int | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        tooltip_text: str | None = None,
        tooltip_markup: str | None = None,
        h_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        v_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        h_expand: bool = False,
        v_expand: bool = False,
        name: str | None = None,
        size: tuple[int] | None = None,
        **kwargs,
    ):
        """
        :param text: the default text, defaults to None
        :type text: str | None, optional
        :param placeholder_text: the placeholder text (displayed when entry is empty), defaults to None
        :type placeholder_text: str | None, optional
        :param editable: whether this entry is editable, defaults to True
        :type editable: bool, optional
        :param characters_visible: whether the characters are visible (used for passwords), defaults to True
        :type characters_visible: bool, optional
        :param max_length: the maximum length, defaults to None
        :type max_length: int | None, optional
        :param visible: whether the widget is initially visible, defaults to True
        :type visible: bool, optional
        :param all_visible: whether all child widgets are initially visible, defaults to False
        :type all_visible: bool, optional
        :param style: inline css style string, defaults to None
        :type style: str | None, optional
        :param style_compiled: whether the passed css should get compiled before applying, defaults to True
        :type style_compiled: bool, optional
        :param style_append: whether the passed css should be appended to the existing css, defaults to False
        :type style_append: bool, optional
        :param style_add_brackets: whether the passed css should be wrapped in brackets if they were missing, defaults to True
        :type style_add_brackets: bool, optional
        :param tooltip_text: the text added to the tooltip, defaults to None
        :type tooltip_text: str | None, optional
        :param tooltip_markup: the markup added to the tooltip, defaults to None
        :type tooltip_markup: str | None, optional
        :param h_align: the horizontal alignment, defaults to None
        :type h_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param v_align: the vertical alignment, defaults to None
        :type v_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param h_expand: the horizontal expansion, defaults to False
        :type h_expand: bool, optional
        :param v_expand: the vertical expansion, defaults to False
        :type v_expand: bool, optional
        :param name: the name of the widget it can be used to style the widget, defaults to None
        :type name: str | None, optional
        :param size: the size of the widget, defaults to None
        :type size: tuple[int] | None, optional
        """
        Gtk.Entry.__init__(self, **kwargs)
        self.set_text(text) if text is not None else None
        self.set_placeholder_text(
            placeholder_text
        ) if placeholder_text is not None else None
        self.set_max_length(max_length) if max_length is not None else None
        self.set_editable(editable)
        self.set_visibility(characters_visible)
        Widget.__init__(
            self,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            name,
            size,
        )
