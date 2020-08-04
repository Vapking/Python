
def main():
    weather_dict = {}
    with open('nyc_weather.csv','r') as f:
        for line in f:
            tokens = line.split(",")
            try:
                if tokens[1] == "temperature(F)\n":
                    weather_dict[tokens[0]] = tokens[1]    
                else:
                    weather_dict[tokens[0]] = int(tokens[1])
            except Exception as e:
                print(e)
    print(weather_dict['Jan 9'])
    print(weather_dict['Jan 4'])

if __name__ == "__main__":
    main()