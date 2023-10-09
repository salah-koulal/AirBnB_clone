# Alx School - AirBnB_clone

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231009%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231009T085123Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5817bf77b89ce6a809b9001f92199a7d498f8d2a3cf410cb6eadb94c36868437)

## Description
This team project is part of the Holberton School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command interpreter program built using the python module cmd. Contains to create, update, delete and print a class instance or all instaces created.

## Helpful Links
* [Python Docs: Cmd](https://docs.python.org/3.4/library/cmd.html)
* [Python Docs: Modules / Packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
* [Python Docs: UUID](https://docs.python.org/3.4/library/uuid.html)
* [Python Docs: datetime](https://docs.python.org/3.4/library/datetime.html)
* [Python Docs: Unit test](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python Tips: args and kwargs](https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [All about cmd](https://pymotw.com/2/cmd/)
* [Give Python a shell](https://coderwall.com/p/w78iva/give-your-python-program-a-shell-with-the-cmd-module)

## Usage:
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt **(hbnb)** and waits for the user for input.

| Command | Example |
| --- | --- |
| Run the console | `./console.py` |
| Quit the console | `(hbnb) quit` |
| Display the help for a command | `(hbnb) help <command>` |
| Create an object (prints its id) | `(hbnb) create <class>` |
| Show an object | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` |
| Destroy an object | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>` |
| Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |

Your shell should work like this in interactive mode:

```shell
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

```shell
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

## Authors

- **Mouad Nait si** [Github](https://github.com/Mouadnait) || [Linkedin](https://www.linkedin.com/in/mouad-nait-si-017b73200/)
- **Salah eddine Koulal** [Github](https://github.com/salah-koulal) || [Linkedin](https://www.linkedin.com/in/salah-koulal-ab2523264/)
