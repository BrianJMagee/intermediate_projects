from weather_gui import WeatherApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp("20001e9c835eedce6a71a11b197ab92b")
    weather_app.show()
