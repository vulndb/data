The server accepts SSL connections which use the insecure SSLv2
protocol. SSLv2 is an old implementation of the Secure Sockets Layer
protocol which suffers from a number of security flaws allowing attackers
to capture and alter information passed between a client and the server.



SSLv2 has been deprecated and is no longer recommended. Note that
neither SSLv2 nor SSLv3 meet the U.S. FIPS 140-2 standard, which governs
cryptographic modules for use in federal information systems. Only the
newer TLS (Transport Layer Security) protocol meets FIPS 140-2
requirements.