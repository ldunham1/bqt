"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""

from contextlib import suppress

with suppress(ModuleNotFoundError):
    import win32gui

from PySide2.QtCore import QObject

from .blender_application import BlenderApplication


class Win32BlenderApplication(BlenderApplication):
    """
    Windows implementation of BlenderApplication
    """

    @staticmethod
    def _get_application_hwnd() -> int:
        """
        This finds the blender application window and collects the
        handler window ID

        Returns int: Handler Window ID
        """

        hwnd = win32gui.FindWindow(None, 'blender')
        return hwnd

    def _on_focus_object_changed(self, focus_object: QObject):
        """
        Args:
            QObject focus_object: Object to track focus change
        """

        if focus_object is self.blender_widget:
            win32gui.SetFocus(self._hwnd)
