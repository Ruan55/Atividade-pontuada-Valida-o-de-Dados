import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))
    return pessoa

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 555

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Ruan"

def test_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Maiara"
    assert pessoa_valida.nome == "Maiara"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "3333-4444"

def test_mudar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "4444-3333"
    assert pessoa_valida.telefone == "4444-3333"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "Ruan55@gmail.com"

def test_mudar_email_valido(pessoa_valida):
    pessoa_valida.email = "Maiara22@gmail.com"
    assert pessoa_valida.email == "Maiara22@gmail.com"

def test_id_negativo():
    with pytest.raises(ValueError, match="O id não pode ser negativo!"):
        Pessoa(-555 , "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_id_tipo_invalido():
    with pytest.raises(TypeError, match="O id deve se manter como um número inteiro!"):
        Pessoa("555", "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve se manter como um texto!"):
        Pessoa(555, 22, "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_nome_vazio():
    with pytest.raises(TypeError, match="O nome não pode estar vazio!"):
        Pessoa(555, "", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_numero_tipo_valido():
    with pytest.raises(TypeError, match="O telefone deve se manter como tipo texto!"):
        Pessoa(555, "Ruan", 33, "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))

def test_email_tipo_valido():
    with pytest.raises(TypeError, match="O email deve se manter como texto!"):
        Pessoa(555, "Ruan", "3333-4444", 222 , Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA))