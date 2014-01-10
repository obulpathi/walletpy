import bitcoinrpc
from bitcoinrpc.exceptions import InsufficientFunds

# JSON-RPC server user, password.  Uses HTTP Basic authentication.
rpcuser="user"
rpcpass="passwd"
fromaddress = "1JhvTbFh4tF5MWx3w8v938YmsXV5CeaKYp"
toaddress = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
amount = "2.0"

connection = bitcoinrpc.connect_to_remote(rpcuser, rpcpass, host='localhost', port=9333, use_https=False)

connection.sendtoaddress(fromaddress, toaddress, amount)
print "From: ", fromaddress, "Paid", amount, " to ", toaddress
