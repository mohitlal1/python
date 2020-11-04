# Regular Expression: 

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Import the re module:
```sh 
	import re
```
Check if the string starts with certain characters i.e. "The" and ends with "cat":
```sh 
Code:
	txt = "The rat plays with cat"
	x = re.search("^The.*cat$", txt)

	if x:
	  print("YES! We have a match!")
	else:
	  print("No match")
```
```sh 
Output: YES! We have a match!
```	  
The re module offers a set of functions that allows us to search a string for a match:
| Function | Description |
| ---- | ---- |
| findall | Returns a list containing all matches|
| search | Returns a Match object if there is a match anywhere in the string|
| split | Returns a list where the string has been split at each match|
| sub |	Replaces one or many matches with a string|

```sh 
Code:
	import re
	#Return a list containing every occurrence of "ai":
	txt = "The rat plays with cat"
	x = re.findall("at", txt)
	y = re.search("\s", txt)
	z = re.split("\s", txt)
	a = re.sub("\s", "9", txt)
	
	print(x)
	print(y)
	print(z)
	print(a)
```
```sh 
Output: 
	['at','at']
	3
	['The', 'rat', 'plays', 'with', 'cat']
	The9rat9plays9with9cat 
```	
	