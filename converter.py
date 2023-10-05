def convertToDuration(cell):
    # Split `00h 00m 00s` string into three components
    cell = cell.split(" ")

    h = 0
    m = 0
    s = 0


    # Remove strings for each components
    for i in cell:
        if 'h' in i:
            h = int(i.replace('h', ''))

        if 'm' in i:
            m = int(i.replace('m', ''))
            
        if 's' in i:
            s = int(i.replace('s', ''))

        else:
            pass


    return f"{h:02d}:{m:02d}:{s:02d}"