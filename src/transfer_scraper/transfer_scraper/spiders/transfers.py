import scrapy


def extract_clubname(box):
    return box.xpath("a/text()").get()


def extract_tables(box):
    return box.xpath("following-sibling::div[@class='responsive-table']//table")


def parse_amount(value):
    if value == "-" or "free transfer" in value or "?" in value:
        return 0
    else:
        if "m" in value:
            return int(float(value.replace("€", "").replace("m", "").replace(",", ".")) * 1000000)

        elif "k" in value:
            return int(float(value.replace("€", "").replace("k", "").replace(",", "."))) * 1000
        else:
            if "End of loan" in value or value == "loan transfer":
                return 0
            if "Loan fee" in value:
                if "m" in value:
                    return int(
                        float(
                            value.replace("Loan fee:", "")
                            .replace("€", "")
                            .replace("m", "")
                            .replace(",", ".")
                            .strip()
                        )
                        * 1000000
                    )
                elif "k" in value:
                    return int(
                        float(
                            value.replace("Loan fee:", "")
                            .replace("€", "")
                            .replace("k", "")
                            .replace(",", ".")
                            .strip()
                        )
                        * 1000
                    )
            else:
                return None


def parse_table(clubname, table, i):
    rows = table.xpath("tbody/tr")
    rows_list = []
    for row in rows:
        # First column is the player name
        player = row.xpath("td/div[@class='di nowrap']/span/a/text()").get()
        # Second column is the player age
        age = row.xpath("td[@class='zentriert alter-transfer-cell']/text()").get()
        # Third column is the player nationality
        nation = row.xpath("td[@class='zentriert nat-transfer-cell']/img/@title").get()
        # Fourth column is the player position
        position = row.xpath("td[@class='kurzpos-transfer-cell zentriert']/text()").get()
        # Fifth column is the player market value
        market_value = row.xpath("td[@class='rechts mw-transfer-cell']/text()").get()
        market_value = parse_amount(market_value)
        # Sixth column is the club
        club = row.xpath("td[@class='no-border-links verein-flagge-transfer-cell']/a/@title").get()
        # Seventh column is the actual transfer fee
        transfer_fee = row.xpath("td[contains(@class, 'rechts')]/a/text()").get()
        if "loan" in transfer_fee.lower():
            loan = True
            if "End of loan" in transfer_fee:
                transfer_type = "loan_end"
                transfer_fee = 0
            elif "Loan fee" in transfer_fee:
                transfer_type = "loan_fee"
                transfer_fee = row.xpath(
                    "td[@class='rechts ']/a/i[@class='normaler-text']/text()"
                ).get()
                transfer_fee = parse_amount(transfer_fee)
            else:
                transfer_type = "loan"
                transfer_fee = 0
        else:
            loan = False
            transfer_type = "transfer"
            transfer_fee = parse_amount(transfer_fee)

        # Create a dictionary with the data
        data = {
            "player": player,
            "age": age,
            "nation": nation,
            "position": position,
            "market_value": market_value,
            "from" if i == 0 else "to": club,
            "to" if i == 0 else "from": clubname,
            "loan": loan,
            "transfer_type": transfer_type,
            "transfer_fee": transfer_fee,
        }
        rows_list.append(data)

    return rows_list


class TransfersSpider(scrapy.Spider):
    name = "transfers"
    start_urls = [
        "https://www.transfermarkt.com/bundesliga/transfers/wettbewerb/L1/plus/?saison_id=2023&s_w=&leihe=1&intern=0",
        "https://www.transfermarkt.com/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=2023&s_w=&leihe=1&intern=0",
        "https://www.transfermarkt.com/primera-division/transfers/wettbewerb/ES1/plus/?saison_id=2023&s_w=&leihe=1&intern=0",
        "https://www.transfermarkt.com/serie-a/transfers/wettbewerb/IT1/plus/?saison_id=2023&s_w=&leihe=1&intern=0",
        "https://www.transfermarkt.com/ligue-1/transfers/wettbewerb/FR1/plus/?saison_id=2023&s_w=&leihe=1&intern=0",
    ]

    def parse(self, response):
        for box in response.xpath(
            "//div[@class='box']/h2[@class='content-box-headline content-box-headline--inverted content-box-headline--logo']"
        ):
            # Extract title of the a tag
            clubname = extract_clubname(box)
            # Get all tables in the box
            tables = extract_tables(box)
            # Parse each table
            for i, table in enumerate(tables):
                table = parse_table(clubname, table, i)
                for row in table:
                    yield row