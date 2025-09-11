from abc import ABC, abstractmethod

class Estimulo(ABC):
    @abstractmethod
    def detectar(self, percepcao):
        """Detecta a presença de um estímulo numa percepção.

        :param percepcao: A percepção na qual o estímulo será detectado.
        :return: A intensidade associada à detecção do estímulo.
        """
        pass  # Implementação do método de detecção do estímulo