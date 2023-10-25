# Web scraping :page_with_curl: 0x14. JavaScript - Web scraping
## In this project :bulb:
## Overview
- This is a javascript porject that mainly loooks at
  - How to manipulate JSON data
  - How to use request and fetchh API
  - And how to read and write a file using the `fs` module
## Requirements of the project
- Used Vi/Vim editor
- Codes are `semistandard` compliant

## Installation of packages
- Installeed Node 14
`$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -`
`$ sudo apt-get install -y nodejs`

- Install semi-standard
[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)
`$ sudo npm install semistandard --global`

- Install request module and use it
[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
`$ sudo npm install request --global`
`$ export NODE_PATH=/usr/lib/node_modules`



### Task 0
Script that reads and prints the content of a file.
- The first argument is the file path
- The content of the file is read in `utf-8`
- If an error occurred during the reading, the error object is printed

This how the code can be tested

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/085319c7-2b88-4686-a6cf-741c5c98e77e)


### Task 1
Script that writes a string to a file
- First argument is the file path
- The second argument is the string to write
- The content of file is writtten in uft-8
- if error occurred during while writing,print the error object

This is how the code can be tested

![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/bd9c9c40-2acf-46b6-9df5-90cbed1ba6d5)

### Task 2
Scirpt that display the status code of a `GET` request
- First arugment is the URL to request (`GET`)
- Status code is printed like `code: <status code>`

This is how the code can be tested

![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/590e973f-f9a1-47ff-b6e7-e8977f6ac343)


### Task 3
Script that prints the title of Star Wars movie where the episode number matches a given integer
- Fist argument is the movie ID
- used [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA) with the endpoint 
https://swapi-api.alx-tools.com/api/films/:id

This is how the code can be tested

![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/68ee11f2-457d-4abd-99f5-6c11446bf8d6)

### Task 4
Script that prints the number of movies where the character “Wedge Antilles” is present.
- The first argument is the API URL of the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA)
- Wedge Antilles is character ID 18 - your script uses this ID for filtering the result of the API

This is how the code can be tested

![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/113ab56a-77e1-4754-8ec1-bafb23345ff1)


### Task 5
Script that gets the content of a webpage and stores it in a file
- First argument is the URL to request
- The second argument is the file path to store the body response
- The file  must be UTF-8 encoded

This is how the code can be tested
`./5-request_store.js http://loripsum.net/api loripsum`
`cat loripsum`

### Task 6
Script that computed the number of tasks completed by user id.
- First argument is the API URL: https://jsonplaceholder.typicode.com/todos
- Only print users with completed task

This is how the code can be tested
`./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`

### Task 7
Script that prints all characters of a Star Wars movie
- First argument is the movie ID - example: 3 = "Return of the Jedi"
- Display one character by line
- Must use the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA)

Run the code with
`./100-starwars_characters.js 3`
Filename:100-starwars_characters.js

### Task 8
Script that prints all characters of a Star Wars movie:
- First argument is the movie ID - example: 3 = "Return of the Jedi"
- Display one character name by line in the same order of the list “characters” in the /films/ response
- used [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA)

Run code with
`./101-starwars_characters.js 3`
Filename: 101-starwars_characters.js

### Useful resources
Task0

[first one](https://nodejs.dev/en/learn/reading-files-with-nodejs/)

Task1

[first one](https://nodejs.dev/en/learn/writing-files-with-nodejs/)

[Second one](https://blog.logrocket.com/using-writefilesync-node-js/)

Task2

[First one](https://www.geeksforgeeks.org/node-js-request-module/)

[Second one](https://www.scaler.com/topics/nodejs/node-js-request/)

Task3

[First one](if u dont wanna use JSON.parse(body))

request have option for json, check last chapter :

[Second one](https://dev.to/isalevine/three-ways-to-retrieve-json-from-the-web-using-node-js-3c88)

Task4

this can be helpful, if wanna do it string way

[first one](https://stackabuse.com/javascript-how-to-count-the-number-of-substring-occurrences-in-a-string/)

Task5

same as task1 and task2

Task6

[first one](https://www.microverse.org/blog/how-to-loop-through-the-array-of-json-objects-in-javascript)
[Second one](https://www.scaler.com/topics/add-property-to-object-javascript/)


### Some other useful resources for concepts

[Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)

[The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)

[request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)

[Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)
