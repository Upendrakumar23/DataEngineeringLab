import requests
from bs4 import BeautifulSoup


def print_unicode_grid(doc_url: str):
    """
    Fetches a published Google Doc containing Unicode characters with x,y coordinates,
    parses the data, and prints the grid of characters.
    """
    # Step 1: Retrieve document HTML
    response = requests.get(doc_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch document: {response.status_code}")
    html = response.text

    # Step 2: Parse the HTML table (columns: x-coordinate, Character, y-coordinate)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if table is None:
        print("No table found in document.")
        return

    # Step 3: Extract grid data from table rows (skip header row)
    grid_data = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"])
        if len(cells) != 3:
            continue
        cell_texts = [cell.get_text(strip=True) for cell in cells]
        try:
            x = int(cell_texts[0])
            char = cell_texts[1]
            y = int(cell_texts[2])
            grid_data.append((char, x, y))
        except ValueError:
            continue

    if not grid_data:
        print("No valid grid data found.")
        return

    # Step 4: Determine grid size
    max_x = max(x for _, x, _ in grid_data)
    max_y = max(y for _, _, y in grid_data)

    # Step 5: Initialize grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 6: Place characters
    for char, x, y in grid_data:
        grid[y][x] = char

    # Step 7: Print grid row by row
    for row in grid:
        print("".join(row))


# Example usage:
doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_unicode_grid(doc_url)
