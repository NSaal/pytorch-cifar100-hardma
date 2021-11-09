import torch
from Hadmar import Hadmar


had=Hadmar(2)
# a = torch.rand(4, 4).cuda()
a=torch.tensor([[1,2],[3,4]]).cuda()
print("befor:",a)
b=had(a)
print("hadma:",had.hadmar)
print("after:",b)
