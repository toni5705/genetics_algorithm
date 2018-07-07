import os
import pyNetLogo
from multiprocessing import Process
from datetime import datetime

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

timer = Timer()


class netlogoComm:
    
    def run(self,name):
            timer.log("Start Thread")
            print("set id " +str(name))
            netlogo = pyNetLogo.NetLogoLink(gui=False)
            netlogo.load_model(r'simulacion.nlogo')
            z = "set id " +str(1)
            for x, y in zip(self.params, self.values):
                netlogo.command(self.mode+" "+str(x)+" "+str(y))
            netlogo.command('setup')
            netlogo.repeat_command('go', 5)
            print("Finished Model")
            timer.log("Final Thread")

    def __init__(self):  
            timer.log("Inicio")
            self.mode = "set"
            self.params = ["infection-rate","initial-probability-of-death","initial-probability-of-chromatin-condensation","mNeptune-effectiveness","viral-reach","initial-infected-cell-percentage","cell-density"]
            self.values = [4.3,0.548,0.3,294.63,2.5,4.527,5.48]
            print("Created Default Config")
            for contador in range(1):
                timer.log("Setup")
                p = Process(target=self.run,args=(contador,), name = str(contador))
                p.start()
            timer.log("Final")
                

if __name__ == '__main__':
    timer = Timer()
    NetLogoInstance = netlogoComm()
