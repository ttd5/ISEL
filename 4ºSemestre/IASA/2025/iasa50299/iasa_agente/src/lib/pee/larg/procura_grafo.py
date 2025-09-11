from pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):

    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
        ProcuraGrafo.nos_repetidos = 0

    

    def _memorizar(self, no):
        if self._manter(no):
            self._explorados[no.estado] = no
            super()._memorizar(no)
        else:
            ProcuraGrafo.nos_repetidos += 1

    def _manter(self, no):
        return no.estado not in self._explorados