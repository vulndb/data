HTTP response splitting occurs when untrusted data is inserted into
the response headers without any sanitisation.

If successful, this
allows cyber-criminals to essentially split the HTTP response in two.
This is abused by cyber-criminals injecting CR (Carriage Return --
`/r`) and LF (Line Feed -- `
`) characters which will then form the
split. If the CR or LF characters are not processed by the server then
it cannot be exploited.

Along with these characters, cyber-criminals
can then construct their own arbitrary response headers and body which
would then form the second response. The second response is entirely
under their control, allowing for a number of other attacks.