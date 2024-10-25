class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "Libre"
        
    def reservar_mesa(self):
        if self.estado == "Libre":
            self.estado == "Ocupada"
            return True
        else:
            return False
    
    def liberar_mesa(self):
        if self.estado == "Ocupada":
            self.estado == "Libre"
            return True
        else:
            return False
    
    def verificar_estado_mesa(self):
        return self.estado
    
    
