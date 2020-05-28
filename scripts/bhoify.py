import re
import io

# script to act upon grepped and sorted content
# 1 loop through and add year sections and heads each time a year is found for the first time
# 2 make it bho syntax

# prescript tasks:
# 1 grep out the relevant lines
# 2 sort the lines on two keys a) the year b) title 
# sort -t"<" -k7,7 -df -k3 - in other words dictionary order for the second sort with a folding flag
# the input XML turns out not to be consistent so munging will have to be done first, before sorting

filename = ''
outfilename = ''

years = ["<awarded>1970</awarded>",  "<awarded>1971</awarded>", "<awarded>1972</awarded>", "<awarded>1973</awarded>", "<awarded>1974</awarded>", "<awarded>1975</awarded>", "<awarded>1976</awarded>", "<awarded>1977</awarded>", "<awarded>1978</awarded>", "<awarded>1979</awarded>", "<awarded>1980</awarded>", "<awarded>1981</awarded>", "<awarded>1982</awarded>", "<awarded>1983</awarded>", "<awarded>1984</awarded>", "<awarded>1985</awarded>", "<awarded>1986</awarded>", "<awarded>1987</awarded>", "<awarded>1988</awarded>", "<awarded>1989</awarded>", "<awarded>1990</awarded>", "<awarded>1991</awarded>", "<awarded>1992</awarded>", "<awarded>1993</awarded>", "<awarded>1994</awarded>", "<awarded>1995</awarded>", "<awarded>1996</awarded>", "<awarded>1997</awarded>", "<awarded>1998</awarded>", "<awarded>1999</awarded>", "<awarded>2000</awarded>", "<awarded>2001</awarded>", "<awarded>2002</awarded>", "<awarded>2003</awarded>", "<awarded>2004</awarded>", "<awarded>2005</awarded>", "<awarded>2006</awarded>", "<awarded>2007</awarded>", "<awarded>2008</awarded>", "<awarded>2009</awarded>", "<awarded>2010</awarded>", "<awarded>2011</awarded>", "<awarded>2012</awarded>", "<awarded>2013</awarded>",  "<awarded>2014</awarded>", "<awarded>2015</awarded>", "<awarded>2016</awarded>", "<awarded>2017</awarded>", "<awarded>2018</awarded>"]

metadata_term = '' #set the redundant metadata term for removal from the specific file, eg Historiography from Historiography, which becomes redundant by virtue of its position in the publication
metadata_term2 = '' #can be blank, used for variants of the above

i = 0
#define function to increment the para and section value
def number_paras(match):
    global i
    i += 1
    return "<para id=\"p"+str(i)+"\">"

i = 0
def number_sections(match):
    global i
    i += 1
    return "<section id=\"s"+str(i)+"\">"
  
with io.open(filename, "r", encoding="utf-8") as f:
    text = f.read()
    for year in years:
        text = re.sub('<row>(.*)'+str(year), '</section>\\n<section>\\n<head>'+str(year)+'</head>\\n<row>\\1'+str(year), text, 1)
        text = text.replace('<head><awarded>', '<head>')
        text = text.replace('</awarded></head>', '</head>')
    #delete the unwanted database elements: ID, type, created, teaser
    text = re.sub('<id>.+?</type>', '', text)
    text = re.sub('<created>.+?</teaser>', '', text)
    text = re.sub('<teaser>.+?</teaser>', '', text)# not all entries have created, it seems
    text = re.sub('<created>.+?</changed>', '', text)# not all created and changed in the same order?
    #delete the metadata term(s) for the specific file
    text = re.sub('<categories>'+str(metadata_term)+'</categories>', '<categories></categories>', text)
    text = re.sub('<categories>'+str(metadata_term)+';', '<categories>', text)
    text = re.sub(';'+str(metadata_term)+'</categories>', '</categories>', text)
    text = re.sub(';'+str(metadata_term)+';', ';', text)
    text = re.sub('<index>'+str(metadata_term)+'</index>', '<index></index>', text)
    text = re.sub('<index>'+str(metadata_term)+';', '<index>', text)
    text = re.sub(';'+str(metadata_term)+'</index>', '</index>', text)
    
    text = re.sub('<categories>'+str(metadata_term2)+'</categories>', '<categories></categories>', text)
    text = re.sub('<categories>'+str(metadata_term2)+';', '<categories>', text)                        
    text = re.sub(';'+str(metadata_term2)+'</categories>', '</categories>', text)                     
    text = re.sub(';'+str(metadata_term2)+';', ';', text)                                            
    text = re.sub('<index>'+str(metadata_term2)+'</index>', '<index></index>', text)                
    text = re.sub('<index>'+str(metadata_term2)+';', '<index>', text)                              
    text = re.sub(';'+str(metadata_term2)+'</index>', '</index>', text)                           
       
    #move everything first; then delete blank lines; then change the elements
    text = re.sub('<row>(.+)(<title>.+</title>)', '<row>\\2\\1', text)
    text = re.sub('</title>(.+)(<authors>.+</authors>)', '</title>\\2\\1', text)
    text = re.sub('</title>(.+)(<authors></authors>)', '</title>\\2\\1', text)#5 blank author elements
    text = re.sub('</degree>(.+)(<university>.+</department>)', '</degree>\\2\\1', text)
    text = re.sub('</department>(.+)(<supervisors>.*?</supervisors>)', '</department>\\2\\1', text)
    text = re.sub('</department>(.+)(<supervisors></supervisors>)', '</department>\\2\\1', text)#5000 blank supervisor elements
    #elements should now be in order
    #cleanup section:
    #add line breaks
    text = text.replace('</supervisors>', '</supervisors><br />\n')
    text = text.replace('</chronnumend>', '</chronnumend><br />\n')
    text = text.replace('</index>', '</index><br />\n')
    text = text.replace('</categories>', '</categories><br />\n')
    #spaces after ;
    text = text.replace(';', '; ')
    text = text.replace('  ', ' ')
    text = re.sub('([^.])</title>', '\\1.</title>', text)# add missing full stop after titles
    text = text.replace('<title>', '<emph type="i">')
    text = text.replace('</title>', '</emph>')
    text = text.replace('<authors>', ' ') #needs a space between title and author
    text = text.replace('</authors>', '<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
    text = text.replace('<awarded>', '<!-- <awarded>')
    text = text.replace('</awarded>', '</awarded>-->')
    text = text.replace('<awarded></awarded>', '')
    text = text.replace('<degree></degree>', '')
    text = text.replace('<university></university>', '')
    text = text.replace('<department></department>', '')
    text = text.replace('<supervisors></supervisors>', '')
    text = text.replace('<degree>', '')
    text = text.replace('</degree>', '')
    text = text.replace('<department>', '(')
    text = text.replace('</department>', ')')
    text = text.replace('<university>', ', ')
    text = text.replace('</university>', '. ')
    text = text.replace('</supervisors>', '')
    text = text.replace('<supervisors>', ' Supervised by ')
    text = text.replace('</awarded>-->,', '</awarded>-->')
    text = text.replace('  ', ' ')
    text = text.replace(') Supervised by', '). Supervised by')
    text = text.replace('<chronnum-range></chronnum-range><chronnum></chronnum><chronnumend></chronnumend><br />', '')
    text = text.replace('<chronnum-range>', '<!--<chronnum-range>')
    text = text.replace('</chronnum-range>', '</chronnum-range> -->')
    text = text.replace('<chronnum>', '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chronological coverage: ')
    text = text.replace('</chronnum><chronnumend>', '&ndash;')
    text = text.replace('</chronnumend>', '')
    text = text.replace('<index></index><br />', '')
    text = text.replace('<index>', '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Index terms: <emph type="i">')
    text = text.replace('</index>', '</emph>')
    text = text.replace('<categories></categories><br />', '')
    text = text.replace('<categories>', '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Categories: ')
    text = text.replace('</categories>', '')
    text = text.replace('<class>', '<!--<class>')
    text = text.replace('</persons>', '</persons>-->')
    text = text.replace('<row>', '<para>')
    text = text.replace('</row>', '</para>')
    text = re.sub('\n\n', '\n', text)
    text = re.sub('\n\n', '\n', text)
    text = re.sub(r'<para>', number_paras, text) # calls the function to renumber paras
    text = re.sub(r'<section>', number_sections, text) # calls the function to renumber sections

    f = io.open(outfilename, 'w', encoding="utf-8")
    f.write(text)
    f.close()

print("Metadata term is: \n\n"+metadata_term+". \n\nAre you sure?")# check because needs to be changed manually each time 



    
