Basic Access Authentication is an authentication method which uses base64 encoding
and transmits login credentials in cleartext between a server and client. This is
considered insecure because credentials are transmitted over unencrypted channels
which makes it vulnerable to network eavesdropping attacks. Furthermore, base64
encoding is considered weak because it can be easily decoded to reveal the original
content.

If an application requires authentication, it will send a `WWW-Authenticate`
header with a `401 Unauthorized` HTTP status code. Then, the client will need to send
the server credentials through an `Authorization` header. The credentials are transmitted
as a 'name:password' string format in the header.A well-positioned attacker can capture
the usernames and passwords by sniffing traffic coming to these services.