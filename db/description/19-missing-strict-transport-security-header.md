The HTTP protocol by itself is clear text, meaning that any data that
is transmitted via HTTP can be captured and the contents viewed. To
keep data private and prevent it from being intercepted, HTTP is often
tunnelled through either Secure Sockets Layer (SSL) or Transport Layer
Security (TLS). When either of these encryption standards are used, it
is referred to as HTTPS.

HTTP Strict Transport Security (HSTS) is an
optional response header that can be configured on the server to
instruct the browser to only communicate via HTTPS. This will be
enforced by the browser even if the user requests a HTTP resource on
the same server.

Cyber-criminals will often attempt to compromise
sensitive information passed from the client to the server using HTTP.
This can be conducted via various Man-in-The-Middle (MiTM) attacks or
through network packet captures.

The tool discovered that the affected
application is using HTTPS however does not use the HSTS header.