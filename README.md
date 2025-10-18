# banana <img src="smolnana.png" id="banana"></img>
<hr>
This is a program made to make uploading files and videos not a hassle.

This program is planning to support <a href="https://www.dropbox.com/">DropBox</a>, <a href="https://catbox.moe/">Catbox/Litterbox</a>, <a href="https://uguu.se/">Uguu/Pomf</a>, and <a href="https://filebin.net/">Filebin</a>. (currently this only supports catbox but feel free to change that with a pr)
<br>IMPORTANT NOTICE: This program <u>heavily</u> relies on file sharing services to function, if any of these change or stop functioning, please open a pr, issue or fork if you want.


### usage:
To use the apis and get more functionality, you would want to declare some keys before using the program. In this case, I am declaring the CatBox userhash, which is currently stored in the Appdata under banana.json.

`` banana -k MY_USERHASH -s cb``

once the userhash is declared, the program should be functional (or have more functionality). You can upload a file like this:

`` banana -f sick_ass_file.txt``

If you do not declare a service with -s, banana will automatically choose one for you. (due to the fact that no other services are present, banana always will choose catbox regardless of any other user input)
Keep in mind that CatBox is limited to files of 200mb of size and restrict against the following file types:
 - exe
 - scr
 - doc
 - cpl
 - jar

If you are using the windows (multi-tabbed) terminal, then just using ctrl+click on the link should make it easier to share.
Thank you for using my program and good luck with trying to figure out how to use it (i am not a good teacher :P)


[insert compiling here]
