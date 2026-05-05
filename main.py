import random

class RBABoardSimulator:
    def __init__(self):
        self.target_inflation = 2.5
        self.neutral_unemployment = 4.3
        self.current_base_rate = 3.85  # Starting point for March 2026

    def simulate_member_vote(self, cpi, unemployment):
        """
        Simulates a single board member's decision with individual bias.
        """
        # Randomization factor: Some members are more sensitive to inflation (Hawks)
        # while others are more sensitive to unemployment (Doves).
        hawk_dove_bias = random.uniform(0.8, 1.2)
        
        inf_pressure = (cpi - self.target_inflation) * hawk_dove_bias
        labour_pressure = (self.neutral_unemployment - unemployment) * (2 - hawk_dove_bias)
        
        # Calculate suggested adjustment
        total_pressure = inf_pressure + labour_pressure
        
        if total_pressure > 1.0:
            return 0.25  # Vote for Hike
        elif total_pressure < -1.0:
            return -0.25 # Vote for Cut
        else:
            return 0.0   # Vote for Hold

    def run_consensus_meeting(self, cpi, unemployment, instances=7):
        votes = []
        
        print(f"--- RBA Board Simulation ({instances} Members) ---")
        for i in range(instances):
            vote = self.simulate_member_vote(cpi, unemployment)
            votes.append(vote)
            print(f"Member {i+1} Vote: {vote:+.2f}%")

        # Averaging the instances
        average_adjustment = sum(votes) / len(votes)
        
        # Central banks usually move in 25bps increments, 
        # so we round the average to the nearest 0.25 for the final "Call"
        final_adjustment = round(average_adjustment * 4) / 4
        new_rate = self.current_base_rate + final_adjustment

        return {
            "Raw Average Adjustment": f"{average_adjustment:+.3f}%",
            "Consensus Adjustment": f"{final_adjustment:+.2f}%",
            "Final Recommended Cash Rate": f"{new_rate:.2f}%"
        }

# Execution with March 2026 economic data
sim = RBABoardSimulator()
results = sim.run_consensus_meeting(cpi=3.8, unemployment=4.1, instances=7)

print("\n--- Final Results ---")
for key, value in results.items():
    print(f"{key}: {value}")
