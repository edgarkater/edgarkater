from check_pw import *

reset_wort(4)
aplhabet=string.ascii_lowercase

for letter4 in aplhabet:
    for letter3 in aplhabet:
        for letter2 in aplhabet:
            for letter1 in aplhabet:
                wort = letter4+letter3+letter2+letter1
                if check(wort):
                    print(wort)
                    break