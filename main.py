
seats = [[3 , 4],[4 , 5],[2 , 3],[3 , 4]]
def init_seats(seats):
    #fill all seats with 0 as default value
    seating = []
    for i,item in enumerate(seats):
        seating.append([])
        for row in range(item[0]):
            seating[i].append([])
            for col in range(item[1]):
                seating[i][row].append(0)
    return seating

sets_grid = init_seats(seats)
max_rows = max([l[0] for l in seats])

def fill_aisle_seats(num_passenger):
    current_passenger = 1
    row = 0
    while(current_passenger<=num_passenger and row  <max_rows):
        for i,part in enumerate(sets_grid):
            if row < len(part) and current_passenger<=num_passenger:
                if i==0:
                    sets_grid[i][row][-1] = current_passenger
                    current_passenger += 1
                elif i==len(sets_grid)-1:
                    sets_grid[i][row][0]=current_passenger
                    current_passenger+=1
                else:
                    sets_grid[i][row][0]=current_passenger
                    current_passenger+=1
                    if current_passenger<=num_passenger and len(part[0])>1:
                        sets_grid[i][row][-1]=current_passenger
                        current_passenger+=1
            elif row>=max_rows:
                break
        row+=1
    return current_passenger

def fill_window_seats(num_passenger,current_passenger):
    row = 0
    while(current_passenger<=num_passenger and row  <max_rows):
        if row < len(sets_grid[0]):
            sets_grid[0][row][0] = current_passenger
            current_passenger += 1
        if row < len(sets_grid[-1]) and current_passenger<=num_passenger:
            sets_grid[-1][row][-1] = current_passenger
            current_passenger += 1   
        row+=1
    return current_passenger


def fill_center_seats(num_passenger,current_passenger):
    row = 0
    while(current_passenger<=num_passenger and row  <max_rows):
        for i,part in enumerate(sets_grid):
            if row < len(part) and current_passenger<=num_passenger and len(part[0])>2:
                for j in range(1,len(part[0])-1):
                    if current_passenger<=num_passenger:
                        sets_grid[i][row][j]=current_passenger
                        current_passenger+=1
                    else:
                        break
            elif row>=max_rows:
                break
        row+=1
    return current_passenger





def display(sets_grid):
    for part in sets_grid:
        for row in part:
            print("| ",end="")
            for col in row:
                if col != 0:
                    if col<10:
                        st = "  " + str(col)
                    elif col <100:
                        st = " " + str(col)
                    else:
                        st = col
                    print(st, end=" | ")
                else:
                    print("   ", end=" | ")
            print()
        print("\n")

num_passenger = 39
next_passenger = fill_aisle_seats(num_passenger)
next_passenger = fill_window_seats(num_passenger,next_passenger)
fill_center_seats(num_passenger,next_passenger)
display(sets_grid)
            

    
