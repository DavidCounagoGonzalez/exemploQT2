import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWin(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title ="GridGTK")

		grid = Gtk.Grid()
		self.add(grid)

		Boton1 = Gtk.Button(label ="Boton 1")
		Boton2 = Gtk.Button(label ="Boton 2")
		Boton3 = Gtk.Button(label ="Boton 3")
		Boton4 = Gtk.Button(label ="Boton 4")
		Boton5 = Gtk.Button(label ="Boton 5")
		Boton6 = Gtk.Button(label ="Boton 6")

		grid.add(Boton1)

		grid.attach(Boton2, 1, 0, 2, 1)

		grid.attach_next_to(Boton3, Boton1, Gtk.PositionType.BOTTOM, 1, 2)
		grid.attach_next_to(Boton4, Boton3, Gtk.PositionType.RIGHT, 2, 1)
		grid.attach(Boton5, 1, 2, 1, 1)
		grid.attach_next_to(Boton6, Boton5, Gtk.PositionType.RIGHT, 1, 1)


win = GridWin()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
