import wget

start_year = 1977
end_year = 2019
ltr_year = 1998

link = "http://berkshirehathaway.com/letters/"

for i in range(start_year, end_year):
    print(i)
    
    letter_link = 0

    if i <ltr_year:
        letter_link = (link+str(i)+".html")
    else:
        letter_link = (link+str(i)+"htm.html")
    print("Printing {}".format(letter_link))
    ilename = wget.download(letter_link)

####this will print the links of the annual letters, now use a file downloader like wget to download the files
#### save this to a file.txt and run `wget -i file.txt` and you are done