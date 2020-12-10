#
# Make plaintext quote lists into fortune files
#

POSSIBLE += $(shell ls -1 | egrep -v '\.dat|README|Makefile|bin' | sed -e 's/$$/.dat/g')

all: ${POSSIBLE}

%.dat : %
	@strfile $< $@


# vim:ft=make
#
