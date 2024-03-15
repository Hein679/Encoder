#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description="Encode command using Hexadecimal or Octal. Usage encoder.py <command> [options...]")
parser.add_argument('command', metavar="<command>", type=str, help='String to Encode')
parser.add_argument('--hex', action='store_true', help='Hex Encoding')
parser.add_argument('--oct', action='store_true', help='Octal Encoding')
parser.add_argument('--binary', action='store_true', help='Octal Encoding')
parser.add_argument('--decimal', action='store_true', help='Octal Encoding')
args = parser.parse_args()

command = args.command
if not (args.hex or args.oct or args.binary or args.decimal): args.hex = True

encoded_command = ''
if (args.hex):
    for c in command:
        encoded_command += f'\{hex(ord(c))[1:]}'
    print("Hex Encoding: ")    
    print(encoded_command, "\n")

encoded_command = ''
if (args.oct):
    for c in command:
        encoded_command += f'\{oct(ord(c))[2:]}'
    print("Oct Encoding: ")    
    print(encoded_command, "\n")

encoded_command = ''
if (args.binary):
    for c in command:
        encoded_command += f'{bin(ord(c))[2:]} '
    print("Binary Encoding: ")    
    print(encoded_command, "\n")

encoded_command = ''
if (args.decimal):
    for c in command:
        encoded_command += f'{ord(c)} '
    print("Binary Encoding: ")    
    print(encoded_command, "\n")