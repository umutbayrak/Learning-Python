def headsOfState(location):
    import datetime


    with open(location, 'r') as fin:
        presidents = fin.readlines()


    pres_list= [line.strip().split() for line in presidents]


    for element in pres_list:
        if element[2][:1].isdigit():
            element[0] = element[0] + ' ' + element[1]
        elif element[3][:1].isdigit():
            element[0] = element[0] + ' ' + element[1] + ' ' + element[2]
        elif element[4][:1].isdigit():
            element[0] = element[0] + ' ' + element[1] + ' ' + element[2] + ' ' + element[3]


    for i in range(0, 3):
        for element in pres_list:
            if element[1][:1].isdigit() == False:
                element.remove(element[1])

    pres_dict = {element[0]:element[1:] for element in pres_list}

    for key, value in pres_dict.items():
        for i in range(len(value)):
            value[i] = value[i].split('/')
            x = value[i][0]
            value[i][0] = int(value[i][2])
            value[i][1] = int(value[i][1])
            value[i][2] = int(x)


    dict2 = {k:[None, None, None, None] for k, v in pres_dict.items()}


    for key, value in pres_dict.items():
        for i in range(len(value)):
            value[i] = datetime.date(value[i][0], value[i][1], value[i][2])


    for key, value in pres_dict.items():
        for i in range(0,4):
            if len(value) < 4:
                value.append(None)

    print(pres_dict)

    # Gives the last version
    for key, value in pres_dict.items():
        pres_dict[key] = tuple(pres_dict[key])

    return pres_dict


