# CSI_3480_Lab_5

Whats is a hash function: a mathematical operation that takes an input of any length and converts it into a fixed-length output, known as a hash value or hash, using a one-way process, meaning it's computationally infeasible to reverse

Whats are the properties of a good cryptographic function: deterministic, efficient, collision-resistant, and exhibit the avalanche effect, meaning a small input change results in a large output change

the avalance effect: a small change in the input of the hash function can lead to a very significant and unpredictable change in the ouput. I will prove this in a screenshot inside of my directory.

Explain how digital signatures ensure authenticity and integrity: by using cryptographic hash functions and asymmetric cryptography, which are functions that will encode the message making it harder for somebody to see the conntents.

A digital signature cannot be created with a public key because the process relies on the sender's private key to encrypt a message (or hash of the message), and only the corresponding public key can decrypt and verify that signature

app.py has the hash function example

app1.py has the ASA encryption and RSA example
