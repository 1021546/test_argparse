if __name__ == '__main__':
    # argparse
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest',
                       default='model/base_model.h5',
                       help='output model path')
    parser.add_argument('-p', '--plot',
                       help='plot the training process',
                       action='store_true')
    parser.add_argument('-v', '--valid',
                       help='validation or not',
                       action='store_true')
    args = parser.parse_args()

# python arg_test.py -h
# usage: arg_test.py [-h] [--dest DEST] [-p] [-v]

# optional arguments:
#   -h, --help   show this help message and exit
#   --dest DEST  output model path
#   -p, --plot   plot the training process
#   -v, --valid  validation or not
