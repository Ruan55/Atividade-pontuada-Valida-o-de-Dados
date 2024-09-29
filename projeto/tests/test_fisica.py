import pytest
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def fisica_valida():
    fisica = Fisica(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002")
    return fisica

def test_data_de_nascimento_valido(fisica_valida):
    assert fisica_valida.datanascimento == "04/08/2002"

def test_mudar_data_de_nascimento_valido(fisica_valida):
    fisica_valida.datanascimento = "05/03/1999"
    assert fisica_valida.datanascimento == "05/03/1999"

def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match="A data de nascimento deve se manter como tipo texto!"):
        Fisica(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, 4082002)