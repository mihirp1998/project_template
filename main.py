# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""
A minimal training script for DiT.
"""
import hydra
from omegaconf import DictConfig
import ipdb
st = ipdb.set_trace

#################################################################################
#                                  Training Loop                                #
#################################################################################

@hydra.main(config_path="config", config_name="config")
def main(args: DictConfig):
    import socket
    while True:
        pass
 

if __name__ == "__main__":
    main()