import MetaTrader5 as mt5

print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)
# cred
login = 51184802
password = "qUidNXzU"
server = "ICMarketsSC-Demo"


mt5.initialize( login=login, server=server, password=password, )

if not mt5.initialize( login=login, server=server, password=password, ):
    print("initialize() failed, error code =",mt5.last_error())
    quit()
else:
    print("successfully logged in")