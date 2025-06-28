# Taproot Wizardry 🧙

Create the virtualenv from the requirements.txt file.
The code has a hard dependency on the master branch of [bitcoin-utils](https://github.com/karask/python-bitcoin-utils/commits/master/) because it needed a hotfix.

The ghey_wizard.jpeg image can be downloaded from [memepool.space](https://memepool.space/tx/0301e0480b374b32851a9462db29dc19fe830a7f7d7a88b81612b9d42099c0ae)

### Scripts

* create_p2tr_tweaked_addr.py: Creates both a normal BIP-86 address and an address tweaked by arbitrary data from the same private key.

* simple_p2tr_spend_tweak.py: Shows how to spend such a tweaked Taproot address by creating a raw transaction that spends the one I showed in the X thread.

* verify_p2tr_tweaked_addr.py: Recomputes the tweaked address just from the internal public key and the arbitrary data (similar to 1st script, but without the private key part).
