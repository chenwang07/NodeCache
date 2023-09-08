## Dependency Graphs Prototype

The idea behind Dependency Graphs is that in intra-day trading, there are tons of calculations and the whole calibration/calculation is time-consuming, and when the market changes, if we re-run the whole calculation, it could take time and therefore is hard for the trader/PM to get live risk feedback.

Dependency Graphs is a way to solve this problem, it is a directed acyclic graph, where each node represents a calculation, and each edge represents a dependency between two calculations. When the market changes, we only need to re-run the calculation that is affected by the market change, and the rest of the calculation will be cached and reused.

Node Cache repo implemented a basic prototype for Dependency Graphs, the user could try to run EquityOptionPricing.py. The details of how to determine the changing components are in the prod version, the prod version Node Cache is integrated into the TraderCopilot Framework.

## Example

![Example Image](res/images/example.png)
