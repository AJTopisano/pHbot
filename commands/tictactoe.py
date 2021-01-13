import discord
from discord.ext import commands
from loguru import logger
from client import client as client
import random

player1 = ''
player2 = ''
gameOver = True
turn = ''
count = 0

board = []  # TicTacToe board

winningConditions = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [0, 4, 8],
                     [1, 4, 7],
                     [2, 4, 6],
                     [2, 5, 8]]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global gameOver
    global turn
    global board
    global count

    if gameOver:
        board = [':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:']

        turn = ''
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ''
        for x in range(len(board)):
            if x in [2, 5, 8]:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # choosing players
        turn = random.choice([player1, player2])
        await ctx.send("It's <@" + str(turn.id) + ">'s turn")
    else:
        await ctx.send("The previous game hasn't yet finished")


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global count
    global board

    if not gameOver:
        mark = ":garlic:"
        if turn == ctx.author:
            if turn == player2:
                mark = ":onion:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print board
                line = ''
                for x in range(len(board)):
                    if x in [2, 5, 8]:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    await ctx.send("It's a tie")

                # switch tuns
                if turn == player1:
                    turn = player2
                else:
                    turn = player1

            else:
                await ctx.send("Choose an integer between (1,9), where the tile is unmarked")

        else:
            await ctx.send("It's not your turn")
    else:
        await ctx.send("Start a new game using tictactoe command")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")

    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention players")

@place.error
async  def place_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a number where you want to place")

    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure it's an integer")