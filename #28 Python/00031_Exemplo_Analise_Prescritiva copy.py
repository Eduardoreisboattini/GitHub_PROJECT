from pulp import LpMaximize, LpProblem, LpVariable, lpSum

class ProblemaOtimizacaoLinear:
    def __init__(self, nome, objetivos, restricoes):
        self.prob = LpProblem(nome, LpMaximize)
        self.variaveis_decisao = LpVariable.dicts("Quantidade", objetivos.keys(), lowBound=0)
        self.objetivos = objetivos
        self.restricoes = restricoes

    def definir_funcao_objetivo(self):
        self.prob += lpSum(self.objetivos[produto] * self.variaveis_decisao[produto] for produto in self.variaveis_decisao), "Total_Profit"

    def adicionar_restricoes(self):
        for nome_restricao, expressao in self.restricoes.items():
            self.prob += expressao, nome_restricao

    def resolver(self):
        self.prob.solve()

    def exibir_resultados(self):
        print(f"Status da otimização: {self.prob.status}")
        print(f"Resultado da otimização - Valor Ótimo: {round(lpSum(self.objetivos[produto] * self.variaveis_decisao[produto].varValue for produto in self.variaveis_decisao).value(), 2)}")
        print("\nQuantidades ótimas de cada produto:")
        for produto in self.variaveis_decisao:
            print(f"{produto}: {self.variaveis_decisao[produto].varValue}")

def realizar_analise_prescritiva():
    # Defina os objetivos (custos)
    custos = {"Produto1": 10, "Produto2": 15}

    # Defina as restrições
    restricoes = {
        "Recurso1": 2 * Problema.variaveis_decisao["Produto1"] + 3 * Problema.variaveis_decisao["Produto2"] <= 20,
        "Recurso2": 4 * Problema.variaveis_decisao["Produto1"] + 2 * Problema.variaveis_decisao["Produto2"] <= 16
    }

    # Crie uma instância do problema de otimização linear
    Problema = ProblemaOtimizacaoLinear("Maximize_Profit", custos, restricoes)

    # Defina a função objetivo e adicione as restrições
    Problema.definir_funcao_objetivo()
    Problema.adicionar_restricoes()

    # Resolva o problema
    Problema.resolver()

    # Exiba os resultados
    Problema.exibir_resultados()

# Realize a análise prescritiva
realizar_analise_prescritiva()

