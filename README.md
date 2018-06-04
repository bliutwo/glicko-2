Uses glicko-2 rating system, documented here http://www.glicko.net/glicko.html

Usage:
```
python3 make_matches_from_challonge.py [username] [api-key] [filename_containing_bracket_urls]
```
THEN:

```
python3 interface.py [filename_containing_matches]
```

To find and replace tags in the resulting matches file,
```
python find_and_replace.py [filename_containing_matches]
```

Tournaments included in 2016-17 ranking period:
- http://challonge.com/stanfordwelcome
- http://challonge.com/lantanalounge1


Tournaments included in 2015-16 ranking period:
- http://challonge.com/robinson_weekly_1
- http://challonge.com/stanfordTreehacks2016
- http://challonge.com/StanfordMelee1
- http://challonge.com/robinson_2
- http://challonge.com/robinson_3
- http://challonge.com/robinson_4
- http://challonge.com/robinson_5

Tournaments included in "Inflate bliutwo's Ego" period:
- http://challonge.com/robinson_4
- http://challonge.com/robinson_5
- http://challonge.com/stanfordwelcome
- http://challonge.com/lantanalounge1
