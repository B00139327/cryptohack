How can you ensure that the person receiving your message knows that you wrote it?

You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.

When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!

We can protect against these attacks by signing the message.

Imagine you write a message M. You encrypt this message with your friend's public key: C = Me0 mod N0.

To sign this message, you calculate the hash of the message: H(M) and "encrypt" this with your private key: S = H(M)d1 mod N1.

In real cryptosystems, it's best practice to use separate keys for encrypting and signing messages.


Your friend can decrypt the message using their private key: m = Cd0 mod N0. Using your public key they calculate s = Se1 mod N1.

Now by computing H(m) and comparing it to s: assert H(m) == s, they can ensure that the message you sent them, is the message that they received!

Sign the flag crypto{Immut4ble_m3ssag1ng} using your private key and the SHA256 hash function.

private.key