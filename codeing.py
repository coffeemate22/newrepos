def save_image(image_url: str, image_title: str) -> None:
    """
    Saves the image of anime character
    """
    image = requests.get(image_url, headers=headers)
    with open(image_title, "wb") as file:
        file.write(image.content)
if __name__ == "__main__":
    title, desc, image_title = random_anime_character()
    print(f"{title}\n\n{desc}\n\nImage saved : {image_title}")

 data = response.json()#good
    if not wanted_data:
        return {id_: data["data"]["children"][id_] for id_ in range(limit)}

    data_dict = {}
    for id_ in range(limit):
        data_dict[id_] = {
            item: data["data"]["children"][id_]["data"][item] for item in wanted_data
        }
    return data_dict#nice
  while True:
        isbn = input("\nEnter the ISBN code to search (or 'quit' to stop): ").strip()
        if isbn.lower() in ("", "q", "quit", "exit", "stop"):
            break

        if len(isbn) not in (10, 13) or not isbn.isdigit():
            print(f"Sorry, {isbn} is not a valid ISBN.  Please, input a valid ISBN.")
            continue
