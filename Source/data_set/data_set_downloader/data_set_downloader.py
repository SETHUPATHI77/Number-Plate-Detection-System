from bing_image_downloader.downloader import download

query_string = 'number plate'

download(query_string, limit=50000, output_dir='data_set_from_google', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
 
print("done")
