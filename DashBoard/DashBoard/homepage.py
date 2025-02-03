from django.http import HttpResponse
from .APP.terminal import Terminal

def homepage(request):
    terminal_app = Terminal()
    return HttpResponse(f"""
    <html>
      <head>
        <title>My Dashboard</title>
        <style>
          body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(blue, white);
            font-family: Arial, sans-serif;
          }}
          .taskbar {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #808080;
            height: 40px;
            display: flex;
            align-items: center;
            color: #fff;
          }}
          .start-button {{
            background-color: #444;
            color: #fff;
            border: 1px solid #333;
            border-radius: 4px;
            padding: 5px 10px;
            margin: 5px;
            cursor: pointer;
            box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
          }}
          .start-button:hover {{
            background-color: #555;
          }}
          .app {{
            text-align: center;
            margin-top: 50px;
          }}
          .app img {{
            width: 100px;
            height: 100px;
          }}
        </style>
      </head>
      <body>
        <div class="app">
          <h2>{terminal_app.name}</h2>
          <img src="{terminal_app.icon}" alt="{terminal_app.name} icon">
        </div>
        <div class="taskbar">
          <button class="start-button">Start</button>
        </div>
      </body>
    </html>
    """)
