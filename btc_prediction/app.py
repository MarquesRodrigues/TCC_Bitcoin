from tkinter import *
import time
import main

root = Tk()


class Funcs():

    def onclick(self):

        variation = main.variation()

        if(variation > 0):
            self.lb_variacao.config(
                text="Haverá uma variação positiva de %.2f" % variation + "%")
        elif(variation < 0):
            self.lb_variacao.config(
                text="Haverá uma variação negativa de %.2f" % variation + "%")
        else:
            self.lb_variacao.config(
                text="Não haverá variação daqui a 1 hora")

    def onclick2(self):
        exit()


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
        self.root.configure(background='#14145a')
        self.root.geometry("800x600")
        self.root.resizable(True, True)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=5, bg="#dcdcdc", highlightbackground="#f7931a",
                             highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def botoes(self):
        self.bt_gerarModelo = Button(
            self.frame_1, text="PREVER", command=self.onclick)
        self.bt_gerarModelo.place(
            relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)
        self.bt_exit = Button(self.frame_1, text="FECHAR",
                              command=self.onclick2)
        self.bt_exit.place(
            relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)

    def labels(self):
        self.lb_titulo = Label(self.frame_1, text="Ferramenta para prever de forma aproximada" +
                               " a variação do preço do Bitcoin para a próxima hora")
        self.lb_titulo.place(relx=0.14, rely=0.00,
                             relwidth=0.7, relheight=0.07)

        self.lb_variacao = Label(self.frame_1)
        self.lb_variacao.place(relx=0.14, rely=0.3,
                               relwidth=0.7, relheight=0.1)


Application()
