import random  # For exploration
import pickle  # For saving and loading Q-table
import os  # To check for file existence


class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1, q_table_file="q_table.pkl"):
        """
        Initialize the Q-learning agent.

        :param actions: List of possible actions (e.g., [90, 270, 180, 0]).
        :param alpha: Learning rate.
        :param gamma: Discount factor.
        :param epsilon: Exploration rate.
        :param q_table_file: File name for saving/loading the Q-table.
        """
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}
        self.q_table_file = q_table_file

        # Load existing Q-table if available
        self.load_q_table()

    def get_q_value(self, state, action):
        """
        Get the Q-value for a given state-action pair.
        If not found, return 0.

        :param state: Current state.
        :param action: Action taken.
        :return: Q-value for the state-action pair.
        """
        return self.q_table.get((state, action), 0)

    def choose_action(self, state):
        """
        Choose an action using epsilon-greedy policy.

        :param state: Current state.
        :return: Index of the chosen action.
        """
        if random.random() < self.epsilon:
            # Exploration: Choose a random action
            return random.randint(0, len(self.actions) - 1)
        else:
            # Exploitation: Choose the action with the highest Q-value
            q_values = [self.get_q_value(state, action) for action in self.actions]
            return q_values.index(max(q_values))

    def update_q_table(self, state, action_index, reward, next_state):
        """
        Update the Q-table using the Q-learning formula.

        Q(s, a) = Q(s, a) + alpha * [reward + gamma * max(Q(s', a')) - Q(s, a)]

        :param state: Current state.
        :param action_index: Index of the chosen action.
        :param reward: Reward received after taking the action.
        :param next_state: The state transitioned to.
        """
        action = self.actions[action_index]
        current_q = self.get_q_value(state, action)
        # Max Q-value for the next state
        next_max_q = max([self.get_q_value(next_state, a) for a in self.actions], default=0)
        # Update Q-value
        new_q = current_q + self.alpha * (reward + self.gamma * next_max_q - current_q)
        self.q_table[(state, action)] = new_q

    def save_q_table(self):
        """
        Save the Q-table to a file.
        """
        try:
            with open(self.q_table_file, "wb") as f:
                pickle.dump(self.q_table, f)
            print(f"Q-table saved successfully to {self.q_table_file}.")
        except Exception as e:
            print(f"Error saving Q-table: {e}")

    def load_q_table(self):
        """
        Load the Q-table from a file if it exists.
        """
        if os.path.exists(self.q_table_file):
            try:
                with open(self.q_table_file, "rb") as f:
                    self.q_table = pickle.load(f)
                print(f"Q-table loaded successfully from {self.q_table_file}.")
            except Exception as e:
                self.q_table = {}
                print(f"Error loading Q-table: {e}. Starting with an empty Q-table.")
        else:
            print("No existing Q-table found. Starting from scratch.")

    def __del__(self):
        """
        Ensure the Q-table is saved when the agent is deleted or the program ends.
        """
        self.save_q_table()
