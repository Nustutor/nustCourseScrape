from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

def seecsScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://seecs.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'seecsqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                    if (program_name.find('COMPUTER SCIENCE') != -1):
                        for index, row in selected_columns.iterrows():
                            f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '", "BS COMPUTER SCIENCE");')
                            f.write('\n')
                    else:
                        for index, row in selected_columns.iterrows():
                            f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                    row[2] + '", "' + row[1] + '","' + program_name + '");' )
                            f.write('\n')
                            
def smmeScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://smme.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'smmequeries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("wef") != -1:
                endindex = program_name.find("wef")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                    if (program_name.find('MECHANICAL ENGINEERING') != -1):
                        for index, row in selected_columns.iterrows():
                            f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '", "BACHELOR OF MECHANICAL ENGINEERING");')
                            f.write('\n')
                    else:
                        for index, row in selected_columns.iterrows():
                            f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                    row[2] + '", "' + row[1] + '","' + program_name + '");' )
                            f.write('\n')
                            
def s3hScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://s3h.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 's3hqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("wef") != -1:
                endindex = program_name.find("wef")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')
                        
def nbsScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://nbs.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'nbsqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("wef") != -1:
                endindex = program_name.find("wef")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')

def scmeScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://scme.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'scmequeries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("wef") != -1:
                endindex = program_name.find("wef")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("FALL") != -1:
                endindex = program_name.find("FALL")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')
                   
def sceeScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://scee.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'sceequeries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("FALL") != -1:
                endindex = program_name.find("FALL")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("Fall ") != -1:
                endindex = program_name.find("Fall ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')

def igisScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://igis.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'igisqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("- FALL") != -1:
                endindex = program_name.find("- FALL")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("Fall ") != -1:
                endindex = program_name.find("Fall ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')

def snsScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://sns.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'snsqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("- FALL") != -1:
                endindex = program_name.find("- FALL")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("Fall ") != -1:
                endindex = program_name.find("Fall ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')

def asabScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://asab.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'asabqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("- FALL") != -1:
                endindex = program_name.find("- FALL")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("Fall ") != -1:
                endindex = program_name.find("Fall ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')

def sadaScrape():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    url = "https://sada.nust.edu.pk/programs/"
    response = requests.get(url, headers=headers)

    html = response.text

    soup = bs(html, "html.parser")

    allLinks = soup.find_all("a", href=True)

    links = [link['href'] for link in allLinks if '/program/' in link['href']]

    program_names = []

    file_path = 'sadaqueries.txt'
    with open(file_path, 'w', encoding = 'UTF-8') as f:
        for link in links:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
            responseLink = requests.get(link, headers=headers)
            htmlLink = responseLink.text
            soupLink = bs(htmlLink, "html.parser")
            
            program_name = soupLink.find("h1", class_="program-heading").text
            if program_name.find("FOR ") != -1:
                endindex = program_name.find("FOR ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("for ") != -1:
                endindex = program_name.find("for ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("For ") != -1:
                endindex = program_name.find("For ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("- FALL") != -1:
                endindex = program_name.find("- FALL")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            elif program_name.find("Fall ") != -1:
                endindex = program_name.find("Fall ")
                program_name = program_name[:endindex]
                program_names.append(program_name)
            else:
                program_names.append(program_name)
            
            tables = soupLink.find_all("table", class_="table table-bordered table-striped")
            for table in tables:
                rows = table.find_all('tr')
                headers = rows[:2]  
                data_rows = rows[2:]
                
                rows_data = []
                
                for row in data_rows:
                    cells = row.find_all(['td', 'th'])
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    rows_data.append(row_data)
                
                df = pd.DataFrame(rows_data)
                filtered_df = df.loc[~(df[1].str.contains('XX') & df[2].str.contains('Elective'))]
                filtered_df = filtered_df.loc[~(df[1].str.contains('xx') & df[2].str.contains('Elective'))]
                
                if not filtered_df.empty:
                    selected_columns = filtered_df.iloc[:, [1, 2]]  
                    selected_columns = selected_columns[~selected_columns.iloc[:, 0].str.startswith('XX')]
                    selected_columns = selected_columns[selected_columns.iloc[:, 0] != '']
                   
                    for index, row in selected_columns.iterrows():
                        f.write('INSERT IGNORE INTO subjects (suid, name, code, degree) VALUES (UUID_TO_BIN(UUID()), "' + 
                                row[2] + '", "' + row[1] + '","' + program_name + '");' )
                        f.write('\n')
sadaScrape()