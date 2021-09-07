# import click

# @click.command()
# def hello():
#     click.echo('Hello there')

# if __name__=='__main__':
#     hello()

# ******************PYTHON CLICK DEFAULT ARGUMENT*******************
# # !/usr/bin/python3
# import click

# @click.command()
# @click.argument('name',default='guest')
# def hello(name):
#     click.echo(f'Hello {name}')

# if __name__=='__main__':
#     hello()


# *****************Python click argument types*************************


# # !/usr/bin/python3
# import click

# @click.command()
# @click.argument('name',default='guest')
# @click.argument('age',type=int)
# def hello(name, age):
#     click.echo(f'{name} is {age} years old')

# if __name__=='__main__':
#     hello()

# ************************Python click variable number of arguments************


# # !/home/development/Documents/Todo Command Line Application/CLI_tool_Typer/venv/bin/python
# import click
# from operator import mul
# from functools import reduce

# @click.command()
# @click.argument('vals',type=int,nargs=-1)
# def process(vals):
#     print(f'The sum is{sum(vals)}')
#     print(f'The product is {reduce(mul,vals,1)}')

# if __name__=='__main__':
#     process()


# ************************Python click simple option*************************

# import click

# @click.command()
# @click.option('--n',type=int, default=1)
# def dots(n):
#     click.echo('.'* n)

# if __name__=='__main__':
#     dots()



# *************************Python click option names******************************

# import click

# @click.command()
# @click.option('-s','--string')
# def output(string):
#     click.echo(string)

# if __name__=='__main__':
#     output()


# *************************Python click prompt for value**********************************

# import click
# @click.command()
# @click.option("--name",prompt="Your name",help="Provide your name")
# def hello(name):
#     click.echo(f"Hello, {name}")

# if __name__=='__main__':
#     hello()


# **************************Python click colour output**************


# import click
# @click.command()
# def coloured():
#     click.secho('Hello there',fg="blue",bold=True)

# if __name__=='__main__':
#     coloured()


# *****************************Python click flags******************

# import click

# @click.command()
# @click.option('--blue', is_flag=True, help='message in blue color')
# def hello(blue):
#     if blue:
#         click.secho('Hello there',fg='blue')
#     else:
#         click.secho('Hello there')


# if __name__=='__main__':
#     hello()


# *********************************click flags2***********************

# import click
# @click.command()
# @click.argument('word')
# @click.option('--shout/--no-shout',default=False)
# def output(word,shout):
#     if shout:
#         click.echo(word.upper())
#     else:
#         click.echo(word)

# if __name__=='__main__':
#     output()


# ********************************Python click environment variables****************
# **********
# import click
# import os

# @click.argument('mydir',envvar='MYDIR',type=click.Path(exists=True))
# @click.command()
# def dolist(mydir):
#     click.echo(os.listdir(mydir))


# if __name__=='__main__':
#     dolist()



# ***************************Python click option tuples********************
# # multi_val.py
# import click

# @click.command()
# @click.option('--data', required=True, type=(str, int))
# def output(data):
#     click.echo(f'name={data[0]} age={data[1]}')

# if __name__=='__main__':
#     output()


# **************************Specifying options multiple times*****************
# multiples.py

# import click

# @click.command()
# @click.option('--word','-w',multiple=True)
# def words(word):
#     click.echo('\n'.join(word))

# if __name__=='__main__':
#     words()


# **********************The click.File type***************************
# head.py

# from typing import Counter
# import click

# @click.command()
# @click.argument('file_name', type=click.File('r'))
# @click.argument('lines',default=-1,type=int)
# def head(file_name, lines):
#     counter=0
#     for line in file_name:
#         print(line.strip())
#         counter+=1

#         if counter == lines:
#             break

# if __name__=='__main__':
#     head()


# ********************The click.Path type*****************************
# head2.py
# from typing import Counter
# import click

# @click.command()
# @click.argument('file_name', type=click.Path(exists=True))
# @click.argument('lines',default=-1, type=int)
# def head(file_name, lines):
#     with open(file_name, 'r') as f:
#         counter=0
#         for line in file_name:
#             print(line.strip())
#             counter+=1
#             if counter == lines:
#                 break


# if __name__=='__main__':
#     head()


# *****************Python click command groups*********************************

# groups.py

# import click

# @click.group()
# def messages():
#     pass

# @click.command()
# def generic():
#     click.echo('Hello there')

# @click.command()
# def welcome():
#     click.echo('Welcome')

# messages.add_command(generic)
# messages.add_command(welcome)

# if __name__=='__main__':
#     messages()


# *************************groups2.py*************

# import click

# @click.group()
# def cli():
#     pass

# @cli.command(name='gen')
# def generic():
#     click.echo('Hello there')

# @cli.command(name='wel')
# def welcome():
#     click.echo('Welcome')

# if __name__=='__main__':
#     cli()


# *******************