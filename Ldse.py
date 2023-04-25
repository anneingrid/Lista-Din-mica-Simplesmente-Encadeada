from No import No


class Ldse:
    def __init__(self):
        self.prim=self.ult=None
        self.quant=0

    def inserir_inicio(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1

    def inserir_fim(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,self.prim)
        self.quant+=1
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info)
            aux = aux.prox

    def remover_inicio(self):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant-=1

    def remover_fim(self):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            aux=self.prim
            for i in range(self.quant-2):
                aux=aux.prox
            aux.prox = None
            self.ult = aux     
        self.quant-=1

    
    def remover(self,valor):
        if self.prim.info == valor:
            self.remover_inicio()
        elif self.ult.info ==valor:
            
            self.remover_fim()
        else:
            
            ant = None
            atual = self.prim
            while atual!=None and atual.info!=valor:
                ant = atual
                atual = atual.prox
            if atual==None:
                print('Não está na lista!')
            else:
                ant.prox = atual.prox                    
                self.quant-=1
        
    # def inserir_apos(self, valor1, valor2):
    #     for i in range(self.quant):
    #         if valor2==self.ult.info:
    #             print('OI')
    #             self.inserir_fim(valor1)
    #         elif valor2
                

    #     # self.quant+=1                 
            
    
'''    def remover_fim(self):
        if self.quant==1:
            self.prim = self.ult = None
        else:
            aux=self.prim
            while aux.prox!=self.ult:
                aux=aux.prox
            aux.prox = None
            self.ult = aux     
        self.quant-=1'''
    # Opção com while ^ 