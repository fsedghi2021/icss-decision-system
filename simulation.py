import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Time
t = np.arange(1, 11)

# Dominance weights
w1 = np.array([0.6]*5 + [0.2]*5)  # Beliefs
w2 = np.array([0.3]*5 + [0.5]*5)  # Habits
w3 = np.array([0.1]*5 + [0.3]*5)  # Social

# Lifestyle Coherence (illustrative)
LC = np.array([0.85, 0.87, 0.86, 0.84, 0.83,
               0.55, 0.50, 0.48, 0.47, 0.46])

# Confidence bands
w_std = 0.05
lc_std = 0.03

# Save data
df = pd.DataFrame({
    'time': t,
    'beliefs': w1,
    'habits': w2,
    'social': w3,
    'LC': LC
})
df.to_csv('icss_data.csv', index=False)

# Create figure
fig, axs = plt.subplots(2, 1, figsize=(6, 8))

# Panel A
axs[0].plot(t, w1, label='Beliefs (L1)')
axs[0].plot(t, w2, label='Habits (L2)')
axs[0].plot(t, w3, label='Social (L3)')

axs[0].fill_between(t, w1 - w_std, w1 + w_std, alpha=0.2)
axs[0].fill_between(t, w2 - w_std, w2 + w_std, alpha=0.2)
axs[0].fill_between(t, w3 - w_std, w3 + w_std, alpha=0.2)

axs[0].set_xlabel('Time (t)')
axs[0].set_ylabel('Weight w_k(t)')
axs[0].set_title('Dynamic Dominance Weights')
axs[0].legend()

# Panel B
axs[1].plot(t, LC, label='Lifestyle Coherence')
axs[1].fill_between(t, LC - lc_std, LC + lc_std, alpha=0.2)

axs[1].set_xlabel('Time (t)')
axs[1].set_ylabel('LC(t)')
axs[1].set_title('Lifestyle Coherence')
axs[1].legend()

plt.tight_layout()
plt.savefig('figures/icss_two_panel_confidence.png')
plt.savefig('figures/icss_two_panel_confidence.pdf')
plt.show()
