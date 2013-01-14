# -*- coding: utf-8 -
import base64
import datetime
import hashlib
from time import time, strftime, gmtime

from suds.sax.element import Element
from suds.sax.date import UTC
from suds.wsse import UsernameToken, wssens, wsuns


wspassd = ('Type',
    'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest')
wsenctype = ('EncodingType',
    'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary')


class UsernameDigestToken(UsernameToken):

    def setcreated(self, *args, **kwargs):
        UsernameToken.setcreated(self, *args, **kwargs)
        self.created = str(UTC(self.created))

    def reset(self):
        self.nonce = None
        self.created = None

    def generate_digest(self):
        if self.nonce is None:
           self.setnonce()
        if self.created is None:
           self.setcreated()
        sha1 = hashlib.sha1(str(self.nonce) + \
                            str(self.created) + self.password)
        digest = base64.encodestring(sha1.digest())[:-1]
        return digest

    def xml(self):
        """
        Get xml representation of the object.
        @return: The root node.
        @rtype: L{Element}
        """
        root = Element('UsernameToken', ns=wssens)

        u = Element('Username', ns=wssens)
        u.setText(self.username)
        root.append(u)

        p = Element('Password', ns=wssens)
        p.setText(self.generate_digest())
        p.set(wspassd[0], wspassd[1])
        root.append(p)

        n = Element('Nonce', ns=wssens)
        n.setText(base64.encodestring(self.nonce)[:-1])
        n.set(wsenctype[0], wsenctype[1])
        root.append(n)

        n = Element('Created', ns=wsuns)
        n.setText(self.created)
        root.append(n)

        self.reset()
        return root
