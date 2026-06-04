def mg_para_g(valor):
    return valor / 1000

def g_para_mg(valor):
    return valor * 1000

def mg_para_mcg(valor):
    return valor * 1000

def mcg_para_mg(valor):
    return valor / 1000

def mL_para_L(valor):
    return valor / 1000

def L_para_mL(valor):
    return valor * 1000

def concentracao_percentual(massa, volume):
    """Calcula a concentração % m/v: (g / mL) * 100"""
    if volume == 0:
        return 0
    return (massa / volume) * 100

def dose_total(dose_por_kg, peso_kg):
    """
    calcula a dose pelo peso do paciente.
    calculo: dose (mg/kg) x peso (kg) = dose total (mg)
    """
    return dose_por_kg * peso_kg    


def pedir_numero(mensagem):
    """Pede um número ao usuário. Fica pedindo até receber um válido."""
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("  ✖ Digite apenas números. Tente novamente.\n")



def menu():
    """Menu interativo principal do conversor."""

    while True:
        print("\n" + "═" * 45)
        print("   CONVERSOR DE UNIDADES FARMACÊUTICAS")
        print("═" * 45)

        print("  1. mg  →  g")
        print("  2. g   →  mg")
        print("  3. mg  →  mcg")
        print("  4. mcg →  mg")
        print("  5. mL  →  L")
        print("  6. L   →  mL")
        print("  7. Concentração % m/v")
        print("  8. Dose total  (mg/kg × peso)")
        print("  0. Sair")
        print("─" * 45)

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            valor = pedir_numero("  Valor em mg: ")
            resultado = mg_para_g(valor)
            print(f"\n  ✔ {valor:.3f} mg = {resultado:.3f} g")

        elif opcao == "2":
            valor = pedir_numero("  Valor em g: ")
            resultado = g_para_mg(valor)
            print(f"\n  ✔ {valor:.3f} g = {resultado:.3f} mg")

        elif opcao == "3":
            valor = pedir_numero("  Valor em mg: ")
            resultado = mg_para_mcg(valor)
            print(f"\n  ✔ {valor:.3f} mg = {resultado:.3f} mcg")

        elif opcao == "4":
            valor = pedir_numero("  Valor em mcg: ")
            resultado = mcg_para_mg(valor)
            print(f"\n  ✔ {valor:.3f} mcg = {resultado:.3f} mg")

        elif opcao == "5":
            valor = pedir_numero("  Valor em mL: ")
            resultado = mL_para_L(valor)
            print(f"\n  ✔ {valor:.3f} mL = {resultado:.3f} L")

        elif opcao == "6":
            valor = pedir_numero("  Valor em L: ")
            resultado = L_para_mL(valor)
            print(f"\n  ✔ {valor:.3f} L = {resultado:.3f} mL")

        elif opcao == "7":
            print("  Concentração % m/v → (massa em g ÷ volume em mL) × 100")
            massa = pedir_numero("  Massa do soluto (g): ")
            volume = pedir_numero("  Volume da solução (mL): ")
            resultado = concentracao_percentual(massa, volume)
            print(f"\n  ✔ Concentração: {resultado:.3f}% m/v")

        elif opcao == "8":
            print("  Dose total → dose (mg/kg) × peso do paciente (kg)")
            dose = pedir_numero("  Dose (mg/kg): ")
            peso = pedir_numero("  Peso do paciente (kg): ")
            resultado = dose_total(dose, peso)
            print(f"\n  ✔ Dose total: {resultado:.3f} mg")

        elif opcao == "0":
            print("\n  Conversor encerrado. Até logo!\n")
            break

        else:
            print("\n  ✖ Opção inválida. Digite um número de 0 a 8.")

if __name__ == "__main__":
    menu()