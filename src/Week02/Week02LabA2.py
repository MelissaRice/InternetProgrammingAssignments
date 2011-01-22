'''
Week2LabA2.py
last revised: 17 January 2011
author: Melissa Rice (UWNetID: mlrice)
purpose: quick test of urllib2 library
         assignment: write a program which reads a text file
         with a single URL on each line and attempts to save
         each to a file. 
'''

import urllib2

urlsFile = open('C:/A/eclipse/projects/InternetProgrammingLabs/src/Week02/urls.txt')
urls = urlsFile.readlines()
j = 0
for url in urls:
    j += 1
    urlObject = urllib2.urlopen(url)
    metadata = urlObject.info()
    urlAddress = urlObject.geturl()
    content = urlObject.readlines()
    print urlAddress
    print metadata
    content = ''.join(content)
    print content
    outFilename = "C:/A/eclipse/projects/InternetProgrammingLabs/src/Week02/url" + str(j) + ".html"
    outFile = open(outFilename,'w')
    outFile.write(urlAddress)
    outFile.write(str(metadata))
    outFile.write(content)
    outFile.close()


urlString = 'http://briandorsey.info/uwpython/week01/email_vm.py'
url = urllib2.urlopen(urlString)
metadata = url.info()
urlAddress = url.geturl()
content = url.readlines()
output = "The url object: %s " % url
output += "\n===> url address (url.geturl()): %s " % urlAddress 
output += "\n===> url metadata (url.info()): %s " % metadata
output += "\n===> url content: "
output += ''.join(content)
print output
outputFilename = 'C:/A/eclipse/projects/InternetProgrammingLabs/src/Week02/Week2LabA1-Output.txt'
outFile = open(outputFilename,'w')
outFile.write(output)
outFile.close()

''' Output of this code is:



'''









