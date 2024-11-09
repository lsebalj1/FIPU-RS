import random

def ocjene(kolegiji):
    return {kolegij: [] for kolegij in kolegiji}

def simuliraj_ocjene(kolegiji):
    return {kolegij: [random.randint(1, 5) for _ in range(5)] for kolegij in kolegiji}