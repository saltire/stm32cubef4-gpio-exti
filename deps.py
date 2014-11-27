from xml.etree import ElementTree

proj = ElementTree.parse('../EWARM/Project.ewp')

incs, srcs, objs = ['../Inc'], ['../Src'], []

for opt in proj.iterfind('.//option'):
    if opt.find('name').text == 'CCIncludePath2':
        for state in opt.iterfind('state'):
            inc = '/'.join(state.text.split('\\')[1:])
            if inc not in incs:
                incs.append(inc)

for file in proj.iterfind('.//file/name'):
    if file.text[-2:] in ['.c', '.s']:
        src = '/'.join(file.text.split('\\')[1:-1])
        if src and src not in srcs:
            srcs.append(src)
        objs.append(file.text.split('\\')[-1][:-1] + 'o')


def replace_lines(lines, startline, newlines):
    start = lines.index(startline) + 1
    end = start + lines[start:].index('')
    return lines[:start] + newlines + lines[end:]


with open('Makefile', 'r') as makefile:
    lines = makefile.read().splitlines()

    lines = replace_lines(lines, 'INC = \\', ['\t-I' + inc + ' \\' for inc in incs])
    lines = replace_lines(lines, 'SRC = \\', ['\t' + src + ' \\' for src in srcs])
    lines = replace_lines(lines, 'OBJ = \\', ['\tbuild/' + obj + ' \\' for obj in objs])

with open('Makefile', 'w') as makefile:
    makefile.write('\n'.join(lines))
