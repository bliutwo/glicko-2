import sys
sys.dont_write_bytecode = True
import requests
import os

def find_subdomain(url):
    pattern = "://"
    s = url.split(pattern,1)[1]
    if s.startswith('challonge'):
        return ''
    else:
        subdomain = s.split('.challonge', 1)[0]
        total = subdomain + '-'
        return total

def parse_link(url):
    pattern = "challonge.com/"
    end = url.split(pattern, 1)[1]
    subdomain = find_subdomain(url)
    combo = subdomain + end
    return combo

def get_info(username, api_key, url, info_str, t_str):
    l = []
    data = requests.get
    data = requests.get("https://api.challonge.com/v1/tournaments/" + \
                         t_str + info_str, auth = (username, api_key))
    for line in data:
        l.append(line)
    print("sizeof " + info_str + "_data: " + str(len(l)))
    return l

# arguments:
# m: matches_str, this is a string that contains the contents of the matches json
# i: ids_str, this is a string that contains the contents of the ids json
def parse_matches_ids_strs(m, i):
    m_list = m.split("}}")
    i_list = i.split("}}")
    # make a list of matches (winner, loser)
    match_pairs = []
    for item in m_list:
        if item == "]":
            break
        begin_index = item.find("winner_id")
        end_index = item.find(",\"started")
        substr = item[begin_index:end_index]
        # get winner and loser id
        win_begin_index = substr.find("\":") + 2
        win_end_index = substr.find(",\"")
        winid = substr[win_begin_index:win_end_index]
        los_begin_index = substr.find("loser_id\":") + 10
        losid = substr[los_begin_index:]
        match_pairs.append((winid, losid))
    # make a dictionary of ids {id: username}
    id_pairs = {}
    for item in i_list:
        begin_index = item.find("\"id\"") + 5
        end_index = item.find(",\"tournament")
        id_num = item[begin_index:end_index]
        bi = item.find("\"name\":") + 8
        ei = item.find("\"seed\":") - 2
        name = item[bi:ei]
        name = name.replace(" ", "_")
        # name = name.lower()
        id_pairs[id_num] = name
    # using list of matches, replace ids with usernames
    print("number of participants: %d" % (len(id_pairs) - 1))
    pairs = []
    for match in match_pairs:
        w = id_pairs[match[0]]
        l = id_pairs[match[1]]
        pairs.append((w, l))
    # return pairs
    print("number of matches: %d\n" % len(pairs))
    return pairs

# returns a list of tuples (winner, loser)
def get_matches(username, api_key, multiple_urls):
    all_match_pairs = []
    with open(multiple_urls) as f:
        for line in f:
            if line[len(line) - 1] == '\n':
                url = line[:-1] # we don't want the newline char included
            else:
                url = line
            print("BRACKET: %s" % url)
            t_str = parse_link(url)
            matches = get_info(username, api_key, url, "/matches.json", t_str)
            ids = get_info(username, api_key, url, "/participants.json", t_str)
            matches_str = ""
            for l in matches:
                matches_str += l.decode('utf-8')
            ids_str = ""
            for l in ids:
                ids_str += l.decode('utf-8')
            match_pairs = parse_matches_ids_strs(matches_str, ids_str)
            print
            for p in match_pairs:
                all_match_pairs.append(p)
    return all_match_pairs
    
def main(argv):
    if len(argv) == 4:
        match_pairs = get_matches(argv[1], argv[2], argv[3])
        name = os.path.splitext(argv[3])[0]
        # filename_matches = 'matches/' + name + '_matches.txt'
        filename_matches = name + '_matches.txt'
        f_matches = open(filename_matches, 'wb')
        first = True
        for pair in match_pairs:
            if first:
                first = False
            else:
                f_matches.write('\n'.encode('utf-8'))
            line = pair[0] + " " + pair[1]
            f_matches.write(line.encode('utf-8'))
        f_matches.close()
        print("Added %s" % filename_matches)
    else:
        print("Usage: python make_matches_from_urls.py [username] [api-key] [filename_containing_bracket_urls]")

if __name__ == "__main__":
    main(sys.argv)
