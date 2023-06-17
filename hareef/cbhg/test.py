# coding: utf-8


import argparse
import random

import numpy as np
import torch

from .tester import DiacritizationTester

SEED = 1234
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", dest="config", type=str, required=True)
    parser.add_argument("--model_path", dest="model_path", type=str, required=False)

    args = parser.parse_args()

    tester = DiacritizationTester(args.config)
    tester.run()


if __name__ == "__main__":
    main()