from iasa_agente.src.contagem.mod_prob.problema_contagem import ProblemaContagem
from lib.pee.prof.procura_profundidade import ProcuraProfundidade

INICIO = 0
META = 9
PASSOS = [1, 2]

mec_proc = ProcuraProfundidade()
problema = ProblemaContagem(INICIO, META, PASSOS)
solucao = mec_proc.procurar(problema)

print(mec_proc.__class__.__name__)
if solucao:
    print([passo.operador._OperadorIncremento__incremento for passo in solucao])
    print("Dimensão:", solucao.dimensao)
    print("Custo:", solucao.custo)
    print("Nós processados:", mec_proc.nos_processados)
    print("Max de nós em memória:", mec_proc.nos_memoria)
else:
    print("Nenhuma solução encontrada.")