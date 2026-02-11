import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter The City Name: " , self)
        self.input = QLineEdit(self)
        self.getWeather = QPushButton("Get Weather" , self)
        self.tempLabel = QLabel(self)
        self.emoji = QLabel(self)
        self.descriptionLabel = QLabel(self)
        self.initUI()

    
    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()


        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.input)
        vbox.addWidget(self.getWeather)
        vbox.addWidget(self.tempLabel)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.descriptionLabel)

        self.setLayout(vbox)

        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.input.setAlignment(Qt.AlignCenter)
        self.tempLabel.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        self.cityLabel.setObjectName("cityLabel")
        self.input.setObjectName("input")
        self.getWeather.setObjectName("getWeather")
        self.tempLabel.setObjectName("tempLabel")
        self.emoji.setObjectName("emoji")
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Roboto;
        }
        QLabel#cityLabel{
            font-size: 40px;
        }
        QLineEdit#input{
            font-size: 40px;
        }
        QPushButton#getWeather{
            font-size: 40px;
            font-weight: bold;
        }
        QLabel#tempLabel{
            font-size: 70px;
        }
        QLabel#emoji{
            font-size: 70px;
            font-family: Segoe UI emoji;
        }
        QLabel#descriptionLabel{
            font-size: 70px;
        }                                    
        """)


        self.getWeather.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "862824379e91c25bee4d1a58dfdf4ea0"
        city = self.input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_Error("Bad Request \nplease check your input")
                case 401:
                    self.display_Error("Unathorized \nInvalid API key")
                case 403:
                    self.display_Error("Forbidden \nAccess is denied")
                case 404:
                    self.display_Error("Not Found \nCity not found")                       
                case 500:
                    self.display_Error("Interntal server error \nplease try again later")
                case 502:
                    self.display_Error("Bad Gateway \nInvalid response for the server")
                case 503:
                    self.display_Error("Service Unavailble \nServer is down")
                case 504:
                    self.display_Error("Gateway Timeout \nNo respone from the server")
                case _:
                    self.display_Error(f"HTTP error occured\n{http_error}")


        except requests.exceptions.ConnectionError:
            self.display_Error("Connection Error: \nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_Error("Timout Error: \nRequests time out")
        except requests.exceptions.TooManyRedirects:
            self.display_Error("Too many Redirects: \nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_Error(f"Request Error: \n{req_error}")


    
    def display_Error(self,message):
        self.tempLabel.setStyleSheet("font-size: 30px;")
        self.tempLabel.setText(message)
        self.emoji.clear()
        self.descriptionLabel.clear()


    def display_weather(self,data):
        self.tempLabel.setStyleSheet("font-size: 70px;")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15

        weather_id = data["weather"][0]["id"]
        weatherDescription = data["weather"][0]["description"]
        self.descriptionLabel.setText(weatherDescription)
        self.emoji.setText(self.get_weather_emoji(weather_id))
        self.tempLabel.setText(f"{round(temp_c,2)}°C")


    @staticmethod
    def get_weather_emoji(weather_id):
        if  200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "🌥️"
        else:
            return ""

def main():
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
