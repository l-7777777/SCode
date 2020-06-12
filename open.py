import gi
import os

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

window = Gtk.Window()

dialog = Gtk.FileChooserDialog(
            "Please choose a folder",
            window,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK,
            ),
        )

dialog.set_default_size(800, 400)

response = dialog.run()
if response == Gtk.ResponseType.OK:
    print("You picked a file!")
elif response == Gtk.ResponseType.CANCEL:
    os.system("killall flask")
    os.system("killall python3")
    
dialog.destroy()

window.set_decorated(False)
window.set_default_size(800, 450)
window.set_position(Gtk.WindowPosition.CENTER)
window.show_all()

Gtk.main()