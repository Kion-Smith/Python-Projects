import os;
#This os library allows for os calls like with in the unix kernal (I think..)

print (os.getpid())

#ges current location like cd in Unix
location = os.getcwd()
print(location)

# list of directories in the files location
listOfDir = os.listdir()
print(listOfDir)


try:
    #makes a new directory like in Unix in current location
    os.mkdir("test")
except:
    print("Test is already a directory")

#removes directory
os.rmdir("test")
print("Removed test directory")

#returns true if item is a file
print(os.path.isfile("/OS.py"))
