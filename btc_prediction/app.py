from tkinter import * 
import time
import main



# variacao = main.get_variacao

root = Tk()      

class Funcs():

    def onclick(self):
        variation = main.variation()
        if(variation >= 0):
            self.lb_variacao.config(text="Houve uma variação positiva de %.2f" % variation + "%")
        else:          
            self.lb_variacao.config(text="Houve uma variação negativa de %.2f" % variation + "%")
    

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.labels()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Bitcoin Prediction")
        self.root.configure(background = '#14145a')
        self.root.geometry("790x500")
        self.root.resizable(True,True)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 10, bg = "#dcdcdc", highlightbackground="#f7931a",
                            highlightthickness=2)
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.96)     
    def botoes(self):
        self.bt_gerarModelo = Button(self.frame_1, text = "PREVER", command = self.onclick)
        self.bt_gerarModelo.place(relx = 0.4, rely = 0.2, relwidth = 0.2, relheight = 0.1)
    def labels(self):
        self.lb_titulo = Label(self.frame_1, text = "Ferramenta para prever de forma aproximada" +
                                " a variação do preço do Bitcoin para a próxima hora")
        self.lb_titulo.place(relx = 0.07, rely = 0.01, relwidth = 0.9, relheight = 0.1) 
        self.lb_variacao = Label(self.frame_1) 
        self.lb_variacao.place(relx = 0.07, rely = 0.5, relwidth = 0.9, relheight = 0.1)

Application()