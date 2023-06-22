import numpy as np
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = pd.read_csv('templates\modified_dataset.csv')
data.head()
# print(df)



def graph1(data):
    state_counts=data['State'].value_counts()
    #create chart
    fig, ax = plt.subplots()
    ax.bar(state_counts.index, state_counts.values, color='skyblue')
    ax.bar(state_counts.index,state_counts.values)

    #customize
    ax.set_title("State-Wise Chart")
    ax.set_xlabel("State")
    ax.set_ylabel("No. of registered societies under MSCS Act,2002")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Set background color
    fig.patch.set_facecolor('lightgray')

    #rotate x axis labels for better readability if required
    plt.xticks(rotation=90)
    plt.show()
    graph_file='media/graph1.png'
    plt.savefig(graph_file)


def grapha(data):
    state_counts = data['State'].value_counts()
    # # Create the chart
    plt.bar(state_counts.index, state_counts.values)
    plt.xlabel('State')
    plt.ylabel('No. of registered societies under MSCS Act,2002')
    plt.title('Societies per State')
   
    # Rotate x-axis labels for better readability if needed
    plt.xticks(rotation=90)

    # Display the chart
    graph_file='media/graph1.png'
    plt.savefig(graph_file)
    plt.show()
    

def graphb(data):
    counts = data['Sector Type'].value_counts()
    # # Create the chart
    plt.bar(counts.index, counts.values)
    plt.xlabel('Types of Societies')
    plt.ylabel('No. of registered societies under MSCS Act,2002')
    plt.title('Type-wise chart')
   
    # Rotate x-axis labels for better readability if needed
    plt.xticks(rotation=90)

    # Display the chart
    graph_file='media/graph2.png'
    plt.savefig(graph_file)
    plt.show()
    

def graphc(data):
    counts = data['Year'].value_counts()
    # # Create the chart
    plt.bar(counts.index, counts.values)
    plt.xlabel('Year')
    plt.ylabel('No. of registered societies under MSCS Act,2002')
    plt.title('Year-wise chart')
   
    # Rotate x-axis labels for better readability if needed
    plt.xticks(rotation=90)

    # Display the chart
    graph_file='media/graph3.png'
    plt.savefig(graph_file)
    plt.show()
    

    


def graph2(data):
    df=pd.DataFrame(data)

    #count the number of societies per type
    society_counts= df['Sector Type'].value_counts()

    #create a bar chart
    fig,ax=plt.subplots()
    ax.bar(society_counts.index, society_counts.values, color='red')
    ax.bar(society_counts.index,society_counts.values)

    # plt.figure(figsize=(12,6))

     #customize
    ax.set_title("Type-Wise Chart")
    ax.set_xlabel("Type of Societies")
    ax.set_ylabel("No. of registered societies under MSCS Act,2002")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Set background color
    fig.patch.set_facecolor('gray')

    #rotate x axis labels for better readability if required
    plt.xticks(rotation=90)
    plt.show()
    graph_file='media/graph2.png'
    plt.savefig(graph_file)




def graph3(data):
    df=pd.DataFrame(data)

    #count the number of societies per type
    society_counts= df['Year'].value_counts()

    #create a bar chart
    fig,ax=plt.subplots()
    ax.bar(society_counts.index, society_counts.values, color='blue')
    ax.bar(society_counts.index,society_counts.values)

    ax.set_title("Year-Wise Chart")
    ax.set_xlabel("Year")
    ax.set_ylabel("No. of registered societies under MSCS Act,2002")
    ax.grid(True, linestyle='--', alpha=0.5)

    # Set background color
    fig.patch.set_facecolor('white')

    #rotate x axis labels for better readability if required
    plt.xticks(rotation=90)
    plt.show()
    graph_file='media/graph3.png'
    plt.savefig(graph_file)


def graph(data):
    grapha(data)
    graphb(data)
    graphc(data)


graph(data)








