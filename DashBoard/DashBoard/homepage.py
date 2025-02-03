from django.http import HttpResponse

def homepage(request):
    return HttpResponse("""
    <html>
      <head>
        <title>My Dashboard</title>
        <style>
          body {
            margin: 0;
            padding: 0;
            background-color: blue;
            font-family: Arial, sans-serif;
          }
          .header {
            background-color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
          }
          .search-bar {
            padding: 5px;
          }
        </style>
      </head>
      <body>
        <div class="header">
          <h1>Welcome to the Dashboard</h1>
          <form>
            <input class="search-bar" type="search" placeholder="Search..." />
          </form>
        </div>
        <p>Here is a simple placeholder for stats or charts.</p>
      </body>
    </html>
    """)
