import bitcoinrpc

# JSON-RPC server user, password.  Uses HTTP Basic authentication.
rpcuser = "user"
rpcpass = "passwd"
address = "1JhvTbFh4tF5MWx3w8v938YmsXV5CeaKYp"
#address = "16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"

connection = bitcoinrpc.connect_to_remote(rpcuser, rpcpass, host='localhost', port=9333, use_https=False)
transactions = connection.listreceivedbyaddress(address)
print transactions
