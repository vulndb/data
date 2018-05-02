Web applications occasionally use DOM input values to store the
address of the page to which the client will be redirected -- for
example: `yoursite.com/#/?redirect=www.yoursite.com/404.asp`

An
unvalidated redirect occurs when the client is able to modify the
affected parameter value and thus control the location of the
redirection. For example, the following URL
`yoursite.com/#/?redirect=www.anothersite.com` will redirect to
`www.anothersite.com`.

Cyber-criminals will abuse these
vulnerabilities in social engineering attacks to get users to
unknowingly visit malicious web sites.

The tool has discovered that
the web page does not validate the parameter value prior to
redirecting the client to the injected value.