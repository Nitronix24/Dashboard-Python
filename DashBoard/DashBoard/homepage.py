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
            background: linear-gradient(blue, white);
            font-family: Arial, sans-serif;
          }
          .taskbar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #808080;
            height: 40px;
            display: flex;
            align-items: center;
            color: #fff;
          }
          .start-button {
            background-color: #444;
            color: #fff;
            border: 1px solid #333;
            border-radius: 4px;
            padding: 5px 10px;
            margin: 5px;
            cursor: pointer;
            box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
          }
          .start-button:hover {
            background-color: #555;
          }
        </style>
      </head>
      <body>
        <div class="taskbar">
          <button class="start-button">Start</button>
        </div>
      </body>
    </html>
    """)
