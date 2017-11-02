Cross-Origin Resource Sharing (CORS) is one of the new HTML5
technologies which is widely implemented to create Web2.0 applications.
CORS allows the browser to perform HTTP requests to a domain outside
the Same-Origin Policy and access the response body. This feature is
secured by a new set of HTTP headers, being `Access-Control-Allow-Origin`
one of the most important ones.



It was possible to identify an HTTP response which contained the
`Access-Control-Allow-Origin` header value set to '*', which allows any
third-party domain to perform requests and read the responses.
While this configuration is not a vulnerability per-se, it's only
recommended for sites which provide information that's public such as
weather or stock prices.