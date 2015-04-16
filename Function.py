import tkinter
import tkinter.filedialog
from PyPDF2 import PdfFileReader

def browse():
    in_path = tkinter.filedialog.askopenfilename()
    return in_path

def mainfunction(input, output):
    fp=PdfFileReader(open(input,'rb'))
    output = open(output, 'w+')
    output.write(",no high school,,,,,,high school,,,,,,4 years college,,,,,\n")
    output.write("county,total,white,black,total,white,black,total,white,black,total,white,black,total,white,black,total,white,black,lbw_total_n,lbw_white_n,lbw_black_n,lbw_total_p,lbw_white_p,lbw_black_p,pre_total_n,pre_white_n,pre_black_n,pre_total_p,pre_white_p,pre_black_p\n")
    pages = fp.getNumPages()
    output_array = []
    for x in range(0,pages):
        page = fp.getPage(x).extractText() #reading each page.
        strings = page.splitlines() #Each page split into an array

        county_line_array = strings[0].split() #get the county name from first line.
        output_array.append(county_line_array[6])

        line_undereight = strings[28].split()
        line_ninetotwelve = strings[29].split()
        line_highschool = strings[30].split()
        line_somecollege = strings[31].split()
        line_associate = strings[32].split()
        line_bachelors = strings[33].split()
        line_masters = strings[34].split()
        line_doctorate = strings[35].split()
        line_lowbirth = strings[9].split()
        line_premature= strings[7].split()

        total_nohighschool = float(line_undereight[14]) + float(line_ninetotwelve[6])
        white_nohighschool = float(line_undereight[15]) + float(line_ninetotwelve[7])
        black_nohighschool = float(line_undereight[16]) + float(line_ninetotwelve[8])
        totalpercent_nohighschool= float(line_undereight[17]) + float(line_ninetotwelve[9])
        whitepercent_nohighschool= float(line_undereight[18]) + float(line_ninetotwelve[10])
        blackpercent_nohighschool= float(line_undereight[19]) + float(line_ninetotwelve[11])

        total_highschool = float(line_highschool[6]) + float(line_somecollege[4]) + float(line_associate[2])
        white_highschool = float(line_highschool[7]) + float(line_somecollege[5]) + float(line_associate[3])
        black_highschool = float(line_highschool[8]) + float(line_somecollege[6]) + float(line_associate[4])
        totalpercent_highschool = float(line_highschool[9]) + float(line_somecollege[7]) + float(line_associate[5])
        whitepercent_highschool = float(line_highschool[10]) + float(line_somecollege[8]) + float(line_associate[6])
        blackpercent_highschool = float(line_highschool[11]) + float(line_somecollege[9]) + float(line_associate[7])

        total_college = float(line_bachelors[2]) + float(line_masters[2]) + float(line_doctorate[1])
        white_college = float(line_bachelors[3]) + float(line_masters[3]) + float(line_doctorate[2])
        black_college = float(line_bachelors[4]) + float(line_masters[4]) + float(line_doctorate[3])
        totalpercent_college = float(line_bachelors[5]) + float(line_masters[5]) + float(line_doctorate[4])
        whitepercent_college = float(line_bachelors[6]) + float(line_masters[6]) + float(line_doctorate[5])
        blackpercent_college = float(line_bachelors[7]) + float(line_masters[7]) + float(line_doctorate[6])

        total_lbw = float(line_lowbirth[5])
        white_lbw = float(line_lowbirth[6])
        black_lbw = float(line_lowbirth[7])
        totalpercent_lbw = float(line_lowbirth[8])
        whitepercent_lbw = float(line_lowbirth[9])
        blackpercent_lbw = float(line_lowbirth[10])

        total_premature = float(line_premature[5])
        white_premature = float(line_premature[6])
        black_premature = float(line_premature[7])
        totalpercent_premature = float(line_premature[8])
        whitepercent_premature = float(line_premature[9])
        blackpercent_premature = float(line_premature[10])

        output_array.extend([total_nohighschool, white_nohighschool, black_nohighschool, "{0:.3f}".format(totalpercent_nohighschool/100), "{0:.3f}".format(whitepercent_nohighschool/100), "{0:.3f}".format(blackpercent_nohighschool/100)])
        output_array.extend([total_highschool, white_highschool, black_highschool, "{0:.3f}".format(totalpercent_highschool/100), "{0:.3f}".format(whitepercent_highschool/100), "{0:.3f}".format(blackpercent_highschool/100)])
        output_array.extend([total_college, white_college, black_college, "{0:.3f}".format(totalpercent_college/100), "{0:.3f}".format(whitepercent_college/100), "{0:.3f}".format(blackpercent_college/100)])
        output_array.extend([total_lbw, white_lbw, black_lbw, "{0:.3f}".format(totalpercent_lbw/100), "{0:.3f}".format(whitepercent_lbw/100), "{0:.3f}".format(blackpercent_lbw/100)])
        output_array.extend([total_premature, white_premature, black_premature, "{0:.3f}".format(totalpercent_premature/100), "{0:.3f}".format(whitepercent_premature/100), "{0:.3f}".format(blackpercent_premature/100)])

        outputstring= ""
        for y in output_array:
            outputstring = outputstring + str(y) + ","
        outputstring = outputstring + "\n"
        output.write(outputstring)
        output_array.clear()
    output.close()

    return "You did not do anything moron."
