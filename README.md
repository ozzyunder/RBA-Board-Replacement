​🏦 RBA Interest Rate Decision Simulator
​A Python-based simulation of the Reserve Bank of Australia (RBA) monetary policy process. This script replicates the "Dual Mandate" logic (balancing inflation and employment) used to determine the Australian Cash Rate.
​📖 Project Overview
​As of May 2026, the RBA operates in a highly volatile economic environment. This tool uses a stochastic (randomized) multi-instance approach to simulate a 7-member board meeting. It accounts for different economic perspectives—ranging from "Hawks" (inflation-focused) to "Doves" (growth-focused)—to arrive at a consensus decision.
​Key Features
​Dual Mandate Logic: Evaluates the gap between current CPI and the 2–3% target, alongside the unemployment rate.
​Stochastic Modeling: Each of the 7 simulated instances (members) has a randomized bias, reflecting the diversity of opinion in a real boardroom.
​Consensus Averaging: Aggregates individual votes and rounds to the nearest 0.25% (25 basis points), mirroring standard central bank movements.
​Real-time Alignment: Updated to reflect the economic conditions of May 2026, where inflation has seen a resurgence to 4.6%.
​🚀 How It Works
​The core logic follows a modified Taylor Rule. The decision-making process is broken down into three stages:
​Data Intake: The script accepts current CPI, Unemployment, and Wage Growth data.
​Stochastic Voting: * Hawks prioritize the inflation gap (CPI - 2.5\%).
​Doves prioritize the labour gap (NAIRU - Unemployment).
​Aggregation: The instances are averaged. A final decision (HIKE, HOLD, or CUT) is made based on the collective "pressure" of the group.
​The Formula
​The simulator essentially solves for the adjustment \Delta R:

🛠 Installation & Usage
1. Clone the repository:
   git clone https://github.com/ozzyunder/rba-simulator.git
2. Run the simulation:
   python rba_decision_model.py
3. Replace the RBA board and save $millions!

​⚖️ Disclaimer
​This project is for educational and simulation purposes only. It is not financial advice. The "Board Members" are represented by randomized variables and do not reflect the specific views of actual RBA Board members.
​Maintained by: ozzyunder (well, AI...)
Last Updated: May 2026
