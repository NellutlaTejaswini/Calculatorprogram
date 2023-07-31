# Calculatorprogram
import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a 3x3 numpy array
    matrix = np.array(numbers).reshape(3, 3)
    
    # Calculate mean, variance, standard deviation, max, min, and sum along rows, columns, and flattened matrix
    mean = [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)]
    variance = [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)]
    std_dev = [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)]
    maximum = [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)]
    minimum = [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)]
    summation = [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
    
    # Create and return the dictionary
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': maximum,
        'min': minimum,
        'sum': summation
    }
    
    return result
