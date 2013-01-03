suds-passworddigest
===================

adds Web Services Security PasswordDigest authentication to SUDS

Installation
----------------

installation is simple

    pip install suds-passworddigest

or

    pip install git+https://github.com/suvit/suds-passworddigest


Usage
-------------------

    from suds.client import Client
    from suds.wsse import Security

    from suds_passworddigest import UsernameDigestToken

    client = Client()
    security = Security()
    token = UsernameDigestToken('my_username', 'my_pass')
    security.tokens.append(token)
    client.set_options(wsse=security)
