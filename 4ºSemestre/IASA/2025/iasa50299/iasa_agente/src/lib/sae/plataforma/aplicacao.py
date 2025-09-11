"""
Aplicação de contexto da simulação
@author: Luís Morgado
"""

import tkinter as tk

from .temporizador import Temporizador


#_____________________________________________________________
# Teclas de eventos

INICIAR = 'i'
"""Reiniciar ambiente"""
PAUSA = 'p'
"""Activar modo de pausa (execução passo-a-passo)"""
EXECUTAR = 'e'
"""Executar passo"""
VELOCIDADE = 'v'
"""Comutar velocidade (máxima/normal)"""
TERMINAR = 't'
"""Terminar simulação"""

#_____________________________________________________________

class Aplicacao:
    """Aplicação de contexto da simulação"""

    def __init__(self):
       """Criar aplicação"""
       self._janela = tk.Tk()
       self._temporizador = None

    def iniciar(self, controlador, tempo_passo, tempo_vmax):
        """Iniciar aplicação associando um controlador"""
        self._controlador = controlador
        self._tempo_passo = tempo_passo
        self._tempo_vmax = tempo_vmax
        # Temporização de passos de simulação
        self._temporizador = Temporizador(self._janela)
        self._temporizar_passo()
        # Ciclo principal da aplicação
        self._janela.mainloop()

    def iniciar_janela(self, x, y, dimx, dimy, titulo):
        """Iniciar janela principal"""
        self._janela.title(titulo)
        self._janela.geometry(f"{dimx}x{dimy}+{x}+{y}")

    def iniciar_controlos(self):
        """Iniciar controlos da janela principal da aplicação"""
        # Checkbox pausa
        self._chk_pausa_var = tk.BooleanVar(value=False)
        self._chk_pausa = tk.Checkbutton(self._janela, text="Pausa", 
                                         variable=self._chk_pausa_var, 
                                         command=self._temporizar_passo)
        self._chk_pausa.pack(side=tk.LEFT, padx=5, pady=5)
        # Checkbox velocidade máxima
        self._chk_vmax_var = tk.BooleanVar(value=False)
        self._chk_vmax = tk.Checkbutton(self._janela, text="Vel. max.", 
                                        variable=self._chk_vmax_var, 
                                        command=self._temporizar_passo)
        self._chk_vmax.pack(side=tk.LEFT, padx=15, pady=5)
        # Botão passo
        self._btn_passo = tk.Button(self._janela, text="Passo", 
                                    command=self._comando_passo)
        self._btn_passo.pack(side=tk.LEFT, padx=5, pady=5)
        # Botão reiniciar
        self._btn_reiniciar = tk.Button(self._janela, text="Reiniciar", 
                                        command=self._comando_reiniciar)
        self._btn_reiniciar.pack(side=tk.LEFT, padx=5, pady=5)
        # Botão terminar
        self._btn_terminar = tk.Button(self._janela, text="Terminar", 
                                       command=self._comando_terminar)
        self._btn_terminar.pack(side=tk.RIGHT, padx=5, pady=5)
        # Processar teclas
        self._janela.bind("<KeyPress>", self._comando_tecla)

    @property
    def janela(self):
        """Acesso à janela principal da aplicação"""
        return self._janela

    def criar_janela(self, x, y, dim_x, dim_y, titulo):
        """Criar nova janela"""
        nova_janela = tk.Toplevel(self._janela)
        nova_janela.title(titulo)
        nova_janela.geometry(f"{dim_x}x{dim_y}+{x}+{y}")
        nova_janela.protocol("WM_DELETE_WINDOW", self._comando_terminar) 
        return nova_janela

    def _temporizar_passo(self):
        """Temporizar passo de execução"""
        if not self._chk_pausa_var.get():
            intervalo = self._tempo_vmax if self._chk_vmax_var.get() else self._tempo_passo
            self._temporizador.iniciar(intervalo, self._comando_passo)
    
    def _comando_passo(self):
        """Comando de execução de passo de simulação"""
        # Processar passo de simulação
        self._controlador.comando_passo()
        # Temporizar passo de simulação
        self._temporizar_passo()
    
    def _comando_reiniciar(self):
        """Comando de reiniciar simulação"""
        self._temporizador.terminar()
        self._controlador.comando_reiniciar()
        self._temporizar_passo()

    def _comando_terminar(self):
        """Comando de terminar simulação"""
        self._janela.quit()

    def _comando_tecla(self, evento):
        """Processar comandos de teclas"""
        tecla = evento.char
        if tecla == INICIAR:
            self._comando_reiniciar()
        elif tecla == EXECUTAR:
            self._comando_passo()
        elif tecla == TERMINAR:
            self._comando_terminar()
        elif tecla == PAUSA:
            self._chk_pausa_var.set(not self._chk_pausa_var.get())
            self._temporizar_passo()
        elif tecla == VELOCIDADE:
            self._chk_vmax_var.set(not self._chk_vmax_var.get())
            self._temporizar_passo()
