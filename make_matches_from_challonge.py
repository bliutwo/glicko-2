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

def get_challonge_matches(username, api_key, url):
    t_str = parse_link(url)
    matches = get_info(username, api_key, url, "/matches.json", t_str)
    ids = get_info(username, api_key, url, "/participants.json", t_str)
    return (matches, ids)
    
def main(argv):
    if len(argv) == 4:
        s = get_challonge_matches(argv[1], argv[2], argv[3])
        filename_matches = parse_link(argv[3]) + '_matches.json'
        f_matches = open(filename_matches, 'w')
        for l in s[0]:
            f_matches.write(l)
#            f.write('\n')
        f_matches.close()
        filename_ids = parse_link(argv[3]) + '_ids.json'
        f_ids = open(filename_ids, 'w')
        for l in s[1]:
            f_ids.write(l)
#            f.write('\n')
        f_ids.close()

    else:
        print "Usage: python make_matches_from_challonge.py [username] [api-key] [url]"

if __name__ == "__main__":
    main(sys.argv)
