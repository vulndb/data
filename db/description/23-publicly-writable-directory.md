There are various methods in which a file (or files) may be uploaded
to a webserver. One method that can be used is the HTTP `PUT` method.
The `PUT` method is mainly used during development of applications and
allows developers to upload (or put) files on the server within the
web root.

By nature of the design, the `PUT` method typically does
not provide any filtering and therefore allows sever side executable
code (PHP, ASP, etc) to be uploaded to the server.

Cyber-criminals
will search for servers supporting the `PUT` method with the intention
of modifying existing pages, or uploading web shells to take control
of the server.

The tool has discovered that the affected path allows
clients to use the `PUT` method. During this test, the tool has `PUT` a
file on the server within the web root and successfully performed a
`GET` request to its location and verified the contents.