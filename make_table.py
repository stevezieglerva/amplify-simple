front = """
<head>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <h1>Hello</h1>


    <div id="users">
        <input class="search" placeholder="Search" />
        <button class="sort" data-sort="name">
            Sort by name
        </button>
        <table>
            <!-- IMPORTANT, class="list" have to be at tbody -->
            <tbody class="list">
"""

end = """

            </tbody>
        </table>

    </div>
    <script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

    <script>
        var options = {
            valueNames: ['name', 'born']
        };

        var userList = new List('users', options);

    </script>

</body>
"""

html = front
for i in range(2000):
    name = "x".ljust(i, "x")
    if i % 100 == 0:
        name = "John " + name
    if i % 33 == 0:
        name = "Jane " + name
    row = f"""               
                    <tr>
                        <td class="name">{i} {name}</td>
                        <td class="born">1983</td>
                    </tr>
    """
    html = html + row

html = html + end
length = len(html)
print(f"html length: {length}")
with open("index.html", "w") as file:
    file.write(html)
