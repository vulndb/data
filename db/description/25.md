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

One of these flags is known as the `secure` flag. When the
secure flag is set, the browser will prevent it from being sent over a
clear text channel (HTTP) and only allow it to be sent when an
encrypted channel is used (HTTPS).

The tool discovered that a cookie
was set by the server without the secure flag being set. Although the
initial setting of this cookie was via an HTTPS connection, any HTTP
link to the same server will result in the cookie being send in clear
text.