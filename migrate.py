from db import get_client

def main():
    client = get_client()
    result = client.query('select location, time, temperature from weather;')
    print len(result[0]['points'])
    for item in result[0]['points']:
        print item
        break
    #    json_body = [{
    #        "points": [
    #            [item[2], item[0], item[3]],
    #            ],
    #        "name": "weather",
    #        "columns": ["location", "time", "temperature"]
    #        }]
    #    client.write_points(json_body)
    
if __name__ == "__main__":
    from utensils.options import define, options, parse_command_line
    from utensils.loggingutils import basicConfig
    main()
