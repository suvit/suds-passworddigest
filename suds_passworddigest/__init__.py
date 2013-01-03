
import base64
import datetime
import hashlib
from time import time, strftime, gmtime

from suds.sax.element import Element
from suds.sax.date import UTC
from suds.wsse import UsernameToken, wssens


VERSION = '0.1.0'


wspassd = ('Type',
    'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest')
wsenctype = ('EncodingType',
    'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary')


class UsernameDigestToken(UsernameToken):
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
        if self.nonce is None:
           self.setnonce()
        if self.created is None:
           self.setcreated()
        sha1 = hashlib.sha1(str(self.nonce) + \
                            str(UTC(self.created)) + self.password)
        p.setText(base64.b64encode(sha1.digest()))
        p.set(wspassd[0], wspassd[1])
        root.append(p)

        n = Element('Nonce', ns=wssens)
        n.setText(base64.b64encode(self.nonce))
        n.set(wsenctype[0], wsenctype[1])
        root.append(n)

        n = Element('Created', ns=wsuns)
        n.setText(str(UTC(self.created)))
        root.append(n)

        return root
