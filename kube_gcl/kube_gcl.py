import argparse
import sys

import gcl
from gcl import query
from gcl import util



def main(argv=None, stdin=None):
  parser = argparse.ArgumentParser(description='Convert a GCL file to a set of YAML files to apply to a k8s cluster.')
  parser.add_argument('file', metavar='FILE', type=str, nargs='?',
                      help='File to parse')

  args = parser.parse_args(argv or sys.argv[1:])
