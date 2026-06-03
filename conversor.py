print("""# ─────────────────────────────────────────
# CONVERSOR DE UNIDADES FARMACÊUTICAS
# Projeto 01 — Python puro
# ─────────────────────────────────────────""")
valor = input('Digite um valor em mg:')
valor = float(valor)

resultado = valor / 1000

print(f'{valor} mg = {resultado} g')