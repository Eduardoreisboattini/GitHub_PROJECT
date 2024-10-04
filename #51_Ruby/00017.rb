require 'json'

json_data = '{"name":"John","age":25}'
parsed_data = JSON.parse(json_data)
puts parsed_data["name"]   # Output: John
