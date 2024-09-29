from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricaoestadual = self._verificar_inscricao_estadual(inscricaoestadual)

    def _verificar_cnpj(self,valor):
        self._verificar_cnpj_tipo_invalido(valor)

        self.cnpj = valor
        return self.cnpj

    def _verificar_inscricao_estadual(self,valor):
        self._verificar_inscricao_estadual_tipo_invalido(valor)

        self.inscricaoestadual = valor
        return self.inscricaoestadual
    
    def _verificar_cnpj_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O cnpj deve se manter como tipo texto!")
        
    def _verificar_inscricao_estadual_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A inscrição estadual deve ser um texto!")

    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\n Cnpj: {self.cnpj}"
                f"\n Inscrição Estadual: {self.inscricaoestadual}")