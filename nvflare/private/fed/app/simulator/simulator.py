# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Federated Simulator launching script."""

import argparse
import os
import sys

from nvflare.private.fed.app.simulator.simulator_runner import SimulatorRunner


def define_simulator_parser(simulator_parser):
    simulator_parser.add_argument("job_folder")
    simulator_parser.add_argument("-w", "--workspace", type=str, help="WORKSPACE folder", required=True)
    simulator_parser.add_argument("-n", "--clients", type=int, help="number of clients")
    simulator_parser.add_argument("-c", "--client_list", type=str, help="client names list")
    simulator_parser.add_argument("-t", "--threads", type=int, help="number of parallel running clients")
    simulator_parser.add_argument("-gpu", "--gpu", type=str, help="list of GPU Device Ids, comma separated")


def run_simulator(simulator_args):
    simulator_driver = SimulatorRunner(simulator_args)

    if simulator_driver.setup():
        run_status = simulator_driver.run()
    else:
        run_status = 1

    return run_status


if __name__ == "__main__":
    """
    This is the main program when running the NVFlare Simulator. Use the Flare simulator API,
    create the SimulatorRunner object, do a setup(), then calls the run().
    """

    if sys.version_info >= (3, 9):
        raise RuntimeError("Python versions 3.9 and above are not yet supported. Please use Python 3.8 or 3.7.")
    if sys.version_info < (3, 7):
        raise RuntimeError("Python versions 3.6 and below are not supported. Please use Python 3.8 or 3.7.")

    parser = argparse.ArgumentParser()
    define_simulator_parser(parser)
    args = parser.parse_args()
    status = run_simulator(args)
    os._exit(status)