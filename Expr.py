import argparse

from utils.utils import *
from run import *

if __name__ == "__main__":
    args = parse_args()
    opt = load_config(args.config)
    
    train(opt, args)
    if args.local_rank <= 0:
        test(opt, args)
        evaluate(opt, args)
