pdfToSpeech
===========
Simple cgi + python + command line utils for a mac os server (uc's webserver)
to allow uploading of a file and conversion of it to an audio m4a file. 
Originally planned to use festival, but the mac os "say" command just sounds
alot better (sorry floss!). 


Prerequisites:
=============
Webserver
cgi-bin
darwin with "say" command


HowTo:
======
go to your web visible root directory
git clone https://github.com/leecarraher/pdfToSpeech.git
cd cgi-bin/
chmod a+x pdftotext
chmod a+x upload.py

thats it!


License:
========
None! There may be some grey area with using mac os speech in this way. I know
festival speech engines have different rules regarding these things, but since
i am not distributing the speech engine, and it is accessed through web service
calls, hosting it should be fine, but you didn't here it from me.
