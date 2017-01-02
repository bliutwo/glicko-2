import sys
sys.dont_write_bytecode = True
import requests

def parse_link(url):
    pattern = "challonge.com/"
    return url.split(pattern, 1)[1]

def get_info(username, api_key, url, info_str, t_str):
    l = []
    data = requests.get
    data = requests.get("https://api.challonge.com/v1/tournaments/" + \
                         t_str + info_str, auth = (username, api_key))
    for line in data:
        l.append(line)
    print "sizeof " + info_str + "_data: " + str(len(l))
    return l

# arguments:
# m: matches_str, this is a string that contains the contents of the matches json
# i: ids_str, this is a string that contains the contents of the ids json
def parse_matches_ids_strs(m, i):
    pairs = []
    m_list = m.split("}}")
    i_list = i.split("}}")
    for item in m_list:
        print item
        print
    print
    for item in i_list:
        print item
        print
    assert(False)
    pairs.append((m, i))
    return pairs

# returns a list of tuples (winner, loser)
def get_challonge_matches(username, api_key, url):
    t_str = parse_link(url)
    matches = get_info(username, api_key, url, "/matches.json", t_str)
    ids = get_info(username, api_key, url, "/participants.json", t_str)
    matches_str = ""
    for l in matches:
        matches_str += (l)
    ids_str = ""
    for l in ids:
        ids_str += l
    match_pairs = parse_matches_ids_strs(matches_str, ids_str)
    return match_pairs
    
def main(argv):
    if len(argv) == 4:
        match_pairs = get_challonge_matches(argv[1], argv[2], argv[3])
        filename_matches = parse_link(argv[3]) + '_matches.json'
        f_matches = open(filename_matches, 'w')
        for pair in match_pairs:
            line = pair[0] + " " + pair[1]
            f_matches.write(line)
            f_matches.write('\n')
        f_matches.close()
    else:
        print "Usage: python make_matches_from_challonge.py [username] [api-key] [url]"

if __name__ == "__main__":
    main(sys.argv)
