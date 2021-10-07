#!/bin/bash

# A script file for Google Colaboratory


# TeX
# apt-get install texlive-latex-extra  &> tex.log
# apt-get install ghostscript &>> tex.log
# apt-get install dvipng &>> tex.log


# https://linux.die.net/man/1/wget
wget -q https://github.com/miscellane/review/raw/develop/review.zip


# https://linux.die.net/man/1/unzip
rm -rf review
unzip -u -q review.zip
rm -rf review.zip