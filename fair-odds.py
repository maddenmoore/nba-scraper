import sys

if __name__ == "__main__":
    prob = float(sys.argv[1])
    if prob == 1:
        print("-1000000")
    elif prob > 0.5:
        print(int(-1 * 100 * prob/(1 - prob)))
    else:
        print("+" + str(int((100 - (prob) * 100) / (prob))))