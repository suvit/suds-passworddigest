import unittest
import base64

from suds.sax.date import DateTime, UTC
from suds_passworddigest.token import UsernameDigestToken

class SudsTest(unittest.TestCase):
    def test_digest_generation(self):
        token = UsernameDigestToken()
        token.username = 'test'

        # case 1
        token.password = 'test'
        token.nonce = base64.decodestring("8kqcOS9SFYxSRslITbBmlw==")
        token.created = "2012-10-29T08:18:34.836Z"

        self.assertEquals(token.generate_digest(),
                          "LOzA3VPv+2hFGOHq8O6gcEXsc/k=")


        # case 2
        token.password = 'ic3'
        token.nonce = base64.decodestring("m4feQj9DG96uNY1tCoFBnA==")
        token.created = "2012-10-29T08:49:58.645Z"

        self.assertEquals(token.generate_digest(),
                          "K80tK4TyuvjuXvMu++O8twrXuTY=")

        # case 3
        token.password = 'wss22wert'
        token.nonce = base64.decodestring("MzI2NjYyNzYxMQ==")
        token.created = "2012-10-29T05:39:24Z"

        self.assertEquals(token.generate_digest(),
                          "88FDZSIoCwQT9zhMqpcekDvZwVo=")

if __name__ == '__main__':
    unittest.main()
