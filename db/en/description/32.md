The HTTP protocol by itself is clear text, meaning that any data that
is transmitted via HTTP can be captured and the contents viewed. To
keep data private and prevent it from being intercepted, HTTP is often
tunnelled through either a Secure Sockets Layer (SSL), or Transport
Layer Security (TLS) connection. When either of these encryption
standards are used, it is referred to as HTTPS.

Cyber-criminals will
often attempt to compromise sensitive information passed from the
client to the server using HTTP. This can be conducted via various
different Man-in-The-Middle (MiTM) attacks or through network packet
captures.

The tool discovered that the affected site is utilising both
HTTP and HTTPS. While the HTML code is served over HTTPS, the server
is also serving resources over an unencrypted channel, which can lead
to the compromise of data, while providing a false sense of security
to the user.