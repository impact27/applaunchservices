# applaunchservices
Simple package for registering an app with apple Launch Services to handle UTI and URL

# Usage example:
```python
import applaunchservices as als
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QEvent, Qt

uniform_type_identifier = "public.python-script"
bundle_identifier = als.get_bundle_identifier()
print(repr(bundle_identifier))


class MacApplication(QApplication):
    def event(self, event):
        print(event.type())
        """Print recieved event"""
        if event.type() == QEvent.FileOpen:
            widget.setWindowTitle(str(event.file()))
        return QApplication.event(self, event)


app = MacApplication([''])
widget = QWidget()
# Reset old handler at the end
old_handler = als.get_UTI_handler(uniform_type_identifier, 'editor')
app.aboutToQuit.connect(
    lambda: als.set_UTI_handler(
        uniform_type_identifier, 'editor', old_handler))

app._starting = True


def handle_applicationStateChanged(state):
    if state == Qt.ApplicationActive and app._starting:
        app._starting = False
        bundle_identifier = als.get_bundle_identifier()
        print(repr(bundle_identifier))
        als.set_UTI_handler(
            uniform_type_identifier, 'editor', bundle_identifier)


app.applicationStateChanged.connect(handle_applicationStateChanged)
widget.setWindowTitle('test')
widget.show()
app.exec_()
```
