There are a number of HTTP methods that can be used on a webserver
(for example `OPTIONS`, `HEAD`, `GET`, `POST`, `PUT`, `DELETE `etc.).
Each of these methods perform a different function, and each has an
associated level of risk when their use is permitted on the webserver.
The `<Limit>` directive within Apache's `.htaccess` file allows
administrators to define which of the methods they would like to
block. However, as this is a blacklisting approach, it is inevitable
that a server administrator may accidentally miss adding certain HTTP
methods to be blocked, thus increasing the level of risk to the
application and/or server.