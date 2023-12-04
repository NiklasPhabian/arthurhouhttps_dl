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
                        

    python3 get_urls.py --server gesdisc --products IMERG --email giessbaum@ucsb.edu --start 2022-05-22 --stop 2022-06-24 --level 3B

    python3 download_gesdisc.py --file_list urls.csv --folder /tablespace/xcal/imerg2022/ 

  
  
## Downloading granules

    python3 download.py --file_list urls.csv 
                        --folder granules/ 
                        --email user@nasa.gov

                        
                        

wget -q -nH -nd "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHL.06/2022/001/" -O - | grep MERRA2_100 | cut -f4 -d\"

