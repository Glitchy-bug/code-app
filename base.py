class Publicacion:
    def __init__(self, autor, texto, imagen=None):
        self.autor = autor
        self.texto = texto
        self.imagen = imagen
        self.comentarios = []
        self.me_gusta = 0

    def dar_me_gusta(self):
        self.me_gusta += 1

    def agregar_comentario(self, autor, texto):
        comentario = Comentario(autor, texto)
        self.comentarios.append(comentario)

    def eliminar_publicacion(self, usuario):
        if usuario == self.autor:
            return True  # Indica que se puede eliminar
        return False


class Comentario:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto


class Usuario:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.amigos = []
        self.publicaciones = []

    def cambiar_contrasena(self, old_password, new_password):
        if self.verificar_contrasena(old_password):
            self.password = new_password

    def verificar_contrasena(self, password):
        return self.password == password

    def seguir_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)

    def hacer_publicacion(self, texto, imagen=None):
        publicacion = Publicacion(self, texto, imagen)
        self.publicaciones.append(publicacion)


class RedSocial:
    def __init__(self):
        self.usuarios = []
        self.publicaciones = []

    def crear_usuario(self, username, email, password):
        nuevo_usuario = Usuario(username, email, password)
        self.usuarios.append(nuevo_usuario)

    def buscar_usuario(self, username):
        for usuario in self.usuarios:
            if usuario.username == username:
                return usuario
        return None

    def iniciar_sesion(self, username, password):
        usuario = self.buscar_usuario(username)
        if usuario and usuario.verificar_contrasena(password):
            return usuario
        return None

    def visualizar_feed(self, usuario):
        feed = []
        for amigo in usuario.amigos:
            feed.extend(amigo.publicaciones)
        return feed