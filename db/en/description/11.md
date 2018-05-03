HTTP by itself is a stateless protocol. Therefore the server is unable
to determine which requests are performed by which client, and which
clients are authenticated or unauthenticated.

The use of HTTP cookies
within the headers, allows a web server to identify each individual
client and can therefore determine which clients hold valid
authentication, from those that do not. These are known as session
cookies.

When a cookie is set by the server (sent the header of an
HTTP response) there are several flags that can be set to configure
the properties of the cookie and how it is to be handled by the
browser.

One of these flags represents the host, or domain. for which
the cookie can be used.

When the cookie is set for the parent domain,
rather than the host, this could indicate that the same cookie could
be used to access other hosts within that domain. While there are many
legitimate reasons for this, it could also be misconfiguration
expanding the possible surface of attacks.