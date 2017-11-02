HTTP by itself is a stateless protocol; therefore, the server is
unable to determine which requests are performed by which client and
which clients are authenticated or unauthenticated.

The use of HTTP
cookies within the headers allows a web server to identify each
individual client and can thus determine which clients hold valid
authentication from those that do not. These are known as session
cookies or session tokens.

To prevent clients from being able to
guess each other's session token, each assigned session token should
be entirely random and be different whenever a session is established
with the server.

Session fixation occurs when the client is able to
specify their own session token value and the value of the session
cookie is not changed by the server after successful authentication.
Occasionally, the session token will also remain unchanged for the
user independently of how many times they have authenticated.
Cyber-criminals will abuse this functionality by sending crafted URL
links with a predetermined session token within the link. The
cyber-criminal will then wait for the victim to login and become
authenticated. If successful, the cyber-criminal will know a valid
session ID and therefore have access to the victim's session.

The tool
has discovered that it is able to set its own session token.