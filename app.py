def calcular_consumo():
    print("=" * 45)
    print(" ⚡ CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE")
    print("=" * 45)

    
    nome_aparelho = input("\nDigite o nome do aparelho (ex.: Geladeira): ").strip()
    
    try:
        potencia = float(input("Digite a potência do aparelho em Watts (W): "))
        horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))
    except ValueError:
        print("\n❌ Erro: Por favor, insira valores numéricos válidos para potência e horas.")
        return

    
    TARIFA_KWH = 0.75

    
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    custo_estimado = consumo_mensal * TARIFA_KWH


    print("\n" + "-" * 45)
    print("📊 RESUMO DO CONSUMO ESTIMADO")
    print("-" * 45)
    print(f"Aparelho: {nome_aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo mensal estimado: R$ {custo_estimado:.2f} (Tarifa: R$ {TARIFA_KWH:.2f}/kWh)")
    print("-" * 45)

if __name__ == "__main__":
    calcular_consumo()