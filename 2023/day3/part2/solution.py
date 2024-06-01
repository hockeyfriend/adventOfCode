def get_advc_file_content(filename):
    with open(filename, 'r') as f:
        content = f.read().splitlines()
    
    return content

def find_all(p, s):
    '''Yields all the positions of the patter p in the string s'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1) # i+1 is the new start value
        
lines = get_advc_file_content('puzzle.txt')

for line in lines:
    # Try to find all * symbol
    indx = line.find('*')
    
    if indx == -1: # no symbol found -> skip line
        continue

    for char in line:
        