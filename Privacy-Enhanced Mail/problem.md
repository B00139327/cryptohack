PEM is a popular format for sending and receiving keys, certificates, and other cryptographic material. It looks like:

-----BEGIN RSA PUBLIC KEY-----
MIIBCgKC... (a whole bunch of base64)
-----END RSA PUBLIC KEY-----

It wraps base64-encoded data by a one-line header and footer to indicate how to parse the data within. Perhaps unexpectedly, it's important for there to be the correct number of hyphens in the header and footer, otherwise cryptographic tools won't be able to recognise the file.

The data that gets base64-encoded is DER-encoded ASN.1 values. Confused? Here is more information about what these acronyms mean but the complexity is there for historical reasons and going too deep into the details may drive you insane.

Extract the private key d as a decimal integer from this PEM-formatted RSA key.

privacy_enhanced_mail.pem

