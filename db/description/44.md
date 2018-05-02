A modern web application will be reliant on several different
programming languages.

These languages can be broken up in two
flavours. These are client-side languages (such as those that run in
the browser -- like JavaScript) and server-side languages (which are
executed by the server -- like ASP, PHP, JSP, etc.) to form the
dynamic pages (client-side code) that are then sent to the client.
Because all server side code should be executed by the server, it
should never be seen by the client. However in some scenarios, it is
possible that:


1. The server side code has syntax errors and therefore is not executed
by the server but is instead sent to the client

2. Using crafted requests it is possible to force the server
into displaying the source code of the application without executing it.



As the server-side source code often contains sensitive
information, such as database connection strings or details into the
application workflow, this can be extremely risky.

Cyber-criminals
will attempt to discover pages that either accidentally or forcefully
allow the server-side source code to be disclosed, to assist in
discovering further vulnerabilities or sensitive information.

The tool
has detected server-side source code within the server's response.
_(False positives may occur when requesting binary files such as
images (.JPG or .PNG) and may require manual verification.)_