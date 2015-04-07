#pass this function an html string and a file name
#without a file extension. It will save the tables from
#the html string in a csv with the input file name provided
def htmlToCsv(htmlString, outputFileName):
    splitHTML = htmlString.split("<table")
    finalString = ""

    tables = 1
    while tables < len(splitHTML):
        tableSplit = splitHTML[tables].split("<tr>")
        tables += 1
        tableSplit = tableSplit[1:]
        
        for each in tableSplit:
            dataItems = each.split("<td>")
            dataItems = dataItems[1:]
            
            for eachy in dataItems:
                dataItem = eachy.split("<")
                finalString = finalString + dataItem[0] + ","
            finalString = finalString.strip(",")
            finalString = finalString + "\n"


    finalString = finalString.strip("\n")
    filey = open(outputFileName+".csv", "w")
    filey.write(finalString)
    filey.close()
