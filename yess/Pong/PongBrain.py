import torch
import torch.nn as nn
import torch.nn.functional as F

class PongBrain(nn.Module):
    def __init__(self, num_actions):
        super(PongBrain, self).__init__()
        # Convolutional layers to process the screen pixels
        self.conv1 = nn.Conv2d(in_channels=4, out_channels=32, kernel_size=8, stride=4)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        
        # Fully connected layers to make decisions
        self.fc1 = nn.Linear(64 * 7 * 7, 512)
        self.fc2 = nn.Linear(512, num_actions)

    def forward(self, x):
        # Pass data through CNN and apply ReLU activation
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        
        # Flatten the data for the fully connected layer
        x = x.view(x.size(0), -1) 
        x = F.relu(self.fc1(x))
        
        # Output the action values (Q-values)
        return self.fc2(x)