import re
open_file = open('combo.txt','r')
save_hits = open('hits.txt','a')
reading = open_file.readlines()
Regex = re.compile(r'Italy')
for i in reading:
    Check = Regex.search(i)
    
    if Check != None:
        save_hits.write(i)

open_file.close()
save_hits.close()