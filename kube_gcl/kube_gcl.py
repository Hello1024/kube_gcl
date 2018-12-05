import argparse
import sys

import yaml

import gcl
from gcl import query
from gcl import util



def main(argv=None, stdin=None):
  parser = argparse.ArgumentParser(description='Convert a GCL file to a set of YAML files to apply to a k8s cluster.')
  parser.add_argument('file', metavar='FILE', type=str, nargs='?',
                      help='File to parse')

  args = parser.parse_args(argv or sys.argv[1:])

  try:
    if args.file and args.file != '-':
      model = gcl.load(args.file)
    else:
      model = gcl.loads((stdin or sys.stdin).read(), filename='<stdin>')

    
    plain = util.to_python(model)

    
    sys.stdout.write(yaml.dump(plain))
  except (gcl.ParseError, RuntimeError) as e:
    sys.stderr.write(str(e) + '\n')
    sys.exit(1)

if __name__== "__main__":
  main()