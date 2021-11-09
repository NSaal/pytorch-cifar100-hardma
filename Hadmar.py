import torch
import torch.nn as nn
import numpy as np


class Hadmar(nn.Module):
    def __init__(self, order: int = 8):
        super(Hadmar, self).__init__()
        self.order = order
        self.hadmar = torch.ones((order, order))
        for i in range(self.order):
            for j in range(self.order):
                self.hadmar[i][j] = self.Creat_Hadmard(i, j)
        # self.hadmar = torch.from_numpy(self.hadmar)
        #self.hadmar = torch.stack((self.hadmar, self.hadmar, self.hadmar), 0)
        self.hadmar=self.hadmar.cuda()

    def Creat_Hadmard(self, i=4, j=4):
        temp = i & j
        result = 0
        for step in range(4):
            result += ((temp >> step) & 1)
        if 0 == result % 2:
            sign = 1
        else:
            sign = -1
        return sign

    def forward(self, input):
        # print(self.hadmar)
        # print("input!!!!",input.size())
        # output=input
        # for i in range(input.size()[0]):
        #     for j in range(input.size()[1]):
        #         # print("inputIJ!!!!",input[i][j].size())
        #         input[i][j] = self.hadmar*input[i][j]*self.hadmar
        # print("output!!!!",input.size())
        #output = torch.reshape(input, (input.szie()[0], 3, self.order, self.order))
        # print(input)
        # input=self.hadmar*input*self.hadmar
        input=torch.matmul(self.hadmar,input)
        input=torch.matmul(input,self.hadmar)

        return input

    def extra_repr(self):
        return 'order={}, hardma={}'.format(
            self.order, self.hardma is not None
        )
