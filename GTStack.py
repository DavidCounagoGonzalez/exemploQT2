import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Exemplo de uso de Gtk.Stack")

        caixaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=4)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        combo = Gtk.ComboBoxText()
        combo.append_text("Púlsame")
        combo.append_text("Etiqueta")
        combo.connect("changed", self.on_combo_changed, stack)

        conmutador = Gtk.StackSwitcher()
        conmutador.set_stack(stack)

        botonCheck = Gtk.CheckButton(label = "Púlsame")
        stack.add_titled(botonCheck, "Boton", "Púlsame!!")

        etiqueta = Gtk.Label()
        etiqueta.set_markup("<big> Unha bonita etiqueta </big>")
        stack.add_titled(etiqueta, "Etiqueta", "Unha etiqueta")

        caixaV.pack_start (combo, True, True, 2)
        caixaV.pack_start(conmutador, True, True, 2)
        caixaV.pack_start(stack, True, True, 0)

        self.add(caixaV)
        self.connect ("destroy", Gtk.main_quit)
        self.show_all()


    def on_combo_changed(self, combo, stack):
        texto = combo.get_active_text()

        if texto == "Púlsame":
            stack.set_visible_child_name("Boton")
        if texto == "Etiqueta":
            stack.set_visible_child_name("Etiqueta")




if __name__=="__main__":
    Aplicacion()
    Gtk.main()