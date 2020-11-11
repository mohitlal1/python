# CSV Data: 
CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format.For working CSV files in python, there is an inbuilt module called csv.

# Writing to a CSV file:

Importing the csv module 
```sh 
        import csv 
```  
Field names 
```sh 
fields = ['Name', 'Power', 'Age', 'Hero'] 
```  
Data rows of csv file 
```sh 
rows = [ ['Tony Stark', 'Suit', '33', 'Iron Man'], 
         ['Steve Rogers', 'Shield', '300', 'Captain America'], 
         ['Thor', 'Lightning and Hammer', '1500', 'Thor-God of Thunder'], 
         ['Bruce Banner', 'Super being', '40', 'Hulk'], 
         ['Peter Parker', 'Web,Spidey sense', '19', 'Spider Man'] ] 
```  
Name of csv file 
```sh 
filename = "heroes.csv"
```  
Writing to csv file 
```sh 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)
```
# Converting CSV to JSON:
```sh 
Code:
import csv 
import json 

csvFilePath = 'heroes.csv'
jsonFilePath = 'heroes.json'

# Read csv file and add to data 
data = {} 
with open(csvFilePath, encoding='utf-8') as csvFile: 
        csvReader = csv.DictReader(csvFile) 
        for rows in csvReader: 
            id = rows['id'] 
            data[id] = rows 
  
# Open a json writer, and use the json.dumps()  
with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile: 
    jsonf.write(json.dumps(data, indent=4)) 
```

# JSON Data: 
JSON is a syntax for storing and exchanging data. JSON is text, written with JavaScript object notation. Python has a built-in package called json, which can be used to work with JSON data.
			In python we can import the json module by using 
```sh 			
			import json 
```
# Parse JSON 
Convert from JSON to Python: If we have a JSON string, we can parse it by using the json.loads() method.The result will be a Python dictionary.
```sh 			
Example
Convert from JSON to Python:
				
	import json
	x =  '{ "name":"John", "age":30, "city":"New York"}'
	y = json.loads(x)
	
	# the result is a Python dictionary:
	print(y["age"]) 
```
```sh 
	Output: 30
```
Convert from Python to JSON: If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
```sh 			
Example:  Convert from Python to JSON:

	import json
	x = { "name": "John",
		  "age": 30,
		  "city": "New York"
		   }
	# convert into JSON:
	y = json.dumps(x)
    # the result is a JSON string:
	print(y) 
```
```sh 
Output: {"name": "John", "age": 30, "city": "New York"}
```
We can convert Python objects of the following types, into JSON strings:
- dict
- list
- tuple
- string
- int
- float
- True
- False
- None
