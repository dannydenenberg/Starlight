# Starlite
A hackable Google-home type helper.

## Installation
1. Clone the repository from the terminal
```bash
$ git clone https://github.com/dannydenenberg/Starlite.git

```
2. Move into the top level directory of the project
```bash
$ cd Starlite

```

## Usage
1. Make sure you are in the top level of the project directory before running
2. Run the main script using python 3
```python
$ python3 main.py
```
3. Talk to Starlite! All commands issued at starlite must begin with the word "starlite", such as "starlite, send an email"

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to test the addition so that it will work on a Raspberry Pi or similar Linux enviornments

## Command file structure
The structure of a command file is as follows:
  * The first line is a list of phrases separated by a vertical bar `|`. The rest of the file will be executed when a user has one of the phrases specified in a sentance he tells starlite.
  * For example, the following code is a command file which will have starlite say "awesome" whenever a user says "starlite jump" or "starlite you are cool":
  ```python
  jump|you are cool
  talkToMe('awesome')
  ```

## Adding/Editing Commands
The file structure for commands goes as follows:
  * All voice activated commands are stored in the ```Starlite/commands``` folder
  * To **edit** a command, move into the ```Starlite/commands``` folder, chose the command, and edit the python 3 code for that specific command
  * To **add** a new command, you could just create a new file in the ```Starlite/commands``` directory, or if you use the atom text editor, vim, nano, or any other one that can be accessed through the terminal, you should run the ```create_new_command``` executable from the terminal as follows: ```$ ./create_new_command "my_new_command_file_name" myTerminalAccesibleTextEditor```. Note, the ```"my_new_command_file_name"``` should NOT include the .py extention.
  
  
 ### Instructions for specific editors
 #### Atom
 ```bash
 $ ./create_new_command "my_new_command_file_name" atom
 ```
 
  #### Vim
 ```bash
 $ ./create_new_command "my_new_command_file_name" vim
 ```
 
  #### Nano
 ```bash
 $ ./create_new_command "my_new_command_file_name" nano
 ```
 
  

## License
[MIT](https://choosealicense.com/licenses/mit/)
