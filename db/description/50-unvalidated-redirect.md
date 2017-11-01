Web applications occasionally use parameter values to store the
address of the page to which the client will be redirected -- for
example: `yoursite.com/page.asp?redirect=www.yoursite.com/404.asp`

An
unvalidated redirect occurs when the client is able to modify the
affected parameter value in the request and thus control the location
of the redirection. For example, the following URL
`yoursite.com/page.asp?redirect=www.anothersite.com` will redirect to
`www.anothersite.com`.

Cyber-criminals will abuse these
vulnerabilities in social engineering attacks to get users to
unknowingly visit malicious web sites.

The tool has discovered that
the server does not validate the parameter value prior to redirecting
the client to the injected value.