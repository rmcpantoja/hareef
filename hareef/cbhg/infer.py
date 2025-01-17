# coding: utf-8

import argparse
import logging
import random
import sys
from itertools import repeat

import numpy as np
import torch
from hareef.utils import find_last_checkpoint

from .config_manager import ConfigManager
from .diacritizer import OnnxCBHGDiacritizer, TorchCBHGDiacritizer
from .model import CBHGModel

_LOGGER = logging.getLogger(__package__)


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        prog="hareef.cbhg.infer",
        description="Inference script using Torch or ONNXRuntime",
    )
    parser.add_argument("--config", dest="config", type=str, required=True)
    parser.add_argument("--seed", type=int, default=1234, help="random seed")
    parser.add_argument(
        "--device",
        type=str,
        default="cpu",
        choices=["cpu", "gpu"],
        help="Device used for inference",
    )
    parser.add_argument("--text", dest="text", type=str, required=True)
    parser.add_argument("--checkpoint", type=str, required=False)
    parser.add_argument("--onnx", type=str, required=False)

    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed(args.seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    config = ConfigManager(args.config)

    if args.onnx:
        diacritizer = OnnxCBHGDiacritizer(config, onnx_model=args.onnx)
    else:
        if not args.checkpoint:
            try:
                checkpoint_filename, epoch, step = find_last_checkpoint(
                    config["logs_root_directory"]
                )
                _LOGGER.info(f"Using checkpoint from: epoch={epoch} - step={step}")
                _LOGGER.info(f"file: {checkpoint_filename}")
                args.checkpoint = checkpoint_filename
            except:
                _LOGGER.exception(
                    "Failed to obtain the path to the last checkpoint", exc_info=True
                )
                sys.exit(1)

        model = CBHGModel.load_from_checkpoint(
            args.checkpoint, map_location=args.device, config=config
        )
        model.freeze()
        diacritizer = TorchCBHGDiacritizer(config, model=model)

    sents, infer_time = diacritizer.diacritize_text(args.text)
    _LOGGER.info(f"Inference time (ms): {infer_time}")
    print("\n".join(sents))


if __name__ == "__main__":
    main()
