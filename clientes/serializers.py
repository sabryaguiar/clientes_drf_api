from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpf_valido, rg_valido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        cpf_valido(cpf)
        return cpf 
    def validate_rg(self, rg):
        rg_valido(rg)
        return rg 
    