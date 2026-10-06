class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
def prestar(self):
    if self.disponible:
        self.disponible = False
        return True
    return False
