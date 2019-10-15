# applaunchservices
Simple package for registering an app with apple Launch Services to handle UTI and URL

## Usage example:
```python
import applaunchservices as als
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QEvent, Qt

# This app opens python scripts as an editor
uniform_type_identifier = "public.python-script"
role = 'editor'


class MacApplication(QApplication):
    """Application that process fileopen events."""
    def event(self, event):
        if event.type() == QEvent.FileOpen:
            widget.setWindowTitle(str(event.file()))
        return QApplication.event(self, event)

# Create application and window
app = MacApplication([''])
widget = QWidget()

# Reset old handler at the end
old_handler = als.get_UTI_handler(uniform_type_identifier, role)
app.aboutToQuit.connect(
    lambda: als.set_UTI_handler(
        uniform_type_identifier, role, old_handler))


# When the app is visible, register itself as a handler
def handle_applicationStateChanged(state):
    if state == Qt.ApplicationActive and app._starting:
        app._starting = False
        bundle_identifier = als.get_bundle_identifier()
        als.set_UTI_handler(
            uniform_type_identifier, role, bundle_identifier)
            
            
app._starting = True
app.applicationStateChanged.connect(handle_applicationStateChanged)

# Launch app
widget.setWindowTitle('test')
widget.show()
app.exec_()
```
