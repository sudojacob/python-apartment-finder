import requests
from bs4 import BeautifulSoup


for i in range(8, 755):
    url = "http://annarborobserver.rentlinx.com/listings/525_S_State_St,_Ann_Arbor,_MI_48109/within:2.0/start:"
    url += str(i)

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")

    row = soup.find('tr', {"class": "RL_DataRow"})
    col = row.find_all("td")

    col.pop(0)
    col.pop(0)
    col.pop(0)
    col.pop(3)
    col.pop(1)

    try:
        num = col[0].text.strip()
        num = int(num[-1])
        rent = col[1].text.strip()
        if "-" in rent:
            rentL = rent.split('-')
            rent = rentL[1].strip()
        rent = rent[1:]
        rent = int(rent.replace(',', ''))
        cost = round(rent / num)
        if cost < 600:
            print("Id:",str(i),"   Rent (probably wrong):","$" + str(cost),url)
            print()
        elif cost < 800:
            print("Id:", str(i), "   Rent:","$" +  str(cost), "**",url)
            print()
        elif cost < 915:
            print("Id:", str(i), "   Rent:","$" +  str(cost),url)
            print()

    except:
        print("Id:",str(i),"   failed")
        print()
