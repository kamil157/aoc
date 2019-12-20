input = """
                                       S       Z       J       X   Q   X     L   Z     W                                         
                                       I       H       S       C   T   F     E   Z     N                                         
  #####################################.#######.#######.#######.###.###.#####.###.#####.#######################################  
  #.#...#...........#.....#...#.......#.#.....#.#.#...........#.......#...#...#...#.....#...#.#.#...#.....#...#.#.#...#.#.....#  
  #.#.#####.#######.#####.###.#####.###.#.###.#.#.#.#.#######.#.#.###.###.#.###.#.#####.#.###.#.###.#.#######.#.#.#.###.#.#####  
  #.#.#.#.#.#.#.......#.....#.#.#.#.....#.#...#...#.#.#.......#.#...#.#...#.....#.#...#.....................#.#.#.#.#.#.....#.#  
  #.#.#.#.###.#.###.###.###.#.#.#.#.###.#.#.###.#######.#.#.#.#######.#.#########.#.###.#########.#.#.#######.#.#.#.#.###.###.#  
  #.......#.....#.#.....#.....#.....#.....#...#...#...#.#.#.#.#.......#...#.....#.....#...#...#...#.#...................#.....#  
  #####.#########.###.#######.###.#####.###.###.###.#.#.#####.#######.###.###.#.#.#####.#####.#######.#.#.#.#.###.#####.#.#####  
  #...#...#...#...#...#...#.......#.#...#.#.#.....#.#.....#.....#.......#.#...#.#.#.......#.#.......#.#.#.#.#.#.....#.....#...#  
  #.###.###.#####.#######.###.###.#.#.###.#.###.#######.#######.#.###.###.#.###.#.#.#####.#.#.#.#####.###.###.###.###.#.#.#.###  
  #.........#.#...............#...#.#.#.#.....#...#.......#.....#.#...#.#.#.#.....#.....#.....#.....#...#.#...#.....#.#.#...#.#  
  #.#.###.###.#.#####.#####.#.###.#.###.#.#####.#######.#########.#.#.#.#.#.###.###.#####.#.#.###.###########.###.#########.#.#  
  #.#.#...#.#.#.#.#...#.....#.#.....#.........#.#...#.#.......#...#.#.#...#.#.#.#.#.....#.#.#...#.#.#...#.......#...#.#...#...#  
  #######.#.#.###.#######.#############.#.#.#.#.###.#.###.###########.#.###.#.###.#.#.#.###.###.###.#.###.###.#######.#.###.###  
  #.#...#.........#...#...#.#.....#.#.#.#.#.#.#...#.........#...#.....#...#.......#.#.#.#.....#.#...#...#.#...............#...#  
  #.###.#.#.#######.#.#.###.#####.#.#.#######.###.#####.#.#.#.#######.###.#.#.#####.###############.#.#####.#.#.#####.#####.###  
  #.#.#.#.#.#.#.....#.#.....#.#...#.#.....#...#...#.#.#.#.#.#.#...#...#...#.#...#.......#.......#.....#.....#.#.....#.....#.#.#  
  #.#.#.#.#.#.#####.###.###.#.#.#.#.###.###.#.###.#.#.#.#####.#.#####.###.#.#.#.###.#.#####.#######.#######.###.#.###########.#  
  #.....#.#.#.#...#.#...#.#.#.#.#.........#.#.#.....#.#.........#.......#.#.#.#.#...#...#.....#.......#...#.#.#.#.....#...#.#.#  
  ###.#####.#.###.#.###.#.###.#######.#.#####.###.###.###.#.#########.#.#.###.#######.###.#########.###.#####.#.#######.###.#.#  
  #.#...#.#.#.#...#...#.#...#.#...#.#.#...#.....#.......#.#.#...#.....#.#...#.....#.#.......#...#.#.#.......#.#...#.#...#.#.#.#  
  #.#.###.#.#.###.###.#####.#.#.###.###.###.#########.###.#####.###.#####.#######.#.#####.#####.#.#.#.###.###.#####.###.#.#.#.#  
  #...#.........#.......#.....................#.......#.........#.....#.....#.......#...#.......#.#.....#.#.#.#.#...#.....#.#.#  
  ###.###.###########.###.#.###.###.#.#######.#.#############.#######.#.#.#####.#####.#.#.#######.#.#######.#.#.#.#######.#.#.#  
  #.#...#.#.....#...#...#.#.#...#.#.#.#...#...#.....#.#...#...#.....#.#.#.#.#.#...#...#.................#.#.#...#...#.....#...#  
  #.#.###.#.#####.#.#.#####.###.#.#.###.#####.###.###.#.#.#.#####.#.#.###.#.#.###.###.###.#####.#########.#.###.#.#######.###.#  
  #...#.#.#...#.#.#.#.#.#...#...#...#.....#...#...#.....#...#.....#.....#.#...#...#.#...#...#.#.#...#.#...#.#.......#.#.#.....#  
  ###.#.#.#.###.###.#.#.#########.###.#.#.###.#.#.#####.###.###.###.#.###.#.#.#.###.###.#.###.#.#.###.###.#.###.#####.#.#.#####  
  #.....#.#...#...#.....#.........#...#.#.#...#.#...#.....#.#.....#.#.#...#.#...#...#...#.#...#.#.....#.#.....#...#...#.#.....#  
  ###.###.#.#####.#.###############.###.#.#.###.#.###.#.#######.#######.###.#######.#.###.###.###.###.#.#.#.###.#####.#.#.#####  
  #.........#.#.......#...#.#.#.#.#.#.#.#...#...#.#...#.......#...#...#.#.........#.....#.#.#.....#.#...#.#...#.#.#.......#.#.#  
  #####.#.###.#####.###.###.#.#.#.###.#.#######.#######.#.#.###.#####.#.#########.###.#####.#.###.#.#.#.###.###.#.#######.#.#.#  
  #.....#.#...#.#.........#.#.#...#...#.....#.......#.#.#.#...#.....#.....#.......#.....#.#.....#...#.#.#.........#.#.#.#.#.#.#  
  #####.###.###.###.#######.#.###.###.#.###.###.#.#.#.#.#.###.###.###.###.#.#######.#####.#.###.#.#######.###.#####.#.#.#.#.#.#  
  #...#...#.......#...#.#.#.......#.....#.....#.#.#.#...#...#.#.....#.#...#.......#.........#...#.#...#.#.#...#.#.............#  
  #.###.###.#######.###.#.#######.#########.###.#############.#.#.#####.#######.#####.#############.###.#####.#.###.#.#####.#.#  
  #...#.#...#...#...#.#.........#...#      D   O             F X P     W       G     R      #...#...#...#...#.#...#.#.#...#.#.#  
  #.###.###.#.###.###.###.###.###.###      V   V             Z F Y     X       S     V      #.#.###.#.###.###.#.#######.###.###  
  #...#...#.....#...#...#.#.#.#.#...#                                                       #.#.#.#.#.#.#.......#.....#...#...#  
  #.#####.###.###.#####.#.#.###.###.#                                                       #.#.#.#.#.#.#####.#######.#.#.#.###  
  #.#.#.............#.#.....#........JX                                                     #.#.#.#.#.#...#.....#.#...#.#.#.#.#  
  #.#.#.#########.###.#.#########.#.#                                                       #.###.#.#.#.#####.###.#.###.###.#.#  
PY....#.#.#.#.#.....#.....#.#.....#.#                                                       #...#...#.#.......................#  
  #.#.#.#.#.#.###.#####.###.#####.###                                                       ###.#.###.#.#.###.###.#.#.#.#.#.###  
  #.#.#.....#.#.#.....#.......#...#.#                                                     PP..#.......#.#.#.#.#.#.#.#.#.#.#.#.#  
  ###.#.#.###.#.###.#.#.#####.###.#.#                                                       #.###.###.###.#.###.#.#########.#.#  
  #.....#.#...#.#.#.#.....#.#.....#.#                                                       #...#.#...........#.....#...#...#..OF
  ###########.#.#.#########.#######.#                                                       #.###.#####.#########.###.###.###.#  
  #.#.#.......#.#.............#.....#                                                       #.........#.#...#.......#...#.....#  
  #.#.#.#####.#.#.###.#.#.#.#.#.###.#                                                       #.#############.###.#.###.###.#####  
OV..#...#...#...#.#.#.#.#.#.#...#...#                                                       #.#...#...........#.#.#.....#.#...#  
  #.#.#########.#.#.#####.###.#####.#                                                       ###.#.#.###.###.#########.#######.#  
  #.#.......#.#.......#...#.....#....ES                                                     #.#.#.....#.#.....#...#.#.#.....#..DV
  #.#####.###.#####.###.#############                                                       #.#.#####.###.#.###.###.#.###.###.#  
  #.........#.#.#.....#.#...#.#.#...#                                                     ZJ..#.....#.#...#.#...#.........#...#  
  #.###.#####.#.#########.###.#.#.###                                                       #.###.#.#####.#####.###.#####.#.#.#  
  #...#...#.............#.....#.....#                                                       #.....#.#.#.............#.......#.#  
  #.#######.#########.###.###.#.###.#                                                       #.#######.###########.#.###########  
  #...#...........#...#.#.#.#...#...#                                                       #.#...........#...#.#.#.......#...#  
  #######.###########.#.#.#.#####.###                                                       #.#.#########.#.#.#.#.###.#####.#.#  
  #.#.#...#.#.#...#...........#...#..BL                                                     #.#.......#.....#...#...#...#...#..GM
  #.#.#.###.#.#.#######.###.#####.#.#                                                       #########.#.#.#####.###########.###  
FZ......#.......#.#.....#.#.#.#.....#                                                     TW..#...#...#.#.#.....#.....#.#.....#  
  ###.#.#####.###.###.#.#.###.#####.#                                                       #.#.#.#.#####.#####.#.###.#.#.#####  
JX..#.#.#...#.......#.#...#.#.....#.#                                                       #...#...#.....#.#.......#.........#  
  #.#######.###.###.#######.#.###.###                                                       ###############.###.#.###.###.#.#.#  
  #.......#.......#.#...#...#.#......SI                                                     #...........#.......#.#...#...#.#.#  
  #.#######.#.###.#####.###.#.#######                                                       ###.#####.#########.#####.#########  
  #.#...#.#.#...#...#...#...#.....#.#                                                       #.....#.....#.#.#...#.#.....#...#.#  
  #.#.###.#####.###.###.###.#####.#.#                                                       #.#####.#####.#.#####.#######.#.#.#  
  #...............#...............#.#                                                       #...#...#.#.#.....#...#...#.#.#.#..RV
  ###.#########.#####.#######.#####.#                                                       ###.#.#####.#.#.###.###.###.#.###.#  
DS..#.#.#.....#...#.#.#.....#.#.....#                                                     QT....#.........#...................#  
  #.#.#.#.###.#.###.###.###.###.###.#                                                       ###############.#.#.#.#.#.#########  
  #.#.#...#...#.#.#.#...#.....#...#.#                                                       #.......#.....#.#.#.#.#.#.#.#...#..PP
  #.###.#.#.#####.#.#.#.#.###.###.#.#                                                       #.#.#.#.#.#.#######.#######.###.#.#  
  #...#.#.#.#.#.#.....#.#.#.......#..XC                                                   MJ..#.#.#...#.....#...#...#.........#  
  #.#####.#.#.#.#.###########.###.#.#                                                       ###.#.#.#.###.#########.###.#######  
  #.......#.......#...#...#...#...#.#                                                       #.#.#.#.#.#...#...#.#.....#.....#.#  
  ###################.###.###########                                                       #.#.#######.#####.#.#.#.#.#####.#.#  
  #.#.#.....#.#.....................#                                                       #.....#...#...........#.#.........#  
  #.#.#.###.#.#.#.#.#.#.###.#.#.###.#                                                       #.#.###.###########################  
  #.#.....#.....#.#.#.#.#...#.#...#.#                                                       #.#.#.#.#.#.#.........#.#...#...#..ZJ
  #.#.###.#######.###########.#.###.#                                                       #.###.#.#.#.#####.###.#.#.#.#.#.#.#  
MJ..#.#.#.......#.#...#.....#.#.#.#.#                                                       #.#.#.#.......#.#...#.....#...#...#  
  #.#########.#####.#.#####.#####.#.#                                                       ###.#.###.#.###.###.#######.###.#.#  
  #.............#.#.#...#.#.#.....#..GM                                                     #.#...#.#.#...#.#.#.....#...#...#.#  
  #####.#########.###.###.#.#####.###                                                       #.#.#.#.###.#.#.###.#######.###.#.#  
  #...#.#.....#.........#.....#...#.#                                                     GR....#.......#.........#.#...#...#.#  
  #.#.###.###.#.#.#####.#.#.#.#.#.#.#                                                       #.###.#.#####.#####.#.#.#.#.###.###  
  #.#.......#...#.#.......#.#...#...#                                                       #.#...#.#.#...#...#.#.#...#...#.#.#  
  #.#.###.###.#.#.###.#.#####.#####.#                                                       #.#.#.#.#.###.###.#####.#.#.###.#.#  
  #.#...#.#...#.#...#.#.#...#.#......DS                                                     #.#.#.#.#...........#...#.#...#...#  
  #.###.#########.###.#.###.#####.#.#                                                       #.#####.###.#.#.#.#.#.#####.#.#.#.#  
GH....#.....#.....#...#.....#.....#.#                                                       #.....#.#.#.#.#.#.#.#...#.#.#.#.#.#  
  #.#.#.#.#.#########.#.###.###.#####          W     J   L         Z           G       O    ###.#.#.#.#.#.###.#.#####.#.###.#.#  
  #.#.#.#.#...#.#.....#.#.#...#...#.#          N     S   E         H           H       F    #.#.#.#...#.#...#.#.#.......#.#.#.#  
  ###.#.###.###.###.###.#.###.#.###.###########.#####.###.#########.###########.#######.#####.#######.#.###.###.#####.#.#.#####  
  #...#.#...#.......#.#...#...#...#.#.#.....#.#.#.#.#...#.#.....#...#...........#.#.....#.#...#...#...#...#...#.#.....#.......#  
  #.#######.#.#.#.#.#.#.#####.#.###.#.#####.#.#.#.#.###.#.#.#.###.###.###.#######.#####.#.#.###.###.#######.###.#.#####.###.###  
  #...#.#...#.#.#.#.#.......#.#.#...#...#.......#...#...#...#...#...#...#.........#...............#.....#.#.#...#.#.....#.....#  
  #.#.#.#.#.#####.#####.#.#####.###.###.###.#####.#.#.#########.#.###.###.#.#.#.#.#####.#.###.#####.#.###.###.#.###########.###  
  #.#.#...#...#.#.....#.#.#.#...#.#.........#.#.#.#.....#.......#.#.#...#.#.#.#.#.#.....#.#.#...#.#.#.#.......#...#.....#.....#  
  #.###.#.###.#.###.#.#####.#.#.#.#######.###.#.#.#########.#.###.#.#.###.###.#########.###.#####.###########.#.#######.###.###  
  #...#.#.#.......#.#.#.......#.#...............#.........#.#...#...#.#.#.#.......#...#.........#.#.#.#.#.....#.#.............#  
  #.###.#.#######.#####.#.###.#.###.#########.#.#######.###.#######.###.#.#.###.#####.#.#########.#.#.#.#####.###########.#####  
  #.#...#.....#.....#.#.#.#...#.#...#.......#.#.#.........#.#...#.....#.#.#.#.....#.....#.....#...........#.......#.........#.#  
  #.#####.#.###.###.#.###.###.#.###.#####.#.###.#.###.#.#.#.#.#.#.#####.#.###.#########.###.###.###.###.#####.#.#########.###.#  
  #.#.#.#.#.#.....#.#...#...#.#.#...#.....#.....#...#.#.#.#...#.#.....#.#.#.....#.#.....#.........#.#.....#...#...#...........#  
  #.#.#.#####.#.#####.###.###########.###.###.###.#.#.#####.###.###.###.###.###.#.#####.#.#####.#########.#.###.#####.#.###.#.#  
  #.......#...#...#.........#...#...#.#.#...#...#.#.#.#.....#.#...#.....#...#...#.#.........#.#.......#.#.#.#.#...#...#...#.#.#  
  #.#.#######.#.#.#.###.#.###.#.#.#####.#.###.###.###.###.###.#.#######.#######.#.#.#######.#.#.#.#####.###.#.#####.#.###.#.#.#  
  #.#.....#...#.#.#.#...#.#...#.......#.....#.#.#...#.#.....#.#.#.....#.#.......#.....#.#.#.#.#.#.#...#.#...#.....#.#.#...#.#.#  
  #.#.#.#.#####.#######.#.#.#########.###.#.###.#.#.#########.#.#.###.#.#######.#####.#.#.###.#####.###.#####.###.###.#####.#.#  
  #.#.#.#.....#.#...#.#.#.#.#.#...........#.#.#...#.#...#...#...#.#.#.....#.....#.#...............#...#.#...#...#.........#.#.#  
  #.###.#.#####.###.#.#######.###########.###.#.#.###.#.#.#####.#.#.###.#######.#.#####.#.#.#####.#.###.#.#.#####.#.###.#####.#  
  #.#...#.#...#.#.....#.#.#.........#.#.#.#...#.#.#.#.#.....#.#.#.#...#.#...........#...#.#.....#...#.....#.#...#.#.#.....#...#  
  #.#########.#####.###.#.###.###.#.#.#.#.###.###.#.#####.###.#.#.###.###.###.#.#.###.#.#############.###.#.###.#.###.#######.#  
  #...#...............#...#...#...#.....#.......#.......#.....#.#...#.#...#...#.#.#...#.........#.#...#.#.#...#...#.........#.#  
  #.#####.###.#######.###.#######.###.#.#.#########.#.#####.#.#.#.#############.#######.###.#####.#.###.#####.#.#.#.#.#.###.###  
  #.#.#...#...#.#...#.#.#.........#.#.#.......#.#...#.#...#.#.#.#...#.#.....#...#...#.#.#.#.#...........#.#...#.#.#.#.#...#...#  
  #.#.###.#####.###.#.#.###.#.#.###.###.#####.#.#.#######.#.#.#.#.###.#####.#.#####.#.#.#.###.#####.#.#.#.###########.#####.###  
  #...#.....#...............#.#...#.........#...#.#...#.#...#...#.....#.....#.#...........#.......#.#.#...#.....#.#.......#...#  
  #####.#######.###.###.#######.#######.#.#.#.#.#.#.###.###.#.#.#.###.###.#.#.###.###.#####.###.###.#.#.###.###.#.###.#######.#  
  #.....#.......#...#.....#.....#.......#.#.#.#.#.....#.#...#.#.#.#.....#.#...#.....#.......#.#...#.#.#.....#.#.#.#.#...#...#.#  
  ###############.###.#.#####.#######.#######.#.#####.#.#.#######.#####.#.#######.###########.###########.###.###.#.#.#####.###  
  #.#.#...#.#.#.#.#.#.#.#.......#.......#...#.#...#.....#.....#.#...#.#.#.......#.#.#...#...............#...........#.#.......#  
  #.#.###.#.#.#.###.###.#.#.#.###.#########.###.###.#.#####.###.###.#.#####.#####.#.#.###.#.#######.###.###.#.#.#.#######.#.###  
  #.........#...........#.#.#...#.#.......#.....#.#.#...#.........#.....#.......#.......#.#...#.#.#...#.#.#.#.#.#.........#.#.#  
  #.###.#.#.#.#.#.###.#.###.###.#######.###.#####.###.#.#.#######.#####.#.#######.###.#.#.###.#.#.#####.#.###.###.###.###.#.#.#  
  #.#...#.#...#.#.#...#.#.....#.#.................#...#.#.......#.#.....#.......#.#...#.....#.........#.....#.#.....#.#...#...#  
  ###########################################.#.#######.###.#########.#######.#########.#######################################  
                                             B A       W   G         G       T         E                                         
                                             L A       X   R         S       W         S                                         """

ex1 = """
         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """

ex2 = """
                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               """

class Maze:
    def __init__(self, map):
        self.map = map


    def solve(self):
        """
        1. Detect all portals.
            - Use linear time string search outside and inside the donut
            - They have a . instead of # on the maze wall
            - Results in a set of portals (nodes), e.g. [AA, BC, FD, ZZ]
            - Remember their position
        2. Find shortest direct paths between portals
            - Run BFS from each portal (without entering them)
            - Make sure to count distance correctly
            - Results in weighted graph edges, e.g. {JP: [(LF, 10)], AA: [(ZZ, 24)]}
            - Combine separate graphs into one
        3. Find shortest path from AA to ZZ using portals
            - Use Dijkstra on the edge list
            - Subtract 1 because we don't warp from ZZ
        """
        pass


assert Maze.solve(ex1) == 23
assert Maze.solve(ex2) == 58
print(Maze.solve(input))