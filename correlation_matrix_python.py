# This program creates a correlation matrix from data stored in a csv file.
# It then saves the correlation matrix as a csv file.

# The data file must be in columns of numbers - no column labels, etc.
# Each column is a data series, X0, X1, X2, etc.

# This data must be saved as a csv file (e.g. use "Save As" in Excel and choose csv format).
# It must be saved in the same folder as this program.
# See the file correlation_data_example.csv for reference.

# In the next line, replace correlation_data_example.csv with the filename of your data:
data_filename = 'AllCorrelation.csv'

# In the next line, replace correlation_matrix with the filename you wish to save as:
output_filename = 'all_correlation.csv'

# The next lines import the necessary package to create the correlation analysis:
import scipy.stats as sps
import numpy as np

data = np.genfromtxt(data_filename,delimiter = ',')

# If there are errors importing the data, you can also copy it in as follows:
# e.g. data = [[737.4776314, 34, 65],
#              [869.2063792, 57, 73],
#              [1033.705248, 59, 100],
#              ...
#              [737.5129466, 66, 49]]
# (Compare this example with the file correlation_data_example.csv)

# This line creates a variable to store whether you want Pearson or Spearman correlation.
# Initially it is set to zero, since you have not yet made your decision.
correlation_type = 0

while correlation_type not in [1,2]:
    
    # The next line asks you whether you want Pearson or Spearman correlation:        
    correlation_type = int(input("Do you want to use Pearson [1] or Spearman [2] correlation? "))
    
    # The next lines calculate, store and print the correlation matrix...
    # ... taking account of whether you have chosen Pearson correlation...
    if correlation_type == 1:
        correlation_matrix = np.corrcoef(data.T)
        print(correlation_matrix)
    
    # ... or Spearman correlation:
    elif correlation_type == 2:
        correlation_matrix, pvalue_matrix = sps.spearmanr(data)
        print(correlation_matrix)
        
    # And the next line tells you what to do again, if you didn't get it the first time.
    else:
        print("You need to choose 1 or 2... It shouldn't be too difficult...")
        # You now get sent back to the line "while correlation_type not in [1,2]:" to try again...

# correlation_matrix[i,j] is the correlation between the series Xi and Xj.

# The next line saves the correlation matrix as a csv file:
np.savetxt(output_filename,correlation_matrix,delimiter=',')