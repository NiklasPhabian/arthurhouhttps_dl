# arthurhouhttps_dl
This is a set of scripts to download remote XCLA data from arthurhouhttps.
https://arthurhouhttps.pps.eosdis.nasa.gov/

We split the download into two steps:

- Retrieve URLs
- Retrieving granules

## Install / requirements
- `pip install bs4 requests lxml`


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

# Example

    python3 get_urls.py --products 1C.GCOMW1.AMSR2 1C.NPP.ATMS 1C.NOAA20.ATMS 1C.GPM.GMI 1C.NOAA19.MHS 1C.METOPB.MHS 1C.MT1.SAPHIR 1C.F16.SSMIS 1C.F17.SSMIS 1C.F18.SSMIS --level 1C --email user@nasa.gov --start 2021-01-10 --stop 2021-02-10

# wget

     wget --http-user=user@nasa.gov --http-password=user@nasa.gov https://arthurhouhttps.pps.eosdis.nasa.gov/pub/gpmdata/2021/02/01/1C/1C.GCOMW1.AMSR2.XCAL2016-V.20210201-S010634-E024526.046331.V05A.HDF5

