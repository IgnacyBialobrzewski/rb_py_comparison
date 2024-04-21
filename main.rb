require('net/http')

JOKE_LIMIT = 10

def fetch_joke
  endpoint = 'https://icanhazdadjoke.com'
  headers = { 'Accept' => 'text/plain' }

  Net::HTTP.get(URI(endpoint), headers)
end

puts 'How many jokes would you like to fetch? (Max 10)'
amount = Integer(gets.chomp)

if amount > 10
  puts 'Limit reached, defaulting to 10'
  amount = 10
end

(1..amount).each do |_|
  puts(fetch_joke)
end