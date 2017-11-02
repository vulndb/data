The HTTP protocol by itself is clear text, meaning that any data that
is transmitted via HTTP can be captured and the contents viewed.

To
keep data private, and prevent it from being intercepted, HTTP is
often tunnelled through either Secure Sockets Layer (SSL), or
Transport Layer Security (TLS). When either of these encryption
standards are used it is referred to as HTTPS.

Cyber-criminals will
often attempt to compromise credentials passed from the client to the
server using HTTP. This can be conducted via various different
Man-in-The-Middle (MiTM) attacks or through network packet captures.
The tool discovered that the affected page contains a `password` input,
however, the value of the field is not sent to the server utilising
HTTPS. Therefore it is possible that any submitted credential may
become compromised.