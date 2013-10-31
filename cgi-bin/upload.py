#!/usr/bin/python
import os
import commands
import cgi, cgitb
num_concurrent = 10
cgitb.enable()
print "Content-Type: text/html"
print
print "loading..."
f = open("concurrent",'r')
id = (int(f.readline())+1)%num_concurrent
f.close()
f = open("concurrent",'w')
f.write(str(id))
f.close()
form = cgi.FieldStorage()
filedata = form["upload"]
voice = form.getvalue("voice")
rate = 200
try:
    rate = int(form.getvalue("rate"))
except ValueError:
    rate = 200
    print "<p/>Please Specify an integer for WPM<p/>"

if filedata.file:
	#print "<br/>conv"+str(id)+".pdf"
	with file("conv"+str(id)+".pdf","w") as outfile:
		outfile.write(filedata.file.read())
	#print "<br/>./pdftotext conv"+str(id)+".pdf conv"+str(id)+".txt"
	print os.system("./pdftotext conv"+str(id)+".pdf conv"+str(id)+".txt")
	#print "<br/>rm conv"+str(id)+".pdf"
	print os.system("rm conv"+str(id)+".pdf")
	#print "<br/>iconv -f utf8 -t utf8 -c conv"+str(id)+".txt > convx"+str(id)+".txt"
	print os.system("iconv -f utf8 -t utf8 -c conv"+str(id)+".txt > convx"+str(id)+".txt")
	#print "<br/>rm conv"+str(id)+".txt"
	print os.system("rm conv"+str(id)+".txt")
	print "<br/>say -o output"+str(id)+".m4a -f convx"+str(id)+".txt -v" + str(voice) + " -r "+str(rate)
	print os.system("say -o output"+str(id)+".m4a -f convx"+str(id)+".txt -v "+str(voice) + " -r "+str(rate))

	#print "<br/>mv output"+str(id)+".m4a ../"
	print os.system("mv output"+str(id)+".m4a ../")
	#print "<br/>rm convx"+str(id)+".txt"
	print os.system("rm convx"+str(id)+".txt")
	
	
	print "<br/>done! <a href=\"../output"+str(id)+".m4a\"> output.m4a</a>"
	f = open("filesconverted",'r')
	cn = int(f.readline())+1
	print "<p/>"+str(cn)+" Files Converted!"
	print "<br/> <a href=\"https://github.com/leecarraher/pdfToSpeech\">Fork It!</a>"
	f.close()
	outfile.close()
	f = open("filesconverted",'w')
	f.write(str(cn))
	f.close()
	



