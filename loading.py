import gi
import os

gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk
from gi.repository import WebKit2 as WebKit

webview = WebKit.WebView()
path = 'loading.html'
path = os.path.realpath(path)
webview.load_uri("file://" + path)

scrolledWindow = Gtk.ScrolledWindow()
scrolledWindow.add(webview)

window = Gtk.Window()
window.set_decorated(False)
window.set_default_size(800, 450)
window.set_position(Gtk.WindowPosition.CENTER)
window.add(scrolledWindow)
window.show_all()

def quit(args):
    Gtk.main_quit()
    os.system("killall flask")
window.connect("destroy", quit)

Gtk.main()