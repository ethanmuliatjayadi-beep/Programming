import numpy as np
import torch.optim as optim

# Initialize the model and optimizer
model = PongBrain(num_actions)
optimizer = optim.Adam(model.parameters(), lr=0.0001)

# Training hyperparameters
episodes = 500
epsilon = 1.0       # Start by taking 100% random actions to explore
epsilon_min = 0.02  # Lowest exploration rate
decay_rate = 0.995

for episode in range(episodes):
    state, info = env.reset()
    state = torch.tensor(np.array(state), dtype=torch.float32).unsqueeze(0)
    
    total_reward = 0
    done = False
    
    while not done:
        # 1. CHOOSE AN ACTION
        if np.random.rand() <= epsilon:
            action = env.action_space.sample() # Explore: Random move
        else:
            with torch.no_grad():
                q_values = model(state)
                action = torch.argmax(q_values).item() # Exploit: Best move from Network
                
        # 2. TAKE ACTION IN THE PONG GAME
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward
        
        # Convert next state to tensor
        next_state_tensor = torch.tensor(np.array(next_state), dtype=torch.float32).unsqueeze(0)
        
        # 3. LEARN FROM THE EXPERIENCE (Simplified)
        # In a full DQN, you save this to a "Replay Buffer" and train on random batches.
        # Here we show the core PyTorch calculation:
        
        # Current prediction
        current_q = model(state)[0][action]
        
        # Target (Reward + best future predicted reward)
        if done:
            target_q = torch.tensor(reward, dtype=torch.float32)
        else:
            with torch.no_grad():
                max_next_q = torch.max(model(next_state_tensor))
                target_q = reward + 0.99 * max_next_q  # 0.99 is the discount factor

        # Calculate loss and update PyTorch weights
        loss = F.mse_loss(current_q, target_q)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Move to the next state
        state = next_state_tensor
        
    # Decay the exploration rate so the agent relies on its network more over time
    if epsilon > epsilon_min:
        epsilon *= decay_rate
        
    print(f"Episode: {episode}, Score: {total_reward}, Epsilon: {epsilon:.2f}")

env.close()