# A canvas base url and API key is needed.
CANVAS_BASE_URL = 'https://canvas.kth.se/'
CANVAS_API_KEY = 'Bearer ...'

class TestUser:
    def __init__(self, sisid, name):
        self.sisid = sisid
        self.name = name

# Replace with some teacher that has lots of course rooms.
testuser = TestUser('u1xyzzyy', 'Test User')
