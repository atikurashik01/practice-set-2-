import torch
import torch.nn as nn
import torch.optim as optim

# -----------------------------
# 1. Tensor তৈরি
# -----------------------------
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

print("Input x:", x)
print("Output y:", y)

# -----------------------------
# 2. Simple Linear Model
# -----------------------------
model = nn.Linear(in_features=1, out_features=1)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# -----------------------------
# 3. Training loop
# -----------------------------
for epoch in range(1000):
    # Forward pass
    y_pred = model(x)
    loss = criterion(y_pred, y)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 200 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')

# -----------------------------
# 4. Test
# -----------------------------
test_input = torch.tensor([[5.0]])
pred = model(test_input)
print("Prediction for input 5:", pred.item())
