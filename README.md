# Starlite
A Google-home type helper


When creating a new command, execute the create_new_command file. Then, in the first line of the new file created, you put the commands you wish to respond to separated by pipes and the code below. For example, if you wanted to respond by printing 'hello' to the person saying 'please say hello', you would write in the file:

please say hello|any thing else to respond to
print('hello')
