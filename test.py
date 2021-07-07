#! /usr/bin/env python3
from collections import Counter
from requests import Session
from auth import CANVAS_BASE_URL, CANVAS_API_KEY, testuser
from sys import argv
from time import time

def check_room_ids(user_id):
    """Run the test for the user with the given sis user_id."""
    url = CANVAS_BASE_URL + "api/v1/users/sis_user_id:" + user_id + "/courses"
    http = Session()
    http.headers.update({'Authorization': CANVAS_API_KEY})
    print("First:", url)
    start = time()
    r = http.get(url, params={'per_page': 96, 'include': ['sections']}, timeout=15)
    print("Got %r in %s s" % (r.url, time() - start))
    ids = response_ids(r, 1)
    all_ids = [ids]

    while 'next' in r.links:
        print("Next:", r.links['next']['url'])
        start = time()
        r = http.get(r.links['next']['url'], timeout=15)
        print("Got %r in %s s" % (r.url, time() - start))
        ids = response_ids(r, len(all_ids) + 1)
        for n, x in enumerate(all_ids):
            # This often happens
            dups = set(x).intersection(set(ids))
            if dups:
                print("DUPLICATES page %s vs %s: %s" % (len(all_ids) + 1, n + 1, dups))
        all_ids.append(ids)

    flat = [item for subl in all_ids for item in subl]
    if len(flat) != len(set(flat)):
        print("Got %s courses, but only %s distinct" % (len(flat), len(set(flat))))
    else:
        print("Got %s distinct courses" % len(flat))


def response_ids(r, page_no):
    """Check that a response was ok, and get the room ids from the json body."""
    r.raise_for_status()
    ids = [c.get('id') for c in r.json()]
    print("Page %s: %s (%s courses)" % (page_no, ids, len(ids)))

    # I have NOT seen this happen
    dups = [x for (x,n) in Counter(ids).items() if n>1]
    if dups:
        print("DUPLICATES IN page %s: %s" % (len(all_ids) + 1, dups))

    return ids

if len(argv) == 2:
    print("Checking courses for %s" % argv[1])
    check_room_ids(argv[1])
else:
    print("Checking courses for %s (%s)" % (testuser.sisid, testuser.name))
    check_room_ids(testuser.sisid)
