from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey

setup("testnet")

with open('ghey_wizard.jpeg', 'rb') as f:
    jpeg = f.read()

internal_private_key = PrivateKey("cRpRgTNc6szD5EG5g6z1gY73XPSDZFGnNXRv6o9RG9PBvaFZptit")
internal_public_key = internal_private_key.get_public_key()

normal_address = internal_public_key.get_taproot_address()
tweaked_address = internal_public_key.get_taproot_address(scripts=jpeg)

print("internal public key:")
print("  " + internal_public_key.to_x_only_hex() + "\n")
print("'normal' taproot address for this public key (default BIP-86 tweak):")
print("  " + normal_address.to_string() + "\n")
print("tweaked address with arbitrary data:")
print("  " + tweaked_address.to_string() + "\n")
