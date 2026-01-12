#!/bin/bash

set -e

cd $(dirname $0)

sphinx-apidoc -H "API Reference" -f -e -q -o ./source/api ../ok_palette_lab
