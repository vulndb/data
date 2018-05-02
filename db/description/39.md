Web applications occasionally use parameter values to store the
location of a file which will later be required by the server.

An
example of this is often seen in error pages, where the actual file
path for the error page is stored in a parameter value -- for example
`example.com/error.php?page=404.php`.

A path traversal occurs when
the parameter value (ie. path to file being called by the server) can
be substituted with the relative path of another resource which is
located outside of the applications working directory. The server then
loads the resource and includes its contents in the response to the
client.

Cyber-criminals will abuse this vulnerability to view files
that should otherwise not be accessible.

A very common example of
this, on *nix servers, is gaining access to the `/etc/passwd` file in
order to retrieve a list of server users. This attack would look like:
`yoursite.com/error.php?page=../../../../etc/passwd`

As path
traversal is based on the relative path, the payload must first
traverse to the file system's root directory, hence the string of
`../../../../`.

The tool discovered that it was possible to substitute
a parameter value with a relative path to a common operating system
file and have the contents of the file included in the response.