class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("joao", "1111444-555")
conta = Conta(c1.get._nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()