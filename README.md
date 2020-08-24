# theses-completed

## Licence

This content is licensed under a Creative Commons licence: CC-BY-NC-SA. You can re-use this data for non-commercial reasons, with attribution, and provided you share any outputs on a similar licence. https://creativecommons.org/licenses/by-nc-sa/3.0/.

## Summary

This repository contains data files from British History Online's theses completed volumes
* *Theses Completed, 1901-1970* https://www.british-history.ac.uk/no-series/theses-1901-70
* *Theses Completed, 1970-2014* https://www.british-history.ac.uk/no-series/theses-1970-2014


## What is in this repo
* ```bho-syntax-1901-1970/```: the BHO XML for the volume on our website, this was rekeyed from print
* ```bho-syntax-1901-1970/```: the BHO XML for the volume on our website, this was generated from the database output
* ```database-output-1970-2014/```: theses complete information from the History Online database, output as XML
* ```flat-files-1970-2004/```: files organised as 1 thesis per line to enable grep-like tools on any string of interest 
* ```scripts```: two Python scripts used to convert the flattened files 1970-2004 into BHO XML, included so users can see how the BHO syntax was created and modify the scripts

## List of categories in the file 
Note that some contain more than one place, eg Europe and Asia. On BHO such theses would appear more than once in our listings, preferring ease of finding over ease of counting.


_Periods_
- 1000-1 BC
- 12th Century
- 13th Century
- 14th Century
- 15th Century
- 16th Century
- 16th-17th Century
- 17th Century
- 18th Century
- 18th-19th Century
- 19th Century
- 20th Century
- 21st Century
- 500-1000
- AD 1-500
- Ancient
- Ancient history

 _Places_
- Africa
- Asia and Middle East
- Australasia and Pacific
- Britain and Ireland
- Europe
- Latin America and West Indies
- North America
- World

_History type_
- Administrative history
- Agriculture
- Archaeology
- Art and Architecture
- Business history
- Byzantine history
- Cultural history
- Ecclesiastical and religious history
- Economic history
- Education
- Environmental history
- Ethnic and migration history
- Gender and Women
- Historical geography
- Historiography
- Imperial and colonial
- Intellectual history
- International history
- Legal history
- Local and regional history
- Local history
- Medicine
- Medieval
- Military and naval history
- Military/naval history
- Modern
- Oral history
- Philosophy of history
- Political history
- Population
- Pre-1000 BC
- Science and technology
- Social history
- Social sciences
- Transport
- Urban history



## Some example data searches using grep

To work with the data you will need a local copy on your machine. If you have the free Git program installed you can either use a graphical program (such as GitKraken) or the command line to _clone_ the data. From the command line you would run:

```git clone https://github.com/ihr-digital/theses-completed/```

If you don't want to do this, click on the green 'Code' button on the page above and choose 'Download ZIP'.

Grep and other line-orientated tools will work best in the ```flat-files-1970-2004/``` directory. An introductory guide to grep can be found on the Programming Historian website: https://programminghistorian.org/en/lessons/research-data-with-unix

Here are a few example uses with the theses data. These are intended to be run from inside the ```flat-files-1970-2004/``` directory.

*Find all theses tagged as 'International History' or 'world'*

``` grep -Ei "<categories[^<]+(International history|world)" *.txt```

*Find all theses tagged as 'Britain and Ireland' and awarded in 2001*

``` grep -Ei "<categories[^<]+Britain and Ireland" *.txt | grep "<awarded>2001"```

*Find all theses tagged as 'Britain and Ireland' which mention the cold war* 

``` grep -Ei "<categories[^<]+Britain and Ireland" *.txt | grep -Ei "cold[ -]war"```

*Count by year awarded theses which mention the cold war* 

``` grep -Ei "cold[ -]war" *.txt | grep -Eo "<awarded>[^<]+<" | sort | uniq -c```
