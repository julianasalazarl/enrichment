import streamlit as st
import pandas as pd
import numpy as np
import io
    
st.set_page_config(page_title="Product Enrichment Tool")
st.title("Seasonal Product Enrichment Tool")
st.markdown("""
Upload your Excel file with the seasonal articles. This tool will automatically enrich missing fields based on name patterns
and provide a downloadable Excel file with the completed data.
""")
    
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
    
def enrich_data(df):
    df = df.copy()
    
    # Create the new enriched column based on conditions
    df["Enriched Product Line"] = df.apply(lambda row: (
        "Agravic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic" in str(row.get("Name", "")).lower() else
        "Samba;60s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba 62" in str(row.get("Name", "")).lower() else
        "Superstar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superstar" in str(row.get("Name", "")).lower() else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in str(row.get("Name", "")).lower() else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in str(row.get("Name", "")).lower() else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in str(row.get("Name", "")).lower() else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in str(row.get("Name", "")).lower() else
        "Hiangle" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hiangle" in str(row.get("Name", "")).lower() else
        "Kestrel" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Kestrel" in str(row.get("Name", "")).lower() else
        "Kirigami" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Kirigami" in str(row.get("Name", "")).lower() else
        "NIAD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten NIAD" in str(row.get("Name", "")).lower() else
        "Sleuth" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Sleuth" in str(row.get("Name", "")).lower() else
        "Trailcross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Trailcross" in str(row.get("Name", "")).lower() else
        "Adventure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Adventure", "Hyperturf", "Mocaturf", "Roverend", "Rovermule", "Superturf"]) else
        "Astir;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Astir" in str(row.get("Name", "")).lower() else
        "Campus" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Campus" in str(row.get("Name", "")).lower() else
        "Forum" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Forum" in str(row.get("Name", "")).lower() else
        "Gazelle;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gazelle" in str(row.get("Name", "")).lower() else
        "Nizza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Nizza" in str(row.get("Name", "")).lower() else
        "NMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "NMD" in str(row.get("Name", "")).lower() else
        "Oz;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Oz " in str(row.get("Name", "")).lower() else
        "Samba;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba" in str(row.get("Name", "")).lower() and "Cycling" not in str(row.get("Name", "")).lower() else
        "Shmoofoil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Shmoofoil" in str(row.get("Name", "")).lower() else
        "Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stan Smith" in str(row.get("Name", "")).lower() else
        "Adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puffylette" in str(row.get("Name", "")).lower() else
        "Adifom" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Supernova" in str(row.get("Name", "")).lower() else
        "adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adilette" in str(row.get("Name", "")).lower() else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["adizero", "Jumpstar", "DistanceStar", "Ubersonic 4", "Sprintstar", "Throwstar"]) else
        "Aeroimpact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aeroimpact" in str(row.get("Name", "")).lower() else
        "Alphaboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["alphaboost", "alphaboost V1"]) else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa" in str(row.get("Name", "")).lower() else
        "Fast Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Fast Impact" in str(row.get("Name", "")).lower() else
        "Optime" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Optime" in str(row.get("Name", "")).lower() else
        "Own the Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["OTR", "Own the Run"]) else
        "Power Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Power Impact" in str(row.get("Name", "")).lower() else
        "Powerreact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerreact" in str(row.get("Name", "")).lower() else
        "Predator" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Predator" in str(row.get("Name", "")).lower() else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tiro" in str(row.get("Name", "")).lower() else
        "Purelounge" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Purelounge" in str(row.get("Name", "")).lower() else
        "Solar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Solarboost", "Solarcontrol", "Solarglide", "Solarmotion"]) else
        "Supernova" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Supernova" in str(row.get("Name", "")).lower() else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost" in str(row.get("Name", "")).lower() else
        "4DFWD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "4DFWD" in str(row.get("Name", "")).lower() else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in str(row.get("Name", "")).lower() else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in str(row.get("Name", "")).lower() else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in str(row.get("Name", "")).lower() else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in str(row.get("Name", "")).lower() else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic Speed Ultra" in str(row.get("Name", "")).lower() else
        "AX4" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX AX4" in str(row.get("Name", "")).lower() else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Eastrail" in str(row.get("Name", "")).lower() else
        "Free Hiker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Free Hiker" in str(row.get("Name", "")).lower() else
        "Skychaser" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Skychaser" in str(row.get("Name", "")).lower() else
        "Swift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Swift" in str(row.get("Name", "")).lower() else
        "Techrock" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Techrock" in str(row.get("Name", "")).lower() else
        "Voyager" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Voyager" in str(row.get("Name", "")).lower() else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xperior" in str(row.get("Name", "")).lower() else
        "Xploric" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xploric" in str(row.get("Name", "")).lower() else
        "Coreflow" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Coreflow Studio" in str(row.get("Name", "")).lower() or "Coreflow Luxe" in str(row.get("Name", "")).lower()) else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cloudfoam Pure" in str(row.get("Name", "")).lower() else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Codechaos" in str(row.get("Name", "")).lower() else
        "Cross Em" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cross Em" in str(row.get("Name", "")).lower() else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["DON", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8"]) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed for Training" in str(row.get("Name", "")).lower() else
        "Exhibit" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Exhibit" in str(row.get("Name", "")).lower() else
        "Go-To" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Go-To" in str(row.get("Name", "")).lower() else
        "Impact FLX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Impact FLX" in str(row.get("Name", "")).lower() else
        "Lillard;Dame" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Dame 8" in str(row.get("Name", "")).lower() or "Dame" in str(row.get("Name", "")).lower()) else
        "MC80" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC80" in str(row.get("Name", "")).lower() else
        "MC87" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC87" in str(row.get("Name", "")).lower() else
        "Retrocross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retrocross" in str(row.get("Name", "")).lower() else
        "S2G" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "S2G" in str(row.get("Name", "")).lower() else
        "Soulstride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soulstride" in str(row.get("Name", "")).lower() else
        "Swift Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Swift Run" in str(row.get("Name", "")).lower() else
        "Teamwear" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Atlanta United", "Austin FC", "CF Montreal", "Charlotte FC", "Chicago Fire", "Colorado Rapids", "Columbus Crew", "D.C. United",
            "FC Cincinnati", "FC Dallas", "Houston Dynamo", "Inter Miami CF", "LA Galaxy", "LAFC", "Los Angeles Football Club",
            "Manchester United", "Minnesota United", "Nashville SC", "New England Revolution", "New York City FC",
            "New York Red Bulls", "Orlando City", "Orlando City SC", "Philadelphia Union", "Portland Timbers", "Real Salt Lake",
            "San Jose Earthquakes", "Seattle Sounders", "Seattle Sounders FC", "Sporting Kansas City", "St. Louis CITY FC",
            "ST Louis City SC", "Toronto FC", "Vancouver Whitecaps", "Jamaica Beckenbauer", "Lightning Third",
            "Washington Huskies", "AFC Ajax", "Benfica", "Celtic FC", "FC Bayern Munich", "Newcastle United FC",
            "Olympique Lyonnais", "Arsenal", "Juventus", "Real Madrid"
        ]) else
        "Trailmaker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Trailmaker" in str(row.get("Name", "")).lower() else
        "TrueCasuals" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TrueCasuals" in str(row.get("Name", "")).lower() else
        "TruePace" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePace" in str(row.get("Name", "")).lower() else
        "Ultimate365" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultimate365" in str(row.get("Name", "")).lower() else
        "ZG" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("ZG23" in str(row.get("Name", "")).lower() or "ZG21" in str(row.get("Name", "")).lower()) else
        "Zoysia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Zoysia" in str(row.get("Name", "")).lower() else
        "Trae" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Trae" in str(row.get("Name", "")).lower() or "Trae Unlimited" in str(row.get("Name", "")).lower()) else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost light" in str(row.get("Name", "")).lower() else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TIRO24" in str(row.get("Name", "")).lower() else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa Gloro" in str(row.get("Name", "")).lower() else
        "True Purpose" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePurpose" in str(row.get("Name", "")).lower() else
        "Response" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Response" in str(row.get("Name", "")).lower() else
        "Daily" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Daily" in str(row.get("Name", "")).lower() else
        "Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Five Ten Impact" in str(row.get("Name", "")).lower() or "Five Ten" in str(row.get("Name", "")).lower()) else
        "Futurecraft" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Futurecraft" in str(row.get("Name", "")).lower() else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s Shoes" in str(row.get("Name", "")).lower() else
        "Run 80s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 80s Shoes" in str(row.get("Name", "")).lower() else
        "Earthlight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Earthlight" in str(row.get("Name", "")).lower() else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Eastrail" in str(row.get("Name", "")).lower() else
        "VULCRAID3R" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VULCRAID3R" in str(row.get("Name", "")).lower() else
        "Sport Pro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adidas x LEGO® Sport Pro Running Shoes" in str(row.get("Name", "")).lower() else
        "Questar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Questar" in str(row.get("Name", "")).lower() else
        "Tensaur" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tensaur" in str(row.get("Name", "")).lower() else
        "Summervent" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Summervent" in str(row.get("Name", "")).lower() else
        "Puig" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puig" in str(row.get("Name", "")).lower() else
        "CourtJam" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "CourtJam" in str(row.get("Name", "")).lower() else
        "Avacourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avacourt" in str(row.get("Name", "")).lower() else
        "Tracefinder" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tracefinder" in str(row.get("Name", "")).lower() else
        "QT Racer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "QT Racer" in str(row.get("Name", "")).lower() else
        "Start Your Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Start Your Run" in str(row.get("Name", "")).lower() else
        "Activeride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Activeride 2.0" in str(row.get("Name", "")).lower() else
        "ZNCHILL" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNCHILL" in str(row.get("Name", "")).lower() else
        "Solarmotion" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solarmotion" in str(row.get("Name", "")).lower() else
        "Kantana" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Kantana Shoes" in str(row.get("Name", "")).lower() else
        "Midcity" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Midcity Low Shoes" in str(row.get("Name", "")).lower() else
        "Winterplay" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Winterplay" in str(row.get("Name", "")).lower() else
        "X" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "X League" in str(row.get("Name", "")).lower() else
        "Retro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Retro Graphic", "Retro Quarter"]) else
        "RDY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["COLD.RDY", "HEAT.RDY", "RAIN.RDY", "SUMMER.RDY", "WIND.RDY"]) else
        "Top Ten" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Top Ten" in str(row.get("Name", "")).lower() else
        "Spezial;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and pd.notna(row.get("PIM - Label")) and "Originals" in str(row.get("PIM - Label", "")).lower() and "Handball Spezial" in str(row.get("Name", "")).lower() else
        "Tyshawn" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tyshawn" in str(row.get("Name", "")).lower() else
        "adiFOM;Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Stan Smith" in str(row.get("Name", "")).lower() else
        "adilette;adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Adilette" in str(row.get("Name", "")).lower() else
        "adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adiFOM" in str(row.get("Name", "")).lower() else
        "BYW Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BYW Select" in str(row.get("Name", "")).lower() else
        "ADI2000" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADI2000" in str(row.get("Name", "")).lower() else
        "Matchbreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak" in str(row.get("Name", "")).lower() else
        "Crazy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy" in str(row.get("Name", "")).lower() else
        "Crazyflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazyflight" in str(row.get("Name", "")).lower() else
        "Adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adibreak" in str(row.get("Name", "")).lower() else
        "Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Select" in str(row.get("Name", "")).lower() else
        "All Me" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "All Me " in str(row.get("Name", "")).lower() else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["D4T", "Designed-for-Training"]) else
        "SL 72;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "SL 72" in str(row.get("Name", "")).lower() else
        "Country;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Country" in str(row.get("Name", "")).lower() else
        "Retropy;2000s;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retropy" in str(row.get("Name", "")).lower() else
        "adicolor;Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Arsenal Beckenbauer", "Real Madrid Beckenbauer", "Juventus Beckenbauer", "Adicolor Classics Beckenbauer"
        ]) else
        "adicolor;VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor VRCT" in str(row.get("Name", "")).lower() else
        "Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Beckenbauer" in str(row.get("Name", "")).lower() else
        "3MC" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "3MC" in str(row.get("Name", "")).lower() else
        "adicolor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor" in str(row.get("Name", "")).lower() else
        "Adimatic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adimatic" in str(row.get("Name", "")).lower() else
        "Adipower" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adipower" in str(row.get("Name", "")).lower() else
        "Adistar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adistar" in str(row.get("Name", "")).lower() else
        "Avaflash" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avaflash" in str(row.get("Name", "")).lower() else
        "AVRYN" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avryn_X" in str(row.get("Name", "")).lower() else
        "Barricade" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Barricade" in str(row.get("Name", "")).lower() else
        "Busenitz" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Busenitz" in str(row.get("Name", "")).lower() else
        "Dropset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Dropset" in str(row.get("Name", "")).lower() else
        "Galaxy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Galaxy" in str(row.get("Name", "")).lower() else
        "Harden" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Harden" in str(row.get("Name", "")).lower() else
        "Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Hoops" in str(row.get("Name", "")).lower() else
        "Icon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Icon" in str(row.get("Name", "")).lower() else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak Super" in str(row.get("Name", "")).lower() else
        "MYSHELTER" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MYSHELTER" in str(row.get("Name", "")).lower() else
        "Powerlift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerlift" in str(row.get("Name", "")).lower() else
        "Pureboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pureboost" in str(row.get("Name", "")).lower() else
        "Rapida" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "RapidaSport" in str(row.get("Name", "")).lower() else
        "Rivalry" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rivalry" in str(row.get("Name", "")).lower() else
        "Sereno" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Sereno" in str(row.get("Name", "")).lower() else
        "Stabil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stabil" in str(row.get("Name", "")).lower() else
        "Tango" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tango" in str(row.get("Name", "")).lower() else
        "Tour360" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tour360" in str(row.get("Name", "")).lower() else
        "ZX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZX" in str(row.get("Name", "")).lower() else
        "adicross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adicross" in str(row.get("Name", "")).lower() else
        "ZPLAASH" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZPLAASH" in str(row.get("Name", "")).lower() else
        "adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADBRK" in str(row.get("Name", "")).lower() else
        "Lacombe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lacombe" in str(row.get("Name", "")).lower() else
        "Hoop York City" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["HYC", "Hoop York City"]) else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNE" in str(row.get("Name", "")).lower() else
        "Koln" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Koln" in str(row.get("Name", "")).lower() else
        "Munchen" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Munchen" in str(row.get("Name", "")).lower() else
        "The Total" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "The Total" in str(row.get("Name", "")).lower() else
        "Amplimove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Amplimove" in str(row.get("Name", "")).lower() else
        "Velostan" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Velostan" in str(row.get("Name", "")).lower() else
        "Novaflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Novaflight" in str(row.get("Name", "")).lower() else
        "VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VRCT" in str(row.get("Name", "")).lower() else
        "Gamemode" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamemode" in str(row.get("Name", "")).lower() else
        "Goletto" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Goletto" in str(row.get("Name", "")).lower() else
        "Anthony Edwards" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anthony Edwards" in str(row.get("Name", "")).lower() else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "D.O.N" in str(row.get("Name", "")).lower() else
        "Megaride;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Megaride" in str(row.get("Name", "")).lower() else
        "Centennial" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Centennial" in str(row.get("Name", "")).lower() else
        "Aloha Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aloha Super" in str(row.get("Name", "")).lower() else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Takumi Sen" in str(row.get("Name", "")).lower() else
        "Helionic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Helionic" in str(row.get("Name", "")).lower() else
        "Alphaskin" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Alphaskin" in str(row.get("Name", "")).lower() else
        "Anylander" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anylander" in str(row.get("Name", "")).lower() else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Xperior" in str(row.get("Name", "")).lower() else
        "EQT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Equipment" in str(row.get("Name", "")).lower() or "EQT" in str(row.get("Name", "")).lower()) else
                "Dugout" if pd.isna(row.get("PIM - Product Line (sportsub)")).lower() and (
            "Baseball" in str(row.get("PIM - Sport", "")).lower() or "Softball" in str(row.get("PIM - Sport", "")).lower()
        ) else
        "Beyond the Course" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf" in str(row.get("PIM - Sport", "")).lower() and "Beyond" in str(row.get("Name", "")).lower() else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf" in str(row.get("PIM - Sport", "")).lower() and "Codechaos" in str(row.get("Name", "")).lower() else
        "Clima" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Clima" in str(row.get("Name", "")).lower() else
        "Everyset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Everyset" in str(row.get("Name", "")).lower() else
        "Rapidmove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rapidmove" in str(row.get("Name", "")).lower() else
        "Stella Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stella McCartney Court" in str(row.get("Name", "")).lower() else
        "GameCourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamecourt" in str(row.get("Name", "")).lower() else
        "Solematch" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solematch" in str(row.get("Name", "")).lower() else
        "TLDR" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TLDR" in str(row.get("Name", "")).lower() else
        "Coursecup" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Coursecup" in str(row.get("Name", "")).lower() else
        "Gym+" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gym+" in str(row.get("Name", "")).lower() else
        "Pacer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pacer" in str(row.get("Name", "")).lower() else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed-for-Training" in str(row.get("Name", "")).lower() else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s" in str(row.get("Name", "")).lower() else
        "Lightblaze " if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lightblaze" in str(row.get("Name", "")).lower() else
        "ZNSORY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNSORY" in str(row.get("Name", "")).lower() else
        "Aspyre" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aspyre" in str(row.get("Name", "")).lower() else
        "BRMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BRMD" in str(row.get("Name", "")).lower() else
        "Ultradream" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultradream" in str(row.get("Name", "")).lower() else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() and "Z.N.E" in str(row.get("Name", "")).lower() else
        "Spezialist" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Spezialist" in str(row.get("Name", "")).lower() else
        "Ligra" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ligra" in str(row.get("Name", "")).lower() else
        "Essentials" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "essentials" in str(row.get("Name", "")).lower() else
        "Worldwide Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Worldwide Hoops" in str(row.get("Name", "")).lower() or "WWH " in str(row.get("Name", "")).lower()) else
        "adilenium" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adilenium" in str(row.get("Name", "")).lower() else
        "Teamwear" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(team.lower() in str(row.get("Name", "")).lower() or team in str(row.get("PIM - Teams", "")).lower() for team in [
            "University of Louisville", "Louisville Cardinals", "Texas A&M", "Texas A&M Aggies", "University of Kansas", "Kansas Jayhawks",
            "University of Miami", "Miami Hurricanes", "University of Nebraska", "Nebraska Cornhuskers",
            "North Carolina State University", "North Carolina", "Arizona State University", "Grambling State University", "Grambling State Tigers",
            "Indiana University", "Indiana Hoosiers", "University of Washington", "Washington Huskies", "NC State", "NC State Wolfpack",
            "New Zealand Rugby", "All Blacks", "Texas Tech", "Hoosiers", "Huskies", "Georgia Tech", "Yellow Jackets",
            "Alcorn State", "Alcorn State Braves", "Arkansas Pine Bluff", "Arkansas-Pine Bluff Golden Lions",
            "Mississippi State University", "Mississippi State Bulldogs", "Alabama State", "Alabama State Hornets",
            "Black History Month University"
        ]) else
        "Initiation" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Initiation" in str(row.get("Name", "")).lower() else
        "BB Legends" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Basketball Legends" in str(row.get("Name", "")).lower() else
        "Crazy Lite" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy lite" in str(row.get("Name", "")).lower() else
        "Ballerina" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ballerina" in str(row.get("Name", "")).lower() else
        "Palos Hills" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Palos Hills" in str(row.get("Name", "")).lower() else
        "Seeulater" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Seeulater" in str(row.get("Name", "")).lower() else
        "Superskate" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superskate" in str(row.get("Name", "")).lower() else
        "Italia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Italia" in str(row.get("Name", "")).lower() else
        "Montreal" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Montreal" in str(row.get("Name", "")).lower() else
        "Adiraptor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adiraptor" in str(row.get("Name", "")).lower() else
        "Ghost Sprint" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ghost Sprint" in str(row.get("Name", "")).lower() else
        "Feroza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport" in str(row.get("PIM - Sport", "")).lower() and "Feroza" in str(row.get("Name", "")).lower() else
        "Adiracer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport" in str(row.get("PIM - Sport", "")).lower() and "Adiracer" in str(row.get("Name", "")).lower() else
        "Heritage" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis" in str(row.get("PIM - Sport", "")).lower() and "Heritage" in str(row.get("Name", "")).lower() else
        "Defiant Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis" in str(row.get("PIM - Sport", "")).lower() and "Defiant" in str(row.get("Name", "")).lower() else
        row.get("PIM - Product Line (sportsub)")
    ), axis=1)
    
    df["Enriched Product Family"] = df.apply(lambda row: (
        "Hyperturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Hyperturf" in str(row.get("Name", "")).lower() else
        "Sambae" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Sambae" in str(row.get("Name", "")).lower() else
        "Mocaturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Mocaturf" in str(row.get("Name", "")).lower() else
        "Roverend" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Roverend" in str(row.get("Name", "")).lower() else
        "Rovermule" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rovermule" in str(row.get("Name", "")).lower() else
        "Superturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superturf" in str(row.get("Name", "")).lower() else
        "Campus 00" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 00" in str(row.get("Name", "")).lower() else
        "Campus 80" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 80" in str(row.get("Name", "")).lower() else
        "Forum High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Forum High" in str(row.get("Name", "")).lower() or "Forum Hi" in str(row.get("Name", "")).lower()) else
        "Forum Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Forum Low" in str(row.get("Name", "")).lower() or "Forum Lo" in str(row.get("Name", "")).lower()) else
        "Forum Mid" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum Mid" in str(row.get("Name", "")).lower() else
        "Nizza High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza High" in str(row.get("Name", "")).lower() else
        "Nizza Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza Low" in str(row.get("Name", "")).lower() else
        "Nizza Mid" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza Mid" in str(row.get("Name", "")).lower() else
        "NMD 360" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD 360" in str(row.get("Name", "")).lower() else
        "NMD_C2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_C2" in str(row.get("Name", "")).lower() else
        "NMD_CS1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_CS1" in str(row.get("Name", "")).lower() else
        "NMD_G1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_G1" in str(row.get("Name", "")).lower() else
        "NMD_R1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1" in str(row.get("Name", "")).lower() else
        "NMD_R1 V2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1 V2" in str(row.get("Name", "")).lower() else
        "NMD_R1 V3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1 V3" in str(row.get("Name", "")).lower() else
        "NMD_R1_PK" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1_PK" in str(row.get("Name", "")).lower() else
        "NMD_R2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R2" in str(row.get("Name", "")).lower() else
        "NMD_TR" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_TR" in str(row.get("Name", "")).lower() else
        "NMD_TS1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_TS1" in str(row.get("Name", "")).lower() else
        "NMD_V3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_V3" in str(row.get("Name", "")).lower() else
        "NMD_W1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_W1" in str(row.get("Name", "")).lower() else
        "NMD_XR1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_XR1" in str(row.get("Name", "")).lower() else
        "Ozelia" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozelia" in str(row.get("Name", "")).lower() else
        "Oznova" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Oznova" in str(row.get("Name", "")).lower() else
        "Ozrah" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozrah" in str(row.get("Name", "")).lower() else
        "Superstar 360" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar 360" in str(row.get("Name", "")).lower() else
        "Superstar ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar ADV" in str(row.get("Name", "")).lower() else
        "adizero Adios Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero adios" in str(row.get("Name", "")).lower() else
        "adizero Afterburner" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Afterburner" in str(row.get("Name", "")).lower() else
        "adizero Boston" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Boston" in str(row.get("Name", "")).lower() else
        "adizero prime" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero prime" in str(row.get("Name", "")).lower() else
        "adizero RC" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero RC" in str(row.get("Name", "")).lower() else
        "adizero Select" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Select" in str(row.get("Name", "")).lower() else
        "adizero SL" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero SL" in str(row.get("Name", "")).lower() else
        "adizero takumi sen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero takumi sen" in str(row.get("Name", "")).lower() else
        "adizero ubersonic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero ubersonic" in str(row.get("Name", "")).lower() else
        "Copa Pure" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Pure" in str(row.get("Name", "")).lower() else
        "Solarboost" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarboost" in str(row.get("Name", "")).lower() else
        "Solarcontrol" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarcontrol" in str(row.get("Name", "")).lower() else
        "Solar Glide" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarglide" in str(row.get("Name", "")).lower() else
        "Solarmotion" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarmotion" in str(row.get("Name", "")).lower() else
        "X Crazyfast" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X Crazyfast" in str(row.get("Name", "")).lower() else
        "X Speedportal" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X Speedportal" in str(row.get("Name", "")).lower() else
        "4DFWD Pulse" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "4DFWD Pulse" in str(row.get("Name", "")).lower() else
        "Ultrabounce DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultrabounce DNA" in str(row.get("Name", "")).lower() else
        "Duramo SL" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Duramo SL" in str(row.get("Name", "")).lower() else
        "Duramo Speed" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Duramo Speed" in str(row.get("Name", "")).lower() else
        "Ultraboost 1.0;Ultraboost DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 1.0" in str(row.get("Name", "")).lower() else
        "xplrphase" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "x_plrphase" in str(row.get("Name", "")).lower() else
        "Ubounce DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ubounce DNA" in str(row.get("Name", "")).lower() else
        "Grand Court 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Grand Court 2.0" in str(row.get("Name", "")).lower() else
        "adilette Aqua" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette aqua" in str(row.get("Name", "")).lower() else
        "adilette Comfort" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette comfort" in str(row.get("Name", "")).lower() else
        "adilette shower" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette shower" in str(row.get("Name", "")).lower() else
        "Grand Court Alpha" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "grand court alpha" in str(row.get("Name", "")).lower() else
        "adilette platform" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette platform" in str(row.get("Name", "")).lower() else
        "Agravic Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Flow" in str(row.get("Name", "")).lower() else
        "Agravic Speed Ultra" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Speed Ultra" in str(row.get("Name", "")).lower() else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Speed" in str(row.get("Name", "")).lower() else
        "Agravic Ultra" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Ultra" in str(row.get("Name", "")).lower() else
        "SL 72 RTN" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 RTN" in str(row.get("Name", "")).lower() else
        "Anthony Edwards 1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Anthony Edwards 1" in str(row.get("Name", "")).lower() else
        "3 Stripes" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("3 Stripes" in str(row.get("Name", "")).lower() or "3-Stripes" in str(row.get("Name", "")).lower()) else
        "F50 Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 Pro" in str(row.get("Name", "")).lower() else
        "F50 Elite" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 Elite" in str(row.get("Name", "")).lower() else
        "F50 League" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 League" in str(row.get("Name", "")).lower() else
        "Stan Smith Lux" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Stan Smith Lux" in str(row.get("Name", "")).lower() else
        "Gazelle Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle Bold" in str(row.get("Name", "")).lower() else
        "Predator Edge" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Edge" in str(row.get("Name", "")).lower() else
        "Predator Club" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Club" in str(row.get("Name", "")).lower() else
        "Predator Accuracy" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Accuracy" in str(row.get("Name", "")).lower() else
        "Predator League" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator League" in str(row.get("Name", "")).lower() else
        "Copa Sense" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Sense" in str(row.get("Name", "")).lower() else
        "Copa Mundial" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Mundial" in str(row.get("Name", "")).lower() else
        "adizero Instinct" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Instinct" in str(row.get("Name", "")).lower() else
        "Free Hiker 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Free Hiker 2" in str(row.get("Name", "")).lower() else
        "Exhibit Select" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Exhibit Select" in str(row.get("Name", "")).lower() else
        "adizero Impact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Impact" in str(row.get("Name", "")).lower() else
        "SL 72 OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 OG" in str(row.get("Name", "")).lower() else
        "SL 72 RS" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 RS" in str(row.get("Name", "")).lower() else
        "Predator Elite" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Elite" in str(row.get("Name", "")).lower() else
        "Forum Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum Bold" in str(row.get("Name", "")).lower() else
        "VL Court 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "VL Court 3.0" in str(row.get("Name", "")).lower() else
        "Ultraboost 20" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 20" in str(row.get("Name", "")).lower() else
        "SL 76" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 76" in str(row.get("Name", "")).lower() else
        "Handball Spezial" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Originals" in str(row.get("PIM - Label", "")).lower() and "Handball Spezial" in str(row.get("Name", "")).lower() else
        "Response CL;2000s" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Response CL" in str(row.get("Name", "")).lower() else
        "Rivalry Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Rivalry 86 Low" in str(row.get("Name", "")).lower() or "Rivalry Summer Low" in str(row.get("Name", ""))).lower() else
        "Rivalry High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rivalry High" in str(row.get("Name", "")).lower() else
        "Ozmillen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozmillen" in str(row.get("Name", "")).lower() else
        "Lite Racer Adapt" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer Adapt" in str(row.get("Name", "")).lower() else
        "Firebird" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Firebird" in str(row.get("Name", "")).lower() else
        "adizero Electric" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Electric" in str(row.get("Name", "")).lower() else
        "Adilette 22" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilette 22" in str(row.get("Name", "")).lower() else
        "Superstar XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar XLG" in str(row.get("Name", "")).lower() else
        "Country XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country XLG" in str(row.get("Name", "")).lower() else
        "Samba XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba XLG" in str(row.get("Name", "")).lower() else
        "Samba OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba OG" in str(row.get("Name", "")).lower() else
        "Y-3 Classic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Y-3 Classic" in str(row.get("Name", "")).lower() or "Y-3 CL" in str(row.get("Name", ""))).lower() else
        "Retro Quarter" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Retro Quarter" in str(row.get("Name", "")).lower() else
        "Retro Graphic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Retro Graphic" in str(row.get("Name", "")).lower() else
        "Activeride 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Activeride 2.0" in str(row.get("Name", "")).lower() else
        "QT Racer 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "QT Racer 3.0" in str(row.get("Name", "")).lower() else
        "Eastrail 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Eastrail 2.0" in str(row.get("Name", "")).lower() else
        "ZG21" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "ZG21" in str(row.get("Name", "")).lower() else
        "ZG23" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "ZG23" in str(row.get("Name", "")).lower() else
        "Daily 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Daily 3.0" in str(row.get("Name", "")).lower() else
        "Copa Gloro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Gloro" in str(row.get("Name", "")).lower() else
        "Tiro 21" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 21" in str(row.get("Name", "")).lower() or "TIRO21" in str(row.get("Name", "")).lower()) else
        "Tiro 23" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 23" in str(row.get("Name", "")).lower() or "TIRO23" in str(row.get("Name", "")).lower()) else
        "Tiro 24" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 24" in str(row.get("Name", "")).lower() or "TIRO24" in str(row.get("Name", "")).lower()) else
        "Ultraboost light" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost light" in str(row.get("Name", "")).lower() else
        "Supernova Stride" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Stride" in str(row.get("Name", "")).lower() else
        "Supernova Solution" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Solution" in str(row.get("Name", "")).lower() else
        "Supernova Rise" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Rise" in str(row.get("Name", "")).lower() else
        "Trae Young Unlimited" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Unlimited" in str(row.get("Name", "")).lower() else
        "Trae Young 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 3" in str(row.get("Name", "")).lower() else
        "Trae Young 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 2" in str(row.get("Name", "")).lower() else
        "Dame Certified" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame Certified" in str(row.get("Name", "")).lower() else
        "Dame 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame 8" in str(row.get("Name", "")).lower() else
        "D.O.N Issue 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 8" in str(row.get("Name", "")).lower() else
        "D.O.N Issue 7" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 7" in str(row.get("Name", "")).lower() else
        "D.O.N Issue 6" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 6" in str(row.get("Name", "")).lower() else
        "D.O.N Issue 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 5" in str(row.get("Name", "")).lower() else
        "Barricade 13" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Barricade 13" in str(row.get("Name", "")).lower() else
        "Crazy 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Crazy 8" in str(row.get("Name", "")).lower() else
        "D.O.N Issue 6" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("D.O.N. ISSUE 6" in str(row.get("Name", "")).lower() or "D.O.N ISSUE #6" in str(row.get("Name", "")).lower()) else
        "D.O.N Issue 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N. Issue #5" in str(row.get("Name", "")).lower() else
        "Forum Hi" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "FORUM 84 HI" in str(row.get("Name", "")).lower() else
        "Forum Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "FORUM 84 LOW" in str(row.get("Name", "")).lower() else
        "Trae Young 4" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 4" in str(row.get("Name", "")).lower() else
        "Pureboost 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pureboost 5" in str(row.get("Name", "")).lower() else
        "Alphaboost V1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphaboost V1" in str(row.get("Name", "")).lower() else
        "Alphaboost V2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphaboost V2" in str(row.get("Name", "")).lower() else
        "Alphabounce+" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphabounce+" in str(row.get("Name", "")).lower() else
        "Country OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country OG" in str(row.get("Name", "")).lower() else
        "Pro Shell ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Shell ADV" in str(row.get("Name", "")).lower() else
        "Gazelle ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle ADV" in str(row.get("Name", "")).lower() else
        "Centennial 85" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Centennial 85" in str(row.get("Name", "")).lower() else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Cloudfoam Pure" in str(row.get("Name", "")).lower() else
        "Supernova Prima" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Prima" in str(row.get("Name", "")).lower() else
        "Ultraboost 5X" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 5X" in str(row.get("Name", "")).lower() else
        "PowerImpact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "PowerImpact" in str(row.get("Name", "")).lower() else
        "Run Pocket" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Run Pocket" in str(row.get("Name", "")).lower() else
        "Soulstride Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Soulstride Flow" in str(row.get("Name", "")).lower() else
        "TLRD Impact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TLRD Impact" in str(row.get("Name", "")).lower() else
        "Campus Vulc" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus Vulc" in str(row.get("Name", "")).lower() else
        "Campus ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus ADV" in str(row.get("Name", "")).lower() else
        "Busenitz Vulc II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Busenitz Vulc II" in str(row.get("Name", "")).lower() else
        "Busenitz Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Busenitz Pro" in str(row.get("Name", "")).lower() else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Matchbreak Super" in str(row.get("Name", "")).lower() else
        "Ozweego" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozweego" in str(row.get("Name", "")).lower() else
        "Samba ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba ADV" in str(row.get("Name", "")).lower() else
        "Gazelle Indoor" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle Indoor" in str(row.get("Name", "")).lower() else
        "Ozmorph" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozmorph" in str(row.get("Name", "")).lower() else
        "Samba Decon" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba Decon" in str(row.get("Name", "")).lower() else
        "Samba Millenium" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Samba MN" in str(row.get("Name", "")).lower() or "Samba Millenium" in str(row.get("Name", "")).lower()) else
        "Stan Smith Decon" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Stan Smith Decon" in str(row.get("Name", "")).lower() else
        "Rivalry Mule" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rivalry Mule" in str(row.get("Name", "")).lower() else
        "Temper Run 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Temper Run 2.0" in str(row.get("Name", "")).lower() else
        "Superstar II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar II" in str(row.get("Name", "")).lower() else
        "Country II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country II" in str(row.get("Name", "")).lower() else
        "Harden Vol. 9" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Harden Vol. 9" in str(row.get("Name", "")).lower() else
        "Crazy 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Crazy 2" in str(row.get("Name", "")).lower() else
        "Tyshawn II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tyshawn II" in str(row.get("Name", "")).lower() else
        "adizero ZG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Golf" in str(row.get("PIM - Sport", "")).lower() and "Adizero ZG" in str(row.get("Name", "")).lower() else
        "adizero Cybersonic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tennis" in str(row.get("PIM - Sport", "")).lower() and "Adizero Cybersonic" in str(row.get("Name", "")).lower() else
        "Entrada 22" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() and "Entrada 22" in str(row.get("Name", "")).lower() else
        "Lite Racer 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer 3.0" in str(row.get("Name", "")).lower() else
        "Swift Run 1.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Swift Run 1.0" in str(row.get("Name", "")).lower() else
        "X_PLR Path" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X_PLR Path" in str(row.get("Name", "")).lower() else
        "Kaptir Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Kaptir Flow" in str(row.get("Name", "")).lower() else
        "Kaptir 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Kaptir 3.0" in str(row.get("Name", "")).lower() else
        "Lite Racer 4.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer 4.0" in str(row.get("Name", "")).lower() else
        "VL Court Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "VL Court Bold" in str(row.get("Name", "")).lower() else
        "Ultradream Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultradream Bold" in str(row.get("Name", "")).lower() else
        "Ultradream DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultradream DNA" in str(row.get("Name", "")).lower() else
        "Adilette Estrap" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilette Estrap" in str(row.get("Name", "")).lower() else
        "Neuclassics" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Neuclassics" in str(row.get("Name", "")).lower() else
        "Superstar 80s" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar 82" in str(row.get("Name", "")).lower() else
        "Adizero Aruku" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Aruku" in str(row.get("Name", "")).lower() else
        "iiinfinity" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "IIInfinity" in str(row.get("Name", "")).lower() else
        "Adilenium Season 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilenium Season 3" in str(row.get("Name", "")).lower() else
        "adizero takumi sen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Takumi Sen" in str(row.get("Name", "")).lower() else
        "Dame 9" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame 9" in str(row.get("Name", "")).lower() else
        "Agravic 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Agravic 3" in str(row.get("Name", "")).lower() else
        "Tracefinder 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tracefinder 2" in str(row.get("Name", "")).lower() else
        "Seeulater 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Seeulater 2" in str(row.get("Name", "")).lower() else
        "Dame X" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame X" in str(row.get("Name", "")).lower() else
        "Forum ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum ADV" in str(row.get("Name", "")).lower() else
        "Pro Model ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Model ADV" in str(row.get("Name", "")).lower() else
        "Initiation" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Initiation" in str(row.get("Name", "")).lower() else
        "Pro Model" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Model" in str(row.get("Name", "")).lower() else
        "Campus 00s Beta" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 00s Beta" in str(row.get("Name", "")).lower() else
        row.get("PIM - Product Family (productlinestyle)")
    ), axis=1)

    df["Enriched Label"] = df.apply(lambda row: (
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "ALL SZN" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Duramo" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ultraboost 1.0" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "X_PLR" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "XPLR" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Z.N.E" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "City Escape" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "FortaRun" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "RunFalcon" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Runfalcon" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Racer TR" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "VL Court" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Front Court" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ownthegame" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ubounce" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Breaknet" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Grand Court 2.0" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Postmove" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "alphaboost" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Alphaboost" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Puremotion" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Kaptir" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Spiritain" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "ZNSORED" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Future Icons" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Lite Racer" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette aqua" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette comfort" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette shower" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "grand court alpha" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "alphabounce" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Alphabounce" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adicane" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette platform" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "advantage" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "courtblock" in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y-3" in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y3" in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y 3" in str(row.get("Name", "")).lower() else
        "Five Ten" if pd.isna(row.get("PIM - Label")) and "Hellcat" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Run 70s Shoes" in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Run 80s Shoes" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "The Gravel Cycling" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ZG23" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ZG21" in str(row.get("Name", "")).lower() else
        "adidas by Stella McCartney" if pd.isna(row.get("PIM - Label")) and "adidas by Stella McCartney" in str(row.get("Name", "")).lower() else
        "adidas by Stella McCartney" if pd.isna(row.get("PIM - Label")) and "aSMC" in str(row.get("Name", "")) else
        "TERREX" if pd.isna(row.get("PIM - Label")) and "Eastrail" in str(row.get("Name", "")).lower() else
        "Impact" if pd.isna(row.get("PIM - Label")) and "Five Ten Impact" in str(row.get("Name", "")).lower() else
        "Five Ten" if pd.isna(row.get("PIM - Label")) and "Five Ten" in str(row.get("Name", "")).lower() else
        "Fear of God Athletics" if pd.isna(row.get("PIM - Label")) and "Fear of God Athletics" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Gazelle" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Samba Messi" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Sambae" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Samba" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Superstar" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Forum" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Stan Smith" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Ozelia" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "NMD" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "OZWEEGO" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "OZMILLEN" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Campus" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Adizero" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ADIZERO" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Rivalry" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Falcon" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Craig Green" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Bad Bunny" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Originals" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Country OG" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Ozthemis" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adi2000" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Spezial" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Response CL" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Response" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adifom" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "AdiFOM" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Wensley" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SPZL" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Moston Super" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL 72" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Pop Trading Co" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "NRTN" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SSTR N" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Wales Bonner" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL76" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL 76" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "TMNT" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Centennial 85" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Civilist ZX" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Crazy" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Nizza" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Solid Crew" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Trefoil" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adibreak" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Korn" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adi Dassler" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adicolor" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "100 Thieves" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Street Neuclassic" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "KSENIASCHNAIDER" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Premium" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Todmorden Smock" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Rossendale" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SST" in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Response", "Ligra", "Fabela", "Adipower", "Jumpstar", "Throwstar", "Lux 2.2S", "2.2 S",
            "Dropset", "Adistar", "Avaflash", "Switch FWD", "Running", "ADIOS", "Ubersonic",
            "Rapidmove", "Everyset", "CourtJam", "Barricade", "Amplimove", "4DFWD", "Bounce Legends",
            "Anthony Edwards 1", "Rugby", "Kakari", "RS15", "X Crazyfast", "Copa Pure", "Predator",
            "Copa Mundial", "Flexcloud", "Copa", "Tennis", "Football", "Training", "Performance",
            "adi 23", "UCL Club", "UCL Training", "Fussballliebe Club", "Euro 24", "4ATHLTS",
            "Gym", "Ripstream", "Yoga Studio", "Own the Run", "OTR", "All Me Light", "Powerimpact",
            "TLRD Impact", "Run Pocket", "FastImpact", "Ultimateadidas", "HIIT", "Power Workout",
            "Techfit", "Manchester United", "Inter Miami", "Belgium 24", "Tiro 24", "Italy 24",
            "Workout", "All Me", "DailyRun", "Optime", "Country NAME 24"
        ]) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Tensaur", "X_PLRBOOST", "SwIft Run", "Kantana", "Osade", "Park Street",
            "X_PLRPHASE", "Heawyn", "Avryn_X", "Adissage", "ZPLAASH", "Sportswear",
            "Z.N.E.", "FARM Rio"
        ]) else
        "TERREX" if pd.isna(row.get("PIM - Label")) and "Terrex" in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Real Madrid 23/24" in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Golf" in str(row.get("PIM - Sport", "")).lower() and any(x.lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() for x in [
            "Gazelle", "Samba", "Stan Smith"
        ]) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Golf" in str(row.get("PIM - Sport", "")).lower() and "Originals" in str(row.get("Name", "")).lower() else
        row.get("PIM - Label")
    ), axis=1)
    df["Enriched Sport"] = df.apply(lambda row: (   
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Freerider" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Aleon" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Crawe" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Hellcat" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Hiangle" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Kestrel" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Kirigami" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten NIAD" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Sleuth" in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Trailcross" in str(row.get("Name", "")).lower() else
        "Basketball;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Forum" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Adifom Supernova" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero adios" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero adios pro" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero Boston" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero prime" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero RC" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero SL" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero takumi sen" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarboost" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarcontrol" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarglide" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Ultrabounce" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ALL SZN" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Duramo" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ultraboost 1.0" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "X_PLR" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "XPLR" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Z.N.E" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "City Escape" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "FortaRun" in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "RunFalcon" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Racer TR" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "VL Court" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Front Court" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ownthegame" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ubounce" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Breaknet" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Grand Court 2.0" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Postmove" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "alphaboost" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Puremotion" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Kaptir" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Spiritain" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ZNSORED" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Future Icons" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Lite Racer" in str(row.get("Name", "")).lower() else
        "Swim; Yoga; Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette aqua" in str(row.get("Name", "")).lower() else
        "Swim; Yoga; Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette comfort" in str(row.get("Name", "")).lower() else
        "Swim; Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette shower" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "grand court alpha" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "alphabounce" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adicane" in str(row.get("Name", "")).lower() else
        "Swim;Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette platform" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "advantage" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "courtblock" in str(row.get("Name", "")).lower() else
        "Swim;Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and pd.notna(row.get("PIM adidas - Product Types")) and "Slides" in row.get("PIM adidas - Product Types").lower() else
        "Dance" if pd.isna(row.get("PIM - Sport")) and "Dance" in str(row.get("Name", "")).lower() else
        "Golf" if pd.isna(row.get("PIM - Sport")) and "Golf" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "TrueCasuals" in str(row.get("Name", "")).lower() else
        "Golf" if pd.isna(row.get("PIM - Sport")) and "Ultimate365" in str(row.get("Name", "")).lower() else
        "Soccer" if pd.isna(row.get("PIM - Sport")) and "Copa Gloro" in str(row.get("Name", "")).lower() else
        "Cycling" if pd.isna(row.get("PIM - Sport")) and "Bike Shoes" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "FARM" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Z.N.E." in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Run 70s Shoes" in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Run 80s Shoes" in str(row.get("Name", "")).lower() else
        "Cycling" if pd.isna(row.get("PIM - Sport")) and "The Gravel Cycling" in str(row.get("Name", "")).lower() else
        "Soccer" if pd.isna(row.get("PIM - Sport")) and any(team.lower() in str(row.get("Name", "")).lower() for team in [
            "Atlanta United", "Austin FC", "CF Montreal", "Charlotte FC", "Chicago Fire", "Colorado Rapids",
            "Columbus Crew", "D.C. United", "FC Cincinnati", "FC Dallas", "Houston Dynamo", "Inter Miami CF",
            "LA Galaxy", "LAFC", "Los Angeles FC", "Manchester United", "Minnesota United", "Nashville SC",
            "New England Revolution", "New York City FC", "New York Red Bulls", "Orlando City", "Philadelphia Union",
            "Real Madrid", "Portland Timbers", "Real Salt Lake", "San Jose Earthquakes", "Seattle Sounders FC",
            "Sporting Kansas City", "St. Louis CITY FC", "Toronto FC", "Vancouver Whitecaps",
            "Jamaica Beckenbauer", "Lightning Third", "Los Angeles Football Club", "Montreal Impact",
            "Orlando City SC", "Seattle Sounders", "ST Louis City SC", "AFC Ajax", "Washington Huskies",
            "Benfica", "Celtic FC", "FC Bayern Munich", "Newcastle United FC", "Olympique Lyonnais", "Arsenal"
        ]) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ZNSORED High" in str(row.get("Name", "")).lower() else
        "Training;Weightlifting" if pd.isna(row.get("PIM - Sport")) and "Dropset" in str(row.get("Name", "")).lower() else
        "Weightlifting" if pd.isna(row.get("PIM - Sport")) and "The Total" in str(row.get("Name", "")).lower() else
        "Basketball;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Fear of God Athletics" in str(row.get("PIM - Label", "")).lower() else
        "Skateboarding;Lifestyle" if pd.isna(row.get("PIM - Sport")) and any(name.lower() in str(row.get("Name", "")).lower() for name in [
            "Samba ADV", "Superstar ADV", "Stan Smith ADV", "Centennial 85 Low ADV",
            "Gazelle ADV", "Pro Model 80 ADV", "Campus ADV"
        ]) else
        row.get("PIM - Sport")
    ), axis=1)
    df["Enriched Activity"] = df.apply(lambda row: (
        "Outdoor;Athletic" if "Hellcat" in str(row.get("Name", "")).lower() else
        "Outdoor;Athletic" if "Terrex" in str(row.get("Name", "")).lower() else
        "Premium" if "Y-3" in str(row.get("PIM - Label", "")).lower() else
        "Premium" if "Fear of God Athletics" in str(row.get("PIM - Label", "")).lower() else
        "Premium" if "adidas by Stella McCartney" in str(row.get("PIM - Label", "")).lower() else
        "Premium" if "Y-3" in str(row.get("Name", "")).lower() else
        "Premium" if "Fear of God" in str(row.get("Name", "")).lower() else
        "Premium" if "100 Thieves" in str(row.get("Name", "")).lower() else
        "Premium" if "Avavav" in str(row.get("Name", "")).lower() else
        "Premium" if "Sporty & Rich" in str(row.get("Name", "")).lower() else
        "Premium" if "Dime" in str(row.get("Name", "")).lower() else
        "Premium" if "Bape" in str(row.get("Name", "")).lower() else
        "Premium" if "Song For The Mute" in str(row.get("Name", "")).lower() else
        "Premium" if "Bad Bunny" in str(row.get("Name", "")).lower() else
        "Premium" if "SPZL" in str(row.get("Name", "")).lower() else
        "Premium" if "Dingyun Zhang" in str(row.get("Name", "")).lower() else
        "Premium" if "Edison Chen" in str(row.get("Name", "")).lower() else
        "Premium" if "SFTM" in str(row.get("Name", "")).lower() else
        "Premium" if "EQT" in str(row.get("Name", "")).lower() else
        "Premium" if "Equipment" in str(row.get("Name", "")).lower() else
        "Premium" if "Korn" in str(row.get("Name", "")).lower() else
        "Premium" if "JJJJound" in str(row.get("Name", "")).lower() else
        "Premium" if "Wales Bonner" in str(row.get("Name", "")).lower() else
        "Premium" if "Willy Chavarria" in str(row.get("Name", "")).lower() else
        "Premium" if "Brain Dead" in str(row.get("Name", "")).lower() else
        "Premium" if "Jabbar" in str(row.get("Name", "")).lower() else
        "Premium" if "Pharrell" in str(row.get("Name", "")).lower() else
        "Premium" if "CP Company" in str(row.get("Name", "")).lower() else
        "Premium" if "Minecraft" in str(row.get("Name", "")).lower() else
        "Premium" if "Fortnite" in str(row.get("Name", "")).lower() else
        "Premium" if "BW Army" in str(row.get("Name", "")).lower() else
        "Premium" if "Spongebob" in str(row.get("Name", "")).lower() else
        "Premium" if "NTS Radio" in str(row.get("Name", "")).lower() else
        "Premium" if "Rolling Links" in str(row.get("Name", "")).lower() else
        row.get("")
    ), axis=1)
    df["Enriched Pattern"] = df.apply(lambda row: (
        "All Over Print" if pd.isna(row.get("PIM - Pattern")) and "All Over Print" in str(row.get("Name", "")).lower() else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Animal" in str(row.get("Name", "")).lower() else
        "Camo" if pd.isna(row.get("PIM - Pattern")) and "Camo" in str(row.get("Name", "")).lower() else
        "Camo" if pd.isna(row.get("PIM - Pattern")) and "Camouflage" in str(row.get("Name", "")).lower() else
        "Graphic Print" if pd.isna(row.get("PIM - Pattern")) and "Graphic" in str(row.get("Name", "")).lower() else
        "Floral" if pd.isna(row.get("PIM - Pattern")) and "Floral" in str(row.get("Name", "")).lower() else
        "Floral" if pd.isna(row.get("PIM - Pattern")) and "Flower" in str(row.get("Name", "")).lower() else
        "Polka Dots" if pd.isna(row.get("PIM - Pattern")) and "Dots" in str(row.get("Name", "")).lower() else
        "Polka Dots" if pd.isna(row.get("PIM - Pattern")) and "Polka Dots" in str(row.get("Name", "")).lower() else
        "Tie Dye" if pd.isna(row.get("PIM - Pattern")) and "Tie-Dye" in str(row.get("Name", "")).lower() else
        "Tie Dye" if pd.isna(row.get("PIM - Pattern")) and "Tie Dye" in str(row.get("Name", "")).lower() else
        "Metallic" if pd.isna(row.get("PIM - Pattern")) and "Metallic" in str(row.get("Name", "")).lower() else
        "Flames" if pd.isna(row.get("PIM - Pattern")) and "Flame" in str(row.get("Name", "")).lower() else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Leopard" in str(row.get("Name", "")).lower() else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Zebra" in str(row.get("Name", "")).lower() else
        "Embroidery" if pd.isna(row.get("PIM - Pattern")) and "Embroidered" in str(row.get("Name", "")).lower() else
        "Logo Print" if pd.isna(row.get("PIM - Pattern")) and "LOGO" in str(row.get("Name", "")).lower() else
        "Glitter" if pd.isna(row.get("PIM - Pattern")) and "Glitter" in str(row.get("Name", "")).lower() else
        "Glitter" if pd.isna(row.get("PIM - Pattern")) and "Rhinestones" in str(row.get("Name", "")).lower() else
        "Logo Print" if pd.isna(row.get("PIM - Pattern")) and "Logo" in str(row.get("Name", "")).lower() else
        "Crochet" if pd.isna(row.get("PIM - Pattern")) and "Crochet" in str(row.get("Name", "")).lower() else
        "Colorblock" if pd.isna(row.get("PIM - Pattern")) and "Colorblock" in str(row.get("Name", "")).lower() else
        "Color Block" if pd.isna(row.get("PIM - Pattern")) and "Color block" in str(row.get("Name", "")).lower() else
        "Plaid" if pd.isna(row.get("PIM - Pattern")) and "Plaid" in str(row.get("Name", "")).lower() else
        row.get("PIM - Pattern")
    ), axis=1)
    df["Enriched Base Material"] = df.apply(lambda row: (
        "Fleece" if pd.isna(row.get("PIM - Base Material")) and "ALL SZN" in str(row.get("Name", "")).lower() else
        "Nuganic" if pd.isna(row.get("PIM - Base Material")) and "Nuganic" in str(row.get("Name", "")).lower() else
        "Denim" if pd.isna(row.get("PIM - Base Material")) and "Denim" in str(row.get("Name", "")).lower() else
        "Satin" if pd.isna(row.get("PIM - Base Material")) and "Satin" in str(row.get("Name", "")).lower() else
        "Velour;Velvet" if pd.isna(row.get("PIM - Base Material")) and (
            "Velour" in str(row.get("Name", "")).lower() or "Velvet" in str(row.get("Name", "")).lower()
        ) else
        "Piqué" if pd.isna(row.get("PIM - Base Material")) and "Pique" in str(row.get("Name", "")).lower() else
        "Microfiber" if pd.isna(row.get("PIM - Base Material")) and "Microfiber" in str(row.get("Name", "")).lower() else
        "Wool" if pd.isna(row.get("PIM - Base Material")) and "Wool" in str(row.get("Name", "")).lower() else
        "Molded" if pd.isna(row.get("PIM - Base Material")) and "Molded" in str(row.get("Name", "")).lower() else
        "Cashmere" if pd.isna(row.get("PIM - Base Material")) and "Cashmere" in str(row.get("Name", "")).lower() else
        "Twistknit" if pd.isna(row.get("PIM - Base Material")) and "Twistknit" in str(row.get("Name", "")).lower() else
        "Recycled Polyester" if pd.isna(row.get("PIM - Base Material")) and
        "Soccer" in str(row.get("PIM - Sport", "")).lower() and (
                "Jerseys" in str(row.get("PIM adidas - Product Types", "")).lower() or
                "Jerseys - Long Sleeve" in str(row.get("PIM adidas - Product Types", "")).lower() or
                "Gloves - Goalkeeper" in str(row.get("PIM adidas - Product Types", "")).lower()
            ) else
        "Cotton" if pd.isna(row.get("PIM - Base Material")) and
            "Soccer" in str(row.get("PIM - Sport", "")).lower() and
            "Shorts" in str(row.get("PIM adidas - Product Types", "")).lower() and (
                "Tiro 24 Sweat Shorts" in str(row.get("Name", "")).lower() or
                "Tiro 24 Shorts" in str(row.get("Name", "")).lower()
            ) else
        "Cotton" if pd.isna(row.get("PIM - Base Material")) and
            "Soccer" in str(row.get("PIM - Sport", "")).lower() and
            "T Shirts" in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Twistweave" if pd.isna(row.get("PIM - Base Material")) and "Twistweave" in str(row.get("Name", "")).lower() else
        row.get("PIM - Base Material")
    ), axis=1)
    df["Enriched Partner"] = df.apply(lambda row: (
        "Disney" if pd.isna(row.get("PIM - Partner")) and "Disney" in str(row.get("Name", "")).lower() else
        "Disney; Star Wars" if pd.isna(row.get("PIM - Partner")) and "Star Wars" in str(row.get("Name", "")).lower() else
        "Disney;Mickey" if pd.isna(row.get("PIM - Partner")) and "Mickey" in str(row.get("Name", "")).lower() else
        "Disney;Moana" if pd.isna(row.get("PIM - Partner")) and "Moana" in str(row.get("Name", "")).lower() else
        "Farm" if pd.isna(row.get("PIM - Partner")) and "FARM" in str(row.get("Name", "")).lower() else
        "UEFA Champions League;Club" if pd.isna(row.get("PIM - Partner")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Juventus", "Manchester United", "Real Madrid", "AFC Ajax"
        ]) else
        "Stella McCartney" if pd.isna(row.get("PIM - Partner")) and "Stella McCartney" in str(row.get("Name", "")).lower() else
        "LEGO" if pd.isna(row.get("PIM - Partner")) and "Lego" in str(row.get("Name", "")).lower() else
        "Marimekko" if pd.isna(row.get("PIM - Partner")) and "Marimekko" in str(row.get("Name", "")).lower() else
        "Disney;Marvel" if pd.isna(row.get("PIM - Partner")) and "Marvel" in str(row.get("Name", "")).lower() else
        "Parley" if pd.isna(row.get("PIM - Partner")) and "Parley" in str(row.get("Name", "")).lower() else
        "MLS" if pd.isna(row.get("PIM - Partner")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Atlanta United", "Austin FC", "CF Montreal", "Charlotte FC", "Chicago Fire", "Colorado Rapids",
            "Columbus Crew", "D.C. United", "FC Cincinnati", "FC Dallas", "Houston Dynamo", "Inter Miami CF",
            "LA Galaxy", "LAFC", "Los Angeles FC", "Minnesota United", "Nashville SC", "New England Revolution",
            "New York City FC", "New York Red Bulls", "Orlando City", "Philadelphia Union", "Portland Timbers",
            "Real Salt Lake", "San Jose Earthquakes", "Seattle Sounders FC", "Sporting Kansas City",
            "St. Louis CITY FC", "Toronto FC", "Vancouver Whitecaps", "Jamaica Beckenbauer", "Lightning Third",
            "Los Angeles Football Club", "Montreal Impact", "Orlando City SC", "Seattle Sounders",
            "ST Louis City SC", "Washington Huskies"
        ]) else
        "Club" if pd.isna(row["PIM - Partner"]) and "Benfica" in str(row.get("Name", "")).lower() else
        "UEFA Champions League;Club" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Celtic FC", "FC Bayern Munich", "Olympique Lyonnais", "Arsenal"
        ]) else
        "Club" if pd.isna(row["PIM - Partner"]) and "Newcastle United FC" in str(row.get("Name", "")).lower() else
        "SPZL" if pd.isna(row["PIM - Partner"]) and "SPZL" in str(row.get("Name", "")).lower() else
        "Andre Saravia" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["André Saraiva", "Andre Saraiva"]) else
        "Edison Chen" if pd.isna(row["PIM - Partner"]) and "Edison Chen" in str(row.get("Name", "")).lower() else
        "Y 3" if pd.isna(row["PIM - Partner"]) and "Y-3" in str(row.get("Name", "")).lower() else
        "Bad Bunny" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Bad Bunny", "Ballerina"]) else
        "KseniaSchnaider" if pd.isna(row["PIM - Partner"]) and "KSENIASCHNAIDER" in str(row.get("Name", "")).lower() else
        "BAPE" if pd.isna(row["PIM - Partner"]) and "BAPE" in str(row.get("Name", "")).lower() else
        "Pop Trading Company" if pd.isna(row["PIM - Partner"]) and "Pop Trading Co" in str(row.get("Name", "")).lower() else
        "Wales Bonner" if pd.isna(row["PIM - Partner"]) and "Wales Bonner" in str(row.get("Name", "")).lower() else
        "Pharrell" if pd.isna(row["PIM - Partner"]) and "Pharrell Williams" in str(row.get("Name", "")).lower() else
        "100 Thieves" if pd.isna(row["PIM - Partner"]) and "100 Thieves" in str(row.get("Name", "")).lower() else
        "Korn" if pd.isna(row["PIM - Partner"]) and "Korn" in str(row.get("Name", "")).lower() else
        "UEFA Champions League" if pd.isna(row["PIM - Partner"]) and "UCL" in str(row.get("Name", "")).lower() else
        "UEFA EURO" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Euro 24", "Fussballliebe"]) else
        "Deadpool;Marvel" if pd.isna(row["PIM - Partner"]) and "Deadpool" in str(row.get("Name", "")).lower() else
        "Yeezy" if pd.isna(row["PIM - Partner"]) and "Yeezy" in str(row.get("Name", "")).lower() else
        "Y3" if pd.isna(row["PIM - Partner"]) and "Y-3" in str(row.get("Name", "")).lower() else
        "Avavav" if pd.isna(row["PIM - Partner"]) and "Avavav" in str(row.get("Name", "")).lower() else
        "Club" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["AS Roma", "Boca Juniors"]) else
        "Lion King" if pd.isna(row["PIM - Partner"]) and "Lion King" in str(row.get("Name", "")).lower() else
        "Fortnite" if pd.isna(row["PIM - Partner"]) and "Fortnite" in str(row.get("Name", "")).lower() else
        "Teamgeist" if pd.isna(row["PIM - Partner"]) and "Teamgeist" in str(row.get("Name", "")).lower() else
        "Willy Chavarria" if pd.isna(row["PIM - Partner"]) and "Willy Chavarria" in str(row.get("Name", "")).lower() else
        "OG LA" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["OG L.A", "OG LA"]) else
        "College" if pd.isna(row["PIM - Partner"]) and (
            "Collegiate" in str(row.get("Name", "")).lower() or
            any(x.lower() in str(row.get("Name", "")).lower() for x in [
                "University of Louisville", "Texas A&M", "University of Kansas",
                "University of Miami", "University of Nebraska", "North Carolina State University",
                "Arizona State University", "Grambling State University", "Indiana University",
                "University of Washington", "NC State", "Nebraska", "New Zealand Rugby",
                "Texas Tech", "Hoosiers", "Huskies", "Georgia Tech", "Yellow Jackets",
                "Kansas Jayhawks", "Alcorn State", "Arkansas Pine Bluff",
                "Mississippi State University", "Alabama State"
            ]) or
            any(x.lower() in str(row.get("PIM - Teams", "")).lower() for x in [
                "Louisville Cardinals", "Texas A&M Aggies", "Kansas Jayhawks",
                "Miami Hurricanes", "Nebraska Cornhuskers", "North Carolina",
                "Arizona State University", "Grambling State Tigers", "Indiana Hoosiers",
                "Washington Huskies", "NC State Wolfpack", "All Blacks", "Texas Tech",
                "Georgia Tech", "Alcorn State Braves", "Arkansas-Pine Bluff Golden Lions",
                "Mississippi State Bulldogs", "Alabama State Hornets"
            ])
        ) else
        row.get("PIM - Partner")
    ), axis=1)
    df["Enriched Product Type"] = df.apply(lambda row: (
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Hellcat" in str(row.get("Name", "")).lower() else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Dame 8" in str(row.get("Name", "")).lower() else
        "Pants" if pd.isna(row["PIM adidas - Product Types"]) and "Pants" in str(row.get("Name", "")).lower() else
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Bike Shoes" in str(row.get("Name", "")).lower() else
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Cycling" in str(row.get("Name", "")).lower() else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Rivalry High" in str(row.get("Name", "")).lower() else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM adidas - Product Types"]) and "High Tops" in str(row["PIM adidas - Product Types"]) else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Run 70s Shoes" in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Run 80s Shoes" in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Puig" in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Samba" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Gazelle" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "SL 72" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Country" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.isna(row["PIM - Product Line (sportsub)"]) and "Originals" in str(row["PIM - Label"]) and "Handball Spezial" in str(row.get("Name", "")).lower() else
        "Slides;Platform" if pd.isna(row["PIM adidas - Product Types"]) and "Platform" in str(row.get("Name", "")).lower() and "Slides" in str(row["PIM adidas - Product Types"]) else
        "Boots" if pd.isna(row["PIM adidas - Product Types"]) and ("Boot" in str(row.get("Name", "")).lower() or "Boots" in str(row.get("Name", "")).lower()) else
        "Platform;Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Bold", "Platform", "XLG", "Sambae"]) else
        "Platform;Clogs" if pd.isna(row["PIM adidas - Product Types"]) and "Stan Smith Mule" in str(row.get("Name", "")).lower() else
        "Balls" if pd.isna(row["PIM adidas - Product Types"]) and "Ball" in str(row.get("Name", "")).lower() else
        "Vests" if pd.isna(row["PIM adidas - Product Types"]) and "Trail Running Vest" in str(row.get("Name", "")).lower() else
        "Belts" if pd.isna(row["PIM adidas - Product Types"]) and "Belt" in str(row.get("Name", "")).lower() else
        "Gloves;Gloves - Goalkeeper" if pd.isna(row["PIM adidas - Product Types"]) and "Goalkeeper Gloves" in str(row.get("Name", "")).lower() else
        "Gloves" if pd.isna(row["PIM adidas - Product Types"]) and "Gloves" in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers;High Tops" if pd.isna(row["PIM adidas - Product Types"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["forum high", "forum hi", "Nizza high"]) else
        "Athletic & Sneakers;Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and "Spezial" in str(row.get("Name", "")).lower() else
        "Pants;Track Suits - Track Pants;Track Suits" if pd.isna(row["PIM adidas - Product Types"]) and "Track Pants" in str(row.get("Name", "")).lower() else
        "Bags;Bags - Crossbody" if pd.isna(row["PIM adidas - Product Types"]) and "Crossbody Bag" in str(row.get("Name", "")).lower() else
        "Bag" if pd.isna(row["PIM adidas - Product Types"]) and "Bag" in str(row.get("Name", "")).lower() else
        "Bags;Bags - Duffle Bags" if pd.isna(row["PIM adidas - Product Types"]) and "Duffle Bag" in str(row.get("Name", "")).lower() else
        "Bags;Bags - Tote" if pd.isna(row["PIM adidas - Product Types"]) and "Tote Bag" in str(row.get("Name", "")).lower() else
        "Platform;Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Gazelle Stack" in str(row.get("Name", "")).lower() else
        row.get("PIM adidas - Product Types")
    ), axis=1)
    df["Enriched Surface"] = df.apply(lambda row: (
        "Multi Ground" if pd.isna(row["PIM - Surface"]) and "Multi ground" in str(row.get("Name", "")).lower() else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "trail running" in str(row["PIM - Sport"]).lower() else 
        "Gravel" if pd.isna(row["PIM - Surface"]) and "The Gravel Cycling" in str(row.get("Name", "")).lower() else 
        "Indoor" if pd.isna(row["PIM - Surface"]) and "THE INDOOR CYCLING SHOE" in str(row.get("Name", "")).lower() else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Originals" in str(row["PIM - Label"]).lower() and (
            "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]).lower() or 
            "Athletic & Sneakers - T Toe" in str(row["PIM adidas - Product Types"]).lower()) else 
        "Artificial Grass" if pd.isna(row["PIM - Surface"]) and "Artificial Grass" in str(row.get("Name", "")).lower() else 
        "Clay Court" if pd.isna(row["PIM - Surface"]) and "Clay" in str(row.get("Name", "")).lower() else 
        "Firm Ground" if pd.isna(row["PIM - Surface"]) and ("Firm Ground" in str(row.get("Name", "")).lower() or "FG" in str(row.get("Name", "")).lower()) else 
        "Soft Ground" if pd.isna(row["PIM - Surface"]) and "Soft Ground" in str(row.get("Name", "")).lower() else 
        "Gravel" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["The Gravel", "Five Ten"]) else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "Trailcross" in str(row.get("Name", "")).lower() else 
        "Turf" if pd.isna(row["PIM - Surface"]) and "Turf" in str(row.get("Name", "")).lower() else 
        "Indoor-Court" if pd.isna(row["PIM - Surface"]) and "Indoor" in str(row.get("Name", "")).lower() and "Soccer" in str(row["PIM - Sport"]).lower() else 
        "Road;Treadmill" if pd.isna(row["PIM - Surface"]) and "Running" in str(row["PIM - Sport"]).lower() and 
            "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]).lower() and any(x.lower() in str(row.get("Name", "")).lower() for x in [
                "4DFWD", "adizero", "Duramo", "Pureboost", "RDY", "Puremotion", "Rapida", "Response", "RunFalcon", 
                "Solar", "speedmotion", "Supernova", "Switch FWD", "Ultrabounce", "Tensaur", "X9000"]) else 
        "Track" if pd.isna(row["PIM - Surface"]) and "Track & Field" in str(row["PIM - Sport"]).lower() and "adizero" in str(row.get("Name", "")).lower() else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "Trail Running" in str(row["PIM - Sport"]).lower() and "Agravic" in str(row.get("Name", "")).lower() else 
        "Road" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Velosamba", "The Road", "Velostan Smith"]) else 
        "Hard Court" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row["PIM - Product Family (productlinestyle)"]).lower() for x in [
            "adizero Cybersonic", "adizero ubersonic"]) else 
        "Clay Court" if pd.isna(row["PIM - Surface"]) and "Tennis" in str(row["PIM - Sport"]).lower() and "Clay" in str(row.get("Name", "")).lower() else 
        "Hard Court" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row["PIM - Product Line (sportsub)"]).lower() for x in [
            "Barricade", "CourtJam", "Avacourt", "GameCourt"]) else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Fear of God Athletics" in str(row["PIM - Label"]).lower() and 
            "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]).lower() else 
        "Indoor-Court;Hard Court" if pd.isna(row["PIM - Surface"]) and "Cross Em" in str(row.get("Name", "")).lower() else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Running" in str(row["PIM - Sport"]).lower() and 
            "Originals" in str(row["PIM - Label"]) and "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]).lower() else 
        row.get("PIM - Surface")
    ), axis=1)
    df["Enriched Athletes"] = df.apply(lambda row: (
        "Ant Edwards" if pd.isna(row["PIM - Athletes"]) and "Anthony Edwards" in str(row.get("Name", "")).lower() else 
        "Donovan Mitchell" if pd.isna(row["PIM - Athletes"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "D.O.N", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8", "D.O.N. Issue 5"]) else 
        "Damian Lillard" if pd.isna(row["PIM - Athletes"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Dame 8", "Dame"]) else 
        "Lionel Messi" if pd.isna(row["PIM - Athletes"]) and "Messi" in str(row.get("Name", "")).lower() else 
        "Trae Young" if pd.isna(row["PIM - Athletes"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Trae", "Trae Young", "Trae Unlimited"]) else 
        "James Harden" if pd.isna(row["PIM - Athletes"]) and "Harden" in str(row.get("Name", "")).lower() else 
        "Tyshawn Jones" if pd.isna(row["PIM - Athletes"]) and "Tyshawn" in str(row.get("Name", "")).lower() else 
        "Dennis Busenitz" if pd.isna(row["PIM - Athletes"]) and "Busenitz" in str(row.get("Name", "")).lower() else 
        "Lucas Puig" if pd.isna(row["PIM - Athletes"]) and "puig" in str(row.get("Name", "")).lower() else 
        "Mark Gonzalez" if pd.isna(row["PIM - Athletes"]) and (
            "shmoofoil" in str(row.get("Name", "")).lower() or "shmoofoil" in str(row["PIM - Product Line (sportsub)"]).lower() or 
            "Gonz" in str(row.get("Name", "")).lower() or "aloha Super" in str(row.get("Name", "")).lower() or "aloha Super" in str(row["PIM - Product Line (sportsub)"]).lower()) else 
        "Patrick Mahomes" if pd.isna(row["PIM - Athletes"]) and "Mahomes" in str(row.get("Name", "")).lower() else 
        "Nora Vasconcellos" if pd.isna(row["PIM - Athletes"]) and "Nora " in str(row.get("Name", "")).lower() else 
        "Heitor Da Silva" if pd.isna(row["PIM - Athletes"]) and "Pro Shell ADV x Heitor" in str(row.get("Name", "")).lower() else 
        "Kader Sylla" if pd.isna(row["PIM - Athletes"]) and "Kader" in str(row.get("Name", "")).lower() else 
        "Henry Jones" if pd.isna(row["PIM - Athletes"]) and "Henry Jones" in str(row.get("Name", "")).lower() else 
        "Jude Bellingham" if pd.isna(row["PIM - Athletes"]) and "Jude Bellingham" in str(row.get("Name", "")).lower() else 
        "Lamine Yamal" if pd.isna(row["PIM - Athletes"]) and "Lamine" in str(row.get("Name", "")).lower() else 
        "George Russell" if pd.isna(row["PIM - Athletes"]) and "George Russell" in str(row.get("Name", "")).lower() else 
        "Kimi Antonelli" if pd.isna(row["PIM - Athletes"]) and "Kimi Antonelli" in str(row.get("Name", "")).lower() else 
        row.get("PIM - Athletes")
    ), axis=1)
    df["Enriched Teams"] = df.apply(lambda row: (
        "Atlanta United" if pd.isna(row["PIM - Teams"]) and "Atlanta United" in str(row.get("Name", "")).lower() else 
        "Austin FC" if pd.isna(row["PIM - Teams"]) and "Austin FC" in str(row.get("Name", "")).lower() else 
        "CF Montreal" if pd.isna(row["PIM - Teams"]) and "CF Montreal" in str(row.get("Name", "")).lower() else 
        "Charlotte FC" if pd.isna(row["PIM - Teams"]) and "Charlotte FC" in str(row.get("Name", "")).lower() else 
        "Chicago Fire" if pd.isna(row["PIM - Teams"]) and "Chicago Fire" in str(row.get("Name", "")).lower() else 
        "Colorado Rapids" if pd.isna(row["PIM - Teams"]) and "Colorado Rapids" in str(row.get("Name", "")).lower() else 
        "Columbus Crew" if pd.isna(row["PIM - Teams"]) and "Columbus Crew" in str(row.get("Name", "")).lower() else 
        "D.C. United" if pd.isna(row["PIM - Teams"]) and "D.C. United" in str(row.get("Name", "")).lower() else 
        "Cincinnati FC" if pd.isna(row["PIM - Teams"]) and "FC Cincinnati" in str(row.get("Name", "")).lower() else 
        "Dallas FC" if pd.isna(row["PIM - Teams"]) and "FC Dallas" in str(row.get("Name", "")).lower() else 
        "Houston Dynamo" if pd.isna(row["PIM - Teams"]) and "Houston Dynamo" in str(row.get("Name", "")).lower() else 
        "Inter Miami CF" if pd.isna(row["PIM - Teams"]) and "Inter Miami CF" in str(row.get("Name", "")).lower() else 
        "Los Angeles Football Club" if pd.isna(row["PIM - Teams"]) and ("Los Angeles Football Club" in str(row.get("Name", "")).lower() or "Los Angeles FC" in str(row.get("Name", "")).lower()) else 
        "Manchester United" if pd.isna(row["PIM - Teams"]) and "Manchester United" in str(row.get("Name", "")).lower() else 
        "Minnesota United" if pd.isna(row["PIM - Teams"]) and "Minnesota United" in str(row.get("Name", "")).lower() else 
        "Nashville SC" if pd.isna(row["PIM - Teams"]) and "Nashville SC" in str(row.get("Name", "")).lower() else 
        "New England Revolution" if pd.isna(row["PIM - Teams"]) and "New England Revolution" in str(row.get("Name", "")).lower() else 
        "New York City FC" if pd.isna(row["PIM - Teams"]) and "New York City FC" in str(row.get("Name", "")).lower() else 
        "New York Red Bulls" if pd.isna(row["PIM - Teams"]) and "New York Red Bulls" in str(row.get("Name", "")).lower() else 
        "Orlando City SC" if pd.isna(row["PIM - Teams"]) and "Orlando City SC" in str(row.get("Name", "")).lower() else 
        "Philadelphia Union" if pd.isna(row["PIM - Teams"]) and "Philadelphia Union" in str(row.get("Name", "")).lower() else 
        "Real Madrid" if pd.isna(row["PIM - Teams"]) and "Real Madrid" in str(row.get("Name", "")).lower() else 
        "Portland Timbers" if pd.isna(row["PIM - Teams"]) and "Portland Timbers" in str(row.get("Name", "")).lower() else 
        "Real Salt Lake" if pd.isna(row["PIM - Teams"]) and "Real Salt Lake" in str(row.get("Name", "")).lower() else 
        "San Jose Earthquakes" if pd.isna(row["PIM - Teams"]) and "San Jose Earthquakes" in str(row.get("Name", "")).lower() else 
        "Seattle Sounders FC" if pd.isna(row["PIM - Teams"]) and "Seattle Sounders FC" in str(row.get("Name", "")).lower() else 
        "Sporting Kansas City" if pd.isna(row["PIM - Teams"]) and "Sporting Kansas City" in str(row.get("Name", "")).lower() else 
        "St Louis City SC" if pd.isna(row["PIM - Teams"]) and "St Louis CITY SC" in str(row.get("Name", "")).lower() else 
        "Toronto FC" if pd.isna(row["PIM - Teams"]) and "Toronto FC" in str(row.get("Name", "")).lower() else 
        "Vancouver Whitecaps" if pd.isna(row["PIM - Teams"]) and "Vancouver Whitecaps" in str(row.get("Name", "")).lower() else 
        "Jamaica" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Jamaica Beckenbauer", "Jamaica OG", "Jamaica"]) else 
        "Tampa Bay Lightning" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Lightning Third", "Tampa Bay"]) else 
        "Arsenal" if pd.isna(row["PIM - Teams"]) and "Arsenal" in str(row.get("Name", "")).lower() else 
        "Juventus" if pd.isna(row["PIM - Teams"]) and "Juventus" in str(row.get("Name", "")).lower() else 
        "Argentina" if pd.isna(row["PIM - Teams"]) and "Argentina" in str(row.get("Name", "")).lower() else 
        "Spain" if pd.isna(row["PIM - Teams"]) and "Spain" in str(row.get("Name", "")).lower() else 
        "Schalke 04" if pd.isna(row["PIM - Teams"]) and "FC Schalke" in str(row.get("Name", "")).lower() else 
        "Scotland" if pd.isna(row["PIM - Teams"]) and "Scotland 24" in str(row.get("Name", "")).lower() else 
        "Italy" if pd.isna(row["PIM - Teams"]) and "Italy" in str(row.get("Name", "")).lower() else 
        "Celtic FC" if pd.isna(row["PIM - Teams"]) and "Celtic FC" in str(row.get("Name", "")).lower() else 
        "Sweden" if pd.isna(row["PIM - Teams"]) and "Sweden" in str(row.get("Name", "")).lower() else 
        "Algeria" if pd.isna(row["PIM - Teams"]) and "Algeria 22" in str(row.get("Name", "")).lower() else 
        "FC Girondins Bordeaux" if pd.isna(row["PIM - Teams"]) and "Girondins de Bordeaux" in str(row.get("Name", "")).lower() else 
        "Hungary" if pd.isna(row["PIM - Teams"]) and "Hungary 24" in str(row.get("Name", "")).lower() else 
        "Colombia" if pd.isna(row["PIM - Teams"]) and "Colombia 24" in str(row.get("Name", "")).lower() else 
        "FC Nürnberg" if pd.isna(row["PIM - Teams"]) and "FC Nürnberg" in str(row.get("Name", "")).lower() else 
        "Leeds United FC" if pd.isna(row["PIM - Teams"]) and "Leeds United FC" in str(row.get("Name", "")).lower() else 
        "Black Ferns" if pd.isna(row["PIM - Teams"]) and "Black Ferns" in str(row.get("Name", "")).lower() else 
        "Mexico" if pd.isna(row["PIM - Teams"]) and "Mexico" in str(row.get("Name", "")).lower() else 
        "Fulham FC" if pd.isna(row["PIM - Teams"]) and "Fulham FC" in str(row.get("Name", "")).lower() else 
        "Racing Club de Strasbourg" if pd.isna(row["PIM - Teams"]) and "RC Strasbourg" in str(row.get("Name", "")).lower() else 
        "AS Roma" if pd.isna(row["PIM - Teams"]) and "AS Roma" in str(row.get("Name", "")).lower() else 
        "Belgium" if pd.isna(row["PIM - Teams"]) and "Belgium" in str(row.get("Name", "")).lower() else 
        "Wales" if pd.isna(row["PIM - Teams"]) and "Wales 24" in str(row.get("Name", "")).lower() else 
        "All Blacks" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["All Blacks", "New Zealand Rugby"]) else 
        "FC Union Berlin" if pd.isna(row["PIM - Teams"]) and "FC Union Berlin" in str(row.get("Name", "")).lower() else 
        "Hamburger SV" if pd.isna(row["PIM - Teams"]) and "Hamburger SV" in str(row.get("Name", "")).lower() else 
        "Northern Ireland" if pd.isna(row["PIM - Teams"]) and "Northern Ireland" in str(row.get("Name", "")).lower() else 
        "France" if pd.isna(row["PIM - Teams"]) and "France" in str(row.get("Name", "")).lower() else 
        "Germany" if pd.isna(row["PIM - Teams"]) and "Germany" in str(row.get("Name", "")).lower() else 
        "LA Galaxy" if pd.isna(row["PIM - Teams"]) and "LA Galaxy" in str(row.get("Name", "")).lower() else 
        "Olympique Lyon" if pd.isna(row["PIM - Teams"]) and "Olympique Lyonnais" in str(row.get("Name", "")).lower() else 
        "Chile" if pd.isna(row["PIM - Teams"]) and "Chile 24" in str(row.get("Name", "")).lower() else 
        "Leicester City" if pd.isna(row["PIM - Teams"]) and "Leicester City FC" in str(row.get("Name", "")).lower() else 
        "AFC Ajax" if pd.isna(row["PIM - Teams"]) and "Ajax" in str(row.get("Name", "")).lower() else 
        "Boca Juniors" if pd.isna(row["PIM - Teams"]) and "Boca Juniors" in str(row.get("Name", "")).lower() else 
        "FC Bayern Munich" if pd.isna(row["PIM - Teams"]) and "FC Bayern" in str(row.get("Name", "")).lower() else 
        "San Diego FC" if pd.isna(row["PIM - Teams"]) and "San Diego FC" in str(row.get("Name", "")).lower() else 
        "Tigres" if pd.isna(row["PIM - Teams"]) and "Tigres UANL" in str(row.get("Name", "")).lower() else 
        "Arsenal FC" if pd.isna(row["PIM - Teams"]) and "AFC " in str(row.get("Name", "")).lower() else 
        "Louisville Cardinals" if pd.isna(row["PIM - Teams"]) and "University of Louisville" in str(row.get("Name", "")).lower() else 
        "Texas A&M Aggies" if pd.isna(row["PIM - Teams"]) and "Texas A&M" in str(row.get("Name", "")).lower() else 
        "Kansas Jayhawks" if pd.isna(row["PIM - Teams"]) and "University of Kansas" in str(row.get("Name", "")).lower() else 
        "Miami Hurricanes" if pd.isna(row["PIM - Teams"]) and "University of Miami" in str(row.get("Name", "")).lower() else 
        "Nebraska Cornhuskers" if pd.isna(row["PIM - Teams"]) and ("University of Nebraska" in str(row.get("Name", "")).lower() or "Nebraska" in str(row.get("Name", "")).lower()) else 
        "Mercedes AMG Petronas Formula One Team" if pd.isna(row["PIM - Teams"]) and "Motorsport" in str(row["PIM - Sport"]).lower() and "Mercedes" in str(row.get("Name", "")).lower() else 
        "NC State Wolfpack" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["North Carolina State University", "NC State"]) else 
        "Arizona State University" if pd.isna(row["PIM - Teams"]) and "Arizona State University" in str(row.get("Name", "")).lower() else 
        "Grambling State Tigers" if pd.isna(row["PIM - Teams"]) and "Grambling State University" in str(row.get("Name", "")).lower() else 
        "Indiana Hoosiers" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Indiana University", "Hoosiers"]) else 
        "Washington Huskies" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["University of Washington", "Huskies"]) else 
        "Georgia Tech" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Yellow Jackets", "Georgia Tech"]) else 
        "Alcorn State Braves" if pd.isna(row["PIM - Teams"]) and "Alcorn State" in str(row.get("Name", "")).lower() else 
        "Arkansas-Pine Bluff Golden Lions" if pd.isna(row["PIM - Teams"]) and "Arkansas Pine Bluff" in str(row.get("Name", "")).lower() else 
        "Alabama State Hornets" if pd.isna(row["PIM - Teams"]) and "Alabama State" in str(row.get("Name", "")).lower() else 
        "Georgia Tech" if pd.isna(row["PIM - Teams"]) and "Georgia Tech" in str(row.get("Name", "")).lower() else 
        row.get("PIM - Teams")
    ), axis=1)
    df["Enriched Team Kits"] = df.apply(lambda row: (
        "Home Kit" if pd.isna(row.get("PIM - Team Kits")) and "Home" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Home Kit" if pd.isna(row.get("PIM - Team Kits")) and "Home" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit" if pd.isna(row.get("PIM - Team Kits")) and "Away" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit" if pd.isna(row.get("PIM - Team Kits")) and "Away" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")).lower() else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")).lower() else
        "Pre-Match" if pd.isna(row.get("PIM - Team Kits")) and "Pre-Match" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Pre-Match" if pd.isna(row.get("PIM - Team Kits")) and "Pre-Match" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")).lower() else
        "Home Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Authentic Home" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Authentic Away" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Home Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "AU Home" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "AU Away" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Fourth Kit" if pd.isna(row.get("PIM - Team Kits")) and "Fourth" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Fourth Kit" if pd.isna(row.get("PIM - Team Kits")) and "Fourth" in str(row.get("Name", "")) and "Lifestyle" in str(row.get("PIM - Sport", "")).lower() else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Driver" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "Driver" in str(row.get("Name", "")).lower() else
        "Mechanic" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "mechanics" in str(row.get("Name", "")).lower() else
        "Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "authentic" in str(row.get("Name", "")).lower() else
        "Replica" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "replica" in str(row.get("Name", "")).lower() else
        row.get("PIM - Team Kits")
    ), axis=1)
    df["Enriched Technologies"] = df.apply(lambda row: (
        "COLD.RDY" if pd.isna(row.get("PIM - Technologies")) and "COLD.RDY" in str(row.get("Name", "")).lower() else
        "HEAT.RDY" if pd.isna(row.get("PIM - Technologies")) and "HEAT.RDY" in str(row.get("Name", "")).lower() else
        "RAIN.RDY" if pd.isna(row.get("PIM - Technologies")) and "RAIN.RDY" in str(row.get("Name", "")).lower() else
        "SUMMER.RDY" if pd.isna(row.get("PIM - Technologies")) and "SUMMER.RDY" in str(row.get("Name", "")).lower() else
        "WIND.RDY" if pd.isna(row.get("PIM - Technologies")) and "WIND.RDY" in str(row.get("Name", "")).lower() else
        "GORE-TEX" if pd.isna(row.get("PIM - Technologies")) and "Gore-tex" in str(row.get("Name", "")).lower() else
        "GORE-TEX" if pd.isna(row.get("PIM - Technologies")) and "GTX" in str(row.get("Name", "")).lower() else
        "AEROREADY" if pd.isna(row.get("PIM - Technologies")) and "AEROREADY" in str(row.get("Name", "")).lower() else
        "4D" if pd.isna(row.get("PIM - Technologies")) and "4D" in str(row.get("Name", "")).lower() else
        "Boost" if pd.isna(row.get("PIM - Technologies")) and "Boost" in str(row.get("Name", "")).lower() else
        "Bounce" if pd.isna(row.get("PIM - Technologies")) and "Bounce" in str(row.get("Name", "")).lower() else
        "Dreamstrike" if pd.isna(row.get("PIM - Technologies")) and "Supernova" in str(row.get("Name", "")).lower() else
        "Techfit" if pd.isna(row.get("PIM - Technologies")) and "Techfit" in str(row.get("Name", "")).lower() else
        "WINTER.RDY" if pd.isna(row.get("PIM - Technologies")) and "WINTER.RDY" in str(row.get("Name", "")).lower() else
        "CORDURA" if pd.isna(row.get("PIM - Technologies")) and "CORDURA" in str(row.get("Name", "")).lower() else
        "PrimaLoft;EVA" if pd.isna(row.get("PIM - Technologies")) and "PUFFYLETTE" in str(row.get("Name", "")).lower() else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "SL 72" in str(row.get("Name", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Ultraboost 5" in str(row.get("Name", "")).lower() else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "Country" in str(row.get("Name", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Anthony Edwards" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "D.O.N" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Trae Young" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Bounce" if pd.isna(row.get("PIM - Technologies")) and "Tech Response" in str(row.get("Name", "")).lower() else
        "Torsion" if pd.isna(row.get("PIM - Technologies")) and "Avacourt" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Bounce;Torsion" if pd.isna(row.get("PIM - Technologies")) and "Courtjam Control" in str(row.get("Name", "")).lower() else
        "Bounce;EVA" if pd.isna(row.get("PIM - Technologies")) and "GameCourt" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Torsion;Boost" if pd.isna(row.get("PIM - Technologies")) and "SoleMatch" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "Country Soft" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Cloudfoam" if pd.isna(row.get("PIM - Technologies")) and "RunFalcon" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "PrimaLoft" if pd.isna(row.get("PIM - Technologies")) and "PrimaLoft" in str(row.get("Name", "")).lower() else
        row.get("PIM - Technologies")
    ), axis=1)
    df["Enriched Features"] = df.apply(lambda row: (
        "Lightweight;Cushioned" if pd.isna(row.get("PIM - Features")) and "SL 72" in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Cushion" in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Ozmillen" in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Water-Repellent;Cushioned" if pd.isna(row.get("PIM - Features")) and "Puffylette" in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "EVA" in str(row.get("PIM - Technologies", "")).lower() else
        "Spikeless" if pd.isna(row.get("PIM - Features")) and "Spikeless" in str(row.get("Name", "")).lower() else
        "Waterproof;Breathable" if pd.isna(row.get("PIM - Features")) and "GORE-TEX" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "LIGHTSTRIKE PRO" in str(row.get("PIM - Technologies", "")).lower() else
        "Pleated" if pd.isna(row.get("PIM - Features")) and "Pleated" in str(row.get("Name", "")).lower() else
        "Reversible" if pd.isna(row.get("PIM - Features")) and "Reversible" in str(row.get("Name", "")).lower() else
        "Cushioned;Lightweight" if pd.isna(row.get("PIM - Features")) and "GameCourt" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Lo profile" in str(row.get("Name", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Taekwondo" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Japan OG" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Tokyo" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Lightstrike" if pd.isna(row.get("PIM - Features")) and "D.O.N" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Bounce" if pd.isna(row.get("PIM - Features")) and "Dame" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Boost;Lightstrike" if pd.isna(row.get("PIM - Features")) and "Harden" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Boost;Lightstrike" if pd.isna(row.get("PIM - Features")) and "Anthony Edwards" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "4D" in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "AEROREADY" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Boost" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Bounce" in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climachill" in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climacool" in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climacool " in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climaheat" in str(row.get("PIM - Technologies", "")).lower() else
        "Breathable;Windproof;Water-Repellent;Waterproof" if pd.isna(row.get("PIM - Features")) and "Climaproof" in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climawarm" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Cloudfoam" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "CLOUDFOAM PLUS" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Dreamstrike" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Dreamstrike+" in str(row.get("PIM - Technologies", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and "Energyrods" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "EVA" in str(row.get("PIM - Technologies", "")).lower() else
        "Period Proof" if pd.isna(row.get("PIM - Features")) and "Flow Shield" in str(row.get("PIM - Technologies", "")).lower() else
        "Breathable;Compression" if pd.isna(row.get("PIM - Features")) and "Formotion" in str(row.get("PIM - Technologies", "")).lower() else
        "Waterproof;Windproof;Breathable" if pd.isna(row.get("PIM - Features")) and "GORE-TEX" in str(row.get("PIM - Technologies", "")).lower() else
        "Lightweight;Cushioned" if pd.isna(row.get("PIM - Features")) and "LIGHT BOOST" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Lightmotion" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned;Lightweight" if pd.isna(row.get("PIM - Features")) and "Lightstrike" in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned;Lightweight;Stability" if pd.isna(row.get("PIM - Features")) and "LIGHTSTRIKEPRO" in str(row.get("PIM - Technologies", "")).lower() else
        "Breathable" if pd.isna(row.get("PIM - Features")) and "Primeknit" in str(row.get("PIM - Technologies", "")).lower() else
        "Waterproof" if pd.isna(row.get("PIM - Features")) and "RAIN.RDY" in str(row.get("PIM - Technologies", "")).lower() else
        "Shock Absorption;Lightweight" if pd.isna(row.get("PIM - Features")) and "REPETITOR" in str(row.get("PIM - Technologies", "")).lower() else
        "Shock Absorption;Lightweight" if pd.isna(row.get("PIM - Features")) and "REPETITOR+" in str(row.get("PIM - Technologies", "")).lower() else
        "Grip;Stability" if pd.isna(row.get("PIM - Features")) and "Stealth C4" in str(row.get("PIM - Technologies", "")).lower() else
        "Compression" if pd.isna(row.get("PIM - Features")) and "Techfit" in str(row.get("PIM - Technologies", "")).lower() else
        "Grip;Stability" if pd.isna(row.get("PIM - Features")) and "Traxion" in str(row.get("PIM - Technologies", "")).lower() else
        "Grip" if pd.isna(row.get("PIM - Features")) and "Anthony Edwards 1" in str(row.get("PIM - Product Family (productlinestyle)", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Spikeless" if pd.isna(row.get("PIM - Features")) and "Golf" in str(row.get("PIM - Sport", "")) and "Spikeless" in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Golf" in str(row.get("PIM - Sport", "")) and "Gazelle" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and "Football" in str(row.get("PIM - Sport", "")) and "adizero Electric" in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport in str(row.get("PIM - Sport", "")) for sport in ["Softball", "Baseball"]) and "adizero Electric" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport in str(row.get("PIM - Sport", "")) for sport in ["Softball", "Baseball"]) and "adizero Impact" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport in str(row.get("PIM - Sport", "")) for sport in ["Softball", "Baseball"]) and "adizero Instinct" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        row.get("PIM - Features")
    ), axis=1)
    df["Enriched Closure"] = df.apply(lambda row: (
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "Country XLG" in str(row.get("Name", "")).lower() else
        "Slip On" if pd.isna(row.get("PIM - Closure")) and "Slip On" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Laceless" if pd.isna(row.get("PIM - Closure")) and "Laceless" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")).lower() else
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "NMD 360" in str(row.get("Name", "")).lower() else
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "Superstar 360" in str(row.get("Name", "")).lower() else
        "Slip On" if pd.isna(row.get("PIM - Closure")) and "adilette 22" in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "BOA Laces" if pd.isna(row.get("PIM - Closure")) and "BOA" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")).lower() else
        row.get("PIM - Closure")
    ), axis=1)
    df["Enriched Best For"] = df.apply(lambda row: (
        'Race;Long Distance;Marathon' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "adizero" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "4D" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort;Neutral' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Duramo" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort;Everyday' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Supernova" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort;Neutral' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Solar" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Neutral' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Response" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Everyday' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Runfalcon" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Long Distance;Marathon' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "adistar" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Speed;Agility;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "F50" in str(row.get("Name", "")).lower() else 
        'Speed;Agility;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "F50" in str(row.get("Name", "")).lower() else 
        'Speed;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Crazyfast" in str(row.get("Name", "")).lower() else 
        'Speed;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "Crazyfast" in str(row.get("Name", "")).lower() else 
        'Control;Inside;Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Copa" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Control;Outside;Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "Copa" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Agility;Accuracy;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Predator" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Agility;Accuracy;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "Predator" in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Agility;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Nemeziz" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Speed;Agility;Comfort' if pd.isna(row.get("PIM - Best For")) and ("Baseball" in str(row.get("PIM - Sport", "")) or "Softball" in str(row.get("PIM - Sport", ""))) and "adizero Electric" in str(row.get("PIM - Product Family (productlinestyle)", "")) else 
        'Speed;Agility;Comfort;Stability' if pd.isna(row.get("PIM - Best For")) and ("Baseball" in str(row.get("PIM - Sport", "")) or "Softball" in str(row.get("PIM - Sport", ""))) and "adizero Impact" in str(row.get("PIM - Product Family (productlinestyle)", "")) else 
        'Speed; Agility;Comfort' if pd.isna(row.get("PIM - Best For")) and ("Baseball" in str(row.get("PIM - Sport", "")) or "Softball" in str(row.get("PIM - Sport", ""))) and "adizero Instinct" in str(row.get("PIM - Product Family (productlinestyle)", "")) else 
        'Agility' if pd.isna(row.get("PIM - Best For")) and ("adizero Cybersonic" in str(row.get("PIM - Product Family (productlinestyle)", "")) or "adizero Ubersonic" in str(row.get("PIM - Product Family (productlinestyle)", ""))) else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Comfy" in str(row.get("Name", "")) else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "adilette" in str(row.get("Name", "")) else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and "T Shirts" in str(row.get("PIM adidas - Product Types", "")) else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "Basketball Legends" in str(row.get("Name", "")) else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "We Ball Together Badge of Sport" in str(row.get("Name", "")) else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "Badge of Sport" in str(row.get("Name", "")) else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "We Ball Together" in str(row.get("Name", "")) else 
        'Off-Court' if pd.isna(row.get("PIM - Best For")) and "Fear of God Athletics" in str(row.get("PIM - Label", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) else 
        'Speed' if pd.isna(row.get("PIM - Best For")) and "adizero Electric" in str(row.get("PIM - Product Family (productlinestyle)", "")) else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "4D" in str(row.get("PIM - Technologies", "")) else 
        'Speed' if pd.isna(row.get("PIM - Best For")) and "adizero Impact" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Staying Cool;Comfort" if pd.isna(row.get("PIM - Best For")) and "AEROREADY" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Boost" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Bounce" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry;Staying Cool" if pd.isna(row.get("PIM - Best For")) and "Climachill" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry;Staying Cool" if pd.isna(row.get("PIM - Best For")) and "Climacool" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry;Staying Warm" if pd.isna(row.get("PIM - Best For")) and "Climaheat" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "Climalite" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "Climaproof" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry;Staying Warm" if pd.isna(row.get("PIM - Best For")) and "Climawarm" in str(row.get("PIM - Technologies", "")) else 
        "Comfort;Everyday" if pd.isna(row.get("PIM - Best For")) and "Cloudfoam" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "CLOUDFOAM PLUS" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry;Staying Warm" if pd.isna(row.get("PIM - Best For")) and "COLD.RDY" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Dreamstrike" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Dreamstrike+" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "EVA" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "Flow Shield" in str(row.get("PIM - Technologies", "")) else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "LIGHT BOOST" in str(row.get("PIM - Technologies", "")) else 
        "Comfort;Speed" if pd.isna(row.get("PIM - Best For")) and "Lightmotion" in str(row.get("PIM - Technologies", "")) else 
        "Comfort;Speed" if pd.isna(row.get("PIM - Best For")) and "Lightstrike" in str(row.get("PIM - Technologies", "")) else 
        "Comfort;Speed" if pd.isna(row.get("PIM - Best For")) and "LIGHTSTRIKEPRO" in str(row.get("PIM - Technologies", "")) else 
        "Versatility;Comfort" if pd.isna(row.get("PIM - Best For")) and "Primeknit" in str(row.get("PIM - Technologies", "")) else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "WIND.RDY" in str(row.get("PIM - Technologies", "")) else 
        "Day Hiking" if pd.isna(row.get("PIM - Best For")) and "Skychaser" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        "Day Hiking" if pd.isna(row.get("PIM - Best For")) and "Anylander" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        "Day Hiking" if pd.isna(row.get("PIM - Best For")) and "Trailmaker" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        "Moderate" if pd.isna(row.get("PIM - Best For")) and "Kirigami" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        "Moderate" if pd.isna(row.get("PIM - Best For")) and "Hiangle" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        "On-Court" if pd.isna(row.get("PIM - Best For")) and any(name.lower() in str(row.get("Name", "")).lower() for name in ["Anthony Edwards", "D.O.N", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8", "Dame 8", "Dame", "Trae", "Trae Unlimited"]) else 
        "On-Court" if pd.isna(row.get("PIM - Best For")) and "Basketball" in str(row.get("PIM - Sport", "")) and "Performance" in str(row.get("PIM - Label", "")) else 
        "Off-Court" if pd.isna(row.get("PIM - Best For")) and "Basketball" in str(row.get("PIM - Sport", "")) and "Performance" not in str(row.get("PIM - Label", "")) else 
        "All Mountain" if pd.isna(row.get("PIM - Best For")) and "Five Ten" in str(row.get("Name", "")) and any(label in str(row.get("PIM - Label", "")) for label in ["Mountain Bike", "Lifestyle"]) else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "RAIN.RDY" in str(row.get("Name", "")) else 
        "Long Distance" if pd.isna(row.get("PIM - Best For")) and "Adistar" in str(row.get("Name", "")) else 
        "Staying Cool;Staying Dry" if pd.isna(row.get("PIM - Best For")) and "HEAT.RDY" in str(row.get("Name", "")) else 
        "Staying Warm" if pd.isna(row.get("PIM - Best For")) and "COLD.RDY" in str(row.get("Name", "")) else 
        "Train" if pd.isna(row.get("PIM - Best For")) and "Training" in str(row.get("PIM - Sport", "")) else 
        "Strength Training" if pd.isna(row.get("PIM - Best For")) and any(x in str(row.get("Name", "")) for x in ["Power", "Optime", "Techfit"]) else 
        "Commute;Cycle" if pd.isna(row.get("PIM - Best For")) and any(x in str(row.get("Name", "")) for x in ["Velosamba", "Velostan Smith"]) else 
        "Cycle" if pd.isna(row.get("PIM - Best For")) and any(x in str(row.get("Name", "")) for x in ["The Road", "The Gravel", "The Indoor", "Velocade"]) else
        row.get("PIM - Best For")
    ), axis=1)
    return df
    
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        enriched_df = enrich_data(df)
    
        # Show preview
        st.success("File processed successfully! Here's a preview:")
        st.dataframe(enriched_df.head())
    
        # Convert to Excel for download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            enriched_df.to_excel(writer, index=False)
        
        st.download_button(
            label="📥 Download Enriched Excel",
            data=output.getvalue(),
            file_name="enriched_products.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    except Exception as e:
        st.error(f"There was an error processing the file: {e}")
    
