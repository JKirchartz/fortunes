#
# Make plaintext quote lists into fortune files
#
# Quote lists have a line or lines containing a quote, then a line that's empty 
# except for a '%' to separate it from the rest.
# ex:
#
# Quote 1...
# is long...
# %
# quote 2 is short
# %
#

POSSIBLE += $(shell ls -1 | egrep -v '\.dat|README|Makefile' | sed -e 's/$$/.dat/g')

all: ${POSSIBLE}

%.dat : %
	@strfile $< $@


# vim:ft=make
#
