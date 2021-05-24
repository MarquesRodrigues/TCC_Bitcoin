from tkinter import *
import model
import time

root = Tk()

curret_time = time.strftime('%H:00:00')

class Funcs():

    def preview(self):

        variation = model.prediction()

        if(variation > 0):
            self.lb_variation.config(
                text="Haverá uma variação positiva de %.2f" % variation + "%")
        elif(variation < 0):
            self.lb_variation.config(
                text="Haverá uma variação negativa de %.2f" % variation + "%")
        else:
            self.lb_variation.config(
                text="Não haverá variação daqui a 1 hora")
        
        self.lb_hour = Label(self.frame, text="Intevalo da previsão: " + curret_time)
        self.lb_hour.place(relx=0.11, rely=0.15, relwidth=0.8, relheight=0.07)

    def exit_program(self):
        exit()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.screen()
        self.screen_frames()
        self.labels()
        self.button()
        root.mainloop()

    def screen(self):
        self.root.title("Bitcoin Prediction")
        self.root.configure(background='#14145a')
        self.root.geometry("800x600")
        self.root.resizable(True, True)

    def screen_frames(self):
        self.frame = Frame(self.root, bd=5, bg="#dcdcdc", highlightbackground="#f7931a",
                           highlightthickness=2)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def button(self):
        self.bt_createModel = Button(
            self.frame, text="PREVER", command=self.preview)
        self.bt_createModel.place(
            relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)
        self.bt_exit = Button(self.frame, text="FECHAR",
                              command=self.exit_program)
        self.bt_exit.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)

    def labels(self):
        self.lb_label = Label(self.frame, text="Ferramenta para prever de forma aproximada" +
                              " a variação do preço do Bitcoin para a próxima hora")
        self.lb_label.place(relx=0.11, rely=0.1, relwidth=0.8, relheight=0.07)
        self.lb_variation = Label(self.frame)
        self.lb_variation.place(relx=0.14, rely=0.45,
                                relwidth=0.7, relheight=0.1)


Application()
