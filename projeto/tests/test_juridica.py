import pytest
from projeto.models.juridica import Juridica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def juridica_valido():
    juridica = Juridica(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232")
    return juridica

def test_cnpj_valido(juridica_valido):
    assert juridica_valido.cnpj == "2323"

def test_mudar_cnpj_valido(juridica_valido):
    juridica_valido.cnpj = "1212"
    assert juridica_valido.cnpj == "1212"

def test_inscricao_estadual_valido(juridica_valido):
    assert juridica_valido.inscricaoestadual == "3232"

def test_mudar_inscricao_estadual_valido(juridica_valido):
    juridica_valido.inscricaoestadual = "4545"
    assert juridica_valido.inscricaoestadual == "4545"

def test_cnpj_tipo_invalido():
    with pytest.raises(TypeError, match="O cnpj deve se manter como tipo texto!"):
        Juridica(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), 2323, "3232")

def test_inscricao_estadual_tipo_invalido():
    with pytest.raises(TypeError, match="A inscrição estadual deve ser um texto!"):
        Juridica(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", 3232)