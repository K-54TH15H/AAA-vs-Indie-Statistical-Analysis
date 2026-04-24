import requests
import pandas

# Certified AAA Publishers
AAA_PUBLISHERS = ["Valve", "Ubisoft", "Rockstar Games", "Electronic Arts", "Activision", 
                  "Bethesda Softworks", "CAPCOM Co., Ltd", "Warner Bros. Games",
                  "PlayStation Publishing LLC", "Xbox Game Studios", "SEGA", 
                  "Amazon Games", "KONAMI", "Disney", "NetEase", "KRAFTON", "Tencent",
                  "CD PROJEKT RED"]

def CreateAndSaveDataSet(url, save_path):
    try:
        # Send a HTTP request to get response
        response = requests.get(url)    
        dict_data = response.json()
    
        # Convert dictionary to pandas Dataframe
        df = pandas.DataFrame.from_dict(dict_data, orient="index")

        # Custom Series for having a review percentage
        df["review_score"] = (df["positive"]/(df["positive"] + df["negative"])) * 100
        # Custom Series for verification of AAA
        df["is_aaa"] = df["publisher"].apply(lambda x: any(pub.lower() in str(x).lower() 
                                                           for pub in AAA_PUBLISHERS))
        df.to_csv(path_or_buf=save_path)

    except Exception:
        print("unknown error occured...")
        print("please try again after validating input.")

    return 

# Main Function
if __name__ == "__main__":
    print("Scraping...")
    url = str(input("Enter url for scraping json format: "))
    save_path = str(input("Enter save path for csv file: "))

    CreateAndSaveDataSet(url, save_path)
    print("Saved.")
