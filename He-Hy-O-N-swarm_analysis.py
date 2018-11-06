#Imports data files collected from previous bolsig runs
#Converts the data files to arrays for data analysis
#and saves them to a database in csv format for use in Bokeh
#plots the data in graphs if required.

import numpy as np
import re
import matplotlib.pyplot as plt
import pandas as pd

def set_plot_params():
    ### Plot axes and labels ###
    plt.title('Townsend ionization coefficient against reduced electric field')
    plt.xlabel("Reduced Electric Field, (E/N)")
    plt.ylabel("Townsend ionization coefficient / N (m^2)")
    plt.xscale('log')
    plt.yscale('log') 
    plt.show()
    
def save_array_to_csv():
    # Save the array to a single database in csv format
    d={}
    for y in range(0,15626):
        d[y]= pd.Series(C[y])
        
    df = pd.DataFrame(d)
    df.to_csv("foo10.csv")  

#convert files to arrays
def convert_files_to_arrays():
    C= np.zeros((15626,40)) #array that holds on data points
    for z in range(0,3):    #nitrogen loop
        nitrogen = 0.001*z  
        nitrogen = round(nitrogen,3)
        for y in range(0,5):    #oxygen loop
            oxygen = 0.001*y    
            oxygen = round(oxygen,3)
            for x in range(0,25):   #hydrogen loop
                
                hydrogen=0.001*x
                hydrogen= round(hydrogen,3)
                
                
                lines = []                  # Declare an empty list named "lines"
                with open (r"C:\Users\Knowhow\Desktop\Bolsig\He\Helium_{a}_{b}_{c}.txt".format(a=hydrogen,b=oxygen,c=nitrogen), 'rt') as in_file:  # Open Helium_raw.txt for reading of text data.
                    for line in in_file:  # For each line of text in in_file, where the data is named "line",
                        lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.
                       
                err_occur = []                         # The list where we will store results.
                pattern = re.compile("trials", re.IGNORECASE)  # Compile a case-insensitive regex pattern.
                try:                              # Try to:
                    with open (r"C:\Users\Knowhow\Desktop\Bolsig\He\Helium_{a}_{b}_{c}.txt".format(a=hydrogen,b=oxygen,c=nitrogen), 'rt') as in_file:        # open file for reading text.
                        for linenum, line in enumerate(in_file):        # Keep track of line numbers.
                            if pattern.search(line) != None:          # If substring search finds a match,
                                err_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
                        for linenum, line in err_occur:              # Iterate over the list of tuples, and
                            start_data = linenum+2 # print results as "Line [linenum]: [line]".
                except FileNotFoundError:                   # If log file not found,
                    print("Log file not found.")                # print an error message. 	
                
                err_occur = []                         # The list where we will store results.
                pattern = re.compile("energy", re.IGNORECASE)  # Compile a case-insensitive regex pattern.
                try:                              # Try to:
                    with open (r"C:\Users\Knowhow\Desktop\Bolsig\He\Helium_{a}_{b}_{c}.txt".format(a=hydrogen,b=oxygen,c=nitrogen), 'rt') as in_file:        # open file for reading text.
                        for linenum, line in enumerate(in_file):        # Keep track of line numbers.
                            if pattern.search(line) != None:          # If substring search finds a match,
                                err_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
                        for linenum, line in err_occur:              # Iterate over the list of tuples, and
                            end_data = linenum+1 # print results as "Line [linenum]: [line]".
                            
                except FileNotFoundError:                   # If log file not found,
                    print("Log file not found.")                # print an error message. 	
                
                
                end_data = linenum
                
                file = open(r"C:\Users\Knowhow\Desktop\Bolsig\He\temp_{a}_{b}_{c}.txt".format(a=hydrogen,b=oxygen,c=nitrogen),"w") 
                for i in range(start_data,end_data):      
                    file.write(lines[i]) 
                    file.write("\n")  
                file.close()  
                loadeddata = np.loadtxt(r"C:\Users\Knowhow\Desktop\Bolsig\He\temp_{a}_{b}_{c}.txt".format(a=hydrogen,b=oxygen,c=nitrogen))
                
                # assign individual variables to arrays
                run_num = loadeddata[:,0]
                e_field = loadeddata[:,1]
                mean_energy = loadeddata[:,2]
                mobility = loadeddata[:,3]
                diffusion = loadeddata[:,4]
                energy_mobility = loadeddata[:,5]
                energy_diff_coeff = loadeddata[:,6]
                total_coll_freq = loadeddata[:,7]
                momentum_freq = loadeddata[:,8]
                total_ionize_freq = loadeddata[:,9]
                townsend_coeff = loadeddata[:,10]
                power = loadeddata[:,11]
                elastic_power_loss = loadeddata[:,12]
                inelastic_power_loss = loadeddata[:,13]
                growth_power = loadeddata[:,14]
                max_energy = loadeddata[:,15]
                num_iter = loadeddata[:,16]
                num_grid_trials = loadeddata[:,17]
                
                
                plt.plot(e_field,mobility)  #plot the chosen variables
                
                # Assigns all variables to large arroy
                update_x = x*1
                update_y = y*1
                update_z = z*1
                update_total = 625*update_z+update_y*25+update_x+1
                update_total = int(update_total)
                C[0]=e_field
                C[update_total] = max_energy

    set_plot_params()     #sets axes and labels for plot
    
    save_array_to_csv()     #save the database to a csv file

convert_files_to_arrays()
    






