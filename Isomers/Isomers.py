def molecularFormula(formula):

    formula = ''.join([i for i in formula if not i.isdigit()])

    truth_table = []
    for i in range(len(formula)):
        truth_table.append(formula[i].isupper())

    if all(truth_table):
        return dict((x, formula.count(x)) for x in set(formula))
    else:
        def getindices(s):
            return [i for i, c in enumerate(s) if c.isupper()]

        uppercase = getindices(formula)

        new_list = []
        for i in range(len(uppercase) - 1):
            new_list.append(formula[uppercase[i]:uppercase[i + 1]])

        new_list.append(formula[uppercase[-1]:])
        return dict((x, new_list.count(x)) for x in set(new_list))

def isomers(formula1, formula2):
    if molecularFormula(formula1) == molecularFormula(formula2):
        return True
    else:
        return False