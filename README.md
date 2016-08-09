# CLI Uplmg

CLI Uplmg use the API of Uplmg's server (you can find the github project [here](https://github.com/Uplimg/server) ) for share and redistribute your files quickly and easily.

##Getting started
The CLI use all of the fonctionnality of the API

- You need Python (at least 3)
- You need Requests for this :
  - You need Pip :
      - `python get-pip.py`
  - And : `pip install requests`
- Clone the repository
- Run ./uplmg
- You're ready to go !

##Lists of commands
- `uplmg <file>` or `uplmg sendfile <file>` : Send a file to the server
- `uplmg download <url / shortname>` : Download the file
- `uplmg showheaders <shortname>` : Show the headers of the file
- `uplmg showstats` : Show the stats of the server
