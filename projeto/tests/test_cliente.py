import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo 
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    cliente = Cliente(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", 22222)
    return cliente

def test_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloatendimento == 22222

def test_mudar_protocolo_de_atendimento_valido(cliente_valido):
    cliente_valido.protocoloatendimento = 33333
    assert cliente_valido.protocoloatendimento == 33333

def test_protocolo_de_atendimento_tipo_invalido():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve conter números inteiros!"):
        Cliente(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "22222")