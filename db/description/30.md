Lightweight Directory Access Protocol (LDAP) is used by web
applications to access and maintain directory information services.
One of the most common uses for LDAP is to provide a Single-Sign-On
(SSO) service that will allow clients to authenticate with a web site
without any interaction (assuming their credentials have been
validated by the SSO provider).

LDAP injection occurs when untrusted
data is used by the web application to query the LDAP directory
without prior sanitisation.

This is a serious security risk, as it
could allow cyber-criminals the ability to query, modify, or remove
anything from the LDAP tree. It could also allow other advanced
injection techniques that perform other more serious attacks.

The tool
was able to detect a page that is vulnerable to LDAP injection based
on known error messages.