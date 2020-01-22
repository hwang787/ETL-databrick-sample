import http.client
import json
import time
import timeit
import sys
import collections
from pygexf.gexf import *


#
# implement your data retrieval code here
#
API=sys.argv[1]
print(API)
host="www.rebrickable.com"
h = http.client.HTTPConnection(host)
print(h)
h.request("GET","https://rebrickable.com/api/v3/lego/sets/?key="+str(API)+'&page_size=290&&min_parts=1100&ordering=-num_parts%2Cid')
r1 = h.getresponse()
print(r1.status, r1.reason)
# Load JSON: json_data
json_data = json.load(r1)
#print(type(json_data))
#print('json_data[results]:'+str(type(json_data['results'])))
#print(type(json_data['results'].pop()))
#print(json_data['results'][-1]['num_parts'])
min_parts=json_data['results'][-1]['num_parts']
#Print each key-value pair in json_data
#for k in json_data.keys():
    #print(k+ ': ',json_data[k])


#Print number of Parts
    #num_parts = json_data["num_parts"]
    #print(json_data["num_parts"])
# complete auto grader functions for Q1.1.b,d

def min_parts():
    # you must replace this with your own value
    return min_parts


sets=json_data['results'];
def lego_sets():
    lego_sets=list()
    for set in sets:
        lego_sets.append(set['num_parts'])    
    """
    return a list of lego sets.
    this may be a list of any type of values
    but each value should represent one set

    e.g.,
    biggest_lego_sets = lego_sets()
    print(len(biggest_lego_sets))
    > 280
    e.g., len(my_sets)
    """
    return lego_sets
set_nums=lego_sets();
r1.close()
#==================================1.b================================================================================
h = http.client.HTTPConnection(host)
print(h)
set_results= json_data['results']

parts={"set_num": list}
for set in set_results:
    set_num= str(set['set_num'])
    print(set_num)
    parts[set_num]=list()
    
    
    #print(set_results)
    
        
    h.request("GET","https://rebrickable.com/api/v3/lego/sets/"+set_num+"/parts/?key="+str(API)+'&page_size=1000/20&is_spare=True&min_quantity=1400&ordering=-results_quantity%2Cid')
    r1 = h.getresponse()
    print(r1.status, r1.reason)
    if r1.status!=200:
        break
    i=0

# Load JSON: json_data
    json_data_part = json.load(r1)
    #print('question1.b:'+str(type(json_data)))

    #print(type(json_data_part['results']))
    #it is a list and this list contain 20 parts for one set
    if json_data_part['results']==None:
        break
    parts_perSet=json_data_part['results']
    #print("FOR ONE SET ")
    #print(parts)
    i=0
    if  len(json_data_part['results'])>20:
        while i<20:
        #if max(parts_perSet, key=lambda x:x['quantity'])==[]:
            #i=i-1
        #else:
            print("trouble maker"+str(set_num))
            maxQuantityPart = max(parts_perSet, key=lambda x:x['quantity'])
            part_info={'part_num': '','part_color': '','part_name': '','part_quantity': '','part_ID': ''}
        #print(part['part'])
            if i>20:
                break
            num=maxQuantityPart['part']['part_num']
            part_info['part_num']=num
            color=maxQuantityPart['color']['rgb']
            part_info['part_color']=color
            part_info['part_name']=maxQuantityPart['part']['name']
            part_info['part_quantity']=maxQuantityPart['quantity']
            part_info['part_ID']=num+'_'+color

            parts[set_num].append(part_info)
            i=i+1
            parts_perSet.remove(maxQuantityPart)
        
    #for part in parts_perSet:
    
        
#print(parts)

#for set in json_data_part['results']:
    #id.append(set['part_num'])
#for set in json_data['colors']:
    #color.append(set['rgb'])
#newID = list(zip(id,color))
#print(newID)
#=======================1.1c=================================================================================================================================

#gexf = Gexf('Paul Girard','A hello world! file')
#graph=gexf.addGraph('directed','static','a hello world graph')
#graph.addNode('0','hello')
#graph.addNode('1','World')
#graph.addEdge('0','0','1')
#output_file=open('hellowrld.gexf','wb')
#gexf.write(output_file)


def gexf_graph():
    """
    return the completed Gexf graph object
    """
    # you must replace these lines and supply your own graph
    my_gexf = Gexf("Hanchen", "bricks_graph")
    graph=my_gexf.addGraph("undirected", "static", "bricks_graph")
    
    
    b=graph.addNodeAttribute(title='Type',type="string")
    i=1
    for set in sets:
        
        set_num=set['set_num']
        #set = Node(graph,set['set_num'],set['name'],r="0", g="0", b="0")
        
        graph.addNode(set['set_num'],set['name'],r="0", g="0", b="0").addAttribute(b,"set")
        #set.addAttribute(set['set_num'],"set")

        for part_info in parts[set_num]:
            graph.addNode(part_info['part_ID'],part_info['part_name'],
                          
                          r=str(int(str(part_info['part_color'][0:2]),16)),
                          g=str(int(str(part_info['part_color'][2:4]),16)),
                          b=str(int(str(part_info['part_color'][4:6]),16))
                          ).addAttribute(b,"part")
            
            graph.addEdge(set['set_num']+part_info['part_ID']+str(part_info['part_quantity']),set['set_num'],part_info['part_ID'],
                          weight=part_info['part_quantity'])
            
            
        
    
    output_file=open('bricks_graph.gexf','wb')
    my_gexf.write(output_file)
    print(i)
    return my_gexf.graphs[0]

gexf_graph();

# complete auto-grader functions for Q1.2.d

def avg_node_degree():
    """
    hardcode and return the average node degree
    (run the function called “Average Degree”) within Gephi
    """
    # you must replace this value with the avg node degree
    return 8.01

def graph_diameter():
    """
    hardcode and return the diameter of the graph
    (run the function called “Network Diameter”) within Gephi
    """
    # you must replace this value with the graph diameter
    return 8

def avg_path_length():
    """
    hardcode and return the average path length
    (run the function called “Avg. Path Length”) within Gephi
    :return:
    """
    # you must replace this value with the avg path length
    return 4.074
