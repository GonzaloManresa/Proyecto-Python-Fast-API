import Menu
import Mesa

class Restaurante:
    def __init__(self):
        self.mesas = []
        self.menu = Menu()
        self.clientes = []
        
    def añadir_mesa(self, numero, capacidad):
        self.mesas.append(Mesa(numero, capacidad))
        
    def remover_mesa(self, numero):
        self.mesas = [mesa for mesa in self.mesas if mesa.numero != numero]
        
    def mostrar_mesas_disponibles(self):
        for mesa in self.mesas:
            if mesa.verificar_estado() == "Libre":
                print(f"Mesa {mesa.numero} (Capacidad: {mesa.capacidad}) esta disponible")
                
    def hacer_reserva(self, cliente, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa and mesa.reservar():
                cliente.asignar_mesa(mesa)
                self.clientes.append(cliente)
                print(f"Mesa {numero_mesa} reservada para {cliente.nombre}.")
                return True
        print(f"Mesa {numero_mesa} no esta disponible")
        return False
    
    def gestionar_pedido(self, cliente, platos):
        if cliente in self.clientes:
            cliente.realizar_pedido(platos)
            print(f"Pedido realizado para {cliente.nombre}.")
        else:
            print("Cliente no registrado")
            
    def mostrar_cuenta(self, cliente):
        if cliente in self.clientes:
            cliente.ver_cuenta()
        else:
            print("Cliente no registrado")