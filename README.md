# arthurhouhttps_dl
This is a set of scripts to download remote XCLA data from arthurhouhttps.
https://arthurhouhttps.pps.eosdis.nasa.gov/

We split the download into two steps:

- Retrieve URLs
- Retrieving granules


## Retrieving URLs

    python3 get_urls.py --products 1C.GCOMW1.AMSR2 1C.NPP.ATMS 
                        --level 1C 
                        --email user@nasa.gov 
                        --start 2021-01-01 --stop 2021-01-02 
                        --out urls.csv
  
  
## Downloading granules

    python3 download.py --file_list urls.csv 
                        --folder granules/ 
                        --email user@nasa.gov
