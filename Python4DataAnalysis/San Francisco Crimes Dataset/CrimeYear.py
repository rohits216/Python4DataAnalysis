#Crimes by year 2003 - 2015
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class CrimeYear:
    
    def __init__(self, data,larceny,assault,drug,vehicle,vandalism,burglary):
        self.data=data
        self.larceny=larceny
        self.assault=assault
        self.drug=drug
        self.vehicle=vehicle
        self.vandalism=vandalism
        self.burglary=burglary
    
    def getYvalues(self):
        y0 = self.larceny.groupby('Year').size().get_values()
        y1 = self.assault.groupby('Year').size().get_values()
        y2 = self.drug.groupby('Year').size().get_values()
        y3 = self.vehicle.groupby('Year').size().get_values()
        y4 = self.vandalism.groupby('Year').size().get_values()
        y5 = self.burglary.groupby('Year').size().get_values()
        return y0,y1,y2,y3,y4,y5
    
    def PlotCrimeYear(self):
        sns.set_style("darkgrid")

        years =self. data.groupby('Year').size().keys()
        occursByYear = self.data.groupby('Year').size().get_values()

        # Linear plot for all crimes
        ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
        ax1.plot(years, occursByYear, 'ro-', linewidth=2)

        ax1.set_title ('All Crimes', fontsize=20)

        start, end = ax1.get_xlim()
        ax1.xaxis.set_ticks(np.arange(start, end, 1))
        # ensure that ticks are only at the bottom and left parts of the plot
        ax1.get_xaxis().tick_bottom()
        ax1.get_yaxis().tick_left()

        # Linear normalized plot for 6 top crimes
        ax2 = plt.subplot2grid((3,3), (1,0), colspan=3, rowspan=2)

        y = np.empty([6,13])
        y[0],y[1],y[2],y[3],y[4],y[5]=self.getYvalues()

        crimes = ['Larceny/theft', 'Assault', 'Drug', 'Vehicle', 'Vandalism', 'Burglary']
        color_sequence = ['#1f77b4', '#ff7f0e', '#2ca02c','#d62728', '#9467bd', '#8c564b']
        h=[None]*6
        
        
        for i in range(0,6):
            h[i] = ax2.plot(years, y[i],'o-', color=color_sequence[i], lw=2)

        ax2.set_ylabel("Crime occurences by year")
    
        start, end = ax2.get_xlim()  
        ax2.xaxis.set_ticks(np.arange(start, end+2, 1))        
        
        ax2.legend((item[0] for item in h), crimes, 
                bbox_to_anchor=(0.87, 1), loc=2, borderaxespad=0., frameon=False)

        
        ax1.set_title("San Franciso Crime Occurence by Year", x=0.5, y=1, fontsize=30)
                    
        plt.show()
        
        
        plt.figure(2)
        sns.set_style("darkgrid")
        yearMonth = self.data.groupby(['Year','Month']).size()
        ax = yearMonth.plot(lw=2)
        plt.title('San Franciso Crimes Trend by Month&Year', fontsize=24)
        plt.show()