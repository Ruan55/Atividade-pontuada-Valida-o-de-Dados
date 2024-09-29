import sys
sys.path.append('/workspaces/Atividade-pontuada-Valida-o-de-Dados')
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.enums.unidade_federativa import UnidadeFederativa
from models.endereco import Endereco
from models.engenheiro import Engenheiro
from models.medico import Medico
from models.advogado import Advogado
from models.cliente import Cliente
from models.prestacao_servicos import PrestacaoServicos
from models.fornecedor import Fornecedor

engenheiro = Engenheiro(555, "Ruan", "3333-4444", "Ruan55@gmail.com", Endereco("Rua K", "5", "N/A", "1111", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "04/08/2002", "2222", "3333", "4444", Setor.ENGENHARIA, 3000, "5555")
medico = Medico(222, "Maiara", "4444-3333", "Maiara22@gmail.com", Endereco("Rua L", "32", "N/A", "2222", "Salvador", UnidadeFederativa.BAHIA), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "03/05/2003", "3333", "4444", "2222", Setor.SAUDE, 5000, "6666")
advogado = Advogado(333, "Roberto", "8899-0033", "Rober@gmail.com", Endereco("Rua U", "67", "N/A", "9999", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO), Sexo.MASCULINO, EstadoCivil.CASADO, "04/02/1978", "4344", "3244", "8943", Setor.JURIDICO, 4500, "7777")
cliente = Cliente(111, "Amanda", "8342-4234", "Amanda323@gmail.com", Endereco("Rua R", "90", "N/A", "3333", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.CASADO, "08/07/2004", 101010)
prestacao_servico = PrestacaoServicos(444, "Roni", "0904-1010", "RoniGol@gmail.com", Endereco("Rua P", "45", "N/A", "7777", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO), "32323", "90804", "20/08/2024", "20/08/2025")
fornecedor = Fornecedor(777, "Palmeiras", "0942-5423", "Palmeiras@gmail.com", Endereco("Rua P", "12", "N/A", "8302", "São Paulo", UnidadeFederativa.RIO_DE_JANEIRO), "32434", "87900", "Uniforme 1")

print(engenheiro)
print(medico)
print(advogado)
print(cliente)
print(prestacao_servico)
print(fornecedor)