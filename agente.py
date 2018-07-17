from random import uniform
class Agente:

      def __init__(self,infection_rate = 4.3,initial_probability_of_death=0.548,initial_probability_of_chromatin_condensation=0.3,mNeptune_effectiveness=294.63,viral_reach=2.5,initial_infected_cell_percentage = 4.527,cell_density= 5.48,dead_cells = 0, live_condensed =0,live=0):
            self.infection_rate = infection_rate 
            self.initial_probability_of_death =initial_probability_of_death
            self.initial_probability_of_chromatin_condensation = initial_probability_of_chromatin_condensation
            self.mNeptune_effectiveness = mNeptune_effectiveness
            self.viral_reach = viral_reach
            self.initial_infected_cell_percentage = initial_infected_cell_percentage
            self.cell_density = cell_density
            self.dead_cells = dead_cells
            self.live_condensed = live_condensed
            self.live = live
            self.error = uniform(0,1)