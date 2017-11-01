To restrict access to specific pages on a webserver, developers can
implement various methods of authentication, therefore only allowing
access to clients with valid credentials. There are several forms of
authentication that can be used. The simplest forms of authentication
are known as 'Basic' and 'Basic Realm'. These methods of
authentication have several known weaknesses such as being susceptible
to brute force attacks.

Additionally, when utilising the NTLM
mechanism in a windows environment, several disclosures of information
exist, and any brute force attack occurs against the server's local
users, or domain users if the web server is a domain member.
Cyber-criminals will attempt to locate protected pages to gain access
to them and also perform brute force attacks to discover valid
credentials.

The tool discovered the following page requires NTLM
based basic authentication in order to be accessed.