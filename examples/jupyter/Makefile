SHELL := /bin/bash
#-----------------------------------------------
#    __  __       _         __ _ _
#   |  \/  | __ _| | _____ / _(_) | ___
#   | |\/| |/ _  | |/ / _ \ |_| | |/ _ \
#   | |  | | (_| |   <  __/  _| | |  __/
#   |_|  |_|\__,_|_|\_\___|_| |_|_|\___|
#
#-----------------------------------------------
#         Makefile for Pyncare PRESS
#-----------------------------------------------
#	Author:      Efrain Torres-Lomas
#	Email:       efrain@fisica.ugto.mx
#	Github:      https://github.com/elchinot7
#-----------------------------------------------
#	Description:
#	     Convert:  Jupyter Nb => Slides HTML
#-----------------------------------------------

.PHONY: press

NOTEBOOK = phi2@poincare_press_COPY.ipynb

default: press

press:
	jupyter-nbconvert --to slides $(NOTEBOOK) --reveal-prefix=reveal.js --post serve
