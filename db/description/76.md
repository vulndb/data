'X-Content-Type-Options' is a type of HTTP header that can be used to prevent MIME
content-sniffing attacks in Internet Explorer and Google Chrome. MIME content-sniffing
is a mechanism that allows browsers to inspect and dynamically guess the content
type and file type.

MIME Sniffing checking algorithm has known problems which
might allow users to upload files that might contain malicous code. If an attacker
can spoof a file type/content and upload it to the application successfully, it is
possible to inject malicous code which can be downloaded and viewed by other
users of the application. This can lead to attacks such as persistant Cross-Site Scripting.