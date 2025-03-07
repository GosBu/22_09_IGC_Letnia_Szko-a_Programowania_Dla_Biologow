# Otworzyć plik fasta, który będzie przekazany jako argument naszego skryptu

import argparse

parser = argparse.ArgumentParser
parser.add_argument('-i', help='FASTA.txt', rquired=True)
args = parser.parser_args()
print(args.i)
