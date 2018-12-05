import argparse
import sys

import yaml
import requests

import gcl
from gcl import query
from gcl import util


def canonicalize_typename(type_name):
  return type_name.replace('.', '_').replace('$', '_')

def canonicalize_type_reference(type_ref):
  return canonicalize_typename(type_ref[14:])

def get_gcl_type(prop):
  if '$ref' in prop:
    return canonicalize_type_reference(prop['$ref'])

  # Not sure exactly what this key means, but it seems to have type info...
  if 'additionalProperties' in prop:
    return get_gcl_type(prop['additionalProperties'])

  type_map = {
    'integer': 'int',
    'string': 'string',
    'number': 'float',
    'boolean': 'bool',
    #'string': 'null'
  }
  prop_type = prop['type']
  if prop_type == 'array':
    return '[' + get_gcl_type(prop['items']) + ']'
  if prop_type in type_map:
    return type_map[prop_type]

  raise ValueError('Invalid type ' + prop_type)

def schema_for_property(prop, prop_value, required):
  result = []

  if required:
    required_str = 'required '
  else:
    required_str = ''
  
  result.append( '  ' + canonicalize_typename(prop) + ': ' + required_str + get_gcl_type(prop_value) +';')

  return '\n'.join(result)


def schema_for_type(type_name, type_def):
  result = []
  result.append( canonicalize_typename(type_name) + ' : private = {')

  required = type_def.get('required', [])

  if 'properties' in type_def:
    for k, v in type_def['properties'].items():
      result.append(schema_for_property(k,v, k in required))

  result.append( '};')
  return '\n'.join(result) + '\n'


def main(argv=None, stdin=None):
  parser = argparse.ArgumentParser(description='Get a JSON schema for Kubernetes objects and generate .gcl type files.')
  parser.add_argument('url', default='https://raw.githubusercontent.com/garethr/kubernetes-json-schema/master/v1.9.9/_definitions.json',
                      metavar='URL', type=str, nargs='?',
                      help='URL to schema')

  args = parser.parse_args(argv or sys.argv[1:])

  schema = requests.get(args.url).json()
  f = open("schema.gcl", "w")

  for k,v in schema['definitions'].items():
    f.write(schema_for_type(k,v))


  return schema

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