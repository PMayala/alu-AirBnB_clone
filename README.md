# 0x00. AirBnB clone - The console
# Background Context
## Welcome to the AirBnB clone project!
### First step: Write a command interpreter to manage your AirBnB objects.
This initial phase marks the inception of your journey toward constructing a comprehensive web application: the **AirBnB clone**. This foundational step holds paramount significance as it lays the groundwork for subsequent project phases, including HTML/CSS templating, database management, API development, and seamless integration of front-end components. Each aspect developed during this stage will serve as a cornerstone for the subsequent phases, ensuring a cohesive and robust final product.

Each task is linked and will help you to:
- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
	- Retrieve an object from a file, a database etc…
	- Do operations on objects (count, compute stats, etc…)
	- Update attributes of an object
	- Destroy an object

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`
