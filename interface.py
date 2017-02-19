import sys
import getopt
sys.dont_write_bytecode = True
import glicko2
import os.path
import operator

def verify_file_exists(fstring):
    if os.path.isfile(fstring):
#        print "%s exists!" % fstring
        return True
    else:
        print "%s does NOT exist!" % fstring
        return False

def match(a, b, d):
#    print a
#    print "Old Rating: " + str(d[a].rating)
#    print("Old Rating Deviation: " + str(d[a].rd))
#    print("Old Volatility: " + str(d[a].vol))
#    print b
#    print "Old Rating: " + str(d[b].rating)
#    print("Old Rating Deviation: " + str(d[b].rd))
#    print("Old Volatility: " + str(d[b].vol))
    aRatingList = []
    aRatingList.append(d[a].rating)
    aDevList = []
    aDevList.append(d[a].rd)
    aBool = []
    aBool.append(1)
    bRatingList = []
    bRatingList.append(d[b].rating)
    bDevList = []
    bDevList.append(d[b].rd)
    bBool = []
    bBool.append(0)
    d[a].update_player(aRatingList, aDevList, aBool)
    d[b].update_player(bRatingList, bDevList, bBool)
#    print a
#    print("New Rating: " + str(d[a].rating))
#    print("New Rating Deviation: " + str(d[a].rd))
#    print("New Volatility: " + str(d[a].vol))
#    print b
#    print("New Rating: " + str(d[b].rating))
#    print("New Rating Deviation: " + str(d[b].rd))
#    print("New Volatility: " + str(d[b].vol))

def update_players(a, b, d):
#    print "Won: %s, Lost: %s" % (a, b)
    if (a not in d) and (b not in d):
#        print "both %s and %s not in database yet" % (a, b)
        d[a] = glicko2.Player()
        d[b] = glicko2.Player()
        match(a, b, d)
    elif (a not in d) and (b in d):
#        print "%s not in d, but %s in d" % (a, b)
        d[a] = glicko2.Player()
        match(a, b, d)
    elif (a in d) and (b not in d):
#        print "%s in d, but %s not in d" % (a, b)
        d[b] = glicko2.Player()
        match(a, b, d)
    else:
#        print "%s and %s in d" % (a, b)
        match(a, b, d)
#    print ""

def create_ratings(fstring):
    f = open(fstring, 'r')
    i = 1
    d = {}
    for line in f:
        l = line.split()
#        update_players(l[0].lower(), l[1].lower(), d)
        update_players(l[0], l[1], d)

    return d

def print_rankings(l, d):
    i = 1
    for key in l:
        print "%d. %s, %f" % (i, key, d[key[0]].rd)
        i += 1

def main(argv):
#    print "%s\t%d" % (argv, len(argv))
    if len(argv) == 2:
        if verify_file_exists(argv[1]):
            d = create_ratings(argv[1])
            e = {}
            for key in d:
                e[key] = d[key].rating
#            print e
            sorted_e = sorted(e.items(), key = operator.itemgetter(1)) # this is a list
            sorted_e.reverse()
            print_rankings(sorted_e, d)
    else:
        print "Usage: python interface.py [filename]"
        
        
    # take file or manual input
    # get players and have them play against each other
    # update scores
    # modify database simultaneously

if __name__ == "__main__":
    main(sys.argv)
