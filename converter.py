import re





def convertToDuration(cell):
    hr = 0
    min = 0
    sec = 0

    hr_matched = re.search('insert regex', cell)
    if hr:
        hr = int(hr_matched.group(1))

    min_matched = re.search('insert regex', cell)
    if min:
        min = int(min_matched.group(1))

    sec_matched = re.search('insert regex', cell)
    if sec:
        sec = int(sec_matched.group(1))

    # duration_in_sec = (hr * 60 * 60) + (min * 60) + (sec)

    output = f"{hr}:{min}:{sec}"

    return output