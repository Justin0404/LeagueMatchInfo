import requests
def main():
    #taking input of the username
    sumName = input("Enter in a username of a player that is in a game\n")
    r = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+sumName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json() #gets Summoner ID
    x = requests.get("https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/"+str(r["id"])+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()#takes info on game
    sumOfRanks = 0

    team = 0
    counter = 0
    indexSumm = 0
    counterAvg = 0
    for counter in range(10):
        if x["participants"][counter]["summonerId"] == r["id"]:
            indexSumm=counter
            if x["participants"][counter]["teamId"] == 100:
                team = 1
            else:
                team = 2
    teammateID = []
    if team ==1:
        for counter2 in range(0,5):
            if x["participants"][counter2]["summonerId"]!=r["id"]:
                teammateName = x["participants"][counter2]["summonerName"]
                teammateID.append(requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+teammateName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json())
                curRank = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+teammateName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()["summonerLevel"]
                sumOfRanks+=curRank
                champ = x["participants"][counter2]["championId"]
                champSpecific = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/"+str(x["participants"][counter2]["summonerId"])+"/by-champion/"+str(x["participants"][counter2]["championId"])+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()
                print("teammate " + str(counter2+1) + " is: " + teammateName + " and is level " + str(curRank) + " \n Level of what champ they are playing based on previous games: " +str(champSpecific["championLevel"]))
        print("\n\n\n")
        for counter3 in range(5, 10):
            enemyName = x["participants"][counter3]["summonerName"]
            enemyAvg=requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+enemyName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()["summonerLevel"]
            counterAvg+=enemyAvg
            champ = x["participants"][counter3]["championId"]
            champSpecific = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/"+str(x["participants"][counter3]["summonerId"])+"/by-champion/"+str(x["participants"][counter3]["championId"])+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()
            print("Enemy number " +str(counter3) + " is "+enemyName + " and is level " +str(enemyAvg) + " \n Level of what champ they are playing based on previous games: " + str(champSpecific["championLevel"]))

            
    else:
        for counter3 in range(0,5):
            if x["participants"][counter3+5]["summonerId"]!=r["id"]:
                teammateName = x["participants"][counter3+5]["summonerName"]
                teammateID.append(requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+teammateName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json())
                curRank=requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+teammateName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()["summonerLevel"]
                sumOfRanks += curRank
                champ = x["participants"][counter3]["championId"]
                champSpecific = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/"+str(x["participants"][counter3]["summonerId"])+"/by-champion/"+str(x["participants"][counter3]["championId"])+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()
                print("teammate " + str(counter3+1) + " is: " + teammateName + " and is level " + str(curRank) + " \n Level of what champ they are playing based on previous games: " +str(champSpecific["championLevel"]))


            else:
                print("teammate " + str(counter3+1) + " is you!")
        print("\n\n\n")
        for counter3 in range(0, 5):
            enemyName=x["participants"][counter3]["summonerName"]
            enemyAvg=requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+enemyName+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()["summonerLevel"]
            counterAvg+=enemyAvg
            champ = x["participants"][counter3]["championId"]
            champSpecific = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/"+str(x["participants"][counter3]["summonerId"])+"/by-champion/"+str(x["participants"][counter3]["championId"])+"?api_key=RGAPI-66b7df8b-baec-4459-8783-868ba124668e").json()
            print("Enemy number " +str(counter3) + " is "+enemyName + " and is level " +str(enemyAvg) + " \n Level of what champ they are playing based on previous games: " + str(champSpecific["championLevel"]))
    sumOfRanks = sumOfRanks/4
    counterAvg=counterAvg/5 
    print("Your team's level avg: " + str(sumOfRanks))
    print("Their team's avg: " + str(counterAvg))
    if(counterAvg>sumOfRanks):
        print("It looks like your opponents are higher level than you, but no worries, you can still win!")
    else:
        print("It looks like your team is higher level than their team, but don't get too cocky, you can still lose")

                
if __name__ == "__main__":
    main()
 
