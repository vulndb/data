Clickjacking (User Interface redress attack, UI redress attack, UI
redressing) is a malicious technique of tricking a Web user into
clicking on something different from what the user perceives they are
clicking on, thus potentially revealing confidential information or
taking control of their computer while clicking on seemingly innocuous
web pages.

The server didn't return an `X-Frame-Options` header which
means that this website could be at risk of a clickjacking attack.
The `X-Frame-Options` HTTP response header can be used to indicate
whether or not a browser should be allowed to render a page inside a
frame or iframe. Sites can use this to avoid clickjacking attacks, by
ensuring that their content is not embedded into other sites.