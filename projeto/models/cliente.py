from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, protocoloatendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento)
        self.protocoloatendimento = self._verificar_protocolo_de_atendimento(protocoloatendimento)

    def _verificar_protocolo_de_atendimento(self,valor):
        self._verificar_protocolo_de_atendimento_tipo_invalido(valor)

        self.protocoloatendimento = valor
        return self.protocoloatendimento

    def _verificar_protocolo_de_atendimento_tipo_invalido(self,valor):
        if not isinstance(valor, int):
            raise TypeError("O protocolo de atendimento deve conter números inteiros!")

    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\n Protocolo de atendimento: {self.protocoloatendimento}")