import os,sys
import pyNetLogo
from multiprocessing import Process
from datetime import datetime
from agente import Agente

class Timer:
	"""
		Tracker using time
	"""
	start = datetime.now()

	def log(self, desc=None):
		difference = datetime.now() - self.start
		if(desc):
			print("** {} - {}".format(difference, desc))
		else:
			print("** {}".format(difference))

	def stop(self):
		self.log(desc="Finished")
		self.start = datetime.now()

	def reset_timer(self):
		self.start = datetime.now()
class netlogoComm:
    
    def run(self,index):
            #timer.log("Start Thread")
            print("set id " +str(index))
            netlogo = pyNetLogo.NetLogoLink(gui=False)
            netlogo.load_model(r'simulacion.nlogo')
            netlogo.command("set id " +str(index))
            netlogo.command(self.comandos[0]+str(self.poblacion[index].infection_rate))
            netlogo.command(self.comandos[1]+str(self.poblacion[index].initial_probability_of_death))
            netlogo.command(self.comandos[2]+str(self.poblacion[index].initial_probability_of_chromatin_condensation))
            netlogo.command(self.comandos[3]+str(self.poblacion[index].mNeptune_effectiveness))
            netlogo.command(self.comandos[4]+str(self.poblacion[index].viral_reach))
            netlogo.command(self.comandos[5]+str(self.poblacion[index].initial_infected_cell_percentage))
            netlogo.command(self.comandos[6]+str(self.poblacion[index].cell_density))
            netlogo.command('setup')
            #timer.log("Final process")
            netlogo.repeat_command('go', 5)
            print("Finished Model process" + str(index))
            #timer.log("Final Thread")

    def set_commands(self):
        self.comandos.append("set infection-rate ")
        self.comandos.append("set initial-probability-of-death ")
        self.comandos.append("set initial-probability-of-chromatin-condensation ")
        self.comandos.append("set mNeptune-effectiveness ")
        self.comandos.append("set viral-reach ")
        self.comandos.append("set initial-infected-cell-percentage ")
        self.comandos.append("set cell-density ")

    def __init__(self):
        self.numero_procesos = 3
        self.poblacion = []
        self.comandos = []
        self.procesos = []
        self.set_commands()
        timer.log("Inicio")
        self.mode = "set"
        for contador in range(self.numero_procesos):
            self.poblacion.append(Agente())   
        print("Created Default Config")
        for contador in range(self.numero_procesos):
            timer.log("Setup")
            p = Process(target=self.run,args=(contador,), name = str(contador))
            self.procesos.append(p)
            p.start()
        for p in self.procesos:
            p.join()
        for contador in range(self.numero_procesos):
            name = str(contador) + ".txt"
            file = open(name,"r+")
            numeros = file.read().split()
            print("Resultados de proceso " + str(contador))
            self.poblacion[contador].dead_cells = float(numeros[0])
            self.poblacion[contador].live_condensed = float(numeros[1])
            self.poblacion[contador].live = float(numeros[2])
            print(self.poblacion[contador].__dict__)
            file.close()
            #os.remove("0.txt")





        print("Todos los procesos terminaron")
                #metodos combinacion y mutación

if __name__ == '__main__':
    timer = Timer()
    NetLogoInstance = netlogoComm()