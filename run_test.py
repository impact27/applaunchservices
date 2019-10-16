#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:02:30 2019

@author: quentinpeter
"""

import pytest
import applaunchservices as als
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QEvent, Qt, QTimer


def test_UTI():

    # This app opens python scripts as an editor
    uniform_type_identifier = "public.python-script"
    role = 'editor'
    url_scheme = "alstest"
    url = url_scheme + '://hello'

    class MacApplication(QApplication):
        """Application that process fileopen events."""

        def event(self, event):
            if event.type() == QEvent.FileOpen:
                filename = str(event.file())
                url = event.url()
                if filename:
                    app._last_file = filename
                elif url:
                    app._last_url = url
                widget.setWindowTitle(filename)
            return QApplication.event(self, event)

    # Create application and window
    app = MacApplication([''])
    widget = QWidget()

    # Reset old handler at the end
    old_UTI_handler = als.get_UTI_handler(uniform_type_identifier, role)
    old_URL_handler = als.get_URL_scheme_handler(url_scheme)

    def reset_handlers():
        als.set_UTI_handler(uniform_type_identifier, role, old_UTI_handler)
        als.set_URL_scheme_handler(url_scheme, old_URL_handler)

    app.aboutToQuit.connect(reset_handlers)

    # When the app is visible, register itself as a handler
    def handle_applicationStateChanged(state):
        if state == Qt.ApplicationActive and app._starting:
            app._starting = False
            bundle_identifier = als.get_bundle_identifier()
            als.set_UTI_handler(
                uniform_type_identifier, role, bundle_identifier)
            als.set_URL_scheme_handler(url_scheme, bundle_identifier)

    app._starting = True
    app.applicationStateChanged.connect(handle_applicationStateChanged)

    # Launch app
    widget.setWindowTitle('test')
    widget.show()

    # Send an event in the future
    timer_url = QTimer(app)
    timer_url.setSingleShot(True)
    timer_url.timeout.connect(lambda: als.open_URL(url))
    timer_url.start(1000)

    # Send an event in the future
    timer_open = QTimer(app)
    timer_open.setSingleShot(True)
    timer_open.timeout.connect(lambda: als.open_path(__file__))
    timer_open.start(1100)

    # Send an event in the future
    timer_close = QTimer(app)
    timer_close.setSingleShot(True)
    timer_close.timeout.connect(lambda: app.quit())
    timer_close.start(2000)

    app.exec_()
    # Check that we recieved the open file event
    assert app._last_file == __file__
    assert app._last_url.scheme() == url_scheme
    # Check that the previous handler is restored
    assert old_UTI_handler == als.get_UTI_handler(uniform_type_identifier, role)
    assert old_URL_handler == als.get_URL_scheme_handler(url_scheme)


if __name__ == "__main__":
    pytest.main()
