# BSOD (Batch splitting of data)
`BSOD` is a command line tool used for the batch splitting of data. 

If the first column of map file in the second-generation sequencing data is all zero, the second column can be split and directly replaced with the first column without changing the data in the second column.

## Getting Started
0.Git clone BSOD

In order to download `BSOD`, you should clone this repository via the commands:
```
git clone https://github.com/Werewolfzy/BSOD.git
cd BSOD
```

1.Prepare the environment：

This script depends on the Python3 software and requires the following dependency packages:
```
pip install -r requirements.txt
```

2.Prepare the map file.

The map file is map format of PLink software.

3.The command line
```
python fenlie.py -i [map file] -o [out_file  (The default is result.txt)]
```









