#! /usr/bin/env python3
import requests
from collections import Counter
from auth import CANVAS_BASE_URL, CANVAS_API_KEY, testuser

def check_room_ids(user_id):
    """Run the test for the user with the given sis user_id."""
    url = CANVAS_BASE_URL + "api/v1/users/sis_user_id:" + user_id + "/courses"
    headers = {'Authorization': CANVAS_API_KEY}

    r = requests.get(url, params={'per_page': 50, 'include': ['sections']},
                     headers=headers, timeout=3)
    ids = response_ids(r, 1)
    all_ids = [ids]

    while 'next' in r.links:
        r = requests.get(r.links['next']['url'], headers=headers, timeout=3)
        ids = response_ids(r, len(all_ids) + 1)
        for n, x in enumerate(all_ids):
            # This often happens
            dups = set(x).intersection(set(ids))
            if dups:
                print("DUPLICATES page %s vs %s: %s" % (len(all_ids) + 1, n + 1, dups))
        all_ids.append(ids)

    flat = [item for subl in all_ids for item in subl]
    print("Got %s rooms" % len(flat))
    if len(flat) != len(set(flat)):
        print("... but only %s distinct" % len(set(flat)))


def response_ids(r, page_no):
    """Check that a response was ok, and get the room ids from the json body."""
    r.raise_for_status()
    ids = [c.get('id') for c in r.json()]
    print("Page %s: %s" % (page_no, ids))

    # I have NOT seen this happen
    dups = [x for (x,n) in Counter(ids).items() if n>1]
    if dups:
        print("DUPLICATES IN page %s: %s" % (len(all_ids) + 1, dups))

    return ids


print("Checing rooms for %s (%s)" % (testuser.sisid, testuser.name))
check_room_ids(testuser.sisid)
