import math
class processing_element (object):
    def sigmoid(self, sumofvalues):
        '''
        Executes sigmoid function with the formula (1/(1+e^-sumofvalues)).
        Takes in a parameter called sumofvalues.
        '''
        result = 1/(1+math.exp(-sumofvalues))  
        return result
    def compute_output(self, weight_list, pattern_list):
        '''
        Executes dot product for each item in weight_list and pattern_list
        & sum up the results.
        '''
        output = 0
        # iterate through each item in weight list
        for i in range(len(weight_list)):  
            # multiply items in weight list and pattern list for the same index
            # sum the results
            output += weight_list[i]*pattern_list[i] 
        # perform sigmoid function on the summed result
        return self.sigmoid(output)
        
class network (object):
    def __init__(self):
        self.matrix = []  # matrix to store weights
        self.load_weights()  # loads the 'weights.in' file to update self.matrix
    
    def load_weights(self):
        '''
        Reads the input file "weights.in" and updates self.matrix which stores weights in a matrix.
        '''
        #file = input("Name of weight file: ")
        file = 'weights.in'
        file_handler = open(file, 'r') # opens file in read mode
        # columns = self.input_neurons, rows = self.output_neurons
        self.input_neurons, self.output_neurons = [int(x) for x in file_handler.readline().rstrip().split()] 
        # first line stripped, separated to store the values in col and row variables respectively
        for each_line in file_handler: # iterate each line in the file. 
        # First line is already read, so it won't be repeated. 
            self.matrix.append([float(x) for x in each_line.rstrip().split()])
            # strip and split each line and store it in rows. Append each row to the matrix.
        file_handler.close() # close the file after reading
        
    def feedforward(self, list_pattern):
        '''
        Computes output for each processing element and returns a list of network output. 
        Intake parameter is list of patterns. 
        '''
        neuron = processing_element() # makes a processing element object 
        network_output = []  # list for all outputs of processing elements. Currently empty.
        for i in range(self.output_neurons):
        # iterates for each PE
            network_output.append(neuron.compute_output(self.matrix[i],list_pattern))
            # Computes output for each PE and append the results to network_output
        return network_output
        # network_output = [(neuron.compute_output(self.matrix[x],list_pattern)) for x in range(self.output_neurons)]
      

def main():
    pattern_file = open('patterns.in','r')  #opens file in read mode
    test_network = network() # creats a network object
    output_file = open('outputs.out','w')
    num_patterns, num_values_per_pattern, max_value = [float(x) for x in pattern_file.readline().rstrip().split()]
    # reads the first line in 'patterns.in' and assign each value respectively to the variables below    
    output_file.write(str(int(num_patterns)) + '\n') 
    # write number of files in the first line of the output file
    for each_line in pattern_file:
    # Iterate for each line in the pattern_file        
        network_output = test_network.feedforward([float(x)/max_value for x in each_line.rstrip().split()])
        # execute feedforward function for current line in the pattern file
        # parameter: converts each line into a list of integers
        output_file.write(' '.join([str(x) for x in network_output])+'\n')
        # writes the network_output list in string format into the output file
    pattern_file.close()
    output_file.close()
    # close both files
main()