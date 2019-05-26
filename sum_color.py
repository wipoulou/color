def avg_color(output):
    """ Image est un output de camera """
    
    #Tiré directement de la documentation
    image = output.array.shape[1]

    #Taille de l'image pour savoir la division qu'il faut faire
    size_h = len(image)
    size_l = len(image[0])

    #Initialisation du tableau qui va stocker les valeurs avg
    avg = [0, 0, 0]

    #Itération sur tous les pixels de l'image
    for line in image:
        for pixel in line:
            for i in range(len(avg)):
                avg[i] += pixel[i]

    #Return la valeur moyenne des pixels
    return [(avg[i]/(size_h*size_l)) for i in range(3)]


def match_color(color):
    if(color[0] > color[1] and color[0] > color[2]):
        return "red"
    elif(color[1] > color[0] and color[1] > color[2]):
        return "green"
    elif(color[2] > color[1] and color[2] > color[0]):
        return "blue"
    else:
        return "Pas de cube"


color_dic = {
    "red" : (255, 0, 0),
    "green": (0, 255, 255),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
}

def find_color(color, tolerance=80, dic=color_dic):

    best = ("none", 0)

    for sample in color_dic:
        avg = [abs(sample[i]-color[i]) for i in range(3)]
        fit = (avg[0]+avg[1]+avg[2])/3

        if fit > tolerance and fit > best[0]:
            best = (color_dic, fit)

    return best
