def keyboardInput(caption, datatype, errormessage, defaultvalue=None):
    value = None
    isErrorInput = True
    while isErrorInput:
        try:
            value = input(caption)
            if value == "":
                if defaultvalue is not None:
                    value = defaultvalue
                else:
                    value = datatype(value)
            else:
                value = datatype(value)
        except ValueError:
            print(errormessage)
        else:
            isErrorInput = False
    return value

# This code will get executed only if you type "python userinput.py" in the terminal
# This code will not get executed if you run "python functionspartone.py" in the terminal

if __name__ == '__main__':
    principle = keyboardInput("principle amount: ", int, "principle amount must be Integer")
    period = keyboardInput("period in years: ", int, "period must be integer")
    rate = keyboardInput("rate in percentage: ", float, "rate must be float")
    interest = (principle * period * rate) / 100

    print("interest amount:", interest)
