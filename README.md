# City-Science-Scientific-Programmer-task
 # Scientific Programmer Task Solution outline:

For this task I used Dijkstra's algorithm see the documentation in:
[1] https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 

User instructions to run the application:

-In the computer terminal input the following line command:
	python network.py exmouth-links.dat <Origin> <Destination>

Process of building the application:

-Line 4: First of all we write the code necessary to read the command line 
 arguments using the package "sys". We will introduce a testcase where 
 the command line input has to be equal to 4 to continue running the 
 program.
 
-Line 11: We then define the command line arguments which will be the application
 file name as "_" to ignore this variable, the network data
 file, the input origin ID and the input destination ID.
 
-Line 14: We then define a dictionary called "network", which will contain our network
 depending on the input origin and destination.
 
-Line 15: The input network is then opened and iterated over the different connecting
 nodes. The connecting node lines are then split into starting node, end or 
 destination and the distance between both nodes is provided as the last
 integer value in the line. We then check whether the start or origin is 
 in the network, if not, the start or origin input is added to the dict
 network variable previously defined as a key and the destination as another
 key with the respective distance values inside the origin key. This dictionary
 contains all the combinations and distances from each connecting node.
 
-Line 23 and 26: Then two testcases are made to make sure the input origin and destination 
 are valid and within the network input file.
 
-Line 31: The Dijkstra's algorithm is defined as a function with input
 parameters of the network dictionary, the origin and destination inputs.
 Taking reference from [1] the algorithm is initialised and the distance variable
 "dist" is set to infinity for every node in the network initially except 
 for the origin. We define another variable called visited as a set of the 
 visited nodes in the network.

-Line 39: A while loop within the function is initialised and set to stop when 
 the destination node enters the visited set. A variable named "curr"
 is defined to track the current node which is being iterated and "curr_dist"
 for the current distance between nodes, to keep track. A for loop is then initialised
 to iterate over the nodes in the network dictionary. Then a conditional
 statement is set to check whether the node has been visited, if it hasn't 
 been visited and the distance of that node is smaller from the previous one,
 redefine "curr_dist" to that distance which is smaller than the previously
 defined. The "curr" variable is also updated to that node ID. After finishing
 the for loop to obtain the shortest distances, the current node "curr" is then
 added to the visited set.

-Line 53: another for loop is initialised after adding the node to the visited
 set which will be in charge of updating the distances between the neighbour nodes
 and the current node to obtain the shortest distances. Inside, the conditional 
 statement checks whether the neighbour of the current node has been visited and
 if not, a new distance is calculated by adding the current distance plus the 
 neighbour distance. Afterwards, if the distance through the current network
 is smaller than the neighbour distance, the neighbour distance is stored as the 
 distance.

-Line 60: a list "path" which will contain the path of nodes is defined with the 
 initial value as the last node, destination. A while loop is initialised while the 
 last value of the "path" list is not the origin node. Then a for loop is iterated over the
 nodes in the network dictionary. If the destination node is in the network node dictionary 
 and the distance of the node plus the distance between the node and the destination
 node is equal to the distance of the destination, then the path list of nodes
 is appended to the "path" list and the destination is defined as the last iterating
 node. The whole path is reverse-engineered from the destination so the "path" 
 the list is inverted in order and returned from the function.

-Line 75 to end: another variable outside de function is defined as "path"
 and the function is called inside to obtain the shortest path between both input
 nodes. Then the path is simply printed and checked as a last testcase for the origin and
 destination in the case the origin and destination are not linked.
 
 
 Example run:
 
 python network.py exmouth-links.dat J1006 J1048
