import tkinter
import tkinter.filedialog
from PyPDF2 import PdfFileReader


def browse():
    in_path = tkinter.filedialog.askopenfilename()
    return in_path


def mainfunction(input, output):
    county_codes = {'ADAMS': '001'
        , 'ALCORN': '003'
        , 'AMITE': '005'
        , 'ATTALA': '007'
        , 'BENTON': '009'
        , 'BOLIVAR': '011'
        , 'CALHOUN': '013'
        , 'CARROLL': '015'
        , 'CHICKASAW': '017'
        , 'CHOCTAW': '019'
        , 'CLAIBORNE': '021'
        , 'CLARKE': '023'
        , 'CLAY': '025'
        , 'COAHOMA': '027'
        , 'COPIAH': '029'
        , 'COVINGTON': '031'
        , 'DESOTO': '033'
        , 'FORREST': '035'
        , 'FRANKLIN': '037'
        , 'GEORGE': '039'
        , 'GREENE': '041'
        , 'GRENADA': '043'
        , 'HANCOCK': '045'
        , 'HARRISON': '047'
        , 'HINDS': '049'
        , 'HOLMES': '051'
        , 'HUMPHREYS': '053'
        , 'ISSAQUENA': '055'
        , 'ITAWAMBA': '057'
        , 'JACKSON': '059'
        , 'JASPER': '061'
        , 'JEFFERSON': '063'
        , 'JEFF DAVIS': '065'
        , 'JONES': '067'
        , 'KEMPER': '069'
        , 'LAFAYETTE': '071'
        , 'LAMAR': '073'
        , 'LAUDERDALE': '075'
        , 'LAWRENCE': '077'
        , 'LEAKE': '079'
        , 'LEE': '081'
        , 'LEFLORE': '083'
        , 'LINCOLN': '085'
        , 'LOWNDES': '087'
        , 'MADISON': '089'
        , 'MARION': '091'
        , 'MARSHALL': '093'
        , 'MONROE': '095'
        , 'MONTGOMERY': '097'
        , 'NESHOBA': '099'
        , 'NEWTON': '101'
        , 'NOXUBEE': '103'
        , 'OKTIBBEHA': '105'
        , 'PANOLA': '107'
        , 'PEARL RIVER': '109'
        , 'PERRY': '111'
        , 'PIKE': '113'
        , 'PONTOTOC': '115'
        , 'PRENTISS': '117'
        , 'QUITMAN': '119'
        , 'RANKIN': '121'
        , 'SCOTT': '123'
        , 'SHARKEY': '125'
        , 'SIMPSON': '127'
        , 'SMITH': '129'
        , 'STONE': '131'
        , 'SUNFLOWER': '133'
        , 'TALLAHATCHIE': '135'
        , 'TATE': '137'
        , 'TIPPAH': '139'
        , 'TISHOMINGO': '141'
        , 'TUNICA': '143'
        , 'UNION': '145'
        , 'WALTHALL': '147'
        , 'WARREN': '149'
        , 'WASHINGTON': '151'
        , 'WAYNE': '153'
        , 'WEBSTER': '155'
        , 'WILKINSON': '157'
        , 'WINSTON': '159'
        , 'YALOBUSHA': '161'
        , 'YAZOO': '163'}
    fp = PdfFileReader(open(input, 'rb'))
    output = open(output, 'w+')
    output.write(
        "Year,County,County ID,nhs_total_n,nhs_white_n,nhs_black_n,nhs_total_p,nhs_white_p,nhs_black_p,hsd_total_n,hsd_white_n,hsd_black_n,hsd_total_p,hsd_white_p,hsd_black_p,4yr_total_n,4yr_white_n,4yr_black_n,4yr_total_p,4yr_white_p,4yr_black_p,lbw_total_n,lbw_white_n,lbw_black_n,lbw_total_p,lbw_white_p,lbw_black_p,pre_total_n,pre_white_n,pre_black_n,pre_total_p,pre_white_p,pre_black_p\n")
    pages = fp.getNumPages()
    output_array = []
    for x in range(0, pages):
        page = fp.getPage(x).extractText()  # reading each page.
        strings = page.splitlines()  # Each page split into an array

        county_line_array = strings[0].split()  # get the county name from first line.
        county_name = county_line_array[6]
        county_year = county_line_array[8]
        if (county_line_array[7] != "County,"):
            county_name = county_name + " " + county_line_array[7]
            county_year = county_line_array[9]
        output_array.extend([county_year, county_name, "28" + county_codes[county_name.upper()]])

        line_undereight = strings[28].split()
        line_ninetotwelve = strings[29].split()
        line_highschool = strings[30].split()
        line_somecollege = strings[31].split()
        line_associate = strings[32].split()
        line_bachelors = strings[33].split()
        line_masters = strings[34].split()
        line_doctorate = strings[35].split()
        line_lowbirth = strings[9].split()
        line_premature = strings[7].split()

        total_nohighschool = float(line_undereight[14]) + float(line_ninetotwelve[6])
        white_nohighschool = float(line_undereight[15]) + float(line_ninetotwelve[7])
        black_nohighschool = float(line_undereight[16]) + float(line_ninetotwelve[8])
        totalpercent_nohighschool = float(line_undereight[17]) + float(line_ninetotwelve[9])
        whitepercent_nohighschool = float(line_undereight[18]) + float(line_ninetotwelve[10])
        blackpercent_nohighschool = float(line_undereight[19]) + float(line_ninetotwelve[11])

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

        output_array.extend([total_nohighschool, white_nohighschool, black_nohighschool,
                             "{0:.3f}".format(totalpercent_nohighschool / 100),
                             "{0:.3f}".format(whitepercent_nohighschool / 100),
                             "{0:.3f}".format(blackpercent_nohighschool / 100)])
        output_array.extend([total_highschool, white_highschool, black_highschool,
                             "{0:.3f}".format(totalpercent_highschool / 100),
                             "{0:.3f}".format(whitepercent_highschool / 100),
                             "{0:.3f}".format(blackpercent_highschool / 100)])
        output_array.extend([total_college, white_college, black_college,
                             "{0:.3f}".format(totalpercent_college / 100),
                             "{0:.3f}".format(whitepercent_college / 100),
                             "{0:.3f}".format(blackpercent_college / 100)])
        output_array.extend([total_lbw, white_lbw, black_lbw,
                             "{0:.3f}".format(totalpercent_lbw / 100),
                             "{0:.3f}".format(whitepercent_lbw / 100),
                             "{0:.3f}".format(blackpercent_lbw / 100)])
        output_array.extend([total_premature, white_premature, black_premature,
                             "{0:.3f}".format(totalpercent_premature / 100),
                             "{0:.3f}".format(whitepercent_premature / 100),
                             "{0:.3f}".format(blackpercent_premature / 100)])

        outputstring = ""
        for y in output_array:
            outputstring = outputstring + str(y) + ","
        outputstring += "\n"
        output.write(outputstring)
        output_array.clear()
    output.close()

    return "CSV file successfully filled out."
