import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def advogado_valido():
    advogado = Advogado(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.SAUDE, 5000, "77777")
    return advogado

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "77777"

def test_mudar_oab_valido(advogado_valido):
    advogado_valido.oab = "88888"
    assert advogado_valido.oab == "88888"

def test_oab_tipo_invalido():
    with pytest.raises(TypeError, match="Oab deve se manter como tipo texto!"):
        Advogado(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.SAUDE, 5000, 77777)