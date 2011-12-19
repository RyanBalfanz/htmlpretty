#!/user/bin/env python
import argparse
import sys

from BeautifulSoup import BeautifulSoup


def prettify(html):
    """
    Prettify some HTML.
    """
    soup = BeautifulSoup(html)
    return soup.prettify()

def setup_parser():
    """
    Setup the command line parser.
    """
    parser = argparse.ArgumentParser(description='Prettify your HTML.')
    parser.add_argument('-f', '--file', dest='file', metavar='FILE', help="Input file")
    parser.add_argument('-o', '--output', dest='output', metavar='FILE', help="Output file")
    parser.add_argument('-w', '--write', dest='write', action="store_true", help="Overwrite the input file")
    parser.add_argument('file')

    return parser

def main(*args, **kwargs):
    """
    Main entry point.
    """
    if args[0]["write"]:
        with open(args[0]["file"], "rw") as inputOutputFile:
            inputOutputFileContents = inputOutputFile.read()
            prettified = prettify(inputOutputFileContents)
            inputOutputFile.write(prettified)
    else:
        with open(args[0]["file"], "r") as inputFile:
            inputFileContents = inputFile.read()
            prettified = prettify(inputFileContents)
    
            if args[0]["output"]:
                with open(args[0]["output"], "w") as outputFile:
                    outputFile.write(prettified)
            else:
                print prettified
                    
if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    sys.exit(main(vars(args)))
