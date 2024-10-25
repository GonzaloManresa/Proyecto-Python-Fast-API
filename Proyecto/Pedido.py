class Pedido:
    def __init__(self):
        self.platos = []
        self.EstadoPlato= "en preparacion"
        
    def agregar_pedido(self, plato):
        self.platos.append(plato)
        
    def quitar_pedido(self, plato):
        if plato in self.platos:
            self.platos.remove(plato)
    
    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)
    
    def cambiar_estado(self,nuevo_estado):
        self.EstadoPlato= nuevo_estado
    
    