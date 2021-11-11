import numpy as np

def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t)**2)

if __name__ == "__main__":
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    print(sum_squares_error(np.array(y), np.array(t)))

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    print(sum_squares_error(np.array(y), np.array(t)))