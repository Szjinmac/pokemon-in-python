
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"







def display_game(game,grid_size):
    result = ""
    for row in range(grid_size):
     result += " |"+str(row+1)+" "
    result += " |\n"
    result += "-"*grid_size*4+"\n"
    for row in range(grid_size):
        result += str(ALPHA[row])+"|"
        for col in range(grid_size):
            index = row*grid_size + col
            result += game[index]+"  |"

        result +="\n" + "-"*grid_size*4+"\n"
    print(result)

def get_game(grid_size):
    initial_game = ""

    m = grid_size*grid_size

    initial_game += "~"*m

    return  initial_game



def main():
    grid_size = input("Please input the number of grid: ")
    grid_size = int(grid_size)
    game = get_game(grid_size)

    display_game(game,grid_size)




if __name__ =="__main__":
    main()


