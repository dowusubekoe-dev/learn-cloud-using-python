### Learn Python

Resource to Learn
https://diagrams.mingrammar.com/docs/getting-started/examples

How to run the code
$ python diagram.py

#### Accept user input
Use either the **input** function or **prompt** function
```py
    name = input('Please enter your name: ')
```
```py
    prompt = 'Please enter your name: \n'
    name = input(prompt)
```

#### Comments
Is used to add notes to the program
E.g.
```py
    # compute the percentage of the hour that has elasped
    percentage = (minute *100)/60
```

#### Exception handling using Try and Except
E.g
```py
    inp = input('Enter Fahrenheit Temperature:')
    try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0/9.0
    print(cel)
    except:
    print('Please enter a number')
```

#### Functions
Python uses the **def** statement to create functions.
E.g.
```py
    def functionName (argument):
```

