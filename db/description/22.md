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

The `HttpOnly` flag assists in the prevention of client
side-scripts (such as JavaScript) accessing and using the cookie.
This can help prevent XSS attacks targeting the cookies holding the
client's session token (setting the `HttpOnly` flag does not prevent,
nor safeguard against XSS vulnerabilities themselves).