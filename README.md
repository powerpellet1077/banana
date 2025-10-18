# banana <img src="smolnana.png" id="banana"></img>
This is a program made to make uploading files and videos not a hassle.

This program is planning to support <a href="https://www.dropbox.com/">DropBox</a>, <a href="https://catbox.moe/">Catbox/Litterbox</a>, <a href="https://uguu.se/">Uguu/Pomf</a>, and <a href="https://filebin.net/">Filebin</a>. (currently this only supports catbox/litterbox and filebin but feel free to change that with a pr)
<br>IMPORTANT NOTICE: This program <u>heavily</u> relies on file sharing services to function, if any of these change or stop functioning, please open a pr, issue or fork if you want.


### usage:
To declare keys or userhashes, you can use the -k command to set the key for the service provided. (most services I am using will not require or need a userhash/api key so you can skip this if you want)

``banana -k MY_USERHASH -s cb``

once the userhash is declared, the program will automatically use it for that service. To actually upload a file, use the -f flag and declare a path (absolute or relative)

``banana -f sick_ass_file.txt``

you can also choose a service with -s and following with the abbreviation for the selected service, (in this case, catbox would be cb)

``banana -f sick_ass_file.txt -s cb``

You can also declare the time for temporary file sharing services (limited to only litterbox at the moment) and will automaticially default to one hour. The possible values for this flag are 1h, 12h, 24h and 72h.

``banana -f sick_ass_file.txt -s lb -t 24h``

As of now, banana supports only Catbox, Litterbox and Filebin. (cb, lb and fb respectively)

If you do not declare a service with -s, banana will automatically choose one for you, going in order of priority and file-specific services to services supporting different types of files and applications. 
Catbox and litterbox restrict against the following types of files:
 - exe/scr
 - cpl
 - doc
 - jar

Keep in mind that Catbox is limited to files of 200MB and Litterbox is limited to files of 1GB.

Filebin only restricts executable files (at least from my limited research as I found no other people had this issue :P)

If you are using the windows (multi-tabbed) terminal, then just using ctrl+click on the link should make it easier to share.


For compiling you will need these dependencies:
 - Pyinstaller
 - Loguru + Requests (these can both be installed via requirements.txt)
 - Git (or just download the zip)

First, clone or download the project: 

```
git clone https://github.com/powerpellet1077/banana.git
cd banana
```

Then, compile with pyinstaller:

```
pyinstaller --noconfirm --onefile --console --icon "banana.ico" --name "banana" --add-data "core;core"  "banana.py" 
```

Then if everything worked out, you should have your binary in ``banana/dist``

```
cd dist
banana
```

If you got a response similar to this:

```
banana.py/47|2025-10-18T12:53:03.659121-0700|[ERROR] please provide a value
```

Then the compilation was successful!

Thank you for using my program and good luck with trying to figure out how to use it (i am not a good teacher :P)
