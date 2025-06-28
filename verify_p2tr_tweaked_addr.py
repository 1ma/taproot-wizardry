from bitcoinutils.setup import setup
from bitcoinutils.keys import PublicKey


setup("testnet")

with open('ghey_wizard.jpeg', 'rb') as f:
    jpeg = f.read()

internal_public_key = PublicKey("1baf348d377cf9a73b39807b051bd7e6921bd9e5f4e78e5640803f1fd9b90501")

tweaked_address = internal_public_key.get_taproot_address(scripts=jpeg)

print("tweaked address with arbitrary data:")
print("  " + tweaked_address.to_string() + "\n")
