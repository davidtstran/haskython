# David Tan Sang Tran 
# Haskython: Haskell and Python Conversion (Python Library)

###
#    Run 'python python_to_haskell.py' to use:
#        python_test.py
#    Run 'python python_to_haskell.py file.py' to use:
#        file.py
###


import sys

PYTHON_FILE = "python_test.py"


def main(pythonFile):
    '''
    Open python file python.py
    Create new haskell file python_haskython.hs
    Converts Python code to haskell code
    Append haskell code to new file
    '''
    curr_file = open(pythonFile, "r")
    new_file = open(f"{pythonFile[0:-3]}_haskython.hs", "w")

    for line in pythonToHaskell(curr_file.readlines()):
        new_file.write(line)

    new_file.close()
    curr_file.close()

    return


def pythonToHaskell(lines):
    return_lines = []
    # TODO
    return return_lines


if __name__ == "__main__":
    '''
    Run 'python python_to_haskell.py' to use:
        python_test.py
    Run 'python python_to_haskell.py file.py' to use:
        file.py
    '''
    if (len(sys.argv) == 1):
        main(PYTHON_FILE)
    else:
        main(sys.argv[1])
