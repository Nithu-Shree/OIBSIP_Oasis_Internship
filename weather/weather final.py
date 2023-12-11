import requests
from rich.progress import Progress
from rich.console import Console
from datetime import datetime, timezone
from rich.table import Table
from rich.box import ROUNDED

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    console = Console()

    if response.status_code == 200:
        console.print(f"Weather in [bold green]📍 {location}:[/bold green]\n")  # Add line break

        with Progress() as progress:
            task = progress.add_task("[green]Processing data... [/green]", total=100)

            for _ in range(100):
                progress.update(task, advance=1)

        console.rule("[bold red]Weather Details[/bold red]", style="red")

        table = Table(show_header=True, header_style="bold", box=ROUNDED, width=40)
        table.add_column("Attribute", style="green", width=20)
        table.add_column("Value", style="blue", width=20)

        details = [
            ("😅 Feels like", f"{weather_data['main']['feels_like']} °C"),
            ("☁️ Description", weather_data['weather'][0]['description']),
            ("❄️ As low as", f"{weather_data['main']['temp_min']} °C"),
            ("🔥 As high as", f"{weather_data['main']['temp_max']} °C"),
            ("📊 Pressure", f"{weather_data['main']['pressure']} Pa"),
            ("💧 Humidity", f"{weather_data['main']['humidity']} %"),
            ("💨 Wind Speed", f"{weather_data['wind']['speed']} km/h"),
            ("🌐 Country", weather_data['sys']['country']),
            ("🌅 Sunrise", str(datetime.fromtimestamp(weather_data['sys']['sunrise'], tz=timezone.utc))),
            ("🌇 Sunset", str(datetime.fromtimestamp(weather_data['sys']['sunset'], tz=timezone.utc)))
        ]

        for attribute, value in details:
            table.add_row(attribute, value)

        console.print(table)

    else:
        console.print(f"[bold red]Failed to retrieve weather data.[/bold red] Status code: {response.status_code}")

def process_data():
    # Simulate data processing
    pass

if __name__ == "__main__":
    api_key = "910ebeab9fd5cf79f94c15aeabcd0d39"
    location = input("Enter city name or pin code: ")
    get_weather(api_key, location)