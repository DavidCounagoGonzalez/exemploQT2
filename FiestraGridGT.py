import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class FiestraPrincipal (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GridGTK1")

        grid = Gtk.Grid()
        self.add(grid)

        texto = Gtk.Entry()
        boton1 = Gtk.Button(label = "1")
        boton2 = Gtk.Button(label="2")
        boton3 = Gtk.Button(label="3")
        boton4 = Gtk.Button(label="4")
        boton5 = Gtk.Button(label="5")
        boton6 = Gtk.Button(label="6")
        boton7 = Gtk.Button(label="7")
        boton8 = Gtk.Button(label="8")
        boton9 = Gtk.Button(label="9")
        boton0 = Gtk.Button(label="0")

        mas = Gtk.Button(label="+")
        menos = Gtk.Button(label="-")
        multi = Gtk.Button(label="*")
        div = Gtk.Button(label="/")
        igual = Gtk.Button(label="=")



        grid.attach(boton1, 0, 0, 1, 1)
        grid.attach_next_to(texto, boton1, Gtk.PositionType.TOP, 3, 1)
        grid.attach_next_to(boton2, boton1, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton3, boton2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton4, boton1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(boton5, boton4, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton7, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(boton8, boton7, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton9, boton8, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(boton0, boton7, Gtk.PositionType.BOTTOM, 3, 1)

        grid.attach_next_to(mas, texto, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(menos, boton3, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(multi, boton6, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(div, boton9, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(igual, boton0, Gtk.PositionType.RIGHT, 1, 1)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    FiestraPrincipal()
    Gtk.main()