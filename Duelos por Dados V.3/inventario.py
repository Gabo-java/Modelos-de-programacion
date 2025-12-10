class InventarioFacade:  
    def __init__(self, pool_objetos):
        self.pool_objetos = pool_objetos
        self.objetos_almacenados = []  
        self.max_objetos = 5
    
     #Agrega un objeto al inventario si hay espacio.
    def agregar_objeto(self, objeto) -> bool:
        if len(self.objetos_almacenados) >= self.max_objetos:
            return False
        self.objetos_almacenados.append(objeto)
        return True
     #Obtiene un objeto del pool y lo guarda en inventario.
    def obtener_objeto_aleatorio_y_guardar(self, calidad: str) -> bool:
        
        objeto = self.pool_objetos.obtener_objeto_aleatorio(calidad)
        if objeto:
            return self.agregar_objeto(objeto)
        return False
    
    def usar_objeto(self, indice: int, jugador, enemigo, contexto: dict) -> tuple[bool, str]:
        # Validaciones
        if jugador.objeto_usado_en_turno:
            return False, "Ya usaste un objeto este turno."
        
        if indice < 0 or indice >= len(self.objetos_almacenados):
            return False, "Índice de objeto inválido."
        
        # Usar objeto
        objeto = self.objetos_almacenados.pop(indice)
        objeto.aplicar(jugador, enemigo, contexto)
        jugador.objeto_usado_en_turno = True
        
        # Devolver al pool
        self.pool_objetos.devolver_objeto(objeto)
        
        return True, f"Usaste: {objeto.nombre}"
    
    def cantidad_objetos(self) -> int:
        return len(self.objetos_almacenados)
    
    def obtener_nombres_objetos(self) -> list[str]:
        return [obj.nombre for obj in self.objetos_almacenados]
    
    def limpiar(self):
        for objeto in self.objetos_almacenados:
            self.pool_objetos.devolver_objeto(objeto)
        self.objetos_almacenados.clear()