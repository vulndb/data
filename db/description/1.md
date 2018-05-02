There are a number of HTTP methods that can be used on a webserver
(`OPTIONS`, `HEAD`, `GET`, `POST`, `PUT`, `DELETE` etc.). Each of
these methods perform a different function and each have an associated
level of risk when their use is permitted on the webserver.

A client
can use the `OPTIONS` method within a request to query a server to
determine which methods are allowed.

Cyber-criminals will almost
always perform this simple test as it will give a very quick
indication of any high-risk methods being permitted by the server.
The tool discovered that several methods are supported by the server.