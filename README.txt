TURGONKEY 1.0

TurgonKey is a simple password generator, written in Python3, that takes parameters from a command line to create secure keys.

It runs on terminal (bash and zch tested), after you add permissions to the .py file to run as a software with chmod. After that, simply open it from the directory with ./TurgonKey.py.

There are 3 possible commands: 'generate', 'help' and 'exit'. 

The first must be followed by 4 other parameters: length of the password (integer), case options (can be 'a' for 'all', 'u' for uppercase only and 'l' for lowercase only), digits option (can be 'usenums' to include digits from 0 to 9 or 'pass' to ignore this parameter), and finally special characters option (can be 'usespcs' to include special characters or 'pass' to ignore the parameter). 

The final command that generates a successful password must have this form: generate [size] [case option] [digit option] [special characters option]

For example: generate 8 a usenums usespcs

The other 2 possible commands do exactly what they indicate: 'help' prints a detailed instruction for each parameter and 'exit' is a way out the software from the command line, without the need to close it by closing the terminal window. This way you can open it, use it and close it, and after that continue to use the terminal for whatever.

That's it, to the gates of Gondolin!

