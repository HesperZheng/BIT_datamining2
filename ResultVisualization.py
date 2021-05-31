import json
import matplotlib.pyplot as plt

class Visualization():

    with open("./results/sup_rata.json") as f1:
        freq = [json.loads(each) for each in f1.readlines()]

    with open("./results/strong_rules_list.json") as f2:
        rules = [json.loads(each) for each in f2.readlines()]

    freq_sup = [each["sup"] for each in freq]
    plt.boxplot(freq_sup)
    plt.ylabel("Frequent item")
    plt.show()

    rules_sup = [each["sup"] for each in rules]
    rules_conf = [each["conf"] for each in rules]

    plt.scatter(rules_sup, rules_conf, marker='o', color='red', s=40)
    plt.xlabel = 'Sup'
    plt.ylabel = 'Conf'
    plt.legend(loc='best')
    plt.show()