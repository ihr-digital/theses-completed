import re
import io

#make minor changes to input file so sorting works correctly

filename = ''
outfilename = ''

with io.open(filename, "r", encoding="utf-8") as f:
    text = f.read()
    text = re.sub("\t", "", text)#remove tabs first
    text = re.sub("<row>(.+?)<title>(.+?)</title>", "<row><title>\\2</title>\\1", text)
    text = re.sub("</title>(.+?)<awarded>(.*?)</awarded>", "</title><awarded>\\2</awarded>\\1", text)
    
    f = io.open(outfilename, 'w', encoding="utf-8")
    f.write(text)
    f.close()

print("Now do this: sort -t\"<\" -k5,5 -df -k3 "+outfilename)



