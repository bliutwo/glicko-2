import sys
sys.dont_write_bytecode = True
import interface

def found_match(s, f_name):
    found = False
    with open(f_name) as f:
        for l in f:
            if l.find(s) != -1:
                return True
    return found

def replace_name(f, r, f_name):
    lines = []
    with open(f_name) as infile:
        for l in infile:
            l = l.replace(f, r)
            lines.append(l)
    with open(f_name, 'w') as outfile:
        for l in lines:
            outfile.write(l)

def main(argv):
    if len(argv) == 2:
        if interface.verify_file_exists(argv[1]):
            print "Now reading: %s" % argv[1]
            while True:
                f_prompt = "Enter the player tag that you want to find: "
                r_prompt = "Enter the new tag you want to replace it with: "
                f = raw_input(f_prompt)
                if found_match(f, argv[1]):
                    print "%s found!" % f
                    r = raw_input(r_prompt)
                    replace_name(f, r, argv[1])
                    print "%s replaced with %s" % (f, r)
                    break
                else:
                    print "%s NOT found!" %f
    else:
        print "Usage: python find_and_replace.py [filename]"
       

if __name__ == "__main__":
    main(sys.argv)
