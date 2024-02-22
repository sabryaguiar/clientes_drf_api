from django.utils import timezone
from rest_framework.serializers import ValidationError

def cpf_valido(numero_do_cpf):
    if numero_do_cpf is None:
        return None
    
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numero_do_cpf if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        # return False
        raise ValidationError("CPF inválido: deve ter 11 dígitos numéricos")

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        # return False
        raise ValidationError("CPF inválido: todos os dígitos são iguais")

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            # return False
            raise ValidationError("CPF inválido")
    # return True

def rg_valido(numero_do_rg):
    if numero_do_rg is None:
        return None
    
    #  Obtém os números do rg e ignora outros caracteres
    rg = [int(char) for char in numero_do_rg if char.isdigit()]

    #  Verifica se o rg tem 9 dígitos
    if len(rg) != 9:
        # return False
        raise ValidationError("rg inválido: deve ter 9 dígitos numéricos")