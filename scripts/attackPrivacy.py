from web3 import Web3
from eth_abi import encode_abi
from Crypto.Hash import keccak


w3 = Web3(
    Web3.HTTPProvider("https://goerli.infura.io/v3/7755d5bcc3fe48e39078a9b963f1f3bf")
)


contract_address = "0xd0129813CB010B8A822c9992762De1ECE54F4C84"
slot_storage_long = "0x8fc011189a555e9d496f2f55b164a1a08925a2971404ea5435c360e2a5102a03"
slot_storage_short = slot_storage_long[2:34]


argument = slot_storage_short + "0" * 32

# print(int(Web3.soliditySha3(['string', 'uint256', 'uint256'], [age ,2, 3]), 16))


def get_method_hex(method_selector_bytes):
    # method = b"unlock(bytes16)"
    k = keccak.new(digest_bits=256)
    method_hex = k.update(method_selector_bytes).hexdigest()
    method_hex_8_bits = method_hex[:8]
    return method_hex_8_bits


def main():
    instance = "0xd0129813CB010B8A822c9992762De1ECE54F4C84"
    account = "0x42DAeF8CCFB20b9f8Fb65ef94882fa3EcFC865d3"
    private_key = ""

    nonce = w3.eth.getTransactionCount(account)

    data = "0x" + get_method_hex(b"unlock(bytes16)") + argument

    tx = {
        "nonce": nonce,
        "to": instance,
        "gas": 200000,
        "chainId": 5,
        "maxFeePerGas": Web3.toWei(4, "gwei"),
        "maxPriorityFeePerGas": Web3.toWei(2, "gwei"),
        "data": data,
    }

    # sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)

    # send transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # get transaction hash
    print(w3.toHex(tx_hash))


main()
