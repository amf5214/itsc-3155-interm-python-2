from numpy import random
import numpy as np

if __name__ == "__main__":

    values = random.rand(10)
    print(f"Random Numbers: {values}")
    print(f"Mean: {np.mean(values)}, Median: {np.median(values)}, Standard Deviation: {np.std(values)}")

