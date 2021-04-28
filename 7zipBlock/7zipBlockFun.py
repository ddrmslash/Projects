# Something fun I thought to do while using https://gchq.github.io/CyberChef/
# The basic concept is to 'encrypt' a block of your drive with 7zip
# This is a tie-in with a different project: 7zip Encryption TOR-style

# Possibilities: 
#	- User can pick their own Junk Files
#	- Adding files would overwrite junk files that are created
#	- Any file added would have its base directory file deleted
#	- Create a sort of shortcut system or another tie in that can search through
#		7zip folders when presented a TopPassword
#	- Create a wordlist inside this file or have an external list
#

# HOW IT WORKS:
#	- Give a TopPassword
#	- Input the size you want the block to be
#	- The script will autogenerate long scrambled passwords for the files that are output to a list


import os
import random

print("Pick a SECURE password:")
TopPass = input()
print("Archive Name:")
archivename = input()
print("Size in MB of Archive:")
size = input()

gg = "7za a -p" + TopPass + " " + archivename
os.system(gg)

num = [1,2,3,4,5,6,7,8,9,0]
down = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# These special characters will mess up python->shell commands
#spec = ['!','#','$','&','*','+','-',':',';','<','=','>','?','@','[',']','^','_','{','|','}','~']
spec = ['yy', 'tt', 'oo', 'rr']

passlength = 15
passgen = 3
gg = []
inc = 0
while(True):
	inc += 1
	if inc == passgen+1:
		break
	for x in range(1, passlength+1):
	        bb = (random.randint(1,len(num)-1))
	        qq = (random.randint(1,len(down)-1))
	        ww = (random.randint(1,len(upp)-1))
	        ee = (random.randint(1,len(spec)-1))
	        gg.append(str(num[bb]) + str(down[qq]) + str(upp[qq]) + str(spec[ee]) )
	
j = []
yyyy = str(gg).replace("[", "")
uuuu = yyyy.replace(" ", "")
iiii = uuuu.replace("'", "")
oooo = iiii.replace(",", "")
#print(oooo)

#touch passfile.txt
passe = []

# A junk file is provided
for x in range(1,int(size)+1):

	copying = "cp door.txt door" + str(x) + ".txt"
	os.system(copying)
	
	print("Junk File " + str(x) + " Created - Success!")

	# 		7za u <archive-filename> <list-of-files-to-update>
	addtoarchive = "7za u " + archivename + ".7z" + " door" + str(x) + ".txt"
	os.system(addtoarchive)

	remove = "rm door" + str(x) + ".txt"
	os.system(remove)
	print("Junk File " + str(x) + " Removed - Success!")


	archlist = ['windsor', 'premium', 'pass', 'song']
	tttt = random.randint(0, len(archlist)-1)
	SArand = archlist[tttt]
	#print(SArand)
	subarchive = "7za a -p" + str(oooo) + " " + str(SArand) + str(x)
	os.system(subarchive)

	subaddtoarchive = "7za u " + archivename + ".7z" + " " + str(SArand) + str(x) + ".7z"
	os.system(subaddtoarchive)

	subarchremove = "rm " + str(SArand) + str(x) + ".7z"
	os.system(subarchremove)

	passe.append(str(SArand) + str(x))
	passe.append(" -> ")
	passe.append(oooo)
	passe.append(" || ")
	
os.system("echo FINISHED!")
print("Passwords used:" + str(passe))