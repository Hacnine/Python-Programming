
# start here
import re

N = int(input())
for _ in range(N):
    t = input().strip()

    if re.search(r'[A-Z].*[A-Z]', t) is not None and re.search(r'[0-9].*[0-9].*[0-9]', t) is not None \
            and re.search(r'^[a-zA-Z0-9]*$', t) is not None and re.search(r'(.).*\1', t) is None and len(t) == 10:
        print('Valid')
    else:
        print('Invalid')
