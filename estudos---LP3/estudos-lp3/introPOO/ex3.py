class ContaBancaria:
    def __init__(this, titular, saldo):
        this._titular = titular
        this._saldo = saldo
        this._ativo = False
    
    def __str__(this):
        return f'{this._ativo} - {this._titular}, você tem {this._saldo} reais'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

User1 = ContaBancaria('Gustavo', 500.00)
User2 = ContaBancaria('Letícia', 650.00)
User3 = ContaBancaria('Sarah', 455.00)

print(User1)
print(User2)
print(f'Antes de ativar: Conta ativa? {User3._ativo}')

ContaBancaria.ativar_conta(User3)
print(f'Depois de ativar: Conta ativa? {User3._ativo}')
print(User3)

