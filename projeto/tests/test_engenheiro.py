import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.ENGENHARIA, 5000, "55555")
    return engenheiro

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "55555"

def test_mudar_crea_valido(engenheiro_valido):
    engenheiro_valido.crea = "33333"
    assert engenheiro_valido.crea == "33333"

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="O crea deve se manter como tipo texto!"):
        Engenheiro(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.ENGENHARIA, 5000, 55555)