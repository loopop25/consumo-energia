# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## 📌 Sobre o Projeto
Sistema desenvolvido em Python para estimar o consumo de energia elétrica mensal (em kWh) e o custo financeiro aproximado de aparelhos eletrodomésticos com base no tempo de uso diário.

---

## 🧮 Fórmula Utilizada
$$\text{consumoMensal} = \frac{\text{potencia} \times \text{horasDia} \times 30}{1000}$$

* **Custo estimado:** Valor calculado multiplicando o consumo em kWh por R$ 0,75/kWh.

---

## 🚀 Como Executar
1. Certifique-se de ter o **Python 3** instalado.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
   ```bash
   python app.py