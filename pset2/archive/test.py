import yahooquery as yq

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


class StockPredictionModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(StockPredictionModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.sigmoid(out)
        return out

class GrowthStrategyModel():
    def __init__(self, input_size, hidden_size, output_size):
        self.model = StockPredictionModel(input_size, hidden_size, output_size)
        self.criterion = nn.BCELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

    def train(self, X_train, y_train, num_epochs=100):
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train, dtype=torch.float32)

        for epoch in range(num_epochs):
            self.optimizer.zero_grad()
            outputs = self.model(X_train_tensor)
            loss = self.criterion(outputs, y_train_tensor.view(-1, 1))
            loss.backward()
            self.optimizer.step()

            if (epoch+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    def predict(self, X_test):
        X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
        with torch.no_grad():
            outputs = self.model(X_test_tensor)
            predicted_labels = (outputs >= 0.5).float().squeeze().numpy()
        return predicted_labels

# Example usage
# 
X_train = 
# Example data
X_train = [...]  # Training features
y_train = [...]  # Training labels

X_test = [...]  # Test features

# Initialize growth strategy model
model = GrowthStrategyModel(input_size=X_train.shape[1], hidden_size=64, output_size=1)

# Train the model
model.train(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
print(predictions)

"""
interval = '3mo'
FEATURES
return on equity (ROE)
return on invested capital (ROIC)
projected three-to-five year sales and EPS growth rates

Earnings Per Share (EPS)
Price to Earnings Ratio (P/E ratio)
Price to Book Ratio (P/B ratio)
Dividend Yield
Revenue Growth Rate
Profit Margin
Debt-to-Equity Ratio
Book Value
Market Capitalization

Supply and demand dynamics
Industry-specific regulations and policies
Competitive landscape
Technological innovations and disruptions

Interest rates (e.g., Federal Reserve rates)
Inflation rates
GDP growth rates
Unemployment rates
Consumer sentiment indices
Volatility indices (e.g., VIX)
Bond yields

DATA

"""
