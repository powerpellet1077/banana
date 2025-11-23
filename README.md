# <img src="assets/banana_title_white.png" id="banana"></img>
This is a program made to make uploading files and videos not a hassle.

This program is planning to support [DropBox](https://dropbox.com), [Catbox/Litterbox](https://catbox.moe), [Uguu/Pomf](https://uguu.se), and [Filebin](https://filebin.net). (currently this only supports catbox/litterbox, filebin and uguu but feel free to change that with a pr)


#### IMPORTANT NOTICE: 
This program _heavily_ relies on file sharing services to function, these may change or break at any time and may take time to resolve so please expect issues...
### usage:
To declare keys or userhashes, you can use the -k command to set the key for the service provided. (most services I am using will not require or need a userhash/api key so you can skip this if you want).

``banana -k MY_USERHASH -s cb``

you can also clear any key/userhash like this:

``banana -k clear -s cb``

For reference, the keys and userhashes are stored in ``banana.json`` within the user's appdata/roaming folder on windows, otherwise it will be in the user's .config folder on linux.

once the userhash is declared, the program will automatically use it for that service. To actually upload a file, use the -f flag and declare a path (absolute or relative)

``banana -f sick_ass_file.txt``

you can choose a service with -s and following with the abbreviation for the selected service, (in this case, catbox would be cb)

``banana -f sick_ass_file.txt -s cb``

You can also declare the time for temporary file sharing services (limited to only litterbox at the moment) and will automaticially default to one hour. The possible values for this flag are 1h, 12h, 24h and 72h.

``banana -f sick_ass_file.txt -s lb -t 24h``

As of now, banana supports only Catbox, Litterbox, Filebin and Uguu. (cb, lb, fb and ug respectively).
You can also list these (as well as some extra info) by running ``banana -l`` or ``banana --list``


If you do not declare a service with -s, banana will automatically choose one for you, going in order of priority and file-specific services to services supporting different types of files and applications. 
Catbox and litterbox restrict against the following types of files:
 - exe/scr
 - cpl
 - doc
 - jar

Keep in mind that Catbox is limited to files of 200MB and Litterbox is limited to files of 1GB.

Filebin only restricts windows executable files (at least from my limited research as I found no other people had this issue :P)

The only (technically) unlimited file service is Uguu, but please do not upload dangerous software to any service provided regardless, (you will be blocked!)

If you are using the windows (multi-tabbed) terminal, then just using ctrl+click on the link should make it easier to share.

### building
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
for linux users:
```
pyinstaller --noconfirm --onefile --console --name "banana" --add-data "core:core"  "./banana.py" 
```
Then if everything worked out, you should have your binary in ``banana/dist``

```
cd dist
banana
```

or ```./dist/banana``` for linux users (without the file extension)

If you got a response similar to this:

```
[banana][ERROR] please provide a value
```

Then the compilation was successful!

Thank you for using my program and good luck to you! (for any questions or concerns, please send me a dm at powerpellet1077 on discord)
