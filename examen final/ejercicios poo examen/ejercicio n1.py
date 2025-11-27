class libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True 

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"has pedido prestado '{self.titulo}'.")
        else:
            print(f"el libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        self.disponible = True
        print(f"has devuelto '{self.titulo}'. Gracias.")

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"'{self.titulo}' de {self.autor} ({estado})"


class biblioteca:
    def __init__(self):
        self.catalogo = []  

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"libro agregado a la biblioteca: {libro.titulo}")

    def buscar_por_titulo(self, titulo_buscado):
        print(f"\n buscando '{titulo_buscado}'...")
        encontrado = False
        
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo_buscado.lower():
                encontrado = True
                print(f"libro encontrado: {libro}")
                
                if libro.disponible:
                    print("esta disponible! puedes pedirlo prestado.")
                else:
                    print("lo sentimos, actualmente está prestado.")
                return 

        if not encontrado:
            print("el libro no se encuentra en el catálogo.")



biblioteca = biblioteca()


libro1 = libro("el principito", "antoine de saint-exupéry")
libro2 = libro("frankenstein", "mary shelley")
libro3 = libro("cien años de soledad", "gabriel garcía márquez")


biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.buscar_por_titulo("frankestein")
libro2.prestar()  


biblioteca.buscar_por_titulo("frankenstein")

libro2.prestar()

libro2.devolver()
biblioteca.buscar_por_titulo("frankenstein")