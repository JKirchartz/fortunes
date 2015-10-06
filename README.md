# Fortune Files

Quote lists have a line or lines containing a quote, then a line that's empty
except for a '%' to separate it from the rest.  ex:

    Let's just pretend Quote 1 is very
    ...very...
    ...very...
    long.
    %
    and quote 2 is short
    %

after adding a new file, "compile" it with

    make

use these with `fortune` like:

    fortune ~/dotfiles/scripts/fortune


* [handey](handey)
  Jack Handey quotes, because you're good enough, you're smart enough, and
  gosh-darnit people like you.
* [memebomb](memebomb)
  [Discordian memebombs][1] scraped with [kwotes.py][2]
* [Makefile](Makefile)
  make & update new fortune files with make

[1]: http://principiadiscordia.com/memebombs/
[2]: https://gist.github.com/JKirchartz/5383142
