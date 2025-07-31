

import random
import time

# Base class for a Player
class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.is_out = False

    def play_ball(self):
        if not self.is_out:
            run = random.choice([0, 1, 2, 3, 4, 6, 'W'])  # W = Wicket
            self.balls += 1
            if run == 'W':
                self.is_out = True
                print(f"🔴 {self.name} is OUT!")
                return 0
            else:
                self.runs += run
                print(f"{self.name} scores {run} run(s). Total: {self.runs}")
                return run
        return 0

# Team class
class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = [Player(p) for p in players]
        self.total_runs = 0
        self.wickets = 0

    def play_innings(self, overs=2):
        print(f"\n🏏 {self.name} is batting...")
        balls = overs * 6
        current_batsman = 0

        for ball in range(balls):
            if current_batsman >= len(self.players):
                break  # All players are out

            print(f"Ball {ball + 1}: ", end="")
            run = self.players[current_batsman].play_ball()
            if self.players[current_batsman].is_out:
                self.wickets += 1
                current_batsman += 1
            else:
                self.total_runs += run

            time.sleep(0.5)  # just to simulate time delay

        print(f"\n{self.name} scored {self.total_runs}/{self.wickets} in {overs} overs.")

    def show_scorecard(self):
        print(f"\n📋 Scorecard for {self.name}:")
        for p in self.players:
            status = "Out" if p.is_out else "Not Out"
            print(f"{p.name}: {p.runs} ({p.balls} balls) - {status}")

# Match class to control the flow
class Match:
    def __init__(self, team1, team2, overs=2):
        self.team1 = team1
        self.team2 = team2
        self.overs = overs

    def start(self):
        self.team1.play_innings(self.overs)
        self.team1.show_scorecard()

        print("\n🕒 Switching innings...\n")
        time.sleep(2)

        self.team2.play_innings(self.overs)
        self.team2.show_scorecard()

        self.declare_winner()

    def declare_winner(self):
        print("\n🏆 Match Result:")
        if self.team1.total_runs > self.team2.total_runs:
            print(f"{self.team1.name} wins by {self.team1.total_runs - self.team2.total_runs} runs!")
        elif self.team2.total_runs > self.team1.total_runs:
            print(f"{self.team2.name} wins by {10 - self.team2.wickets} wickets!")
        else:
            print("It's a Tie!")

# ---------- Game Start ----------
team_a_players = ["Virat", "Rohit", "Dhoni", "Kohli", "Hardik"]
team_b_players = ["Smith", "Warner", "Finch", "Maxwell", "Starc"]

team1 = Team("India", team_a_players)
team2 = Team("Australia", team_b_players)

game = Match(team1, team2, overs=2)
game.start()
