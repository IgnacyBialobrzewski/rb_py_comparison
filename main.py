from http import client

JOKE_LIMIT = 10


def fetch_joke(conn: client.HTTPSConnection) -> bytes:
    headers = {"Accept": "text/plain"}

    conn.request(method="GET", url="/", headers=headers)
    response = conn.getresponse()

    return response.read()


def main():
    http_conn = client.HTTPSConnection("icanhazdadjoke.com")

    joke_amount = int(
            input("How many jokes would you like to fetch? (Max 10)\n")
    )

    if joke_amount > JOKE_LIMIT:
        joke_amount = 10
        print("Limit reached, defaulting to 10")

    try:
        for _ in range(joke_amount):
            print(fetch_joke(http_conn).decode("utf-8"))
    except:
        http_conn.close()

    http_conn.close()


if __name__ == "__main__":
    main()
