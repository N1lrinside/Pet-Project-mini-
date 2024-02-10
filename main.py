from fastapi import FastAPI
from starlette.responses import HTMLResponse
import random
import functools
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def read_root():
    list_id_games = [10, 570, 620, 730,242760]
    r=random.choice(list_id_games)
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Рандом игра из вашей библиотеки Steam</title>
<style>
    body, html {{
        height: 100%;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }}
    .button-container {{
        display: flex;
        gap: 20px;
    }}
    .centered-button {{
        margin-top: 100px;
        padding: 10px 20px;
        background-color: #8b00ff;
        color: white;
        border: none;
        border-radius: 100px;
        font-size: 30px;
        cursor: pointer;
    }}
    .refresh-button {{
        margin-top: 100px;
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 100px;
        font-size: 20px;
        cursor: pointer;
    }}
</style>
</head>
<body>
<div class="empty-space"></div>
<img class="game_header_image_full" src="https://cdn.akamai.steamstatic.com/steam/apps/{r}/header.jpg?t=1706131787">
<div id="appHubAppName_responsive" style="display: none;" class="apphub_AppName">Grand Theft Auto V</div>
<div data-panel="{{&quot;type&quot;:&quot;PanelGroup&quot;}}" id="appHeaderGridContainer" class="app_header_grid_container" style="display:none">
<a id="game-link" href="https://store.steampowered.com/app/{r}">Ссылка на игру</a>
</div>
<div class="button-container">
    <button id="play-button" class="centered-button">Нажми</button>
    <button id="refresh-button" class="refresh-button">Обновить</button>
</div>

<script>
    // Получаем ссылку на кнопку "Нажми" и кнопку "Обновить"
    var playButton = document.getElementById('play-button');
    var refreshButton = document.getElementById('refresh-button');

    // Добавляем обработчик события клика на кнопку "Нажми"
    playButton.addEventListener('click', function() {{
        // Переходим по ссылке на игру
        window.location.href = gameLink.href;
    }});

    // Добавляем обработчик события клика на кнопку "Обновить"
    refreshButton.addEventListener('click', function() {{
        // Обновляем страницу
        location.reload();
    }});
</script>

</body>
</html>'''

    return HTMLResponse(content=html_content, status_code=200)

