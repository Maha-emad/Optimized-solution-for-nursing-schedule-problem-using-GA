#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import prettytable as prettytable
import random as rnd
from tkinter import *
from tkinter import ttk
import random
POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1

data = 0

_Nurses = [['Mai Khaled', 0,'Null'], ['Rahma Mohamed', 0,'Null'], ['Huda Ahmed', 1, 'm'], ['Toka Khaled', 0,'Null'],
                        ['Mona Ali', 0,'Null'], ['Rana Mohsen', 0,'Null'],
                        ['Nada Alaa', 0,'Null'], ['Rehab Emad', 0,'Null'], ['Reem Ibrahim', 0,'Null'], ['Maria Zaky', 0,'Null'],
                        ['Marwa Ahmed', 1, 'e'], ['Yasmeen Ali', 0,'Null'],
                        ['Nashwa Ali', 0,'Null'], ['Nadia Mohsen', 1, 'n'], ['Neven Mohamed', 0,'Null'], ['Somia Adel', 0,'Null'],
                        ['Omnia Salah', 0,'Null'], ['Magda Hany', 0,'Null'],
                        ['Mayada Mahdy', 0,'Null'], ['Gomana Mmdouh', 0,'Null'], ['Gehad Selim', 0,'Null'], ['Dalia Amgad', 0,'Null'],
                        ['Menna Fouad', 0,'Null'], ['Menna Foua', 0,'Null']]

_Shifts = ['e', 'o', 'm', 'n']
_Skills = [4, 1, 2, 3]

# %%

class Data:
    def __init__(self):
        self._nurses = _Nurses
        self.shifts = _Shifts
        self.skills = _Skills

    def get_Shifts(self):
        self.shifts.sort(key=self.shifts[0].__eq__)
        return self.shifts

    def get_skills(self):
        self.skills.sort(key=self.skills[0].__eq__)
        return self.skills

    def get_nurses(self):
        return self._nurses


# %%

class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())

    def get_schedules(self): return self._schedules


# %%

class Schedule:
    def __init__(self):

        self._data = data
        self._schedule = []
        self.nurse_data = []
        self.day = []
        self.skill = self._data.get_skills()
        self.shift = self._data.get_Shifts()
        self.countShift = 0
        self.countSkill = 0
        self.max_patient = 150
        self.max_patientForNurse = 10
        self.sumPatient = 0
        self.numbOfConflicts = 0
        self.z = []
        self.fitness = -1
        self._isFitnessChanged = True

    def get_numbOfConflicts(self):
        return self.numbOfConflicts

    def initialize(self):
        for i in range(0, len(self._data.get_nurses())):
            if self._data.get_nurses()[i][1] == 1:
                self.shift = [self._data.get_nurses()[i][2], self._data.get_nurses()[i][2],
                              self._data.get_nurses()[i][2], 'o']
            else:
                self.shift = self._data.get_Shifts()
            self.countShift = 0
            self.countSkill = self.countSkill + 1
            if self.countSkill == 5:
                self.skill = self._data.get_skills()
                self.countSkill = 1
            self.nurse_data = []
            for j in range(0, 7):
                self.day = []
                self.day.append(self.shift[self.countShift])
                self.countShift = self.countShift + 1
                if self.countShift == 4:
                    self.countShift = 0
                self.day.append(self.skill[self.countSkill - 1])
                if self.day[0] == 'o':
                    self.day.append(0)
                else:
                    self.day.append(rnd.randrange(1, self.max_patientForNurse))
                self.nurse_data.append(self.day)
                if (self.nurse_data[j - 1][0] == 'n' and self.nurse_data[j][0] == 'm'):
                    self.nurse_data[j][0] = 'e'
            self._schedule.append(self.nurse_data)
        return self._schedule

    def calculate_fitness(self, pop, num):
        self.s = 0
        self.sumPatient = 0
        self.sumO = 0
        self.patient = 0
        self.x = {}
        self.y = []
        self.n = 0
        for i in range(0, num):
            self.s = population[i]
            for j in range(0, len(self._data.get_nurses())):
                for k in range(0, 7):
                    if self.s[j][k][0] == 'o':
                        self.sumO = self.sumO + 1
                    if self.s[j][k - 1][0] == 'n' and self.s[j][k][0] == 'm':
                        self.numbOfConflicts = self.numbOfConflicts + 1
                    if len(self.s[j][k]) > 3:
                        self.numbOfConflicts = self.numbOfConflicts + 1
                    if self._data.get_nurses()[i][1] == 1:
                        self.pref = self._data.get_nurses()[i][2]
                        if k == 6:
                            break
                        elif self.s[j][k][0] != self.pref or self.s[j][k + 1][0] != self.pref:
                            self.numbOfConflicts = self.numbOfConflicts + 1

                if self.sumO > 2:
                    self.numbOfConflicts = self.numbOfConflicts + 1
            for j in range(0, 7):
                for k in range(0, len(self._data.get_nurses())):
                    self.patient = self.s[k][j][2]
                    self.sumPatient = self.sumPatient + self.patient
                if self.sumPatient > self.max_patient:
                    self.numbOfConflicts = self.numbOfConflicts + 1
            self.fitness = 1 / ((1.0 * self.numbOfConflicts + 1))
            self.x.update({self.fitness: i})
            self.y.append(self.fitness)
        self.y.sort(reverse=True)
        for i in range(0, num):
            self.n = self.x.get(self.y[i])
            self.z.append(population[self.n])
        return self.z


# %%

class GeneticAlgorithm:
    def __init__(self):
        self.__data = data

    def evolve(self, population):
        return self.mutate_population(self.crossover_population(population))

    def crossover_population(self, pop):
        crossover_pop = Population(0).get_schedules()
        for i in range(0, NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.append(pop[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self.select_tournament_population(pop)
            schedule2 = self.select_tournament_population(pop)
            crossover_pop.append(self.crossover_schedule(schedule1, schedule2))
            i = i + 1
        return crossover_pop

    def crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(self.__data.get_nurses())):
            if rnd.random() > 0.5:
                crossoverSchedule[i] = schedule1[i]
            else:
                crossoverSchedule[i] = schedule2[i]
        return crossoverSchedule

    def select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop[rnd.randrange(0, POPULATION_SIZE)])
            i = i + 1
        tournament_pop = Schedule().calculate_fitness(tournament_pop, TOURNAMENT_SELECTION_SIZE)
        return tournament_pop[0]

    def mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self.mutate_schedule(population[i])
        return population

    def mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(self.__data.get_nurses())):
            if rnd.random() < MUTATION_RATE:
                mutateSchedule[i] = schedule[i]
        return mutateSchedule


# %%


ws  = Tk()
ws.config(background='white')

#nurses = []

ws.title('nursing schedule')
ws.geometry('2000x500')
nursing_schedule = Frame(ws)
nursing_schedule.pack()
my_table = ttk.Treeview(nursing_schedule)

#set = ttk.Treeview(ws)
my_table.pack()

my_table['columns'] = ('Nurses', 'Saturday', 'Sunday', 'Monday', 'Tuesday','Wednsday','Thursday','Friday')
my_table.column("#0", width=0, stretch=NO)
my_table.column("Nurses", anchor=CENTER, width=200)
my_table.column("Saturday", anchor=CENTER, width=200)
my_table.column("Sunday", anchor=CENTER, width=200)
my_table.column("Monday", anchor=CENTER, width=200)
my_table.column("Tuesday", anchor=CENTER, width=200)
my_table.column("Wednsday", anchor=CENTER, width=200)
my_table.column("Thursday", anchor=CENTER, width=200)
my_table.column("Friday", anchor=CENTER, width=200)

my_table.heading("#0", text="", anchor=CENTER)
my_table.heading("Nurses", text="Nurses", anchor=CENTER)
my_table.heading("Saturday", text="Saturday", anchor=CENTER)
my_table.heading("Sunday", text="Sunday", anchor=CENTER)
my_table.heading("Monday", text="Monday", anchor=CENTER)
my_table.heading("Tuesday", text="Tuesday", anchor=CENTER)
my_table.heading("Wednsday", text="Wednsday", anchor=CENTER)
my_table.heading("Thursday", text="Thursday", anchor=CENTER)
my_table.heading("Friday", text="Friday", anchor=CENTER)


data = Data()
population = Population(POPULATION_SIZE).get_schedules()
population = Schedule().calculate_fitness(population, POPULATION_SIZE)
generationNumber = 0
geneticAlgorithm = GeneticAlgorithm()
while generationNumber < 6:
    population = geneticAlgorithm.evolve(population)
    population = Schedule().calculate_fitness(population, POPULATION_SIZE)
    generationNumber = generationNumber + 1
print(population[0])

nurses = data.get_nurses()
for i in range(0,len(nurses)):
   my_table.insert(parent='', index='end', iid=i, text='',
               value=(str(nurses[i]),str(population[0][i][0]) ,
                      str(population[0][i][1]), str(population[0][i][2]),
                      str(population[0][i][3]),str(population[0][i][4]),
                      str(population[0][i][5]),str(population[0][i][6])))


Input_frame = Frame(ws)
Input_frame.pack()

name_Nurses = Label(Input_frame, text="name of nurse")
name_Nurses.grid(row=0, column=0)

preferance = Label(Input_frame, text="preferance")
preferance.grid(row=0, column=1)

shift = Label(Input_frame, text="shift")
shift.grid(row=0, column=2)


name_Nurses_entry = Entry(Input_frame)
name_Nurses_entry.grid(row=1, column=0)

preferance_entry = Entry(Input_frame)
preferance_entry.grid(row=1, column=1)

shift_entry = Entry(Input_frame)
shift_entry.grid(row=1, column=2)


def input_record():
    global data
    global population
    global geneticAlgorithm
    _Nurses.append([name_Nurses_entry.get(),int(preferance_entry.get()),shift_entry.get()])
    for i in my_table.get_children():
        my_table.delete(i)
    #random.shuffle(_Nurses)
    data = Data()
    population = Population(POPULATION_SIZE).get_schedules()
    population = Schedule().calculate_fitness(population, POPULATION_SIZE)
    generationNumber = 0
    geneticAlgorithm = GeneticAlgorithm()
    while generationNumber < 6:
        population = geneticAlgorithm.evolve(population)
        population = Schedule().calculate_fitness(population, POPULATION_SIZE)
        generationNumber = generationNumber + 1
    print(population[0])

    nurses = data.get_nurses()
    for i in range(0,len(nurses)):
       my_table.insert(parent='', index='end', iid=i, text='',
                   value=(str(nurses[i]),str(population[0][i][0]) ,
                          str(population[0][i][1]), str(population[0][i][2]),
                          str(population[0][i][3]),str(population[0][i][4]),
                          str(population[0][i][5]),str(population[0][i][6])))



# button
Input_button = Button(ws, text="Input Record", command=input_record)

Input_button.pack()

ws.mainloop()


# In[ ]:




