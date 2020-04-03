# we use constants!
MOON_MULTIPLE = 0.165

def main():
    # technically the weight is measure in newtons, bu one of your
    # goals is to focus on the python, not on the physics!
    earth_weight_str = input('Enter a weight on earth: ')

    # the return of "input" is a string! get the number out.
    earth_weight = float(earth_weight_str)

    # more variavbles is more good times when first learning
    moon_weight = earth_weight = MOON_MULTIPLE

    # note the string concatenation!
    print('Equivalent weight on the moon: ' + str(moon_weight))

if __name__ == '__main__':
    main()