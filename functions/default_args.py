def net_price(list_price, discount=0, tax=0.23): # discount and tax have default values, default must be palced after non-defaults 
    return list_price * (1-discount) * (1+tax)


print(net_price(500))