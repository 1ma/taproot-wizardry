# Copyright (C) 2018-2025 The python-bitcoin-utils developers
#
# This file is part of python-bitcoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoin-utils, including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.
from bitcoinutils.hdwallet import HDWallet
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, TxWitnessInput
from bitcoinutils.keys import PrivateKey, P2trAddress


def main():
    # always remember to setup the network
    setup("testnet")

    with open('ghey_wizard.jpeg', 'rb') as f:
        message = f.read()

    priv = PrivateKey("cRpRgTNc6szD5EG5g6z1gY73XPSDZFGnNXRv6o9RG9PBvaFZptit")

    # UTXO of fromAddress
    first_amount = 499888
    txid = "57831d40a5d97e72bec655004e61d0abc6d117f91009db90d2c628d8f947cb66"
    vout = 0

    toAmount = 499776
    toAddress = P2trAddress("tb1pjylrzhkl3twy2aww26hy0umv57nftlc4hha49ysmar50yqw2v4jse35upy")



    pub = priv.get_public_key()

    fromAddress = pub.get_taproot_address(message)
    print(fromAddress.to_string())

    # all amounts are needed to sign a taproot input
    # (depending on sighash)
    amounts = [first_amount]

    # all scriptPubKeys are needed to sign a taproot input
    # (depending on sighash) but always of the spend input
    first_script_pubkey = fromAddress.to_script_pub_key()

    # alternatively:
    # first_script_pubkey = Script(['OP_1', pub.to_taproot_hex()])

    utxos_script_pubkeys = [first_script_pubkey]

    # create transaction input from tx id of UTXO
    txin = TxInput(txid, vout)

    # create transaction output
    txOut = TxOutput(toAmount, toAddress.to_script_pub_key())

    # create transaction without change output - if at least a single input is
    # segwit we need to set has_segwit=True
    tx = Transaction([txin], [txOut], has_segwit=True)

    print("\nRaw transaction:\n" + tx.serialize())

    print("\ntxid: " + tx.get_txid())
    print("\ntxwid: " + tx.get_wtxid())

    # sign taproot input
    # to create the digest message to sign in taproot we need to
    # pass all the utxos' scriptPubKeys and their amounts
    sig = priv.sign_taproot_input(tx, 0, utxos_script_pubkeys, amounts, script_path=False, tapleaf_scripts=message, tweak=True)

    tx.witnesses.append(TxWitnessInput([sig]))

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + tx.serialize())

    print("\nTxId:", tx.get_txid())
    print("\nTxwId:", tx.get_wtxid())

    print("\nSize:", tx.get_size())
    print("\nvSize:", tx.get_vsize())


if __name__ == "__main__":
    main()
