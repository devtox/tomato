import sys
import cairo
import gi
import time
from threading import Timer

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Pango', '1.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib, Gtk, Gdk, GdkPixbuf, Pango, GObject

# Need an infinite timer
class Timer(Timer):
    """
    See: https://hg.python.org/cpython/file/2.7/Lib/threading.py#l1079
    """

    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.interval)
            self.function(*self.args, **self.kwargs)

        self.finished.set()

class CountdownTimer(Gtk.Window):

    seconds = 10
    def __init__(self, seconds):
        self.seconds = seconds
        Gtk.Window.__init__(self)

        self.set_size_request(300, 220)

        self.connect('destroy', Gtk.main_quit)
        self.connect('draw', self.draw)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)


        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_keep_above(True)
        self.set_decorated(False)
        self.stick()
        self.set_property('accept-focus', False)
        self.set_property('focus-on-map', False)
        self.set_position(Gtk.Align.CENTER)
        #bgcolor = Gdk.color_parse("black")
        #self.modify_bg(Gtk.NORMAL, bgcolor)

        markup = '<span foreground="orange" font="64">                                      </span>'
        _, attr, text, _ = Pango.parse_markup(markup, -1, '\0')
        self.label = Gtk.Label(self.format_duration(self.seconds))
        self.label.set_attributes(attr)
        self.add(self.label)

        self.set_app_paintable(True)
        self.show_all()

        self.timer = Timer(1, self.on_timeout)
        self.timer.start()        

    def on_timeout(self):
        self.seconds = self.seconds - 1
        mm, ss = divmod(self.seconds, 60)
        hh, mm= divmod(mm, 60)
        t = self.format_duration(self.seconds)
        self.label.set_text(t)

        if self.seconds <=0:
            self.timer.cancel()
            self.destroy()

    def format_duration(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

    def draw(self, widget, context):
        context.set_source_rgba(0, 0, 0, 0)
        context.set_operator(cairo.OPERATOR_SOURCE)
        context.paint()
        context.set_operator(cairo.OPERATOR_OVER)

if len(sys.argv) < 2:
    print('Use "python3 tomato.py seconds"')
    print('For example: python3 tomato.py 5')
else:
    seconds = int(sys.argv[1])

    CountdownTimer(seconds)
    Gtk.main()
