import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", "Placa de video")
    return fornecedor

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Placa de video"

def test_mudar_produto_valido(fornecedor_valido):
    fornecedor_valido.produto = "Processador"
    assert fornecedor_valido.produto == "Processador"

def test_produto_tipo_invalido():
    with pytest.raises(TypeError, match="O produto deve se manter do tipo texto!"):
        Fornecedor(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", 4444)