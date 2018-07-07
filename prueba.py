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
            z = "set id " +str(1)
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
            print("Finished Model")
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
            self.poblacion = []
            self.comandos = []
            self.set_commands()
            timer.log("Inicio")
            self.mode = "set"
            for contador in range(10):
                self.poblacion.append(Agente())   
            print("Created Default Config")
            #for contador in range(1):
                #timer.log("Setup")
                #p = Process(target=self.run,args=(contador,), name = str(contador))
                #p.start()
            self.run(0);
                

if __name__ == '__main__':
    timer = Timer()
    NetLogoInstance = netlogoComm()