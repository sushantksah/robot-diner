# The Robot Diner
### Multi-Agent Robotic Pathfinding and Navigation Simulation

The Robot Diner is a multi-robot navigation and pathfinding simulation set in an autonomous restaurant environment.

The project explores how multiple autonomous robots can navigate a shared environment, discover obstacles, communicate with one another, avoid collisions, and dynamically recalculate routes using A* search algorithms.

## Core Features - SUBJECT TO CHANGE

- **Multi-Agent Navigation:** Multiple autonomous robots navigating a shared grid environment.
- **Pathfinding Algorithms:** Implementation and comparison of Greedy Best-First Search, A*, Weighted A*, and Simplified Memory-Bounded A* (SMA*).
- **Heuristic Comparison:** Manhattan, Euclidean, custom, relaxed-problem-derived, and learned linear heuristics.
- **Partial Observability:** Robots operate with limited sensor ranges and incomplete knowledge of the environment.
- **Collaborative Mapping:** Robots communicate discovered obstacles and share environmental updates.
- **Collision Avoidance:** Robots coordinate movement to prevent collisions.
- **Dynamic Obstacles:** Moving obstacles require robots to update their maps and recalculate paths.
- **AI Path Comparison:** Integration with the Gemini API or an alternative LLM provider to compare AI-generated paths against traditional pathfinding algorithms.

## Environment

The simulation represents a restaurant with:

- A central kitchen.
- Dining areas and tables.
- A central navigation track with connecting corridors.
- Static obstacles such as walls, tables, and counters.
- Dynamic obstacles such as moving customers and restaurant staff.
- Multiple autonomous delivery robots.
- A designated common rendezvous point.

Robots begin at different positions and must navigate toward a shared rendezvous point while adapting to obstacles and information received from other robots.

## Technology Stack
TBD 
*The technology stack and implementation details may evolve during development.*

## Project Objectives

1. Implement and compare multiple search algorithms and heuristic functions.
2. Evaluate heuristic admissibility and consistency.
3. Simulate multiple robots operating under partial observability.
4. Implement real-time communication and collaborative obstacle discovery.
5. Demonstrate collision avoidance and dynamic path replanning.
6. Evaluate performance based on execution time, path optimality, scalability, and communication efficiency.
7. Compare traditional pathfinding approaches with AI-generated alternatives.

## Getting Started

Installation instructions, dependencies, and execution commands will be added as the project implementation develops.

## Project Status

Currently in initial development and architectural planning.

The project is being developed as part of a term project focused on multi-agent path planning using A* algorithms.