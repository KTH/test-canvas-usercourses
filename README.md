# test-canvas-usercourses
A little test program for a specific canvas api we use.

We seem to have a problem that some course rooms are sometimes missing
from a response.
This tests shows that sometimes some rooms are duplicated, but the
total number of rooms included the duplicates stays the same, so when
some rooms are duplicated, others are missing.

To run the test, copy `auth.in.py` to `auth.py` and provide a canvas
key and a SIS user id, then run `test.py`.
