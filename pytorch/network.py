# encoding=utf-8
"""
    Created on 10:41 2018/11/10 
    @author: Jindong Wang
"""
import torch.nn as nn
import torch.nn.functional as F


#class Network(nn.Module):
#    def __init__(self):
#        super(Network, self).__init__()
#        self.conv1 = nn.Sequential(
#            nn.Conv2d(in_channels=9, out_channels=32, kernel_size=(1, 9)),
#            nn.ReLU(),
#            nn.MaxPool2d(kernel_size=(1, 2), stride=2)
#        )
#        self.conv2 = nn.Sequential(
#            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(1, 9)),
#            nn.ReLU(),
#            nn.MaxPool2d(kernel_size=(1, 2), stride=2)
#        )
#        self.fc1 = nn.Sequential(
#            nn.Linear(in_features=64 * 26, out_features=512),
#            nn.Dropout(0.5),
#            nn.ReLU()
#        )
#        self.fc2 = nn.Sequential(
##            nn.Linear(in_features=512, out_features=128),
##            nn.Dropout(0.5),
##            nn.ReLU()
#        )
#        self.fc3 = nn.Sequential(
#            nn.Linear(in_features=512, out_features=6)
#        )
#
#    def forward(self, x):
#        out = self.conv1(x)
#        out = self.conv2(out)
#        out = out.reshape(-1, 64 * 26)
#        out = self.fc1(out)
#        out = self.fc2(out)
#        out = self.fc3(out)
#        out = F.softmax(out, dim=1)
#        return out

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.lstm1 = nn.LSTM(9, 64) 
        self.fc1 = nn.Sequential(
            nn.Linear(in_features=64, out_features=64),
            nn.Dropout(0.5),
            nn.ReLU()
        )
        self.fc2 = nn.Sequential(
#            nn.Linear(in_features=512, out_features=128),
#            nn.Dropout(0.5),
#            nn.ReLU()
        )
        self.fc3 = nn.Sequential(
            nn.Linear(in_features=64, out_features=6)
        )

    def forward(self, x):
        out, _ = self.lstm1(x, None)
        out = out.reshape(-1, 64)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        out = F.softmax(out, dim=1)
        return out