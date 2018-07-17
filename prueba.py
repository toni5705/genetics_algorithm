import os,sys
import pyNetLogo
from multiprocessing import Process
from datetime import datetime
from agente import Agente
from random import randint
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
            netlogo.repeat_command('go', 120)
            print("Finished Model process" + str(index))
            #timer.log("Final Thread")


    #Método para elegir la aptidud del nuevo agente a partir de los padres, este escoge los atributos intercalados de uno en uno 
    def cruce1(self,agente1,agente2):
        hijo = Agente()
        if randint(0,1) >0:
            padre1 = agente1
            padre2 = agente2
        else:
            padre1 = agente2
            padre2 = agente1
        
        hijo.infection_rate = padre1.infection_rate
        hijo.initial_probability_of_death = padre2.initial_probability_of_death
        hijo.initial_probability_of_chromatin_condensation = padre1.initial_probability_of_chromatin_condensation
        hijo.mNeptune_effectiveness = padre2.mNeptune_effectiveness
        hijo.viral_reach = padre1.viral_reach
        hijo.initial_infected_cell_percentage = padre2.initial_infected_cell_percentage
        hijo.cell_density = padre1.cell_density
        return hijo
    #Método para elegir la aptidud del nuevo agente a partir de los padres, este escoge los atributos intercalados cada 2
    def cruce2(self,agente1,agente2):
        hijo = Agente()
        if randint(0,1) >0:
            padre1 = agente1
            padre2 = agente2
        else:
            padre1 = agente2
            padre2 = agente1
        
        hijo.infection_rate = padre1.infection_rate
        hijo.initial_probability_of_death = padre1.initial_probability_of_death
        hijo.initial_probability_of_chromatin_condensation = padre2.initial_probability_of_chromatin_condensation
        hijo.mNeptune_effectiveness = padre2.mNeptune_effectiveness
        hijo.viral_reach = padre1.viral_reach
        hijo.initial_infected_cell_percentage = padre1.initial_infected_cell_percentage
        hijo.cell_density = padre2.cell_density
        return hijo

    #Método para elegir la aptidud del nuevo agente a partir de los padres, este escoge los atributos aleatoriamente
    def cruce3(self,agente1,agente2):
        hijo = Agente()
        if randint(0,1) >0:
            padre1 = agente1
            padre2 = agente2
        else:
            padre1 = agente2
            padre2 = agente1
        
        if randint(0,1) >0:
            hijo.infection_rate = padre1.infection_rate
        else:
            hijo.infection_rate = padre2.infection_rate

        if randint(0,1) >0:
            hijo.initial_probability_of_death = padre1.initial_probability_of_death
        else:
            hijo.initial_probability_of_death = padre2.initial_probability_of_death

        if randint(0,1) >0:
            hijo.initial_probability_of_chromatin_condensation = padre1.initial_probability_of_chromatin_condensation
        else:
            hijo.initial_probability_of_chromatin_condensation = padre2.initial_probability_of_chromatin_condensation

        if randint(0,1) >0:
            hijo.mNeptune_effectiveness = padre1.mNeptune_effectiveness
        else:
            hijo.mNeptune_effectiveness = padre2.mNeptune_effectiveness    
        
        if randint(0,1) >0:
            hijo.viral_reach = padre1.viral_reach
        else:
            hijo.viral_reach = padre2.viral_reach  
        
        if randint(0,1) >0:
            hijo.initial_infected_cell_percentage = padre1.initial_infected_cell_percentage
        else:
            hijo.initial_infected_cell_percentage = padre2.initial_infected_cell_percentage

        if randint(0,1) >0:
            hijo.cell_density = padre1.cell_density
        else:
            hijo.cell_density = padre2.cell_density
        return hijo


    def set_commands(self):
        self.comandos.append("set infection-rate ")
        self.comandos.append("set initial-probability-of-death ")
        self.comandos.append("set initial-probability-of-chromatin-condensation ")
        self.comandos.append("set mNeptune-effectiveness ")
        self.comandos.append("set viral-reach ")
        self.comandos.append("set initial-infected-cell-percentage ")
        self.comandos.append("set cell-density ")



    def nueva_generación(self):
        agente1 = Agente()
        agente1.error = 1000000000000
        agente2 = Agente()
        agente2.error = 1000000000000
        indice_superior = len(self.poblacion) - 1
        limite = len(self.poblacion)/2
        for contador in range(int(limite)):
            print("Individuo")
            print(self.poblacion[contador].__dict__)

            if self.poblacion[contador].error < agente1.error:
                agente1 = self.poblacion[contador]
            if self.poblacion[indice_superior].error < agente2.error:
                agente2 = self.poblacion[indice_superior]
            indice_superior -= 1
        print("*******************************************El individuo más alto de la generación**********************************************************")
        if agente1.error < agente2.error:
            print(agente1.__dict__)
        else:
            print(agente2.__dict__)
        for contador in range(len(self.poblacion)):
            self.poblacion.pop()
        for contador in range(self.numero_procesos):
            cruce = randint(0,2)
            if cruce == 0:
                self.poblacion.append(self.cruce1(agente1, agente2))
            else:
                if cruce == 1:
                    self.poblacion.append(self.cruce2(agente1, agente2))
                else:
                    self.poblacion.append(self.cruce3(agente1, agente2))

    def mutar_poblacion(self):
        porcentaje_cambio = 0.10
        for contador in range(len(self.poblacion)):
            if randint(0,100) >95:
                atributo = randint(0,6)
                if atributo == 0:
                    if randint(0,1) >0:
                        self.poblacion[contador].infection_rate += (self.poblacion[contador].infection_rate * porcentaje_cambio)
                        if self.poblacion[contador].infection_rate > 15:
                            self.poblacion[contador].infection_rate = 15
                    else:
                        self.poblacion[contador].infection_rate -= (self.poblacion[contador].infection_rate * porcentaje_cambio)
                        if self.poblacion[contador].infection_rate < 0:
                            self.poblacion[contador].infection_rate = 0
                elif atributo == 1:
                    if randint(0,1) >0:
                        self.poblacion[contador].initial_probability_of_death += (self.poblacion[contador].initial_probability_of_death * porcentaje_cambio)
                        if self.poblacion[contador].initial_probability_of_death > 2:
                            self.poblacion[contador].initial_probability_of_death = 2
                    else:
                        self.poblacion[contador].initial_probability_of_death -= (self.poblacion[contador].initial_probability_of_death * porcentaje_cambio)
                        if self.poblacion[contador].initial_probability_of_death < 0:
                            self.poblacion[contador].initial_probability_of_death = 0
                elif atributo == 2:
                    if randint(0,1) >0:
                        self.poblacion[contador].initial_probability_of_chromatin_condensation += (self.poblacion[contador].initial_probability_of_chromatin_condensation * porcentaje_cambio)
                        if self.poblacion[contador].initial_probability_of_chromatin_condensation > 3:
                            self.poblacion[contador].initial_probability_of_chromatin_condensation = 3
                    else:
                        self.poblacion[contador].initial_probability_of_chromatin_condensation -= (self.poblacion[contador].initial_probability_of_chromatin_condensation * porcentaje_cambio)
                        if self.poblacion[contador].initial_probability_of_chromatin_condensation < 0:
                            self.poblacion[contador].initial_probability_of_chromatin_condensation = 0                                             
                elif atributo == 3:
                    if randint(0,1) >0:
                        self.poblacion[contador].mNeptune_effectiveness += (self.poblacion[contador].mNeptune_effectiveness * porcentaje_cambio)
                        if self.poblacion[contador].mNeptune_effectiveness > 400:
                            self.poblacion[contador].mNeptune_effectiveness = 400
                    else:
                        self.poblacion[contador].mNeptune_effectiveness -= (self.poblacion[contador].mNeptune_effectiveness * porcentaje_cambio)
                        if self.poblacion[contador].mNeptune_effectiveness < 0:
                            self.poblacion[contador].mNeptune_effectiveness = 0                        
                elif atributo == 4:
                    if randint(0,1) >0:
                        self.poblacion[contador].viral_reach += (self.poblacion[contador].viral_reach * porcentaje_cambio)
                        if self.poblacion[contador].viral_reach > 3:
                            self.poblacion[contador].viral_reach = 3
                    else:
                        self.poblacion[contador].viral_reach -= (self.poblacion[contador].viral_reach * porcentaje_cambio)
                        if self.poblacion[contador].viral_reach < 0:
                            self.poblacion[contador].viral_reach = 0
                elif atributo == 5:
                    if randint(0,1) >0:
                        self.poblacion[contador].initial_infected_cell_percentage += (self.poblacion[contador].initial_infected_cell_percentage * porcentaje_cambio)
                        if self.poblacion[contador].initial_infected_cell_percentage > 100:
                            self.poblacion[contador].initial_infected_cell_percentage = 100
                    else:
                        self.poblacion[contador].initial_infected_cell_percentage -= (self.poblacion[contador].initial_infected_cell_percentage * porcentaje_cambio)
                        if self.poblacion[contador].initial_infected_cell_percentage < 0:
                            self.poblacion[contador].initial_infected_cell_percentage = 0
                else:
                    if randint(0,1) >0:
                        self.poblacion[contador].cell_density += (self.poblacion[contador].cell_density * porcentaje_cambio)
                        if self.poblacion[contador].cell_density > 20:
                            self.poblacion[contador].cell_density = 20
                    else:
                        self.poblacion[contador].cell_density -= (self.poblacion[contador].cell_density * porcentaje_cambio)
                        if self.poblacion[contador].cell_density < 0:
                            self.poblacion[contador].cell_density = 0           


    def __init__(self):
        self.generaciones = 15
        self.numero_procesos = 15
        self.poblacion = []
        self.comandos = []
        self.procesos = []
        self.set_commands()
        timer.log("Inicio")
        self.mode = "set"
        for contador in range(self.numero_procesos):
            self.poblacion.append(Agente())
        self.mutar_poblacion()
        for iteraciones in range(self.generaciones):
            print("Generación número: " + str(iteraciones))
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
                #print("Resultados de proceso " + str(contador))
                self.poblacion[contador].dead_cells = float(numeros[1])
                self.poblacion[contador].live_condensed = float(numeros[0])
                self.poblacion[contador].live = float(numeros[2])
                #print(self.poblacion[contador].__dict__)
                file.close()
                os.remove(name)
                self.poblacion[contador].calculate_error()
            self.nueva_generación()
            self.mutar_poblacion()
            for contador in range(self.numero_procesos):
                self.procesos.pop()




        print("Todos los procesos terminaron")
                #metodos combinacion y mutación

if __name__ == '__main__':
    timer = Timer()
    NetLogoInstance = netlogoComm()

# *************Aca se ejecuta el método de calcular error**********************
'''*********Valores teóricos
    dead cells = 68.1157972
    LiveCondensed = 11.1009198
    Live = 20.7832829'''