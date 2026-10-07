graph = {
    "Almeria": [("Granada", 167), ("Murcia", 218)],
    "Granada": [("Almeria", 167), ("Jaen", 92), ("Malaga", 123)],
    "Murcia": [("Almeria", 218), ("Albacete", 146), ("Alicante", 81)],
    "Albacete": [("Murcia", 146), ("Alicante", 167), ("Cuenca", 144), ("Madrid", 257)],
    "Alicante": [("Murcia", 81), ("Albacete", 167), ("Valencia", 166)],
    "Jaen": [("Granada", 92), ("Cordoba", 120), ("Madrid", 331)],
    "Malaga": [("Granada", 123), ("Sevilla", 206), ("Cadiz", 235)],
    "Sevilla": [("Malaga", 206), ("Cadiz", 121), ("Cordoba", 140), ("Merida", 192)],
    "Cadiz": [("Malaga", 235), ("Huelva", 210), ("Sevilla", 121)],
    "Huelva": [("Cadiz", 210)],
    "Cordoba": [("Sevilla", 140), ("Jaen", 120), ("CiudadReal", 195)],
    "CiudadReal": [("Cordoba", 195), ("Toledo", 118)],
    "Merida": [("Sevilla", 192), ("Badajoz", 64), ("Caceres", 75)],
    "Badajoz": [("Merida", 64)],
    "Caceres": [("Merida", 75), ("Madrid", 301), ("Salamanca", 202)],
    "Valencia": [("Alicante", 166), ("Castellon", 74), ("Cuenca", 199)],
    "Castellon": [("Valencia", 74), ("Tarragona", 187), ("Teruel", 144)],
    "Cuenca": [("Valencia", 199), ("Teruel", 148), ("Albacete", 144), ("Madrid", 168)],
    "Teruel": [("Castellon", 144), ("Cuenca", 148), ("Zaragoza", 171)],
    "Zaragoza": [("Teruel", 171), ("Lleida", 152), ("Huesca", 74), ("Pamplona", 178), ("Soria", 159), ("Guadalajara", 256)],
    "Tarragona": [("Castellon", 187), ("Barcelona", 99)],
    "Barcelona": [("Tarragona", 99), ("Lleida", 163), ("Gerona", 103)],
    "Lleida": [("Barcelona", 163), ("Gerona", 229), ("Huesca", 112), ("Zaragoza", 152)],
    "Gerona": [("Barcelona", 103), ("Lleida", 229)],
    "Huesca": [("Lleida", 112), ("Zaragoza", 74), ("Pamplona", 165)],
    "Pamplona": [("Zaragoza", 178), ("Huesca", 165)],
    "Soria": [("Zaragoza", 159), ("Burgos", 142), ("Guadalajara", 171), ("Logrono", 101)],
    "Guadalajara": [("Zaragoza", 256), ("Madrid", 60), ("Soria", 171)],
    "Madrid": [("Jaen", 331), ("Albacete", 257), ("Cuenca", 168), ("Guadalajara", 60), ("Burgos", 245), ("Segovia", 92), ("Avila", 109), ("Caceres", 301), ("Toledo", 72)],
    "Burgos": [("Madrid", 245), ("Palencia", 92), ("Soria", 142), ("Vitoria", 118), ("Santander", 181)],
    "Segovia": [("Madrid", 92), ("Avila", 66), ("Valladolid", 115)],
    "Avila": [("Madrid", 109), ("Salamanca", 109), ("Segovia", 66)],
    "Toledo": [("CiudadReal", 118), ("Madrid", 72)],
    "Salamanca": [("Avila", 109), ("Caceres", 202), ("Zamora", 66)],
    "Zamora": [("Salamanca", 66), ("Valladolid", 100), ("Leon", 141), ("Orense", 259)],
    "Valladolid": [("Segovia", 115), ("Leon", 136), ("Zamora", 100), ("Palencia", 51)],
    "Palencia": [("Valladolid", 51), ("Burgos", 92)],
    "Leon": [("Valladolid", 136), ("Zamora", 141), ("Lugo", 223), ("Oviedo", 125)],
    "Logrono": [("Soria", 101), ("Vitoria", 94)],
    "Vitoria": [("Logrono", 94), ("Burgos", 118), ("SanSebastian", 100), ("Bilbao", 62)],
    "SanSebastian": [("Vitoria", 100), ("Bilbao", 101)],
    "Bilbao": [("Vitoria", 62), ("SanSebastian", 101), ("Santander", 100)],
    "Santander": [("Bilbao", 100), ("Burgos", 181), ("Oviedo", 192)],
    "Oviedo": [("Santander", 192), ("Leon", 125), ("Lugo", 227), ("Coruna", 287)],
    "Lugo": [("Leon", 223), ("Oviedo", 227), ("Coruna", 98), ("Pontevedra", 195)],
    "Coruna": [("Lugo", 98), ("Oviedo", 287), ("Santiago", 75)],
    "Pontevedra": [("Lugo", 195), ("Santiago", 64), ("Orense", 119)],
    "Orense": [("Pontevedra", 119), ("Zamora", 259)],
    "Santiago": [("Coruna", 75), ("Pontevedra", 64)]
} 

cities = {
    "Almeria": 571, "Granada": 507, "Jaen": 439, "Cordoba": 419, "Malaga": 550,
    "Huelva": 525, "Sevilla": 487, "Cadiz": 586, "Murcia": 510, "Albacete": 383,
    "Alicante": 515, "Valencia": 441, "Castellon": 435, "Tarragona": 502, "Barcelona": 576,
    "Lleida": 445, "Gerona": 627, "Merida": 334, "Badajoz": 363, "Caceres": 280,
    "CiudadReal": 305, "Toledo": 208, "Cuenca": 280, "Guadalajara": 173, "Zaragoza": 319,
    "Teruel": 337, "Huesca": 362, "Logrono": 209, "Vitoria": 215, "Bilbao": 232,
    "SanSebastian": 292, "Santander": 215, "Oviedo": 212, "Coruna": 357, "Santiago": 343,
    "Pontevedra": 335, "Orense": 271, "Lugo": 278, "Madrid": 162, "Leon": 126,
    "Zamora": 87, "Salamanca": 109, "Segovia": 94, "Valladolid": 0, "Burgos": 114,
    "Palencia": 43, "Soria": 187, "Pamplona": 284, "Avila": 110
}


def find_shortest_path(graph, start, end, path =[]): 
    if start == end: 
        return path
         
    while start != end : #until we're not arrived to the destination 
        shortest = float('inf') #minus infinte, shortest reprenst the shortest/closest path from the current city to any other city considering the straight line value to the destination
        s_city = None
        for city, num in graph[start]: #checking all the neighbors
            if city not in path: 
                newpath = cities[city]
                if newpath < shortest: #if we have never been to that city and it's the closest to the target then we select it as our planned destination 
                        shortest = newpath
                        s_city = city
        path = path + [start] #add the city we chose to go to to our list retracing our path
        start = s_city 

    path = path + [end]
    return  path 
          
# the shortest path 
print("the path from Malaga to Valladolid using greedy best-first is \n", find_shortest_path(graph, 'Malaga', 'Valladolid')) 

from collections import deque
import queue

def a_star(graph, start, end, path =[]): 
    visited = set()
    cost = 0

    if start == end: 
        return curr_path
    
    pq = queue.PriorityQueue()
    pq.put(  (0,start,0,[start]) ) #initial case
    

    while not pq.empty() :
        fn , curr_city, curr_cost, curr_path = pq.get()  #pop the element with the least value according to the first argument of the queue

        if curr_city == end :
            return curr_path

        if curr_city not in visited: 
                visited.add(curr_city) #add to my repertory of visited cities

        else : continue

        for city, num in graph[curr_city]: 
                if(city not in visited) :
                    pq.put( (num + cities[city] + curr_cost, city, curr_cost + num, curr_path + [city]) )
        

    return print("impossible")

print("the path from Malaga to Valladolid using a* search is \n" ,a_star(graph, 'Malaga', 'Valladolid') ) 

#Made by EL OTMANI Youssef