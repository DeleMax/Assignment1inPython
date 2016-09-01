import time
from tkinter import*

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

def do():
    filename = entry_1.get()
    start = time.time() 
    
    f = open(filename, 'r')
    
    content = list(f)
    
    graph = {'vertices': [], 'edges': []}
    
    graph['vertices'] = range(0, len(content))
    
    edges = set()
    
    for i in range(len(content)):
      str_arr = content[i].split()
      for j in range(len(str_arr)):
         edges.add((int(str_arr[j]),i,j))
        
    graph['edges'] = edges
    
    minimum_spanning_tree = kruskal(graph)

    p = open("resultPython.txt", 'w+')
    v= open("resultPython2.txt", 'w+')
    
    result = '\n'.join([ str(myelement) for myelement in minimum_spanning_tree ])
    p.write(result)
    
    v.write("The total number of edges in the minimum spanning tree is: " + str(len(minimum_spanning_tree))+'\n')
    
    v.write("The number of nodes is: " + str(len(content))+'\n')

    v.write("The total cost of the spanning tree is: " + str(sum([x[0] for x in minimum_spanning_tree]))+'\n')
    end = (time.time() - start)
    v.write("Total Execution time = "+str(end)+" seconds")

    
    v.close()
    p.close()
    
    f = open('resultPython2.txt','r')
    conttent = set(f)
    sprintt =  '\n'.join([ str(myelement) for myelement in conttent ])
    label_2.config(text=sprintt)
    f.close() 
       
def loadme():
    f = open('resultPython.txt','r')
    content = set(f)
    sprint =  '\n'.join([ str(myelement) for myelement in content ])
    label_2.config(text=sprint)
    f.close()
    
root = Tk()

label_l = Label(root, text = "File Name")
entry_1 = Entry(root)

label_2 = Label(root, text = '')

label_l.grid(row=0)
entry_1.grid(row=0, column=1)

label_2.grid(columnspan = 10)


c_1 = Checkbutton(root, text= "Use Kruskal's Algorithm")
c_2 = Checkbutton(root, text= "Use Prim's Algorithm")
c_1.select()
c_1.grid(columnspan=2)
c_2.grid(columnspan=2)

button_1 = Button(root, text = "Compute", command= do)
button_2 = Button(root, text = "Step", command = loadme)

button_1.grid(columnspan = 3)
button_2.grid(columnspan = 4)

root.mainloop()


