# CLI Uplmg

CLI Uplmg use the API of Uplimg's server (you can find the github project [here](https://github.com/Uplimg/server)) to share and redistribute your files quickly and easily.

## Getting started

The app let you use the entire API from the command line.

- You need Python (3 is recommanded)
- You need Requests:
  - You need Pip:
      - `wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py` (see [here](https://pip.pypa.io/en/stable/installing/))
  - And : `pip install requests`
- Clone the repository
- Run ./uplmg
- You're ready to go !

## Lists of commands

- `uplmg <file>` or `uplmg sendfile <file>`: Send a file to the server
- `uplmg download <url / shortname>`: Download the file
- `uplmg showheaders <shortname>`: Show the headers of the file
- `uplmg showstats`: Show the stats of the server

## And more

Something is missing... Let me think... Ah yeah! Just imagine how easily you could share files from the CLI if you add the app to your PATH... It's amazing, isn't it :-D?
