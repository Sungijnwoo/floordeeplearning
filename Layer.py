class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

class MulLayer(object):
    def __init__(self):
        self.x = None
        self.y = None
    
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy

class AddLayer(object):
    def __init__(self):
        pass

    def forward(sef, x, y):
        return x + y
    
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy




if __name__ == "__main__":
    # apple = 100
    # apple_num = 2
    # orange = 150
    # orange_num = 3
    # tax = 1.1

    # mul_apple_layer = MulLayer()
    # mul_tax_layer = MulLayer()
    # add_apple_orange_layer = AddLayer()
    # mul_orange_layer = MulLayer()

    # apple_price = mul_apple_layer.forward(apple, apple_num)
    # orange_price = mul_orange_layer.forward(orange, orange_num)
    # all_price = add_apple_orange_layer.forward(apple_price, orange_price)
    # price = mul_tax_layer.forward(all_price, tax) 

    # print(price)

    # dprice = 1
    # dall_price, dtax = mul_tax_layer.backward(dprice)
    # dapple_price, dorange_price =  add_apple_orange_layer.backward(dall_price)
    # dorange, dorange_num = mul_orange_layer.backward(dorange_price)
    # dapple, dapple_num =  mul_apple_layer.backward(dapple_price)

    # print(dapple_num, dapple, dorange, dorange_num, dtax)
    import numpy as np
    x = np.array([[1.0, -0.5], [-2.0, 3.0]])
    a = Relu()
    print(a.forward(x))
    