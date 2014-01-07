import bitcoinrpc
from bitcoinrpc.exceptions import InsufficientFunds

# JSON-RPC server user, password.  Uses HTTP Basic authentication.
rpcuser="user"
rpcpass="passwd"
address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

connection = bitcoinrpc.connect_to_remote(rpcuser, rpcpass, host='localhost', port=9333, use_https=False)

address = "bitcoin address"
amount = 1.00
connection.sendtoaddress(address, amount)
print "Paid", amount, " to ", address
