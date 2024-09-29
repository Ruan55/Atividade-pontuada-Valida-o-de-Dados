import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def medico_valido():
    medico = Medico(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.SAUDE, 5000, "66666")
    return medico

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "66666"

def test_mudar_crm_valido(medico_valido):
    medico_valido.crm = "33333"
    assert medico_valido.crm == "33333"

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match="O crm deve se manter como tipo texto!"):
        Medico(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.SAUDE, 5000, 66666)