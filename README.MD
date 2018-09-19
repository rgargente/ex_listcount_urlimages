# Coding exercise: Counting lists elements and getting images from a website
The first exercise counts the amount of elements in a list, without using Python's built in len. It assumes the only
way to interact with the list is getting the element at a given index.

The other one reads images from several given URLs and creates a json file with information about them.


## How to run the program

The zip file contains all the source code. It also contains a git bundle file in case you are interested in checking
the git history. There is more information about how to unbundle it here:
https://git-scm.com/docs/git-bundle

The exercise is implemented using Python 3. 

I have provided an Anaconda environment file to easily create an environment to run the software. If you have Anaconda
installed, simply run the following command in a terminal:
```
 conda env create -f environment.yml
```

Otherwise install each dependency using ```pip install ```. You can read the environment.yml file to know which 
dependencies you need, but I would recommend just running the program and seeing what is missing. 

There are two folders, one for each exercise. Please read the comments included with the code as the provide some 
insight about the design.

### Countlist
There is no user interactive script here. The best way to try the software is probably running the tests. Just run 
```pytest``` from the countlist folder.

There is also a benchmarking test that you can play with to see which is the faster counting algorithm in each case.


### UrlImages
There is a file called inputurls.txt. This can be edited and the script will read all the urls provided.
There is a wrong url in the file to show that the program handles it gracefully.
The easiest way to run the program as expected is by running the readfile script:
```
python urlimages.py
```
The script will create a urlimages.json file.