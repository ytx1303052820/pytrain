import csv
#author Yu Tongxin(Front) from Room1
portFile = "data/Portfolio.csv"
indicesFile = "data/Indices.csv"
priceFile = "data/Prices.csv"
ratesFile = "data/Rates.csv"
secFile = "data/Securities.csv"


def loadData(fileName, key, value):
    dict={}
    with open(fileName, "r", encoding="utf-8-sig") as f:
        fileReader = csv.DictReader(f)
        for row in fileReader:
            dict[row[key]]=row[value]
    f.close()
    return dict

def loadPrice():
    dict = {}
    with open(priceFile, "r", encoding="utf-8-sig") as f:
        fileReader = csv.DictReader(f)
        for row in fileReader:
            dict[row['Symbol']+"_"+row['Date']] = row['Price']
    f.close()
    return dict
def loadRates():
    dict = {}
    with open(ratesFile, "r", encoding="utf-8-sig") as f:
        fileReader = csv.DictReader(f)
        for row in fileReader:
            dict[row['Base']+"_"+row['Terms']+"_"+row['Date']] = row['FxRate']
    f.close()
    return dict
def run(date):
    indicesDict = loadData(indicesFile, 'Index', 'CCY')
    portfoDict = loadData(portFile, 'Symbol', 'Qty')
    securitiesDict = loadData(secFile, 'Symbol', 'Index')
    symbol_datePriceDict = loadPrice()
    rates = loadRates()
    print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format("Symbol","Price","Qty","CCY","FX Rate","Val(USD)"))
    totalValue=0
    for (k,v) in portfoDict.items():
        price = symbol_datePriceDict[k+"_"+date]
        qty = v
        index = securitiesDict[k]
        base = indicesDict[index]
        if rates.get(base+"_"+"USD"+"_"+date,0)!=0:
            rate = rates[base + "_" + "USD" + "_" + date]
            value = float(price) * float(rate)
        elif rates.get("USD_"+base+"_"+date,0)!=0:
            rate = rates["USD_"+base+"_"+date]
            value = float(price) / float(rate)
            rate = 1.0/float(rate)
        else:
            continue
        total = value*float(qty)
        totalValue+=total
        print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'\
              .format(k, price, qty, base, "%.6f"%float(rate), "%.2f"%float(total)))
    print("\tTotal Value on", date," ", totalValue," USD")
run("12/01/2017")

