# Agentic-AI-learning
My journey learning agentic AI and robotics

## About
This is my learning journey into Agentic Ai and Robotics.
I come from an embedded C background and I'm returning to engineering

## What I'm Learning
- Python basics
- Agentic AI(an AI that chooses and uses tools to reach a goal)
- ROS 2 and robotics (controlling a robot with AI)

## Progress notes
- Set up WSL,Ubuntu, and ROS 2
- Ran my first robot simulation(turtlesim)

# Robot AI Agent
## What it is
An AI agent that controls a robot using natural language.
## How it works
The user types a request,gemini picks a tool and the robot class runs it
## Tools
- move
- turn 
- battery
- stop
## What I learnt
Python classes,API,error handling and Git
## How to run it
- Activate the venv:'source venv/bin/activate'
- Install packages: 'pip install google-genai python-dotenv'
- Make a .env file with their own 'GEMINI_API_KEY'
- Run: 'python3 robot_class_agent.py'