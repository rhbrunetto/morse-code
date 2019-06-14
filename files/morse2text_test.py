import sys

from ..app import parse_args, run


sys.argv[1:] = ['test_files/input_0.morse']
run(arguments=parse_args())
