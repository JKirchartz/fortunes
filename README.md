# Fortune Files

Quote databases have a line or lines containing a quote, then a line that only contains a '%' (percent sign) to separate it from the others.  ex:

    Let's just pretend Quote 1 is very
    ...very...
    ...very...
    long.
    %
    and quote 2 is short
    %

after adding or altering a new file recreate the index files for

    strfile <filename>

you can compile every fortune file in this directory with `make`

use these with `fortune` like:

    fortune ~/path/to/this/repo/named/fortunes

or you can combine these with the fortune files already on your system by asking fortune where it's databases are like so:

    fortune ~/path/to/this/repo/named/fortunes $(fortune -f 2>&1 | head -n1 | cut -d' ' -f2)


* [Makefile](Makefile):
  make & update new fortune files with `make`
* [handey](handey):
  Jack Handey quotes, because you're good enough, you're smart enough, and
  gosh-darnit people like you.
* [chuckfacts](chuckfacts):
  Facts about Chuck Norris (because 2005 should never end)
* [memebomb](memebomb):
  [Discordian memebombs][1] scraped with [kwotes.py][2], plus [krmaxwell's "Discordian Quote Sample"](https://gist.github.com/krmaxwell/7131789), plus [KBuxton's Discordian Quotes](https://kbuxton.com/discordia/discordianquotes.html)
* [alt.discordia][17] "Current state of the Discordian quotes file on Lost Souls LPmud" -- 22/01/1994 usenet Discordian Quote File
* [yow](yow):
  The file consists of Zippy the Pinhead quotations (from various comic books and
  strips by Bill Griffith) notable accesible using the the m-x yow command in GNU Emacs.
* [Oblique Strategies](ObliqueStrategies): Brian Eno's Oblique Strategies cards
  to help you get out of a creative rut.
* [Real Facts](realfacts) as real as Snapple makes 'em!
* [English As She Is Spoke](EnglishAsSheIsSpoke) Familiar Phrases, Idiotisms\[sic\] and Proverbs, and Anecdotes as found in [English As She Is Spoke, or A Jest in Somber Earnest](http://www.gutenberg.org/cache/epub/30411/pg30411-images.html)
* [rfc1925](rfc1925) is taken from [IETF Network Working Group RFC 1925: The Twelve Networking Truths](https://www.ietf.org/rfc/rfc1925.txt)
* [The Seventy Maxims of Maximally Effective Mercenaries](SeventyMaximsOfMaximallyEffectiveMercenaries) is taken from the [Schlock Mercenary][3] webcomic.
* [Enkiv2's Glossary of Tech Industry Terms](enkiv2s-glossary-of-tech-industry-terms) taken from [A short glossary of tech industry terms][7]
* [The Holy Bible: Abridged beyond the point of usefulness](BibleAbridged) by Zach Weinersmith, 2015. Some Rights Reserved.  [Attribution-Noncommercial 3.0 Unported](http://creativecommons.org/licenses/by-nc/3.0/)
* [Anathem Glossary](anathem-glossary) from [Anathem by Neal Stephenson][8], as compiled by [David Blume][9]
* [Infinite States](infinitestates) from [Fortunate by Mr Led][10] (P.S. check out this link for a neat "twitter to fortune file" script)
* [Shower Thoughts](showerthoughts) from [Nullprogram A.K.A. skeeto A.K.A. Chris][11] - he's got [a script][12] to suss these out from Reddit submission histories (P.S. Chris was my best friend in like 1st-6th grade, he's still smarter & younger than me, blows my mind to see him around the web now-a-days.)
* [Simpson's Chalkboard](SimpsonsChalkboard) collected from [Simpsons Wiki][12]
* [Obscure Sorrows](obscuresorrows) from [Dictionary of Obscure Sorrows][13]
* [EPIGRAMS IN PROGRAMMING](epigrams_in_programming) from [exerpts of ACM's SIGPLAN publication, (September, 1982), Article "Epigrams in Programming", by Alan J. Perlis of Yale University.][14]
* [Larry Wall Quotes](lwall-quotes) [http://www.cpan.org/misc/lwall-quotes.txt.gz](https://web.archive.org/web/20110701000000*/http://www.cpan.org/misc/lwall-quotes.txt.gz) containing quips from 1991(ish)-2005(ish)
* [Heraclitus, Fragments](HeraclitusFragments) converted from [Roberto's Collection](https://github.com/r03ert0/Heraclitus-Fragments)
* [Reyna d’Assia: The Key to Immortal Consciousness](immortal_consciousness), teachings from her father, [George Gurdjieff](https://en.wikipedia.org/wiki/George_Gurdjieff). ([source](https://voxpopulisphere.com/2016/05/18/14591/))
* [PA Historical Markers](PA-historical-markers) retrieved from [PHMC Marker Search][15] and parsed with `jq -r '.[] | "\(.markerTitle)\n\(.markerText)\n\(.locationDescription)\n%"' PA-historical-markers.json > PA-historical-markers`
* [Twenty Lessons On Tyranny](Twenty_Lessons_On_Tyranny_LONG) retrieved from [The Author's Newsletter](https://snyder.substack.com/p/twenty-lessons-on-tyranny) summarizes 20 lessons from the book "On Tyranny" - in long or [short](Twenty_Lessons_On_Tyranny) format.
* [Jack Kerouac's Belief & Technique for Modern Prose][16] - 30 "essential" maxims.
* [Tao](tao) quotes compiled by Stefan Stenudd at [Taotastic.com](https://www.taoistic.com/)
* Many other quotes manualy collected, scraped from [goodreads][4] or [brainyquotes][5], or from random sites with my [page-scraping bookmarklet, found here.][6]

[1]: http://principiadiscordia.com/memebombs/
[2]: https://gist.github.com/JKirchartz/5383142
[3]: http://SchlockMercenary.com
[4]: https://gist.github.com/JKirchartz/80ad6ec90d44b58486db89058d2fdb37
[5]: https://gist.github.com/JKirchartz/05b1132a1151bb497bb408fdf4d0cc56
[6]: http://jkirchartz.com/demos/bookmarklets.html
[7]: https://medium.com/@enkiv2/a-short-glossary-of-tech-industry-terms-4b5f9fef8db3
[8]: https://en.wikipedia.org/wiki/Anathem
[9]: http://anathem.dlma.com/
[10]: https://github.com/mrled/fortunate
[11]: https://nullprogram.com/blog/2016/12/01/
[12]: https://simpsons.fandom.com/wiki/List_of_chalkboard_gags
[13]: https://www.dictionaryofobscuresorrows.com/
[14]: http://www.cs.yale.edu/homes/perlis-alan/quotes.html
[15]: https://share.phmc.pa.gov/markers/
[16]: https://www.writing.upenn.edu/~afilreis/88/kerouac-technique.html
[17]: https://www.usenetarchives.com/view.php?id=alt.discordia&mid=PDJocmNobCRvZjRAY2Fycm9sbDEuY2MuZWR1Pg
