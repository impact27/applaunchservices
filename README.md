# applaunchservices
Simple package for registering an app with apple Launch Services to handle UTI and URL. See Apple documentations for details.

## URL
Launch Services allows a GUI app to register a URL scheme.
This means the app can be called when the user types a URL like `<scheme>://<something>`.

 - `set_URL_scheme_handler`: Sets the given bundleid as the default handler for a given url scheme.
 - `get_URL_scheme_handler`: Gets the default bundleid for a given url scheme.
 - `open_URL`: Opens the given URL with launch services

## Files
Launch Services allows a GUI app to register a uniform type identifier (UTI).
This means the app can be called when the user double click on a file in the finder that matches this scheme.
Or if the user types an url like `<file:///path/to/file.ext>`.

- `set_UTI_handler`: Sets the given bundleid as the default handler for a given uniform type identifier and role.
- `get_UTI_handler`: Gets the default bundleid for a given uniform type identifier and role.
- `open_path`: Opens the given path with launch services

The roles are:
 - 'none'
 - 'viewer'
 - 'editor'
 - 'shell'
 - 'all'


## Bundle Identifier
The bundle identifier is used to identify an app. Two functions are supplied:

 - `get_bundle_identifier()`: Gets the current bundle identifier if it exists (The app is a GUI app)
 - `get_bundle_identifier(pid)`: Gets the bundle identifier for the given process id if it exists (The app is a GUI app)
 - `get_bundle_identifier_for_path(path)`: Gets the bundle identifier if the path points to a bundle

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
# The app can now receive file open events
```
