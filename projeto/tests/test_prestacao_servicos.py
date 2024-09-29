import pytest
from projeto.models.prestacao_servicos import PrestacaoServicos
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def prestacao_servicos_valido():
    prestacaoservico = PrestacaoServicos(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", "28/09/2024", "28/09/2025")
    return prestacaoservico

def test_contrato_inicio_valido(prestacao_servicos_valido):
    assert prestacao_servicos_valido.contratoinicio == "28/09/2024"

def test_mudar_contrato_inicio_valido(prestacao_servicos_valido):
    prestacao_servicos_valido.contratoinicio = "02/03/2024"
    assert prestacao_servicos_valido.contratoinicio == "02/03/2024"

def test_contrato_fim_valido(prestacao_servicos_valido):
    assert prestacao_servicos_valido.contratofim == "28/09/2025"

def test_mudar_contrato_fim_valido(prestacao_servicos_valido):
    prestacao_servicos_valido.contratofim = "02/03/2025"
    assert prestacao_servicos_valido.contratofim == "02/03/2025"

def test_contrato_inicio_tipo_invalido():
    with pytest.raises(TypeError, match="O inicio de contrato deve se manter como texto!"):
        PrestacaoServicos(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", 28092024, "28/09/2025")

def test_contrato_fim_tipo_invalido():
    with pytest.raises(TypeError, match="O fim de contrato deve se manter como texto!"):
        PrestacaoServicos(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), "2323", "3232", "28/09/2024", 28092025)