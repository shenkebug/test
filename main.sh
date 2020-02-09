#!/bin/bash

set -eux

python test.py $USER $PASSWORD $SENDER $RECEIVER
