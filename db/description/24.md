The browser security model normally prevents web content from one
domain from accessing data from another domain. This is commonly known
as the "same origin policy".

URL policy files grant cross-domain
permissions for reading data. They permit operations that are not
permitted by default. The URL policy file for Silverlight is located,
by default, in the root directory of the target server, with the name
`ClientAccessPolicy.xml` (for example, at
`www.example.com/ClientAccessPolicy.xml`).

When a domain is specified
in `ClientAccessPolicy.xml`, the site declares that it is willing to
allow the operators of any servers in that domain to obtain any
document on the server where the policy file resides.

The
`ClientAccessPolicy.xml` file deployed on this website opens the
server to all domains (use of a single asterisk "*" as a pure wildcard
is supported).