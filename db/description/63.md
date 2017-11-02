The `TRACE` HTTP method allows a client so send a request to the
server, and have the same request then send back in the server's
response. This allows the client to determine if the server is
receiving the request as expected or if specific parts of the request
are not arriving as expected. For example incorrect encoding or a load
balancer has filtered or changed a value. On many default
installations the `TRACE` method is still enabled.

While not
vulnerable by itself, it does provide a method for cyber-criminals to
bypass the `HTTPOnly` cookie flag, and therefore could allow a XSS
attack to successfully access a session token.

The tool has discovered
that the affected page permits the HTTP `TRACE` method.