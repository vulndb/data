A modern web application will be reliant on several different
programming languages.

These languages can be broken up in two
flavours. These are client-side languages (such as those that run in
the browser -- like JavaScript) and server-side languages (which are
executed by the server -- like ASP, PHP, JSP, etc.) to form the
dynamic pages (client-side code) that are then sent to the client.
Because all server-side code should be executed by the server, it
should only ever come from a trusted source.

Code injection occurs
when the server takes untrusted code (ie. from the client) and
executes it.

Cyber-criminals will abuse this weakness to execute
arbitrary code on the server, which could result in complete server
compromise.

The tool was able to inject specific server-side code and
have the executed output from the code contained within the server
response. This indicates that proper input sanitisation is not
occurring.