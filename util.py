# parse user input
# return a list of selected numbers
def parseInput(raw_in):
    raw_in = raw_in + ' ' 
    id_sel = list()
    buff = ''
    for pos, item in enumerate(raw_in):
        if item != ' ':
            buff += item
            continue
        elif item == ' ':
            if '-' in buff:
                start = int(buff.split('-')[0])
                end = int(buff.split('-')[1])+1
                for n in range(start, end):
                    id_sel.append(str(n))
                buff = ''
            else:
                id_sel.append(buff)
                buff = ''
    return id_sel
