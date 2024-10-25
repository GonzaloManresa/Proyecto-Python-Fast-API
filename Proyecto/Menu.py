import PlatoMenu

class Menu:
    def __init__(self):
        self.platos = []
        
    def agregar_plato(self, nombre, descripcion, precio):
        self.pedidos.append(PlatoMenu(nombre, descripcion, precio))
    
    def remover_plato(self, nombre):
        self.pedidos = [plato for plato in self.platos if plato.nombre != nombre]
        
    def mostrar_menu(self):
        for plato in self.platos:
            print(f"{plato.nombre}: {plato.descripcion} - ${plato.precio}")
    
    