from __future__ import division, print_function, absolute_import 

import matplotlib as mpl
mpl.use('Agg')
mpl.rc('font', size=8)
import matplotlib.pylab as plt
import numpy as np
import deepdish as dd
from vzlog import VzLog
import itertools as itr
import os

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('losses', nargs='+', type=str)
    parser.add_argument('-o', '--output', default='log-loss', type=str)
    parser.add_argument('--dataset', default='Test', type=str)
    parser.add_argument('--captions', nargs='+', type=str)

    args = parser.parse_args()

    rs = np.random.RandomState(0)


    vz = VzLog(args.output)
    print(args.captions)

    plt.figure()
    for i, loss_fn in enumerate(args.losses):
        print('file', loss_fn)
        data = dd.io.load(loss_fn)
        for seed, info in enumerate(data):
            if seed > 0:
                continue
            print('info', info.keys())
            values = info[args.dataset]
            if args.captions:
                caption = args.captions[i]
            else:
                caption = loss_fn
            plt.plot(values[0], values[2], label=caption)

    plt.legend()
    plt.ylabel('Loss')
    plt.xlabel('Iteration')
    plt.savefig(vz.impath('svg'))
    plt.close()

    plt.figure()
    for i, loss_fn in enumerate(args.losses):
        print('file', loss_fn)
        data = dd.io.load(loss_fn)
        for seed, info in enumerate(data):
            if seed > 0:
                continue
            print('info', info.keys())
            values = info[args.dataset]
            if args.captions:
                caption = args.captions[i]
            else:
                caption = loss_fn
            plt.plot(values[0], 100*(1-values[1]), label=caption)

    plt.legend()
    plt.ylabel('Error rate (%)')
    plt.xlabel('Iteration')
    plt.savefig(vz.impath('svg'))
    plt.close()

if __name__ == '__main__':
    main()
