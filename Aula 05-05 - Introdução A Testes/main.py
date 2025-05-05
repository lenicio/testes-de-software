import inspect

def depositar(valor, nr_conta, self):
    pass

sig = len(inspect.signature(depositar).parameters)

print(sig)