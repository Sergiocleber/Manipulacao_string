class ExtratorArgumentoUrl:
    def __init__(self,url):
        if self.urlEhValida(url):
            sel.url = url
        else:
            raise LookupError("Url Inválida!! ")

    @staticmethod # Definindo que o metodo é estatico
    def urlEhValida(url):
        if url:
            return True
        else:
            return False