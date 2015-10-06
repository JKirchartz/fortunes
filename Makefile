#
# Make plaintext quote lists into fortune files
# Separate quotes with a newline containing only '%'
#

POSSIBLE += $(shell ls -1 | egrep -v '\.dat|README|Makefile' | sed -e 's/$$/.dat/g')

all: ${POSSIBLE}

%.dat : %
	@strfile $< $@


# vim:ft=make
#
