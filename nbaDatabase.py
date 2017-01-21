import requests
from bs4 import BeautifulSoup
import sys, os, time

# os.system("clear")

EC=[]
record_ec=[]
ec_stats={}

WC=[]
record_wc=[]
wc_stats={}

def getTeams():

    url="http://scorecenter.espn.go.com/nba/standings?sort=leagueWinPercent"
    r=requests.get(url)
    soup=BeautifulSoup(r.text, "lxml")


    table_rows=soup.select(".tablehead tr")

    for i in range(2,17):   #EAST CONFERENCE
        table_cells_ec=table_rows[i].select("td")
        team_ec=table_cells_ec[0]

        r=str(table_cells_ec[1].text.strip())+"-"+str(table_cells_ec[2].text.strip()) #record

        WP_ec=table_cells_ec[3].text.strip()
        GB_ec=table_cells_ec[4].text.strip()
        HOME_ec=table_cells_ec[5].text.strip()
        ROAD_ec=table_cells_ec[6].text.strip()
        DIV_ec=table_cells_ec[7].text.strip()
        CONF_ec=table_cells_ec[8].text.strip()
        PF_ec=table_cells_ec[9].text.strip()
        PA_ec=table_cells_ec[10].text.strip()
        STRK_ec=table_cells_ec[12].text.strip()
        L10_ec=table_cells_ec[13].text.strip()

        EC.append(team_ec.text.strip())
        record_ec.append(r)

        ec_stats[team_ec.text.strip()]=[WP_ec, GB_ec, HOME_ec, ROAD_ec, DIV_ec, CONF_ec, PF_ec, PA_ec, STRK_ec, L10_ec]

    for i in range(19,34):
        table_cells_wc=table_rows[i].select("td")
        team_wc=table_cells_wc[0]

        if len(team_wc.text.strip().split(" "))==2:
            team_wc=team_wc.text.strip().split(" ")[0]+"-"+team_wc.text.strip().split(" ")[1]
        else:
            team_wc=team_wc.text.strip()

        r=str(table_cells_wc[1].text.strip())+"-"+str(table_cells_wc[2].text.strip())

        WP_wc=table_cells_wc[3].text.strip()
        GB_wc=table_cells_wc[4].text.strip()
        HOME_wc=table_cells_wc[5].text.strip()
        ROAD_wc=table_cells_wc[6].text.strip()
        DIV_wc=table_cells_wc[7].text.strip()
        CONF_wc=table_cells_wc[8].text.strip()
        PF_wc=table_cells_wc[9].text.strip()
        PA_wc=table_cells_wc[10].text.strip()
        STRK_wc=table_cells_wc[12].text.strip()
        L10_wc=table_cells_wc[13].text.strip()


        WC.append(team_wc)
        record_wc.append(r)

        wc_stats[team_wc]=[WP_wc, GB_wc, HOME_wc, ROAD_wc, DIV_wc, CONF_wc, PF_wc, PA_wc, STRK_wc, L10_wc]

def printClassification():
    getTeams()
    print("Eastern Conference")
    print(" |# |TEAM        |REC    |WP   |GB   |HOME |ROAD |DIV   |CONF  |PF   |PA   |STRK    |L10    |")

    for i in range(0,15):
        print(" |"+ str(i+1)+ " "*(2-len(str(i+1)))+"|"+EC[i]+" "*(12-len(EC[i]))+"| "+record_ec[i]+" "*(6-len(record_ec[i]))+"|"\
        +ec_stats[EC[i]][0]+" | "+ec_stats[EC[i]][1]+" "*(4-len(ec_stats[EC[i]][1]))+"|"+ec_stats[EC[i]][2]+" "*(5-len(ec_stats[EC[i]][2]))+"|"\
        +ec_stats[EC[i]][3]+" "*(5-len(ec_stats[EC[i]][3]))+"|"+ec_stats[EC[i]][4]+" "*(6-len(ec_stats[EC[i]][4]))+"|"+ec_stats[EC[i]][5]+" "\
        *(6-len(ec_stats[EC[i]][5]))+"|"+ec_stats[EC[i]][6]+" "*(5-len(ec_stats[EC[i]][6]))+"|"+ec_stats[EC[i]][7]+" "*(5-len(ec_stats[EC[i]][7]))+"| "+\
        ec_stats[EC[i]][8]+" "*(7-len(ec_stats[EC[i]][8]))+"| "+ec_stats[EC[i]][9]+" "*(6-len(ec_stats[EC[i]][9]))+"|")

    print("\nWestern Conference")
    print(" |# |TEAM         |REC    |WP   |GB   |HOME |ROAD |DIV   |CONF  |PF   |PA   |STRK    |L10    |")

    for i in range(0,15):
        print(" |"+ str(i+1)+ " "*(2-len(str(i+1)))+"|"+WC[i]+" "*(13-len(WC[i]))+"| "+record_wc[i]+" "*(6-len(record_wc[i]))+"|"\
        +wc_stats[WC[i]][0]+" | "+wc_stats[WC[i]][1]+" "*(4-len(wc_stats[WC[i]][1]))+"|"+wc_stats[WC[i]][2]+" "*(5-len(wc_stats[WC[i]][2]))+"|"\
        +wc_stats[WC[i]][3]+" "*(5-len(wc_stats[WC[i]][3]))+"|"+wc_stats[WC[i]][4]+" "*(6-len(wc_stats[WC[i]][4]))+"|"+wc_stats[WC[i]][5]+" "\
        *(6-len(wc_stats[WC[i]][5]))+"|"+wc_stats[WC[i]][6]+" "*(5-len(wc_stats[WC[i]][6]))+"|"+wc_stats[WC[i]][7]+" "*(5-len(wc_stats[WC[i]][7]))+"| "\
        +wc_stats[WC[i]][8]+" "*(7-len(wc_stats[WC[i]][8]))+"| "+wc_stats[WC[i]][9]+" "*(6-len(wc_stats[WC[i]][9]))+"|")

roster={}
roster_stats={}
teams=[]
def getRoster(team):
    url_roster="http://basketball.realgm.com/nba/depth-charts"
    r_roster=requests.get(url_roster)
    soup_roster=BeautifulSoup(r_roster.text, "lxml")

    counter=0
    divs=soup_roster.findAll("div", {"class":"large-column-left"})
    for div in divs:

        team_a=soup_roster.findAll("h2", {"class":"clearfix"})[counter]
        team_b=team_a.text.strip().split(" ")[1]+" "+team_a.text.strip().split(" ")[2]  #Cleveland Cavaliers
        teams.append(team_b)
        tr_starters=div.findAll("tr", {"class":"depth_starters"})
        td_starters=tr_starters[0].findAll("td")



        PG=td_starters[1].findAll("a")[0].text.strip()
        SG=td_starters[2].findAll("a")[0].text.strip()
        SF=td_starters[3].findAll("a")[0].text.strip()
        PF=td_starters[4].findAll("a")[0].text.strip()
        C=td_starters[5].findAll("a")[0].text.strip()

        starters=[PG,SG,SF, PF,C]

        stats=[]
        for i in range(1,6):
            r=td_starters[i].text.strip()
            stat=r.split("\n")[1]
            stats.append(stat)



        tr_bench=div.findAll("tr", {"class":"depth_rotation"})
        bench_pt=[]
        stats_bench=[]
        for tr in tr_bench:
            td_bench=tr.findAll("td")
            for r in td_bench:
                if r.text.strip()=="Rotation" or r.text.strip()=="":
                    pass
                else:
                    bench_pt.append(r.text.strip().split("\n")[0])
                    stats_bench.append(r.text.strip().split("\n")[1])

        roster[team_b]=starters+bench_pt
        roster_stats[team_b]=stats+stats_bench

        counter=counter+1

        if team.lower()==team_b.split(" ")[0].lower() or team.lower()==team_b.split(" ")[1].lower():    #lower or single words
            return(roster[team_b], roster_stats[team_b])
            break
        elif team=="all":
            pass
    if team not in teams:
        return(False)
    else:
        pass

def printRoster(team):
    if getRoster(team)==False:
        print("Team not found")
    else:
        rosterr=getRoster(team)
        s=" |POSITION|NAME          |SEASON STATS  |"
        print(" |POSITION|NAME          |SEASON STATS  |")
        print(" |PG      |"+rosterr[0][0]+" "*(14-len(rosterr[0][0]))+"|"+rosterr[1][0]+" "*(14-len(rosterr[1][0]))+"|")
        print(" |SG      |"+rosterr[0][1]+" "*(14-len(rosterr[0][1]))+"|"+rosterr[1][1]+" "*(14-len(rosterr[1][1]))+"|")
        print(" |SF      |"+rosterr[0][2]+" "*(14-len(rosterr[0][2]))+"|"+rosterr[1][2]+" "*(14-len(rosterr[1][2]))+"|")
        print(" |PF      |"+rosterr[0][3]+" "*(14-len(rosterr[0][3]))+"|"+rosterr[1][3]+" "*(14-len(rosterr[1][3]))+"|")
        print(" |C       |"+rosterr[0][4]+" "*(14-len(rosterr[0][4]))+"|"+rosterr[1][4]+" "*(14-len(rosterr[1][4]))+"|")
        print(" "+"-"*(len(s)-1))
        for i in range(5,len(rosterr[0])):
            print(" |BENCH   |"+rosterr[0][i]+" "*(14-len(rosterr[0][i]))+"|"+rosterr[1][i]+" "*(14-len(rosterr[1][i]))+"|")

leaders={}
def getLeaders(team):
    url_roster="http://basketball.realgm.com/nba/depth-charts"
    r_roster=requests.get(url_roster)
    soup_roster=BeautifulSoup(r_roster.text, "lxml")

    div2=soup_roster.findAll("div", {"class":"small-column-right"})
    count=0
    for divs in div2:
        team_c=teams[count]#divs.findAll("h3")[0].text.strip().split(" ")[1]
        tr=divs.findAll("table")[0].findAll("tbody")[0].findAll("tr")
        r=[]
        count=count+1
        for t in tr:
            heading=t.findAll("th")[0].text.strip()
            player=t.findAll("td")[0].text.strip()
            how_much=t.findAll("td")[1].text.strip()
            result=[heading,player,how_much]
            r.append(result)
        leaders[team_c]=r
        if team.lower()==team_c.split(" ")[0].lower():    #lower or single words#only picks up hawks or cavaliers
            return(leaders[team_c])
            break
    if getRoster(team)==False:
        return False
    else:
        pass

def printLeaders(team):
    if getLeaders(team)==False:
        return ("")
    else:
        leaders=getLeaders(team)
        print("\nSEASON LEADERS:")
        for i in range(0,len(leaders)):
            print(leaders[i][0]+":  "+leaders[i][1]+" --> "+leaders[i][2])


def printSchedule(date):
    url_schedules="http://www.si.com/nba/scoreboard?date="+date
    r_schedules=requests.get(url_schedules)
    soup_schedules=BeautifulSoup(r_schedules.text,"lxml")


    divs=soup_schedules.findAll("div", {"class":"pre-game"})

    for div in divs:
        time=div.findAll("div", {"class":["float-left", "status-container"]})[0].text.strip()



        team1p=div.findAll("div", {"class":["media", "vertically-center", "team"]})[0].text.strip()
        team2p=div.findAll("div",{"class":["media" ,"verrically-center", "team"]})[1].text.strip()
        team1location=team1p.split("\n")[0]
        team2location=team2p.split("\n")[0]

        for t in team1p.split("\n"):
            if len(t)>0:
                team1name=t
        for t in team2p.split("\n"):
            if len(t)>0:
                team2name=t
        team1=team1location+" "+team1name
        team2=team2location+" "+team2name
        print(time+": "+team1+" - "+team2)

def printScores(date):

    url_scores="http://www.cbssports.com/nba/scoreboard/"+date
    r_scores=requests.get(url_scores)
    soup_scores=BeautifulSoup(r_scores.text, "lxml")
    countter=0
    divs=soup_scores.findAll("div",{"class":["in-progress-table"]})
    for div in divs:
        team1=div.findAll("td",{"class":"team"})[0].findAll("a")[0].text.strip()
        team2=div.findAll("td",{"class":"team"})[1].findAll("a")[0].text.strip()



        score1=div.findAll("td")[len(div.findAll("td"))/2-1].text.strip()
        score2=div.findAll("td")[len(div.findAll("td"))-1].text.strip()

        player1=soup_scores.findAll("div",{"class":"team-player-stats"})[countter].findAll("td")[1].text.strip()
        player2=soup_scores.findAll("div",{"class":"team-player-stats"})[countter].findAll("td")[3].text.strip()
        print(team1.upper()+" "+score1+" - "+score2+" "+team2.upper())
        print(player1.split("\n")[0]+" ("+player1.split("\n")[1]+") "+player1.split("\n")[2])
        print(player2.split("\n")[0]+" ("+player2.split("\n")[1]+") "+player2.split("\n")[2]+"\n")
        countter=countter+1

def searchPlayers(player):
    getRoster("all")
    print("|PLAYER          |TEAM                 |SEASON STATS    |")
    c=0
    for x,m in roster.items():

        counter=0
        for i in m:
            for r in i.split(" "):
                if player.lower()==r.lower() or player.lower()==i.lower():
                    print("| "+i+" "*(15-len(i))+"| "+x+" "*(20-len(x))+"| "+roster_stats[x][counter]+" "*(15-len(roster_stats[x][counter]))+"|")
                    c=c+1
                    break
                else:
                    pass
            counter=counter+1
    if c==0:
        print("|"+"x"*16+"|"+"x"*21+"|"+"x"*16+"|")
    else:
        pass


################################################3

if len(sys.argv)<2:
    os.system("figlet NBA")
    print(" "*6+"DATABASE"+" "*6)
    print("\n\n [*] Created by JAIME ENRIQUEZ")
    print(" [*] Insert parameter --> python ... .py -h")

elif len(sys.argv)>=2:
    if sys.argv[1]=="-c" or sys.argv[1]=="--classification":
        printClassification()
    elif sys.argv[1]=="-r" or sys.argv[1]=="--roster":
        if len(sys.argv)!=3:
            print("Insert team")
        else:
            printRoster(sys.argv[2])

            printLeaders(sys.argv[2])
    elif sys.argv[1]=="-s" or sys.argv[1]=="--search":
        if len(sys.argv)==3:
            player=sys.argv[2]
            searchPlayers(player)
        elif len(sys.argv)==4:
            player=sys.argv[2]+" "+sys.argv[3]
            searchPlayers(player)
        else:
            print("Insert name/surname")
    elif sys.argv[1]=="-ls" or sys.argv[1]=="--livescore":
        if len(sys.argv)==2:
            day=int(time.strftime("%d"))-1
            date=time.strftime("%Y"+"%m")+str(day)
            printScores(date)
        else:
            date=sys.argv[2].split("-")[0]+sys.argv[2].split("-")[1]+sys.argv[2].split("-")[2]
            printScores(date)
    elif sys.argv[1]=="-sc" or sys.argv[1]=="--schedule":
        if len(sys.argv)<3:
            print("Insert date in YEAR-MONTH-DAY format")
        elif sys.argv[2]=="today":
            today=time.strftime("%Y-%m-%d")
            printSchedule(today)
        else:
            today=sys.argv[2]
            printSchedule(today)
    elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
        print ("                   HELP MENU\n")
        print ("  ------------------------------------------------------------")
        print (" |COMMAND            |                 USE                    |")
        print ("  ------------------------------------------------------------")
        print (" |-c/--classification| prints current classification          |")
        print (" |-r/--roster        | prints roster from entered team        |")
        print (" |-s/-search         | searches for player in nba database    |")
        print (" |-ls/--livescore    | prints stored scores from lastest games|")
        print (" |-sc/--schedule     | searches for given date games          |")
        print (" |-h/--help          | shows this menu                        |")
        print ("  ------------------------------------------------------------")
    else:
        print("Command not recognised")
