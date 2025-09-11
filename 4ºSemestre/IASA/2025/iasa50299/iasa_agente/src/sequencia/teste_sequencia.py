from lib.pee.larg.procura_grafo import ProcuraGrafo
from lib.pee.larg.procura_largura import ProcuraLargura
from mod_prob.problema_sequencia import ProblemaSequencia
from lib.pee.mec_proc.solucao import Solucao

#mec_proc = ProcuraLargura()
mec_proc = ProcuraGrafo()


seq_inicial = [4, 3, 1, 2]
seq_final = [1, 2, 3, 4]


problema = ProblemaSequencia(seq_inicial, seq_final)

solucao_no_final = mec_proc.procurar(problema)
solucao = Solucao(solucao_no_final)

print("Custo:", solucao.custo)

if solucao:
    print(mec_proc.__class__.__name__)
    print("Solucao")
    for no in solucao:
        if no.operador:
            print(no.estado, no.operador)
        else:
            print(no.estado)
    print("Dimensao:", solucao.dimensao)
    print("Custo:", solucao.custo)
    print("Complexidade temporal:", mec_proc.nos_processados)
    print("Complexidade espacial:", len(mec_proc.fronteira))