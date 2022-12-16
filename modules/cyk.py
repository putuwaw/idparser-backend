from modules.cnf import get_set_of_production

TRIANGULAR_TABLE = {}

def is_accepted(inputString):
    global TRIANGULAR_TABLE
    TRIANGULAR_TABLE.clear()
    prodRules = get_set_of_production()
    temp = inputString.lower().split(" ")
    inputString = temp
    for i in range(1,len(inputString)+1):
        for j in range(i, len(inputString)+1):
            TRIANGULAR_TABLE[(i,j)] = []
    for i in reversed(range(1, len(inputString)+1)):
        for j in range(1, i+1):
            if (j == j + len(inputString) - i):
                tempList = []
                for key, value in prodRules.items():
                    for val in value:
                        if (val == inputString[j-1] and key not in tempList):
                            tempList.append(key)
                TRIANGULAR_TABLE[(j, j + len(inputString) - i)] = tempList
            else:
                tempList = []
                resultList = []
                for k in range(len(inputString) - i):
                    first = TRIANGULAR_TABLE[(j,j+k)]
                    second = TRIANGULAR_TABLE[(j+k+1,j+len(inputString) - i)]
                    for fi in first:
                        for se in second:
                            if (fi + " " + se not in tempList):
                                tempList.append(fi + " " + se)
                for key, value in prodRules.items():
                    for val in value:
                        if (val in tempList and key not in resultList):
                            resultList.append(key)
                TRIANGULAR_TABLE[(j,j+len(inputString) - i)] = resultList
    if "K" in TRIANGULAR_TABLE[(1, len(inputString))]:
        return True
    else:
        return False