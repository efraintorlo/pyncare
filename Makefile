SHELL := /bin/bash

#-----------------------------------------------
#         Makefile for PyncareDynSys
#-----------------------------------------------
#	Author:      Efrain Torres
#	Email:       efraazu@gmail.com
#	Github:      https://github.com/elchinot7
#	Description: This can be used to
#	            - Install
#	            - Reinstall
#	            - Run
#	            python package and scripts
#-----------------------------------------------

#  --------------------------------------
#  Apps needed are different for Linux/Mac
#  --------------------------------------
ifeq ($(shell uname -s),Darwin)
    OPEN = open
	PYTHON = python
else
    OPEN = xdg-open
	PYTHON = python
endif
#  --------------------------------------

.PHONY: plot docs install reinstall

# --------------------------------------
#INSTALL_OPT = install
INSTALL_OPT = develop
INSTALL_DEST = ~/Programs/pyncare
# --------------------------------------
SCRIPTS_DIR = examples
#PYTHON_FILE ?= quintessence_1.py
# --------------------------------------


default: plot

install: setup.py
	python setup.py $(INSTALL_OPT) --prefix=$(INSTALL_DEST)

# ---------------------------------------------------------------------------
# This is the simplest way to install packages into https://cloud.sagemath.com
# This will intall inside
# ~/.local/lib/python2.7/site-packages
# See:
#     https://groups.google.com/forum/#!topic/sage-cloud/5ReEM8DSx1Q
# ---------------------------------------------------------------------------
sage-install: setup.py
	sage --python setup.py install --user

reinstall: setup.py
	python setup.py install --prefix=$(INSTALL_DEST)

plot: $(SCRIPTS_DIR)/$(PYTHON_FILE)
	cd $(SCRIPTS_DIR) && $(PYTHON) -W ignore $(PYTHON_FILE)

docs:
	cd docs && make clean && make html
	$(OPEN) docs/_build/html/index.html

# -----------------------------
# Some styles and colors to be
# used in Terminal outputs
# -----------------------------
REDC = \033[31m
BOLD = \033[1m
GREENC = \033[32m
UNDERLINE = \033[4m
ENDC = \033[0m
# -----------------------------

# --------------------------------------------------------------
help:
	@echo "------------------------------------------------------"
	@echo -e "                    $(UNDERLINE)$(REDC) < Pyncare >$(ENDC)"
	@echo -e "                   $(GREENC) Makefile Menu$(ENDC)"
	@echo "------------------------------------------------------"
	@echo "Please use 'make <target>' where target is one of:"
	@echo
	@echo -e "$(REDC)default$(ENDC)    > Default Action"
	@echo
	@echo -e "               '$(GREENC)Solve & Plot$(ENDC)'"
	@echo
	@echo -e "$(REDC)plot$(ENDC)       > Solve & Plot"
	@echo
	@echo -e "$(REDC)install$(ENDC)    > Install Pyncare"
	@echo
	@echo -e "$(REDC)reinstall$(ENDC)  > Reinstall Pyncare"
	@echo
	@echo -e "$(REDC)docs$(ENDC)       > Generate & shows documentation"
	@echo
	@echo -e "$(REDC)help$(ENDC)       > Show this menu"
	@echo "------------------------------------------------------"
# --------------------------------------------------------------
