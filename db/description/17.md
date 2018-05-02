Web applications occasionally use parameter values to store the
location of a file which will later be required by the server.

An
example of this is often seen in error pages, where the actual file
path for the error page is stored in a parameter value -- for example
`example.com/error.php?page=404.php`.

A file inclusion occurs when
the parameter value (ie. path to file) can be substituted with the
path of another resource on the same server, effectively allowing the
displaying of arbitrary, and possibly restricted/sensitive, files.
The tool discovered that it was possible to substitute a parameter
value with another resource and have the server return the contents of
the resource to the client within the response.