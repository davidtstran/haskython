# David Tan Sang Tran 
# Haskython: Haskell and Python Conversion (Python Library)

###
#    Run 'python haskell_to_python.py' to use:
#        haskell_test.hs
#    Run 'python haskell_to_python.py file.hs' to use:
#        file.hs
###


import sys

HASKELL_FILE = "haskell_test.hs"
FUNCTION_DECLARATION = "::"
PARAMETER_DECLARATION = "->"
LIST_DELIMITER = ":"
LIST_RETURN = "xs"
NEW_LINE = "\n"


def main(haskellFile):
    '''
    Open haskell file haskell.hs
    Create new Python file haskell_haskython.py
    Converts haskell code to Python code
    Append Python code to new file
    '''
    curr_file = open(haskellFile, "r")
    new_file = open(f"{haskellFile[0:-3]}_haskython.py", "w")

    for line in haskellToPython(curr_file.readlines()):
        new_file.write(line)

    new_file.close()
    curr_file.close()

    return


def haskellToPython(lines):
    return_lines = []
    function_name = ""
    choice_count = 0
    for line in lines:
        if line == NEW_LINE:
            return_lines.append(line * 2)
        elif FUNCTION_DECLARATION in line:
            parseFD = parseFunctionDeclaration(line)
            function_name = parseFD.split(" ")[1]
            return_lines.append(parseFD)
            choice_count = 0 
        elif function_name in line: 
            parseC = parseChoices(line, choice_count)
            choice_count += 1
            return_lines.append(parseC)
    return_lines.append("\n")
    return return_lines


def parseFunctionDeclaration(line):
    return_line = "def "
    function_declaration = line.split(FUNCTION_DECLARATION)
    return_line += f"{function_declaration[0].strip()} ("
    parameter_declaration = function_declaration[1].split(PARAMETER_DECLARATION)
    for i in range(len(parameter_declaration) - 1):
        parameter = parameter_declaration[i].strip()
        if (parameter == "[Integer]"):
            return_line += f"integer_list{str(i)},"
        elif (parameter == "Integer"):
            return_line += f"integer{str(i)},"
    return_line += "):"

    return return_line


def parseChoices(line, count):
    return_line = "\n\t"
    split_line = line.split("=")
    parameters = split_line[0].split(" ")
    parameters.remove("")

    if (len(parameters) == 2): # function name + 1 param
        if (parameters[1]) == "[]":
            return_line += "if integer_list0 == []:"
        elif (parameters[1]) == "(x:xs)":
            return_line += "else:"
    elif (len(parameters) == 3): # name + 2 params
        if (parameters[1].isalpha() and parameters[2].isnumeric()):
            if count == 0:
                return_line += f"if integer1 == {parameters[2]}:"
            else:
                return_line += f"elif integer1 == {parameters[2]}:"
        elif (parameters[2].isalpha() and parameters[1].isnumeric()):
            if count == 0:
                return_line += f"if integer0 == {parameters[1]}:"
            else:
                return_line += f"elif integer0 == {parameters[1]}:"
        else: 
            return_line += "else:"

    return_line += "\n\t\t"
    return_type = split_line[1].strip()
    
    if return_type == "[]":
        return_line += "return []"
    elif return_type.isnumeric():
        return_line += f"return {return_type}"
    elif return_type in parameters:
        if return_type.isalpha():
            return_line += f"return integer{parameters.index(return_type)-1}"
        else:
            return_line += f"return integer_list{parameters.index(return_type)-1}"
    else:
       return_line += collectFunctionMethod(return_type, parameters)

    return return_line


def collectFunctionMethod(code, parameters):
    return_line = ""
    method_name = parameters[0]
    if LIST_RETURN in code:
        if f" {LIST_DELIMITER} " in code:
            split_list = code.split(f" {LIST_DELIMITER} ")
            return_line += "returnList = "
            return_line += f"[integer_list0[0]{split_list[0][1:]}]"
            return_line += "\n\t\t"
            return_line += f"returnList.extend({method_name}(integer_list0[1:]))"
            return_line += "\n\t\t"
            return_line += "return returnList"
            return return_line
        for op in ["+", "-", "/", "*"]:
            if op in code:
                return_line += "return "
                return_line += f"integer_list0[0] {op} "
                return_line += f"{method_name}(integer_list0[1:])"
                return return_line  
    else:
        return_line += "return "
        for i in code: 
            if i in parameters:
                return_line += f"integer{parameters.index(i)-1}"
            else:
                return_line += i
    if method_name in return_line:
        return_line = return_line.replace(f"{method_name} ", f"{method_name}(")
        return_line += ")"
    for i in range(1, len(parameters)):
        first_param = f"{method_name}(integer{i-1}"
        if first_param in return_line:
            return_line = return_line.replace(first_param, f"{first_param},")
        subseq_param = f", integer{i-1}"
        if subseq_param in return_line:
            return_line = return_line.replace(subseq_param, f"{subseq_param},")

    return return_line


if __name__ == "__main__":
    '''
    Run 'python haskell-to-python-py' to use:
        haskell-test.hs
    Run 'python haskell-to-python.py file.hs' to use:
        file.hs
    '''
    if (len(sys.argv) == 1):
        main(HASKELL_FILE)
    else:
        main(sys.argv[1])
