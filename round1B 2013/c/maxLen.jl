fDict = open("garbled_email_dictionary.txt", "r")
# dict = [Set{ASCIIString}() for i in 1:60]
maxLen = 0
for line in eachline(fDict)
    s = strip(line)
    maxLen = max(length(s), maxLen)
end
println("maxLen $(maxLen)")
