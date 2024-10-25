import Pedido

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesa_asignada = None
        self.pedido_actual = Pedido()
        
    def asignar_mesa(self, mesa):
        self.mesa_asignada = mesa
        
    def realizar_pedido(self, platos):
        for plato in platos:
            self.pedido_actual.agregar_pedido(plato)
            
    def ver_cuenta(self):
        total = self.pedido_actual.calcular_total()
        print(f"Total a pagar: ${total}")
        return total
    
    