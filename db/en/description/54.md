XML Path Language (XPath) queries are used by web applications for
selecting nodes from XML documents. Once selected, the value of these
nodes can then be used by the application.

A simple example for the
use of XML documents is to store user information. As part of the
authentication process, the application will perform an XPath query to
confirm the login credentials and retrieve that user's information to
use in the following request.

XPath injection occurs where untrusted
data is used to build XPath queries.

Cyber-criminals may abuse this
injection vulnerability to bypass authentication, query other user's
information, or, if the XML document contains privileged user
credentials, allow the cyber-criminal to escalate their privileges.
The tool injected special XPath query characters into the page and
based on the responses from the server, has determined that the page
is vulnerable to XPath injection.