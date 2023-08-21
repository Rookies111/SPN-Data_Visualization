import pandas as pd
class CovidData:
    # Constructor
    def __init__(self, filename=None):
        # attribute to read data from csv file
        self.newCase = pd.read_csv(filename, usecols=['new_case'])
        self.totalCase = pd.read_csv(filename, usecols=['total_case'])
        self.newRecovered = pd.read_csv(filename, usecols=['new_recovered'])
        self.totalRecovered = pd.read_csv(filename, usecols=['total_recovered'])
        self.newDeath = pd.read_csv(filename, usecols=['new_death'])
        self.totalDeath = pd.read_csv(filename, usecols=['total_death'])
    # methods to get new cases, total cases
    def get_newCases(self):
        newCase = ['New Case']
        newCase.extend(["Week"] + [i for i in range(1, len(self.newCase)+1)])
        newCase.extend(["People"] + [self.newCase.iloc[i, 0] for i in range(len(self.newCase))])
        return newCase
    def get_totalCases(self):
        totalCase = ['total_case']
        totalCase.extend(["Week"] + [i for i in range(1, len(self.totalCase)+1)])
        totalCase.extend(["People"] + [self.totalCase.iloc[i, 0] for i in range(len(self.totalCase))])
        return totalCase
    # methods to get new recovered, total recovered
    def get_newRecovered(self):
        newRecovered = ['new_recovered']
        newRecovered.extend(["Week"] + [i for i in range(1, len(self.totalCase)+1)])
        for i in range(len(self.newRecovered)):
            temp = (self.newRecovered.iloc[i, 0])
            newRecovered.append(temp)
        return newRecovered
    def get_totalRecovered(self):
        totalRecovered = ['total_recovered']
        for i in range(len(self.totalRecovered)):
            temp = (self.totalRecovered.iloc[i, 0])
            totalRecovered.append(temp)
        return totalRecovered
    # methods to get new death, total death
    def get_newDeath(self):
        newDeath = ['new_death']
        for i in range(len(self.newDeath)):
            temp = (self.newDeath.iloc[i, 0])
            newDeath.append(temp)
        return newDeath
    def get_totalDeath(self):
        totalDeath = ['total_death']
        for i in range(len(self.totalDeath)):
            temp = (self.totalDeath.iloc[i, 0])
            totalDeath.append(temp)
        return totalDeath

# just for testing
data = CovidData('timeline-cases-all.csv')
print(data.get_newCases())
print(data.get_totalCases())
print(data.get_newRecovered())
print(data.get_totalRecovered())
print(data.get_newDeath())
print(data.get_totalDeath())