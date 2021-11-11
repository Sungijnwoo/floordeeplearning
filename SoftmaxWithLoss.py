from softmax import softmax
from cross_entropy_error import cross_entropy_error

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y, self.t = None, None

    def forward(self, x, t):
        self.t =  t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backward(self, dout=1):
        bath_size = self.t.shape[0]
        dx = (self.y - self.t) / bath_size

        return dx
