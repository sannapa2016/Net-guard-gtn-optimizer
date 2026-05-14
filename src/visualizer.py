import matplotlib.pyplot as plt

def plot_gtn_waterfall(wac, rebate, gov, fees):
    labels = ['WAC', 'Rebates', 'Gov/340B', 'Fees', 'Net Price']
    values = [wac, -rebate, -gov, -fees]
    net = wac - rebate - gov - fees
    values.append(net)
    
    # Simple cumulative logic for plotting
    current = 0
    for i, val in enumerate(values):
        plt.bar(labels[i], val, bottom=current if i < 4 else 0, color='green' if val > 0 else 'red')
        current += val if i < 4 else 0
        
    plt.title("Gross-to-Net Revenue Erosion")
    plt.ylabel("USD")
    plt.savefig('data/gtn_waterfall.png')
