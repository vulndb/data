Web Distributed Authoring and Versioning (WebDAV) is a facility that
enables basic file management (reading and writing) to a web server.
It essentially allows the webserver to be mounted by the client as a
traditional file system allowing users a very simplistic means to
access it as they would any other medium or network share.

If
discovered, attackers will attempt to harvest information from the
WebDAV enabled directories, or even upload malicious files that could
then be used to compromise the server.

The tool discovered that the
affected page allows WebDAV access. This was discovered as the server
allowed several specific methods that are specific to WebDAV
(`PROPFIND`, `PROPPATCH`, etc.), however, further testing should be
conducted on the WebDAV component specifically as the tool does support
this feature.