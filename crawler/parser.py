def namechart_parser(response=None):
    import re
    from selenium.webdriver.common.by import By

    data = []

    table = response.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[3]/div[2]/table')
    tbody = table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    
    for index, row in enumerate(rows):
        row_rank = row.find_elements(By.TAG_NAME, "td")[0]
        row_name = row.find_elements(By.TAG_NAME, "td")[1]
        row_total = row.find_elements(By.TAG_NAME, "td")[2] 

        name = row_name.text.strip()
        ranks = row_rank.text.splitlines()
        rank = re.sub(r'[^0-9]', '', ranks[0])
        prevrank = ranks[1].replace('―', '0')
        total = row_total.text.replace(',', '').replace('명', '').strip()
    
        result = {
            "NO": index+1
            , "NAME": name
            , "RANK": int(rank)
            , "PREVRANK": int(prevrank)
            , "TOTAL": int(total)
        }
 
        data.append(result)
 
    return data
