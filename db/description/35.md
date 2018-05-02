Origin headers are utilised by proxies and/or load balancers to track
the originating IP address of the client.

As the request progresses
through a proxy, the origin header is added to the existing headers,
and the value of the client's IP is then set within this header.
Occasionally, poorly implemented access restrictions are based off of
the originating IP address alone.

For example, any public IP address
may be forced to authenticate, while an internal IP address may not.
Because this header can also be set by the client, it allows
cyber-criminals to spoof their IP address and potentially gain access
to restricted pages.

The tool discovered a resource that it did not
have permission to access, but been granted access after spoofing the
address of localhost (127.0.0.1), thus bypassing any requirement to
authenticate.