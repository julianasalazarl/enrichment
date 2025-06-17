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
        "Agravic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic" in str(row.get("Name", "")) else
        "Samba;60s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba 62" in str(row.get("Name", "")) else
        "Superstar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superstar" in str(row.get("Name", "")) else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in str(row.get("Name", "")) else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in str(row.get("Name", "")) else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in str(row.get("Name", "")) else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in str(row.get("Name", "")) else
        "Hiangle" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hiangle" in str(row.get("Name", "")) else
        "Kestrel" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Kestrel" in str(row.get("Name", "")) else
        "Kirigami" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Kirigami" in str(row.get("Name", "")) else
        "NIAD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten NIAD" in str(row.get("Name", "")) else
        "Sleuth" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Sleuth" in str(row.get("Name", "")) else
        "Trailcross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Trailcross" in str(row.get("Name", "")) else
        "Adventure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["Adventure", "Hyperturf", "Mocaturf", "Roverend", "Rovermule", "Superturf"]) else
        "Astir;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Astir" in str(row.get("Name", "")) else
        "Campus" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Campus" in str(row.get("Name", "")) else
        "Forum" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Forum" in str(row.get("Name", "")) else
        "Gazelle;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gazelle" in str(row.get("Name", "")) else
        "Nizza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Nizza" in str(row.get("Name", "")) else
        "NMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "NMD" in str(row.get("Name", "")) else
        "Oz;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Oz " in str(row.get("Name", "")) else
        "Samba;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba" in str(row.get("Name", "")) and "Cycling" not in str(row.get("Name", "")) else
        "Shmoofoil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Shmoofoil" in str(row.get("Name", "")) else
        "Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stan Smith" in str(row.get("Name", "")) else
        "Adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puffylette" in str(row.get("Name", "")) else
        "Adifom" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Supernova" in str(row.get("Name", "")) else
        "adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adilette" in str(row.get("Name", "")) else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["adizero", "Jumpstar", "DistanceStar", "Ubersonic 4", "Sprintstar", "Throwstar"]) else
        "Aeroimpact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aeroimpact" in str(row.get("Name", "")) else
        "Alphaboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["alphaboost", "alphaboost V1"]) else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa" in str(row.get("Name", "")) else
        "Fast Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Fast Impact" in str(row.get("Name", "")) else
        "Optime" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Optime" in str(row.get("Name", "")) else
        "Own the Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["OTR", "Own the Run"]) else
        "Power Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Power Impact" in str(row.get("Name", "")) else
        "Powerreact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerreact" in str(row.get("Name", "")) else
        "Predator" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Predator" in str(row.get("Name", "")) else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tiro" in str(row.get("Name", "")) else
        "Purelounge" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Purelounge" in str(row.get("Name", "")) else
        "Solar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["Solarboost", "Solarcontrol", "Solarglide", "Solarmotion"]) else
        "Supernova" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Supernova" in str(row.get("Name", "")) else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost" in str(row.get("Name", "")) else
        "4DFWD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "4DFWD" in str(row.get("Name", "")) else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat" in str(row.get("Name", "")) else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider" in str(row.get("Name", "")) else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon" in str(row.get("Name", "")) else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe" in str(row.get("Name", "")) else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic Speed Ultra" in str(row.get("Name", "")) else
        "AX4" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX AX4" in str(row.get("Name", "")) else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Eastrail" in str(row.get("Name", "")) else
        "Free Hiker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Free Hiker" in str(row.get("Name", "")) else
        "Skychaser" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Skychaser" in str(row.get("Name", "")) else
        "Swift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Swift" in str(row.get("Name", "")) else
        "Techrock" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Techrock" in str(row.get("Name", "")) else
        "Voyager" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Voyager" in str(row.get("Name", "")) else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xperior" in str(row.get("Name", "")) else
        "Xploric" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xploric" in str(row.get("Name", "")) else
        "Coreflow" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Coreflow Studio" in str(row.get("Name", "")) or "Coreflow Luxe" in str(row.get("Name", ""))) else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cloudfoam Pure" in str(row.get("Name", "")) else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Codechaos" in str(row.get("Name", "")) else
        "Cross Em" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cross Em" in str(row.get("Name", "")) else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["DON", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8"]) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed for Training" in str(row.get("Name", "")) else
        "Exhibit" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Exhibit" in str(row.get("Name", "")) else
        "Go-To" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Go-To" in str(row.get("Name", "")) else
        "Impact FLX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Impact FLX" in str(row.get("Name", "")) else
        "Lillard;Dame" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Dame 8" in str(row.get("Name", "")) or "Dame" in str(row.get("Name", ""))) else
        "MC80" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC80" in str(row.get("Name", "")) else
        "MC87" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC87" in str(row.get("Name", "")) else
        "Retrocross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retrocross" in str(row.get("Name", "")) else
        "S2G" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "S2G" in str(row.get("Name", "")) else
        "Soulstride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soulstride" in str(row.get("Name", "")) else
        "Swift Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Swift Run" in str(row.get("Name", "")) else
        "Teamwear" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in [
            "Atlanta United", "Austin FC", "CF Montreal", "Charlotte FC", "Chicago Fire", "Colorado Rapids", "Columbus Crew", "D.C. United",
            "FC Cincinnati", "FC Dallas", "Houston Dynamo", "Inter Miami CF", "LA Galaxy", "LAFC", "Los Angeles Football Club",
            "Manchester United", "Minnesota United", "Nashville SC", "New England Revolution", "New York City FC",
            "New York Red Bulls", "Orlando City", "Orlando City SC", "Philadelphia Union", "Portland Timbers", "Real Salt Lake",
            "San Jose Earthquakes", "Seattle Sounders", "Seattle Sounders FC", "Sporting Kansas City", "St. Louis CITY FC",
            "ST Louis City SC", "Toronto FC", "Vancouver Whitecaps", "Jamaica Beckenbauer", "Lightning Third",
            "Washington Huskies", "AFC Ajax", "Benfica", "Celtic FC", "FC Bayern Munich", "Newcastle United FC",
            "Olympique Lyonnais", "Arsenal", "Juventus", "Real Madrid"
        ]) else
        "Trailmaker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Trailmaker" in str(row.get("Name", "")) else
        "TrueCasuals" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TrueCasuals" in str(row.get("Name", "")) else
        "TruePace" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePace" in str(row.get("Name", "")) else
        "Ultimate365" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultimate365" in str(row.get("Name", "")) else
        "ZG" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("ZG23" in str(row.get("Name", "")) or "ZG21" in str(row.get("Name", ""))) else
        "Zoysia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Zoysia" in str(row.get("Name", "")) else
        "Trae" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Trae" in str(row.get("Name", "")) or "Trae Unlimited" in str(row.get("Name", ""))) else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost light" in str(row.get("Name", "")) else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TIRO24" in str(row.get("Name", "")) else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa Gloro" in str(row.get("Name", "")) else
        "True Purpose" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePurpose" in str(row.get("Name", "")) else
        "Response" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Response" in str(row.get("Name", "")) else
        "Daily" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Daily" in str(row.get("Name", "")) else
        "Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Five Ten Impact" in str(row.get("Name", "")) or "Five Ten" in str(row.get("Name", ""))) else
        "Futurecraft" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Futurecraft" in str(row.get("Name", "")) else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s Shoes" in str(row.get("Name", "")) else
        "Run 80s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 80s Shoes" in str(row.get("Name", "")) else
        "Earthlight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Earthlight" in str(row.get("Name", "")) else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Eastrail" in str(row.get("Name", "")) else
        "VULCRAID3R" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VULCRAID3R" in str(row.get("Name", "")) else
        "Sport Pro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adidas x LEGO® Sport Pro Running Shoes" in str(row.get("Name", "")) else
        "Questar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Questar" in str(row.get("Name", "")) else
        "Tensaur" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tensaur" in str(row.get("Name", "")) else
        "Summervent" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Summervent" in str(row.get("Name", "")) else
        "Puig" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puig" in str(row.get("Name", "")) else
        "CourtJam" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "CourtJam" in str(row.get("Name", "")) else
        "Avacourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avacourt" in str(row.get("Name", "")) else
        "Tracefinder" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tracefinder" in str(row.get("Name", "")) else
        "QT Racer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "QT Racer" in str(row.get("Name", "")) else
        "Start Your Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Start Your Run" in str(row.get("Name", "")) else
        "Activeride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Activeride 2.0" in str(row.get("Name", "")) else
        "ZNCHILL" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNCHILL" in str(row.get("Name", "")) else
        "Solarmotion" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solarmotion" in str(row.get("Name", "")) else
        "Kantana" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Kantana Shoes" in str(row.get("Name", "")) else
        "Midcity" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Midcity Low Shoes" in str(row.get("Name", "")) else
        "Winterplay" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Winterplay" in str(row.get("Name", "")) else
        "X" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "X League" in str(row.get("Name", "")) else
        "Retro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["Retro Graphic", "Retro Quarter"]) else
        "RDY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["COLD.RDY", "HEAT.RDY", "RAIN.RDY", "SUMMER.RDY", "WIND.RDY"]) else
        "Top Ten" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Top Ten" in str(row.get("Name", "")) else
        "Spezial;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and pd.notna(row.get("PIM - Label")) and "Originals" in str(row.get("PIM - Label", "")) and "Handball Spezial" in str(row.get("Name", "")) else
        "Tyshawn" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tyshawn" in str(row.get("Name", "")) else
        "adiFOM;Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Stan Smith" in str(row.get("Name", "")) else
        "adilette;adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Adilette" in str(row.get("Name", "")) else
        "adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adiFOM" in str(row.get("Name", "")) else
        "BYW Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BYW Select" in str(row.get("Name", "")) else
        "ADI2000" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADI2000" in str(row.get("Name", "")) else
        "Matchbreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak" in str(row.get("Name", "")) else
        "Crazy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy" in str(row.get("Name", "")) else
        "Crazyflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazyflight" in str(row.get("Name", "")) else
        "Adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adibreak" in str(row.get("Name", "")) else
        "Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Select" in str(row.get("Name", "")) else
        "All Me" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "All Me " in str(row.get("Name", "")) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["D4T", "Designed-for-Training"]) else
        "SL 72;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "SL 72" in str(row.get("Name", "")) else
        "Country;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Country" in str(row.get("Name", "")) else
        "Retropy;2000s;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retropy" in str(row.get("Name", "")) else
        "adicolor;Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in [
            "Arsenal Beckenbauer", "Real Madrid Beckenbauer", "Juventus Beckenbauer", "Adicolor Classics Beckenbauer"
        ]) else
        "adicolor;VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor VRCT" in str(row.get("Name", "")) else
        "Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Beckenbauer" in str(row.get("Name", "")) else
        "3MC" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "3MC" in str(row.get("Name", "")) else
        "adicolor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor" in str(row.get("Name", "")) else
        "Adimatic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adimatic" in str(row.get("Name", "")) else
        "Adipower" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adipower" in str(row.get("Name", "")) else
        "Adistar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adistar" in str(row.get("Name", "")) else
        "Avaflash" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avaflash" in str(row.get("Name", "")) else
        "AVRYN" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avryn_X" in str(row.get("Name", "")) else
        "Barricade" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Barricade" in str(row.get("Name", "")) else
        "Busenitz" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Busenitz" in str(row.get("Name", "")) else
        "Dropset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Dropset" in str(row.get("Name", "")) else
        "Galaxy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Galaxy" in str(row.get("Name", "")) else
        "Harden" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Harden" in str(row.get("Name", "")) else
        "Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Hoops" in str(row.get("Name", "")) else
        "Icon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Icon" in str(row.get("Name", "")) else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak Super" in str(row.get("Name", "")) else
        "MYSHELTER" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MYSHELTER" in str(row.get("Name", "")) else
        "Powerlift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerlift" in str(row.get("Name", "")) else
        "Pureboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pureboost" in str(row.get("Name", "")) else
        "Rapida" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "RapidaSport" in str(row.get("Name", "")) else
        "Rivalry" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rivalry" in str(row.get("Name", "")) else
        "Sereno" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Sereno" in str(row.get("Name", "")) else
        "Stabil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stabil" in str(row.get("Name", "")) else
        "Tango" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tango" in str(row.get("Name", "")) else
        "Tour360" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tour360" in str(row.get("Name", "")) else
        "ZX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZX" in str(row.get("Name", "")) else
        "adicross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adicross" in str(row.get("Name", "")) else
        "ZPLAASH" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZPLAASH" in str(row.get("Name", "")) else
        "adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADBRK" in str(row.get("Name", "")) else
        "Lacombe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lacombe" in str(row.get("Name", "")) else
        "Hoop York City" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x in str(row.get("Name", "")) for x in ["HYC", "Hoop York City"]) else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNE" in str(row.get("Name", "")) else
        "Koln" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Koln" in str(row.get("Name", "")) else
        "Munchen" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Munchen" in str(row.get("Name", "")) else
        "The Total" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "The Total" in str(row.get("Name", "")) else
        "Amplimove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Amplimove" in str(row.get("Name", "")) else
        "Velostan" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Velostan" in str(row.get("Name", "")) else
        "Novaflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Novaflight" in str(row.get("Name", "")) else
        "VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VRCT" in str(row.get("Name", "")) else
        "Gamemode" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamemode" in str(row.get("Name", "")) else
        "Goletto" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Goletto" in str(row.get("Name", "")) else
        "Anthony Edwards" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anthony Edwards" in str(row.get("Name", "")) else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "D.O.N" in str(row.get("Name", "")) else
        "Megaride;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Megaride" in str(row.get("Name", "")) else
        "Centennial" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Centennial" in str(row.get("Name", "")) else
        "Aloha Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aloha Super" in str(row.get("Name", "")) else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Takumi Sen" in str(row.get("Name", "")) else
        "Helionic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Helionic" in str(row.get("Name", "")) else
        "Alphaskin" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Alphaskin" in str(row.get("Name", "")) else
        "Anylander" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anylander" in str(row.get("Name", "")) else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Xperior" in str(row.get("Name", "")) else
        "EQT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Equipment" in str(row.get("Name", "")) or "EQT" in str(row.get("Name", ""))) else
                "Dugout" if pd.isna(row.get("PIM - Product Line (sportsub)")) and (
            "Baseball" in str(row.get("PIM - Sport", "")) or "Softball" in str(row.get("PIM - Sport", ""))
        ) else
        "Beyond the Course" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf" in str(row.get("PIM - Sport", "")) and "Beyond" in str(row.get("Name", "")) else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf" in str(row.get("PIM - Sport", "")) and "Codechaos" in str(row.get("Name", "")) else
        "Clima" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Clima" in str(row.get("Name", "")) else
        "Everyset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Everyset" in str(row.get("Name", "")) else
        "Rapidmove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rapidmove" in str(row.get("Name", "")) else
        "Stella Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stella McCartney Court" in str(row.get("Name", "")) else
        "GameCourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamecourt" in str(row.get("Name", "")) else
        "Solematch" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solematch" in str(row.get("Name", "")) else
        "TLDR" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TLDR" in str(row.get("Name", "")) else
        "Coursecup" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Coursecup" in str(row.get("Name", "")) else
        "Gym+" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gym+" in str(row.get("Name", "")) else
        "Pacer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pacer" in str(row.get("Name", "")) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed-for-Training" in str(row.get("Name", "")) else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s" in str(row.get("Name", "")) else
        "Lightblaze " if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lightblaze" in str(row.get("Name", "")) else
        "ZNSORY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNSORY" in str(row.get("Name", "")) else
        "Aspyre" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aspyre" in str(row.get("Name", "")) else
        "BRMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BRMD" in str(row.get("Name", "")) else
        "Ultradream" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultradream" in str(row.get("Name", "")) else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soccer" in str(row.get("PIM - Sport", "")) and "Z.N.E" in str(row.get("Name", "")) else
        "Spezialist" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Spezialist" in str(row.get("Name", "")) else
        "Ligra" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ligra" in str(row.get("Name", "")) else
        "Essentials" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Essentials" in str(row.get("Name", "")) else
        "Worldwide Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Worldwide Hoops" in str(row.get("Name", "")) or "WWH " in str(row.get("Name", ""))) else
        "adilenium" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adilenium" in str(row.get("Name", "")) else
        "Teamwear" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(team in str(row.get("Name", "")) or team in str(row.get("PIM - Teams", "")) for team in [
            "University of Louisville", "Louisville Cardinals", "Texas A&M", "Texas A&M Aggies", "University of Kansas", "Kansas Jayhawks",
            "University of Miami", "Miami Hurricanes", "University of Nebraska", "Nebraska Cornhuskers",
            "North Carolina State University", "North Carolina", "Arizona State University", "Grambling State University", "Grambling State Tigers",
            "Indiana University", "Indiana Hoosiers", "University of Washington", "Washington Huskies", "NC State", "NC State Wolfpack",
            "New Zealand Rugby", "All Blacks", "Texas Tech", "Hoosiers", "Huskies", "Georgia Tech", "Yellow Jackets",
            "Alcorn State", "Alcorn State Braves", "Arkansas Pine Bluff", "Arkansas-Pine Bluff Golden Lions",
            "Mississippi State University", "Mississippi State Bulldogs", "Alabama State", "Alabama State Hornets",
            "Black History Month University"
        ]) else
        "Initiation" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Initiation" in str(row.get("Name", "")) else
        "BB Legends" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Basketball Legends" in str(row.get("Name", "")) else
        "Crazy Lite" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy lite" in str(row.get("Name", "")) else
        "Ballerina" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ballerina" in str(row.get("Name", "")) else
        "Palos Hills" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Palos Hills" in str(row.get("Name", "")) else
        "Seeulater" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Seeulater" in str(row.get("Name", "")) else
        "Superskate" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superskate" in str(row.get("Name", "")) else
        "Italia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Italia" in str(row.get("Name", "")) else
        "Montreal" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Montreal" in str(row.get("Name", "")) else
        "Adiraptor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adiraptor" in str(row.get("Name", "")) else
        "Ghost Sprint" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ghost Sprint" in str(row.get("Name", "")) else
        "Feroza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "Feroza" in str(row.get("Name", "")) else
        "Adiracer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "Adiracer" in str(row.get("Name", "")) else
        "Heritage" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis" in str(row.get("PIM - Sport", "")) and "Heritage" in str(row.get("Name", "")) else
        "Defiant Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis" in str(row.get("PIM - Sport", "")) and "Defiant" in str(row.get("Name", "")) else
        row.get("PIM - Product Line (sportsub)")
    ), axis=1)
    
    df["Enriched Product Family"] = df.apply(lambda row: (
        "Hyperturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Hyperturf" in str(row.get("Name", "")) else
        "Sambae" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Sambae" in str(row.get("Name", "")) else
        "Mocaturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Mocaturf" in str(row.get("Name", "")) else
        "Roverend" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Roverend" in str(row.get("Name", "")) else
        "Rovermule" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rovermule" in str(row.get("Name", "")) else
        "Superturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superturf" in str(row.get("Name", "")) else
        "Campus 00" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 00" in str(row.get("Name", "")) else
        "Campus 80" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 80" in str(row.get("Name", "")) else
        "Forum High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Forum High" in str(row.get("Name", "")) or "Forum Hi" in str(row.get("Name", ""))) else
        "Forum Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Forum Low" in str(row.get("Name", "")) or "Forum Lo" in str(row.get("Name", ""))) else
        "Forum Mid" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum Mid" in str(row.get("Name", "")) else
        "Nizza High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza High" in str(row.get("Name", "")) else
        "Nizza Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza Low" in str(row.get("Name", "")) else
        "Nizza Mid" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza Mid" in str(row.get("Name", "")) else
        "NMD 360" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD 360" in str(row.get("Name", "")) else
        "NMD_C2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_C2" in str(row.get("Name", "")) else
        "NMD_CS1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_CS1" in str(row.get("Name", "")) else
        "NMD_G1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_G1" in str(row.get("Name", "")) else
        "NMD_R1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1" in str(row.get("Name", "")) else
        "NMD_R1 V2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1 V2" in str(row.get("Name", "")) else
        "NMD_R1 V3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1 V3" in str(row.get("Name", "")) else
        "NMD_R1_PK" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1_PK" in str(row.get("Name", "")) else
        "NMD_R2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R2" in str(row.get("Name", "")) else
        "NMD_TR" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_TR" in str(row.get("Name", "")) else
        "NMD_TS1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_TS1" in str(row.get("Name", "")) else
        "NMD_V3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_V3" in str(row.get("Name", "")) else
        "NMD_W1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_W1" in str(row.get("Name", "")) else
        "NMD_XR1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_XR1" in str(row.get("Name", "")) else
        "Ozelia" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozelia" in str(row.get("Name", "")) else
        "Oznova" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Oznova" in str(row.get("Name", "")) else
        "Ozrah" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozrah" in str(row.get("Name", "")) else
        "Superstar 360" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar 360" in str(row.get("Name", "")) else
        "Superstar ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar ADV" in str(row.get("Name", "")) else
        "adizero Adios Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero adios" in str(row.get("Name", "")) else
        "adizero Afterburner" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Afterburner" in str(row.get("Name", "")) else
        "adizero Boston" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Boston" in str(row.get("Name", "")) else
        "adizero prime" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero prime" in str(row.get("Name", "")) else
        "adizero RC" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero RC" in str(row.get("Name", "")) else
        "adizero Select" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Select" in str(row.get("Name", "")) else
        "adizero SL" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero SL" in str(row.get("Name", "")) else
        "adizero takumi sen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero takumi sen" in str(row.get("Name", "")) else
        "adizero ubersonic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero ubersonic" in str(row.get("Name", "")) else
        "Copa Pure" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Pure" in str(row.get("Name", "")) else
        "Solarboost" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarboost" in str(row.get("Name", "")) else
        "Solarcontrol" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarcontrol" in str(row.get("Name", "")) else
        "Solar Glide" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarglide" in str(row.get("Name", "")) else
        "Solarmotion" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarmotion" in str(row.get("Name", "")) else
        "X Crazyfast" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X Crazyfast" in str(row.get("Name", "")) else
        "X Speedportal" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X Speedportal" in str(row.get("Name", "")) else
        "4DFWD Pulse" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "4DFWD Pulse" in str(row.get("Name", "")) else
        "Ultrabounce DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultrabounce DNA" in str(row.get("Name", "")) else
        "Duramo SL" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Duramo SL" in str(row.get("Name", "")) else
        "Duramo Speed" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Duramo Speed" in str(row.get("Name", "")) else
        "Ultraboost 1.0;Ultraboost DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 1.0" in str(row.get("Name", "")) else
        "xplrphase" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "x_plrphase" in str(row.get("Name", "")) else
        "Ubounce DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ubounce DNA" in str(row.get("Name", "")) else
        "Grand Court 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Grand Court 2.0" in str(row.get("Name", "")) else
        "adilette Aqua" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette aqua" in str(row.get("Name", "")) else
        "adilette Comfort" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette comfort" in str(row.get("Name", "")) else
        "adilette shower" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette shower" in str(row.get("Name", "")) else
        "Grand Court Alpha" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "grand court alpha" in str(row.get("Name", "")) else
        "adilette platform" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette platform" in str(row.get("Name", "")) else
        "Agravic Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Flow" in str(row.get("Name", "")) else
        "Agravic Speed Ultra" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Speed Ultra" in str(row.get("Name", "")) else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Speed" in str(row.get("Name", "")) else
        "Agravic Ultra" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Ultra" in str(row.get("Name", "")) else
        "SL 72 RTN" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 RTN" in str(row.get("Name", "")) else
        "Anthony Edwards 1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Anthony Edwards 1" in str(row.get("Name", "")) else
        "3 Stripes" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("3 Stripes" in str(row.get("Name", "")) or "3-Stripes" in str(row.get("Name", ""))) else
        "F50 Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 Pro" in str(row.get("Name", "")) else
        "F50 Elite" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 Elite" in str(row.get("Name", "")) else
        "F50 League" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 League" in str(row.get("Name", "")) else
        "Stan Smith Lux" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Stan Smith Lux" in str(row.get("Name", "")) else
        "Gazelle Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle Bold" in str(row.get("Name", "")) else
        "Predator Edge" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Edge" in str(row.get("Name", "")) else
        "Predator Club" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Club" in str(row.get("Name", "")) else
        "Predator Accuracy" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Accuracy" in str(row.get("Name", "")) else
        "Predator League" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator League" in str(row.get("Name", "")) else
        "Copa Sense" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Sense" in str(row.get("Name", "")) else
        "Copa Mundial" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Mundial" in str(row.get("Name", "")) else
        "adizero Instinct" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Instinct" in str(row.get("Name", "")) else
        "Free Hiker 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Free Hiker 2" in str(row.get("Name", "")) else
        "Exhibit Select" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Exhibit Select" in str(row.get("Name", "")) else
        "adizero Impact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Impact" in str(row.get("Name", "")) else
        "SL 72 OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 OG" in str(row.get("Name", "")) else
        "SL 72 RS" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 RS" in str(row.get("Name", "")) else
        "Predator Elite" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Elite" in str(row.get("Name", "")) else
        "Forum Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum Bold" in str(row.get("Name", "")) else
        "VL Court 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "VL Court 3.0" in str(row.get("Name", "")) else
        "Ultraboost 20" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 20" in str(row.get("Name", "")) else
        "SL 76" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 76" in str(row.get("Name", "")) else
        "Handball Spezial" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Originals" in str(row.get("PIM - Label", "")) and "Handball Spezial" in str(row.get("Name", "")) else
        "Response CL;2000s" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Response CL" in str(row.get("Name", "")) else
        "Rivalry Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Rivalry 86 Low" in str(row.get("Name", "")) or "Rivalry Summer Low" in str(row.get("Name", ""))) else
        "Rivalry High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rivalry High" in str(row.get("Name", "")) else
        "Ozmillen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozmillen" in str(row.get("Name", "")) else
        "Lite Racer Adapt" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer Adapt" in str(row.get("Name", "")) else
        "Firebird" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Firebird" in str(row.get("Name", "")) else
        "adizero Electric" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Electric" in str(row.get("Name", "")) else
        "Adilette 22" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilette 22" in str(row.get("Name", "")) else
        "Superstar XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar XLG" in str(row.get("Name", "")) else
        "Country XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country XLG" in str(row.get("Name", "")) else
        "Samba XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba XLG" in str(row.get("Name", "")) else
        "Samba OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba OG" in str(row.get("Name", "")) else
        "Y-3 Classic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Y-3 Classic" in str(row.get("Name", "")) or "Y-3 CL" in str(row.get("Name", ""))) else
        "Retro Quarter" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Retro Quarter" in str(row.get("Name", "")) else
        "Retro Graphic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Retro Graphic" in str(row.get("Name", "")) else
        "Activeride 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Activeride 2.0" in str(row.get("Name", "")) else
        "QT Racer 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "QT Racer 3.0" in str(row.get("Name", "")) else
        "Eastrail 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Eastrail 2.0" in str(row.get("Name", "")) else
        "ZG21" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "ZG21" in str(row.get("Name", "")) else
        "ZG23" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "ZG23" in str(row.get("Name", "")) else
        "Daily 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Daily 3.0" in str(row.get("Name", "")) else
        "Copa Gloro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Gloro" in str(row.get("Name", "")) else
        "Tiro 21" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 21" in str(row.get("Name", "")) or "TIRO21" in str(row.get("Name", ""))) else
        "Tiro 23" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 23" in str(row.get("Name", "")) or "TIRO23" in str(row.get("Name", ""))) else
        "Tiro 24" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 24" in str(row.get("Name", "")) or "TIRO24" in str(row.get("Name", ""))) else
        "Ultraboost light" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost light" in str(row.get("Name", "")) else
        "Supernova Stride" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Stride" in str(row.get("Name", "")) else
        "Supernova Solution" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Solution" in str(row.get("Name", "")) else
        "Supernova Rise" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Rise" in str(row.get("Name", "")) else
        "Trae Young Unlimited" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Unlimited" in str(row.get("Name", "")) else
        "Trae Young 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 3" in str(row.get("Name", "")) else
        "Trae Young 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 2" in str(row.get("Name", "")) else
        "Dame Certified" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame Certified" in str(row.get("Name", "")) else
        "Dame 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame 8" in str(row.get("Name", "")) else
        "D.O.N Issue 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 8" in str(row.get("Name", "")) else
        "D.O.N Issue 7" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 7" in str(row.get("Name", "")) else
        "D.O.N Issue 6" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 6" in str(row.get("Name", "")) else
        "D.O.N Issue 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 5" in str(row.get("Name", "")) else
        "Barricade 13" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Barricade 13" in str(row.get("Name", "")) else
        "Crazy 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Crazy 8" in str(row.get("Name", "")) else
        "D.O.N Issue 6" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("D.O.N. ISSUE 6" in str(row.get("Name", "")) or "D.O.N ISSUE #6" in str(row.get("Name", ""))) else
        "D.O.N Issue 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N. Issue #5" in str(row.get("Name", "")) else
        "Forum Hi" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "FORUM 84 HI" in str(row.get("Name", "")) else
        "Forum Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "FORUM 84 LOW" in str(row.get("Name", "")) else
        "Trae Young 4" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 4" in str(row.get("Name", "")) else
        "Pureboost 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pureboost 5" in str(row.get("Name", "")) else
        "Alphaboost V1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphaboost V1" in str(row.get("Name", "")) else
        "Alphaboost V2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphaboost V2" in str(row.get("Name", "")) else
        "Alphabounce+" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphabounce+" in str(row.get("Name", "")) else
        "Country OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country OG" in str(row.get("Name", "")) else
        "Pro Shell ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Shell ADV" in str(row.get("Name", "")) else
        "Gazelle ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle ADV" in str(row.get("Name", "")) else
        "Centennial 85" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Centennial 85" in str(row.get("Name", "")) else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Cloudfoam Pure" in str(row.get("Name", "")) else
        "Supernova Prima" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Prima" in str(row.get("Name", "")) else
        "Ultraboost 5X" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 5X" in str(row.get("Name", "")) else
        "PowerImpact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "PowerImpact" in str(row.get("Name", "")) else
        "Run Pocket" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Run Pocket" in str(row.get("Name", "")) else
        "Soulstride Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Soulstride Flow" in str(row.get("Name", "")) else
        "TLRD Impact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TLRD Impact" in str(row.get("Name", "")) else
        "Campus Vulc" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus Vulc" in str(row.get("Name", "")) else
        "Campus ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus ADV" in str(row.get("Name", "")) else
        "Busenitz Vulc II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Busenitz Vulc II" in str(row.get("Name", "")) else
        "Busenitz Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Busenitz Pro" in str(row.get("Name", "")) else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Matchbreak Super" in str(row.get("Name", "")) else
        "Ozweego" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozweego" in str(row.get("Name", "")) else
        "Samba ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba ADV" in str(row.get("Name", "")) else
        "Gazelle Indoor" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle Indoor" in str(row.get("Name", "")) else
        "Ozmorph" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozmorph" in str(row.get("Name", "")) else
        "Samba Decon" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba Decon" in str(row.get("Name", "")) else
        "Samba Millenium" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Samba MN" in str(row.get("Name", "")) or "Samba Millenium" in str(row.get("Name", ""))) else
        "Stan Smith Decon" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Stan Smith Decon" in str(row.get("Name", "")) else
        "Rivalry Mule" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rivalry Mule" in str(row.get("Name", "")) else
        "Temper Run 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Temper Run 2.0" in str(row.get("Name", "")) else
        "Superstar II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar II" in str(row.get("Name", "")) else
        "Country II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country II" in str(row.get("Name", "")) else
        "Harden Vol. 9" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Harden Vol. 9" in str(row.get("Name", "")) else
        "Crazy 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Crazy 2" in str(row.get("Name", "")) else
        "Tyshawn II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tyshawn II" in str(row.get("Name", "")) else
        "adizero ZG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Golf" in str(row.get("PIM - Sport", "")) and "Adizero ZG" in str(row.get("Name", "")) else
        "adizero Cybersonic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tennis" in str(row.get("PIM - Sport", "")) and "Adizero Cybersonic" in str(row.get("Name", "")) else
        "Entrada 22" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Soccer" in str(row.get("PIM - Sport", "")) and "Entrada 22" in str(row.get("Name", "")) else
        "Lite Racer 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer 3.0" in str(row.get("Name", "")) else
        "Swift Run 1.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Swift Run 1.0" in str(row.get("Name", "")) else
        "X_PLR Path" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X_PLR Path" in str(row.get("Name", "")) else
        "Kaptir Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Kaptir Flow" in str(row.get("Name", "")) else
        "Kaptir 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Kaptir 3.0" in str(row.get("Name", "")) else
        "Lite Racer 4.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer 4.0" in str(row.get("Name", "")) else
        "VL Court Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "VL Court Bold" in str(row.get("Name", "")) else
        "Ultradream Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultradream Bold" in str(row.get("Name", "")) else
        "Ultradream DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultradream DNA" in str(row.get("Name", "")) else
        "Adilette Estrap" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilette Estrap" in str(row.get("Name", "")) else
        "Neuclassics" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Neuclassics" in str(row.get("Name", "")) else
        "Superstar 80s" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar 82" in str(row.get("Name", "")) else
        "Adizero Aruku" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Aruku" in str(row.get("Name", "")) else
        "iiinfinity" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "IIInfinity" in str(row.get("Name", "")) else
        "Adilenium Season 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilenium Season 3" in str(row.get("Name", "")) else
        "adizero takumi sen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Takumi Sen" in str(row.get("Name", "")) else
        "Dame 9" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame 9" in str(row.get("Name", "")) else
        "Agravic 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Agravic 3" in str(row.get("Name", "")) else
        "Tracefinder 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tracefinder 2" in str(row.get("Name", "")) else
        "Seeulater 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Seeulater 2" in str(row.get("Name", "")) else
        "Dame X" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame X" in str(row.get("Name", "")) else
        "Forum ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum ADV" in str(row.get("Name", "")) else
        "Pro Model ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Model ADV" in str(row.get("Name", "")) else
        "Initiation" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Initiation" in str(row.get("Name", "")) else
        "Pro Model" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Model" in str(row.get("Name", "")) else
        "Campus 00s Beta" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 00s Beta" in str(row.get("Name", "")) else
        row.get("PIM - Product Family (productlinestyle)")
    ), axis=1)

    df["Enriched Label"] = df.apply(lambda row: (
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "ALL SZN" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Duramo" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ultraboost 1.0" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "X_PLR" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "XPLR" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Z.N.E" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "City Escape" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "FortaRun" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "RunFalcon" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Runfalcon" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Racer TR" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "VL Court" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Front Court" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ownthegame" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ubounce" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Breaknet" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Grand Court 2.0" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Postmove" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "alphaboost" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Alphaboost" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Puremotion" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Kaptir" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Spiritain" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "ZNSORED" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Future Icons" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Lite Racer" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette aqua" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette comfort" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette shower" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "grand court alpha" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "alphabounce" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Alphabounce" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adicane" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette platform" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "advantage" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "courtblock" in str(row.get("Name", "")) else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y-3" in str(row.get("Name", "")) else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y3" in str(row.get("Name", "")) else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y 3" in str(row.get("Name", "")) else
        "Five Ten" if pd.isna(row.get("PIM - Label")) and "Hellcat" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Run 70s Shoes" in str(row.get("Name", "")) else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Run 80s Shoes" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "The Gravel Cycling" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ZG23" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ZG21" in str(row.get("Name", "")) else
        "adidas by Stella McCartney" if pd.isna(row.get("PIM - Label")) and "adidas by Stella McCartney" in str(row.get("Name", "")) else
        "adidas by Stella McCartney" if pd.isna(row.get("PIM - Label")) and "aSMC" in str(row.get("Name", "")) else
        "TERREX" if pd.isna(row.get("PIM - Label")) and "Eastrail" in str(row.get("Name", "")) else
        "Impact" if pd.isna(row.get("PIM - Label")) and "Five Ten Impact" in str(row.get("Name", "")) else
        "Five Ten" if pd.isna(row.get("PIM - Label")) and "Five Ten" in str(row.get("Name", "")) else
        "Fear of God Athletics" if pd.isna(row.get("PIM - Label")) and "Fear of God Athletics" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Gazelle" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Samba Messi" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Sambae" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Samba" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Superstar" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Forum" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Stan Smith" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Ozelia" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "NMD" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "OZWEEGO" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "OZMILLEN" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Campus" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Adizero" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ADIZERO" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Rivalry" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Falcon" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Craig Green" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Bad Bunny" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Originals" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Country OG" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Ozthemis" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adi2000" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Spezial" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Response CL" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Response" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adifom" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "AdiFOM" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Wensley" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SPZL" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Moston Super" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL 72" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Pop Trading Co" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "NRTN" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SSTR N" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Wales Bonner" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL76" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL 76" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "TMNT" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Centennial 85" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Civilist ZX" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Crazy" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Nizza" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Solid Crew" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Trefoil" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adibreak" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Korn" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adi Dassler" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adicolor" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "100 Thieves" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Street Neuclassic" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "KSENIASCHNAIDER" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Premium" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Todmorden Smock" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Rossendale" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SST" in str(row.get("Name", "")) else
        "Performance" if pd.isna(row.get("PIM - Label")) and any(x in str(row.get("Name", "")) for x in [
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
        "Sportswear" if pd.isna(row.get("PIM - Label")) and any(x in str(row.get("Name", "")) for x in [
            "Tensaur", "X_PLRBOOST", "SwIft Run", "Kantana", "Osade", "Park Street",
            "X_PLRPHASE", "Heawyn", "Avryn_X", "Adissage", "ZPLAASH", "Sportswear",
            "Z.N.E.", "FARM Rio"
        ]) else
        "TERREX" if pd.isna(row.get("PIM - Label")) and "Terrex" in str(row.get("Name", "")) else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Real Madrid 23/24" in str(row.get("Name", "")) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Golf" in str(row.get("PIM - Sport", "")) and any(x in str(row.get("PIM - Product Line (sportsub)", "")) for x in [
            "Gazelle", "Samba", "Stan Smith"
        ]) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Golf" in str(row.get("PIM - Sport", "")) and "Originals" in str(row.get("Name", "")) else
        row.get("PIM - Label")
    ), axis=1)
    df["Enriched Sport"] = df.apply(lambda row: (   
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Freerider" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Aleon" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Crawe" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Hellcat" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Hiangle" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Kestrel" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Kirigami" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten NIAD" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Sleuth" in str(row.get("Name", "")) else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Trailcross" in str(row.get("Name", "")) else
        "Basketball;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Forum" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Adifom Supernova" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero adios" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero adios pro" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero Boston" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero prime" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero RC" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero SL" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero takumi sen" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarboost" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarcontrol" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarglide" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Ultrabounce" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ALL SZN" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Duramo" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ultraboost 1.0" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "X_PLR" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "XPLR" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Z.N.E" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "City Escape" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "FortaRun" in str(row.get("Name", "")) else
        "Running" if pd.isna(row.get("PIM - Sport")) and "RunFalcon" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Racer TR" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "VL Court" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Front Court" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ownthegame" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ubounce" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Breaknet" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Grand Court 2.0" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Postmove" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "alphaboost" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Puremotion" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Kaptir" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Spiritain" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ZNSORED" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Future Icons" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Lite Racer" in str(row.get("Name", "")) else
        "Swim; Yoga; Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette aqua" in str(row.get("Name", "")) else
        "Swim; Yoga; Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette comfort" in str(row.get("Name", "")) else
        "Swim; Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette shower" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "grand court alpha" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "alphabounce" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adicane" in str(row.get("Name", "")) else
        "Swim;Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette platform" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "advantage" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "courtblock" in str(row.get("Name", "")) else
        "Swim;Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and pd.notna(row.get("PIM adidas - Product Types")) and "Slides" in row.get("PIM adidas - Product Types") else
        "Dance" if pd.isna(row.get("PIM - Sport")) and "Dance" in str(row.get("Name", "")) else
        "Golf" if pd.isna(row.get("PIM - Sport")) and "Golf" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "TrueCasuals" in str(row.get("Name", "")) else
        "Golf" if pd.isna(row.get("PIM - Sport")) and "Ultimate365" in str(row.get("Name", "")) else
        "Soccer" if pd.isna(row.get("PIM - Sport")) and "Copa Gloro" in str(row.get("Name", "")) else
        "Cycling" if pd.isna(row.get("PIM - Sport")) and "Bike Shoes" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "FARM" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Z.N.E." in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Run 70s Shoes" in str(row.get("Name", "")) else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Run 80s Shoes" in str(row.get("Name", "")) else
        "Cycling" if pd.isna(row.get("PIM - Sport")) and "The Gravel Cycling" in str(row.get("Name", "")) else
        "Soccer" if pd.isna(row.get("PIM - Sport")) and any(team in str(row.get("Name", "")) for team in [
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
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ZNSORED High" in str(row.get("Name", "")) else
        "Training;Weightlifting" if pd.isna(row.get("PIM - Sport")) and "Dropset" in str(row.get("Name", "")) else
        "Weightlifting" if pd.isna(row.get("PIM - Sport")) and "The Total" in str(row.get("Name", "")) else
        "Basketball;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Fear of God Athletics" in str(row.get("PIM - Label", "")) else
        "Skateboarding;Lifestyle" if pd.isna(row.get("PIM - Sport")) and any(name in str(row.get("Name", "")) for name in [
            "Samba ADV", "Superstar ADV", "Stan Smith ADV", "Centennial 85 Low ADV",
            "Gazelle ADV", "Pro Model 80 ADV", "Campus ADV"
        ]) else
        row.get("PIM - Sport")
    ), axis=1)
    df["Enriched Activity"] = df.apply(lambda row: (
        "Outdoor;Athletic" if "Hellcat" in str(row.get("Name", "")) else
        "Outdoor;Athletic" if "Terrex" in str(row.get("Name", "")) else
        "Premium" if "Y-3" in str(row.get("PIM - Label", "")) else
        "Premium" if "Fear of God Athletics" in str(row.get("PIM - Label", "")) else
        "Premium" if "adidas by Stella McCartney" in str(row.get("PIM - Label", "")) else
        "Premium" if "Y-3" in str(row.get("Name", "")) else
        "Premium" if "Fear of God" in str(row.get("Name", "")) else
        "Premium" if "100 Thieves" in str(row.get("Name", "")) else
        "Premium" if "Avavav" in str(row.get("Name", "")) else
        "Premium" if "Sporty & Rich" in str(row.get("Name", "")) else
        "Premium" if "Dime" in str(row.get("Name", "")) else
        "Premium" if "Bape" in str(row.get("Name", "")) else
        "Premium" if "Song For The Mute" in str(row.get("Name", "")) else
        "Premium" if "Bad Bunny" in str(row.get("Name", "")) else
        "Premium" if "SPZL" in str(row.get("Name", "")) else
        "Premium" if "Dingyun Zhang" in str(row.get("Name", "")) else
        "Premium" if "Edison Chen" in str(row.get("Name", "")) else
        "Premium" if "SFTM" in str(row.get("Name", "")) else
        "Premium" if "EQT" in str(row.get("Name", "")) else
        "Premium" if "Equipment" in str(row.get("Name", "")) else
        "Premium" if "Korn" in str(row.get("Name", "")) else
        "Premium" if "JJJJound" in str(row.get("Name", "")) else
        "Premium" if "Wales Bonner" in str(row.get("Name", "")) else
        "Premium" if "Willy Chavarria" in str(row.get("Name", "")) else
        "Premium" if "Brain Dead" in str(row.get("Name", "")) else
        "Premium" if "Jabbar" in str(row.get("Name", "")) else
        "Premium" if "Pharrell" in str(row.get("Name", "")) else
        "Premium" if "CP Company" in str(row.get("Name", "")) else
        "Premium" if "Minecraft" in str(row.get("Name", "")) else
        "Premium" if "Fortnite" in str(row.get("Name", "")) else
        "Premium" if "BW Army" in str(row.get("Name", "")) else
        "Premium" if "Spongebob" in str(row.get("Name", "")) else
        "Premium" if "NTS Radio" in str(row.get("Name", "")) else
        "Premium" if "Rolling Links" in str(row.get("Name", "")) else
        row.get("")
    ), axis=1)
    df["Enriched Pattern"] = df.apply(lambda row: (
        "All Over Print" if pd.isna(row.get("PIM - Pattern")) and "All Over Print" in str(row.get("Name", "")) else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Animal" in str(row.get("Name", "")) else
        "Camo" if pd.isna(row.get("PIM - Pattern")) and "Camo" in str(row.get("Name", "")) else
        "Camo" if pd.isna(row.get("PIM - Pattern")) and "Camouflage" in str(row.get("Name", "")) else
        "Graphic Print" if pd.isna(row.get("PIM - Pattern")) and "Graphic" in str(row.get("Name", "")) else
        "Floral" if pd.isna(row.get("PIM - Pattern")) and "Floral" in str(row.get("Name", "")) else
        "Floral" if pd.isna(row.get("PIM - Pattern")) and "Flower" in str(row.get("Name", "")) else
        "Polka Dots" if pd.isna(row.get("PIM - Pattern")) and "Dots" in str(row.get("Name", "")) else
        "Polka Dots" if pd.isna(row.get("PIM - Pattern")) and "Polka Dots" in str(row.get("Name", "")) else
        "Tie Dye" if pd.isna(row.get("PIM - Pattern")) and "Tie-Dye" in str(row.get("Name", "")) else
        "Tie Dye" if pd.isna(row.get("PIM - Pattern")) and "Tie Dye" in str(row.get("Name", "")) else
        "Metallic" if pd.isna(row.get("PIM - Pattern")) and "Metallic" in str(row.get("Name", "")) else
        "Flames" if pd.isna(row.get("PIM - Pattern")) and "Flame" in str(row.get("Name", "")) else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Leopard" in str(row.get("Name", "")) else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Zebra" in str(row.get("Name", "")) else
        "Embroidery" if pd.isna(row.get("PIM - Pattern")) and "Embroidered" in str(row.get("Name", "")) else
        "Logo Print" if pd.isna(row.get("PIM - Pattern")) and "LOGO" in str(row.get("Name", "")) else
        "Glitter" if pd.isna(row.get("PIM - Pattern")) and "Glitter" in str(row.get("Name", "")) else
        "Glitter" if pd.isna(row.get("PIM - Pattern")) and "Rhinestones" in str(row.get("Name", "")) else
        "Logo Print" if pd.isna(row.get("PIM - Pattern")) and "Logo" in str(row.get("Name", "")) else
        "Crochet" if pd.isna(row.get("PIM - Pattern")) and "Crochet" in str(row.get("Name", "")) else
        "Colorblock" if pd.isna(row.get("PIM - Pattern")) and "Colorblock" in str(row.get("Name", "")) else
        "Color Block" if pd.isna(row.get("PIM - Pattern")) and "Color block" in str(row.get("Name", "")) else
        "Plaid" if pd.isna(row.get("PIM - Pattern")) and "Plaid" in str(row.get("Name", "")) else
        row.get("PIM - Pattern")
    ), axis=1)
    df["Enriched Base Material"] = df.apply(lambda row: (
        "Fleece" if pd.isna(row.get("PIM - Base Material")) and "ALL SZN" in str(row.get("Name", "")) else
        "Nuganic" if pd.isna(row.get("PIM - Base Material")) and "Nuganic" in str(row.get("Name", "")) else
        "Denim" if pd.isna(row.get("PIM - Base Material")) and "Denim" in str(row.get("Name", "")) else
        "Satin" if pd.isna(row.get("PIM - Base Material")) and "Satin" in str(row.get("Name", "")) else
        "Velour;Velvet" if pd.isna(row.get("PIM - Base Material")) and (
            "Velour" in str(row.get("Name", "")) or "Velvet" in str(row.get("Name", ""))
        ) else
        "Piqué" if pd.isna(row.get("PIM - Base Material")) and "Pique" in str(row.get("Name", "")) else
        "Microfiber" if pd.isna(row.get("PIM - Base Material")) and "Microfiber" in str(row.get("Name", "")) else
        "Wool" if pd.isna(row.get("PIM - Base Material")) and "Wool" in str(row.get("Name", "")) else
        "Molded" if pd.isna(row.get("PIM - Base Material")) and "Molded" in str(row.get("Name", "")) else
        "Cashmere" if pd.isna(row.get("PIM - Base Material")) and "Cashmere" in str(row.get("Name", "")) else
        "Twistknit" if pd.isna(row.get("PIM - Base Material")) and "Twistknit" in str(row.get("Name", "")) else
        "Recycled Polyester" if pd.isna(row.get("PIM - Base Material")) and
        "Soccer" in str(row.get("PIM - Sport", "")) and (
                "Jerseys" in str(row.get("PIM adidas - Product Types", "")) or
                "Jerseys - Long Sleeve" in str(row.get("PIM adidas - Product Types", "")) or
                "Gloves - Goalkeeper" in str(row.get("PIM adidas - Product Types", ""))
            ) else
        "Cotton" if pd.isna(row.get("PIM - Base Material")) and
            "Soccer" in str(row.get("PIM - Sport", "")) and
            "Shorts" in str(row.get("PIM adidas - Product Types", "")) and (
                "Tiro 24 Sweat Shorts" in str(row.get("Name", "")) or
                "Tiro 24 Shorts" in str(row.get("Name", ""))
            ) else
        "Cotton" if pd.isna(row.get("PIM - Base Material")) and
            "Soccer" in str(row.get("PIM - Sport", "")) and
            "T Shirts" in str(row.get("PIM adidas - Product Types", "")) else
        "Twistweave" if pd.isna(row.get("PIM - Base Material")) and "Twistweave" in str(row.get("Name", "")) else
        row.get("PIM - Base Material")
    ), axis=1)
    df["Enriched Partner"] = df.apply(lambda row: (
        "Disney" if pd.isna(row.get("PIM - Partner")) and "Disney" in str(row.get("Name", "")) else
        "Disney; Star Wars" if pd.isna(row.get("PIM - Partner")) and "Star Wars" in str(row.get("Name", "")) else
        "Disney;Mickey" if pd.isna(row.get("PIM - Partner")) and "Mickey" in str(row.get("Name", "")) else
        "Disney;Moana" if pd.isna(row.get("PIM - Partner")) and "Moana" in str(row.get("Name", "")) else
        "Farm" if pd.isna(row.get("PIM - Partner")) and "FARM" in str(row.get("Name", "")) else
        "UEFA Champions League;Club" if pd.isna(row.get("PIM - Partner")) and any(x in str(row.get("Name", "")) for x in [
            "Juventus", "Manchester United", "Real Madrid", "AFC Ajax"
        ]) else
        "Stella McCartney" if pd.isna(row.get("PIM - Partner")) and "Stella McCartney" in str(row.get("Name", "")) else
        "LEGO" if pd.isna(row.get("PIM - Partner")) and "Lego" in str(row.get("Name", "")) else
        "Marimekko" if pd.isna(row.get("PIM - Partner")) and "Marimekko" in str(row.get("Name", "")) else
        "Disney;Marvel" if pd.isna(row.get("PIM - Partner")) and "Marvel" in str(row.get("Name", "")) else
        "Parley" if pd.isna(row.get("PIM - Partner")) and "Parley" in str(row.get("Name", "")) else
        "MLS" if pd.isna(row.get("PIM - Partner")) and any(x in str(row.get("Name", "")) for x in [
            "Atlanta United", "Austin FC", "CF Montreal", "Charlotte FC", "Chicago Fire", "Colorado Rapids",
            "Columbus Crew", "D.C. United", "FC Cincinnati", "FC Dallas", "Houston Dynamo", "Inter Miami CF",
            "LA Galaxy", "LAFC", "Los Angeles FC", "Minnesota United", "Nashville SC", "New England Revolution",
            "New York City FC", "New York Red Bulls", "Orlando City", "Philadelphia Union", "Portland Timbers",
            "Real Salt Lake", "San Jose Earthquakes", "Seattle Sounders FC", "Sporting Kansas City",
            "St. Louis CITY FC", "Toronto FC", "Vancouver Whitecaps", "Jamaica Beckenbauer", "Lightning Third",
            "Los Angeles Football Club", "Montreal Impact", "Orlando City SC", "Seattle Sounders",
            "ST Louis City SC", "Washington Huskies"
        ]) else
        "Club" if pd.isna(row["PIM - Partner"]) and "Benfica" in str(row.get("Name", "")) else
        "UEFA Champions League;Club" if pd.isna(row["PIM - Partner"]) and any(x in str(row.get("Name", "")) for x in [
            "Celtic FC", "FC Bayern Munich", "Olympique Lyonnais", "Arsenal"
        ]) else
        "Club" if pd.isna(row["PIM - Partner"]) and "Newcastle United FC" in str(row.get("Name", "")) else
        "SPZL" if pd.isna(row["PIM - Partner"]) and "SPZL" in str(row.get("Name", "")) else
        "Andre Saravia" if pd.isna(row["PIM - Partner"]) and any(x in str(row.get("Name", "")) for x in ["André Saraiva", "Andre Saraiva"]) else
        "Edison Chen" if pd.isna(row["PIM - Partner"]) and "Edison Chen" in str(row.get("Name", "")) else
        "Y 3" if pd.isna(row["PIM - Partner"]) and "Y-3" in str(row.get("Name", "")) else
        "Bad Bunny" if pd.isna(row["PIM - Partner"]) and any(x in str(row.get("Name", "")) for x in ["Bad Bunny", "Ballerina"]) else
        "KseniaSchnaider" if pd.isna(row["PIM - Partner"]) and "KSENIASCHNAIDER" in str(row.get("Name", "")) else
        "BAPE" if pd.isna(row["PIM - Partner"]) and "BAPE" in str(row.get("Name", "")) else
        "Pop Trading Company" if pd.isna(row["PIM - Partner"]) and "Pop Trading Co" in str(row.get("Name", "")) else
        "Wales Bonner" if pd.isna(row["PIM - Partner"]) and "Wales Bonner" in str(row.get("Name", "")) else
        "Pharrell" if pd.isna(row["PIM - Partner"]) and "Pharrell Williams" in str(row.get("Name", "")) else
        "100 Thieves" if pd.isna(row["PIM - Partner"]) and "100 Thieves" in str(row.get("Name", "")) else
        "Korn" if pd.isna(row["PIM - Partner"]) and "Korn" in str(row.get("Name", "")) else
        "UEFA Champions League" if pd.isna(row["PIM - Partner"]) and "UCL" in str(row.get("Name", "")) else
        "UEFA EURO" if pd.isna(row["PIM - Partner"]) and any(x in str(row.get("Name", "")) for x in ["Euro 24", "Fussballliebe"]) else
        "Deadpool;Marvel" if pd.isna(row["PIM - Partner"]) and "Deadpool" in str(row.get("Name", "")) else
        "Yeezy" if pd.isna(row["PIM - Partner"]) and "Yeezy" in str(row.get("Name", "")) else
        "Y3" if pd.isna(row["PIM - Partner"]) and "Y-3" in str(row.get("Name", "")) else
        "Avavav" if pd.isna(row["PIM - Partner"]) and "Avavav" in str(row.get("Name", "")) else
        "Club" if pd.isna(row["PIM - Partner"]) and any(x in str(row.get("Name", "")) for x in ["AS Roma", "Boca Juniors"]) else
        "Lion King" if pd.isna(row["PIM - Partner"]) and "Lion King" in str(row.get("Name", "")) else
        "Fortnite" if pd.isna(row["PIM - Partner"]) and "Fortnite" in str(row.get("Name", "")) else
        "Teamgeist" if pd.isna(row["PIM - Partner"]) and "Teamgeist" in str(row.get("Name", "")) else
        "Willy Chavarria" if pd.isna(row["PIM - Partner"]) and "Willy Chavarria" in str(row.get("Name", "")) else
        "OG LA" if pd.isna(row["PIM - Partner"]) and any(x in str(row.get("Name", "")) for x in ["OG L.A", "OG LA"]) else
        "College" if pd.isna(row["PIM - Partner"]) and (
            "Collegiate" in str(row.get("Name", "")) or
            any(x in str(row.get("Name", "")) for x in [
                "University of Louisville", "Texas A&M", "University of Kansas",
                "University of Miami", "University of Nebraska", "North Carolina State University",
                "Arizona State University", "Grambling State University", "Indiana University",
                "University of Washington", "NC State", "Nebraska", "New Zealand Rugby",
                "Texas Tech", "Hoosiers", "Huskies", "Georgia Tech", "Yellow Jackets",
                "Kansas Jayhawks", "Alcorn State", "Arkansas Pine Bluff",
                "Mississippi State University", "Alabama State"
            ]) or
            any(x in str(row.get("PIM - Teams", "")) for x in [
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
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Hellcat" in str(row.get("Name", "")) else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Dame 8" in str(row.get("Name", "")) else
        "Pants" if pd.isna(row["PIM adidas - Product Types"]) and "Pants" in str(row.get("Name", "")) else
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Bike Shoes" in str(row.get("Name", "")) else
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Cycling" in str(row.get("Name", "")) else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Rivalry High" in str(row.get("Name", "")) else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM adidas - Product Types"]) and "High Tops" in str(row["PIM adidas - Product Types"]) else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Run 70s Shoes" in str(row.get("Name", "")) else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Run 80s Shoes" in str(row.get("Name", "")) else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Puig" in str(row.get("Name", "")) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Samba" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Gazelle" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "SL 72" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Country" in str(row["PIM - Product Line (sportsub)"]) else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.isna(row["PIM - Product Line (sportsub)"]) and "Originals" in str(row["PIM - Label"]) and "Handball Spezial" in str(row.get("Name", "")) else
        "Slides;Platform" if pd.isna(row["PIM adidas - Product Types"]) and "Platform" in str(row.get("Name", "")) and "Slides" in str(row["PIM adidas - Product Types"]) else
        "Boots" if pd.isna(row["PIM adidas - Product Types"]) and ("Boot" in str(row.get("Name", "")) or "Boots" in str(row.get("Name", ""))) else
        "Platform;Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and any(x in str(row.get("Name", "")) for x in ["Bold", "Platform", "XLG", "Sambae"]) else
        "Platform;Clogs" if pd.isna(row["PIM adidas - Product Types"]) and "Stan Smith Mule" in str(row.get("Name", "")) else
        "Balls" if pd.isna(row["PIM adidas - Product Types"]) and "Ball" in str(row.get("Name", "")) else
        "Vests" if pd.isna(row["PIM adidas - Product Types"]) and "Trail Running Vest" in str(row.get("Name", "")) else
        "Belts" if pd.isna(row["PIM adidas - Product Types"]) and "Belt" in str(row.get("Name", "")) else
        "Gloves;Gloves - Goalkeeper" if pd.isna(row["PIM adidas - Product Types"]) and "Goalkeeper Gloves" in str(row.get("Name", "")) else
        "Gloves" if pd.isna(row["PIM adidas - Product Types"]) and "Gloves" in str(row.get("Name", "")) else
        "Athletic & Sneakers;High Tops" if pd.isna(row["PIM adidas - Product Types"]) and any(x in str(row.get("Name", "")) for x in ["forum high", "forum hi", "Nizza high"]) else
        "Athletic & Sneakers;Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and "Spezial" in str(row.get("Name", "")) else
        "Pants;Track Suits - Track Pants;Track Suits" if pd.isna(row["PIM adidas - Product Types"]) and "Track Pants" in str(row.get("Name", "")) else
        "Bags;Bags - Crossbody" if pd.isna(row["PIM adidas - Product Types"]) and "Crossbody Bag" in str(row.get("Name", "")) else
        "Bag" if pd.isna(row["PIM adidas - Product Types"]) and "Bag" in str(row.get("Name", "")) else
        "Bags;Bags - Duffle Bags" if pd.isna(row["PIM adidas - Product Types"]) and "Duffle Bag" in str(row.get("Name", "")) else
        "Bags;Bags - Tote" if pd.isna(row["PIM adidas - Product Types"]) and "Tote Bag" in str(row.get("Name", "")) else
        "Platform;Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Gazelle Stack" in str(row.get("Name", "")) else
        row.get("PIM adidas - Product Types")
    ), axis=1)
    df["Enriched Surface"] = df.apply(lambda row: (
        "Multi Ground" if pd.isna(row["PIM - Surface"]) and "Multi ground" in str(row.get("Name", "")) else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "trail running" in str(row["PIM - Sport"]).lower() else 
        "Gravel" if pd.isna(row["PIM - Surface"]) and "The Gravel Cycling" in str(row.get("Name", "")) else 
        "Indoor" if pd.isna(row["PIM - Surface"]) and "THE INDOOR CYCLING SHOE" in str(row.get("Name", "")) else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Originals" in str(row["PIM - Label"]) and (
            "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]) or 
            "Athletic & Sneakers - T Toe" in str(row["PIM adidas - Product Types"])) else 
        "Artificial Grass" if pd.isna(row["PIM - Surface"]) and "Artificial Grass" in str(row.get("Name", "")) else 
        "Clay Court" if pd.isna(row["PIM - Surface"]) and "Clay" in str(row.get("Name", "")) else 
        "Firm Ground" if pd.isna(row["PIM - Surface"]) and ("Firm Ground" in str(row.get("Name", "")) or "FG" in str(row.get("Name", ""))) else 
        "Soft Ground" if pd.isna(row["PIM - Surface"]) and "Soft Ground" in str(row.get("Name", "")) else 
        "Gravel" if pd.isna(row["PIM - Surface"]) and any(x in str(row.get("Name", "")) for x in ["The Gravel", "Five Ten"]) else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "Trailcross" in str(row.get("Name", "")) else 
        "Turf" if pd.isna(row["PIM - Surface"]) and "Turf" in str(row.get("Name", "")) else 
        "Indoor-Court" if pd.isna(row["PIM - Surface"]) and "Indoor" in str(row.get("Name", "")) and "Soccer" in str(row["PIM - Sport"]) else 
        "Road;Treadmill" if pd.isna(row["PIM - Surface"]) and "Running" in str(row["PIM - Sport"]) and 
            "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]) and any(x in str(row.get("Name", "")) for x in [
                "4DFWD", "adizero", "Duramo", "Pureboost", "RDY", "Puremotion", "Rapida", "Response", "RunFalcon", 
                "Solar", "speedmotion", "Supernova", "Switch FWD", "Ultrabounce", "Tensaur", "X9000"]) else 
        "Track" if pd.isna(row["PIM - Surface"]) and "Track & Field" in str(row["PIM - Sport"]) and "adizero" in str(row.get("Name", "")) else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "Trail Running" in str(row["PIM - Sport"]) and "Agravic" in str(row.get("Name", "")) else 
        "Road" if pd.isna(row["PIM - Surface"]) and any(x in str(row.get("Name", "")) for x in ["Velosamba", "The Road", "Velostan Smith"]) else 
        "Hard Court" if pd.isna(row["PIM - Surface"]) and any(x in str(row["PIM - Product Family (productlinestyle)"]) for x in [
            "adizero Cybersonic", "adizero ubersonic"]) else 
        "Clay Court" if pd.isna(row["PIM - Surface"]) and "Tennis" in str(row["PIM - Sport"]) and "Clay" in str(row.get("Name", "")) else 
        "Hard Court" if pd.isna(row["PIM - Surface"]) and any(x in str(row["PIM - Product Line (sportsub)"]) for x in [
            "Barricade", "CourtJam", "Avacourt", "GameCourt"]) else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Fear of God Athletics" in str(row["PIM - Label"]) and 
            "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]) else 
        "Indoor-Court;Hard Court" if pd.isna(row["PIM - Surface"]) and "Cross Em" in str(row.get("Name", "")) else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Running" in str(row["PIM - Sport"]) and 
            "Originals" in str(row["PIM - Label"]) and "Athletic & Sneakers" in str(row["PIM adidas - Product Types"]) else 
        row.get("PIM - Surface")
    ), axis=1)
    df["Enriched Athletes"] = df.apply(lambda row: (
        "Ant Edwards" if pd.isna(row["PIM - Athletes"]) and "Anthony Edwards" in str(row.get("Name", "")) else 
        "Donovan Mitchell" if pd.isna(row["PIM - Athletes"]) and any(x in str(row.get("Name", "")) for x in [
            "D.O.N", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8", "D.O.N. Issue 5"]) else 
        "Damian Lillard" if pd.isna(row["PIM - Athletes"]) and any(x in str(row.get("Name", "")) for x in ["Dame 8", "Dame"]) else 
        "Lionel Messi" if pd.isna(row["PIM - Athletes"]) and "Messi" in str(row.get("Name", "")) else 
        "Trae Young" if pd.isna(row["PIM - Athletes"]) and any(x in str(row.get("Name", "")) for x in ["Trae", "Trae Young", "Trae Unlimited"]) else 
        "James Harden" if pd.isna(row["PIM - Athletes"]) and "Harden" in str(row.get("Name", "")) else 
        "Tyshawn Jones" if pd.isna(row["PIM - Athletes"]) and "Tyshawn" in str(row.get("Name", "")) else 
        "Dennis Busenitz" if pd.isna(row["PIM - Athletes"]) and "Busenitz" in str(row.get("Name", "")) else 
        "Lucas Puig" if pd.isna(row["PIM - Athletes"]) and "Puig" in str(row.get("Name", "")) else 
        "Mark Gonzalez" if pd.isna(row["PIM - Athletes"]) and (
            "Shmoofoil" in str(row.get("Name", "")) or "Shmoofoil" in str(row["PIM - Product Line (sportsub)"]) or 
            "Gonz" in str(row.get("Name", "")) or "Aloha Super" in str(row.get("Name", "")) or "Aloha Super" in str(row["PIM - Product Line (sportsub)"])) else 
        "Patrick Mahomes" if pd.isna(row["PIM - Athletes"]) and "Mahomes" in str(row.get("Name", "")) else 
        "Nora Vasconcellos" if pd.isna(row["PIM - Athletes"]) and "Nora " in str(row.get("Name", "")) else 
        "Heitor Da Silva" if pd.isna(row["PIM - Athletes"]) and "Pro Shell ADV x Heitor" in str(row.get("Name", "")) else 
        "Kader Sylla" if pd.isna(row["PIM - Athletes"]) and "Kader" in str(row.get("Name", "")) else 
        "Henry Jones" if pd.isna(row["PIM - Athletes"]) and "Henry Jones" in str(row.get("Name", "")) else 
        "Jude Bellingham" if pd.isna(row["PIM - Athletes"]) and "Jude Bellingham" in str(row.get("Name", "")) else 
        "Lamine Yamal" if pd.isna(row["PIM - Athletes"]) and "Lamine" in str(row.get("Name", "")) else 
        "George Russell" if pd.isna(row["PIM - Athletes"]) and "George Russell" in str(row.get("Name", "")) else 
        "Kimi Antonelli" if pd.isna(row["PIM - Athletes"]) and "Kimi Antonelli" in str(row.get("Name", "")) else 
        row.get("PIM - Athletes")
    ), axis=1)
    df["Enriched Teams"] = df.apply(lambda row: (
        "Atlanta United" if pd.isna(row["PIM - Teams"]) and "Atlanta United" in str(row.get("Name", "")) else 
        "Austin FC" if pd.isna(row["PIM - Teams"]) and "Austin FC" in str(row.get("Name", "")) else 
        "CF Montreal" if pd.isna(row["PIM - Teams"]) and "CF Montreal" in str(row.get("Name", "")) else 
        "Charlotte FC" if pd.isna(row["PIM - Teams"]) and "Charlotte FC" in str(row.get("Name", "")) else 
        "Chicago Fire" if pd.isna(row["PIM - Teams"]) and "Chicago Fire" in str(row.get("Name", "")) else 
        "Colorado Rapids" if pd.isna(row["PIM - Teams"]) and "Colorado Rapids" in str(row.get("Name", "")) else 
        "Columbus Crew" if pd.isna(row["PIM - Teams"]) and "Columbus Crew" in str(row.get("Name", "")) else 
        "D.C. United" if pd.isna(row["PIM - Teams"]) and "D.C. United" in str(row.get("Name", "")) else 
        "Cincinnati FC" if pd.isna(row["PIM - Teams"]) and "FC Cincinnati" in str(row.get("Name", "")) else 
        "Dallas FC" if pd.isna(row["PIM - Teams"]) and "FC Dallas" in str(row.get("Name", "")) else 
        "Houston Dynamo" if pd.isna(row["PIM - Teams"]) and "Houston Dynamo" in str(row.get("Name", "")) else 
        "Inter Miami CF" if pd.isna(row["PIM - Teams"]) and "Inter Miami CF" in str(row.get("Name", "")) else 
        "Los Angeles Football Club" if pd.isna(row["PIM - Teams"]) and ("Los Angeles Football Club" in str(row.get("Name", "")) or "Los Angeles FC" in str(row.get("Name", ""))) else 
        "Manchester United" if pd.isna(row["PIM - Teams"]) and "Manchester United" in str(row.get("Name", "")) else 
        "Minnesota United" if pd.isna(row["PIM - Teams"]) and "Minnesota United" in str(row.get("Name", "")) else 
        "Nashville SC" if pd.isna(row["PIM - Teams"]) and "Nashville SC" in str(row.get("Name", "")) else 
        "New England Revolution" if pd.isna(row["PIM - Teams"]) and "New England Revolution" in str(row.get("Name", "")) else 
        "New York City FC" if pd.isna(row["PIM - Teams"]) and "New York City FC" in str(row.get("Name", "")) else 
        "New York Red Bulls" if pd.isna(row["PIM - Teams"]) and "New York Red Bulls" in str(row.get("Name", "")) else 
        "Orlando City SC" if pd.isna(row["PIM - Teams"]) and "Orlando City SC" in str(row.get("Name", "")) else 
        "Philadelphia Union" if pd.isna(row["PIM - Teams"]) and "Philadelphia Union" in str(row.get("Name", "")) else 
        "Real Madrid" if pd.isna(row["PIM - Teams"]) and "Real Madrid" in str(row.get("Name", "")) else 
        "Portland Timbers" if pd.isna(row["PIM - Teams"]) and "Portland Timbers" in str(row.get("Name", "")) else 
        "Real Salt Lake" if pd.isna(row["PIM - Teams"]) and "Real Salt Lake" in str(row.get("Name", "")) else 
        "San Jose Earthquakes" if pd.isna(row["PIM - Teams"]) and "San Jose Earthquakes" in str(row.get("Name", "")) else 
        "Seattle Sounders FC" if pd.isna(row["PIM - Teams"]) and "Seattle Sounders FC" in str(row.get("Name", "")) else 
        "Sporting Kansas City" if pd.isna(row["PIM - Teams"]) and "Sporting Kansas City" in str(row.get("Name", "")) else 
        "St Louis City SC" if pd.isna(row["PIM - Teams"]) and "St Louis CITY SC" in str(row.get("Name", "")) else 
        "Toronto FC" if pd.isna(row["PIM - Teams"]) and "Toronto FC" in str(row.get("Name", "")) else 
        "Vancouver Whitecaps" if pd.isna(row["PIM - Teams"]) and "Vancouver Whitecaps" in str(row.get("Name", "")) else 
        "Jamaica" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["Jamaica Beckenbauer", "Jamaica OG", "Jamaica"]) else 
        "Tampa Bay Lightning" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["Lightning Third", "Tampa Bay"]) else 
        "Arsenal" if pd.isna(row["PIM - Teams"]) and "Arsenal" in str(row.get("Name", "")) else 
        "Juventus" if pd.isna(row["PIM - Teams"]) and "Juventus" in str(row.get("Name", "")) else 
        "Argentina" if pd.isna(row["PIM - Teams"]) and "Argentina" in str(row.get("Name", "")) else 
        "Spain" if pd.isna(row["PIM - Teams"]) and "Spain" in str(row.get("Name", "")) else 
        "Schalke 04" if pd.isna(row["PIM - Teams"]) and "FC Schalke" in str(row.get("Name", "")) else 
        "Scotland" if pd.isna(row["PIM - Teams"]) and "Scotland 24" in str(row.get("Name", "")) else 
        "Italy" if pd.isna(row["PIM - Teams"]) and "Italy" in str(row.get("Name", "")) else 
        "Celtic FC" if pd.isna(row["PIM - Teams"]) and "Celtic FC" in str(row.get("Name", "")) else 
        "Sweden" if pd.isna(row["PIM - Teams"]) and "Sweden" in str(row.get("Name", "")) else 
        "Algeria" if pd.isna(row["PIM - Teams"]) and "Algeria 22" in str(row.get("Name", "")) else 
        "FC Girondins Bordeaux" if pd.isna(row["PIM - Teams"]) and "Girondins de Bordeaux" in str(row.get("Name", "")) else 
        "Hungary" if pd.isna(row["PIM - Teams"]) and "Hungary 24" in str(row.get("Name", "")) else 
        "Colombia" if pd.isna(row["PIM - Teams"]) and "Colombia 24" in str(row.get("Name", "")) else 
        "FC Nürnberg" if pd.isna(row["PIM - Teams"]) and "FC Nürnberg" in str(row.get("Name", "")) else 
        "Leeds United FC" if pd.isna(row["PIM - Teams"]) and "Leeds United FC" in str(row.get("Name", "")) else 
        "Black Ferns" if pd.isna(row["PIM - Teams"]) and "Black Ferns" in str(row.get("Name", "")) else 
        "Mexico" if pd.isna(row["PIM - Teams"]) and "Mexico" in str(row.get("Name", "")) else 
        "Fulham FC" if pd.isna(row["PIM - Teams"]) and "Fulham FC" in str(row.get("Name", "")) else 
        "Racing Club de Strasbourg" if pd.isna(row["PIM - Teams"]) and "RC Strasbourg" in str(row.get("Name", "")) else 
        "AS Roma" if pd.isna(row["PIM - Teams"]) and "AS Roma" in str(row.get("Name", "")) else 
        "Belgium" if pd.isna(row["PIM - Teams"]) and "Belgium" in str(row.get("Name", "")) else 
        "Wales" if pd.isna(row["PIM - Teams"]) and "Wales 24" in str(row.get("Name", "")) else 
        "All Blacks" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["All Blacks", "New Zealand Rugby"]) else 
        "FC Union Berlin" if pd.isna(row["PIM - Teams"]) and "FC Union Berlin" in str(row.get("Name", "")) else 
        "Hamburger SV" if pd.isna(row["PIM - Teams"]) and "Hamburger SV" in str(row.get("Name", "")) else 
        "Northern Ireland" if pd.isna(row["PIM - Teams"]) and "Northern Ireland" in str(row.get("Name", "")) else 
        "France" if pd.isna(row["PIM - Teams"]) and "France" in str(row.get("Name", "")) else 
        "Germany" if pd.isna(row["PIM - Teams"]) and "Germany" in str(row.get("Name", "")) else 
        "LA Galaxy" if pd.isna(row["PIM - Teams"]) and "LA Galaxy" in str(row.get("Name", "")) else 
        "Olympique Lyon" if pd.isna(row["PIM - Teams"]) and "Olympique Lyonnais" in str(row.get("Name", "")) else 
        "Chile" if pd.isna(row["PIM - Teams"]) and "Chile 24" in str(row.get("Name", "")) else 
        "Leicester City" if pd.isna(row["PIM - Teams"]) and "Leicester City FC" in str(row.get("Name", "")) else 
        "AFC Ajax" if pd.isna(row["PIM - Teams"]) and "Ajax" in str(row.get("Name", "")) else 
        "Boca Juniors" if pd.isna(row["PIM - Teams"]) and "Boca Juniors" in str(row.get("Name", "")) else 
        "FC Bayern Munich" if pd.isna(row["PIM - Teams"]) and "FC Bayern" in str(row.get("Name", "")) else 
        "San Diego FC" if pd.isna(row["PIM - Teams"]) and "San Diego FC" in str(row.get("Name", "")) else 
        "Tigres" if pd.isna(row["PIM - Teams"]) and "Tigres UANL" in str(row.get("Name", "")) else 
        "Arsenal FC" if pd.isna(row["PIM - Teams"]) and "AFC " in str(row.get("Name", "")) else 
        "Louisville Cardinals" if pd.isna(row["PIM - Teams"]) and "University of Louisville" in str(row.get("Name", "")) else 
        "Texas A&M Aggies" if pd.isna(row["PIM - Teams"]) and "Texas A&M" in str(row.get("Name", "")) else 
        "Kansas Jayhawks" if pd.isna(row["PIM - Teams"]) and "University of Kansas" in str(row.get("Name", "")) else 
        "Miami Hurricanes" if pd.isna(row["PIM - Teams"]) and "University of Miami" in str(row.get("Name", "")) else 
        "Nebraska Cornhuskers" if pd.isna(row["PIM - Teams"]) and ("University of Nebraska" in str(row.get("Name", "")) or "Nebraska" in str(row.get("Name", ""))) else 
        "Mercedes AMG Petronas Formula One Team" if pd.isna(row["PIM - Teams"]) and "Motorsport" in str(row["PIM - Sport"]) and "Mercedes" in str(row.get("Name", "")) else 
        "NC State Wolfpack" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["North Carolina State University", "NC State"]) else 
        "Arizona State University" if pd.isna(row["PIM - Teams"]) and "Arizona State University" in str(row.get("Name", "")) else 
        "Grambling State Tigers" if pd.isna(row["PIM - Teams"]) and "Grambling State University" in str(row.get("Name", "")) else 
        "Indiana Hoosiers" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["Indiana University", "Hoosiers"]) else 
        "Washington Huskies" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["University of Washington", "Huskies"]) else 
        "Georgia Tech" if pd.isna(row["PIM - Teams"]) and any(x in str(row.get("Name", "")) for x in ["Yellow Jackets", "Georgia Tech"]) else 
        "Alcorn State Braves" if pd.isna(row["PIM - Teams"]) and "Alcorn State" in str(row.get("Name", "")) else 
        "Arkansas-Pine Bluff Golden Lions" if pd.isna(row["PIM - Teams"]) and "Arkansas Pine Bluff" in str(row.get("Name", "")) else 
        "Alabama State Hornets" if pd.isna(row["PIM - Teams"]) and "Alabama State" in str(row.get("Name", "")) else 
        "Georgia Tech" if pd.isna(row["PIM - Teams"]) and "Georgia Tech" in str(row.get("Name", "")) else 
        row.get("PIM - Teams")
    ), axis=1)
    df["Enriched Team Kits"] = df.apply(lambda row: (
        "Home Kit" if pd.isna(row.get("PIM - Team Kits")) and "Home" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Home Kit" if pd.isna(row.get("PIM - Team Kits")) and "Home" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")) else
        "Away Kit" if pd.isna(row.get("PIM - Team Kits")) and "Away" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Away Kit" if pd.isna(row.get("PIM - Team Kits")) and "Away" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")) else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")) else
        "Pre-Match" if pd.isna(row.get("PIM - Team Kits")) and "Pre-Match" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Pre-Match" if pd.isna(row.get("PIM - Team Kits")) and "Pre-Match" in str(row.get("Name", "")) and "Hockey" in str(row.get("PIM - Sport", "")) else
        "Home Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Authentic Home" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Away Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Authentic Away" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Home Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "AU Home" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Away Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "AU Away" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Fourth Kit" if pd.isna(row.get("PIM - Team Kits")) and "Fourth" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Fourth Kit" if pd.isna(row.get("PIM - Team Kits")) and "Fourth" in str(row.get("Name", "")) and "Lifestyle" in str(row.get("PIM - Sport", "")) else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Driver" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "Driver" in str(row.get("Name", "")) else
        "Mechanic" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "mechanics" in str(row.get("Name", "")) else
        "Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "authentic" in str(row.get("Name", "")) else
        "Replica" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport" in str(row.get("PIM - Sport", "")) and "replica" in str(row.get("Name", "")) else
        row.get("PIM - Team Kits")
    ), axis=1)
    df["Enriched Technologies"] = df.apply(lambda row: (
        "COLD.RDY" if pd.isna(row.get("PIM - Technologies")) and "COLD.RDY" in str(row.get("Name", "")) else
        "HEAT.RDY" if pd.isna(row.get("PIM - Technologies")) and "HEAT.RDY" in str(row.get("Name", "")) else
        "RAIN.RDY" if pd.isna(row.get("PIM - Technologies")) and "RAIN.RDY" in str(row.get("Name", "")) else
        "SUMMER.RDY" if pd.isna(row.get("PIM - Technologies")) and "SUMMER.RDY" in str(row.get("Name", "")) else
        "WIND.RDY" if pd.isna(row.get("PIM - Technologies")) and "WIND.RDY" in str(row.get("Name", "")) else
        "GORE-TEX" if pd.isna(row.get("PIM - Technologies")) and "Gore-tex" in str(row.get("Name", "")) else
        "GORE-TEX" if pd.isna(row.get("PIM - Technologies")) and "GTX" in str(row.get("Name", "")) else
        "AEROREADY" if pd.isna(row.get("PIM - Technologies")) and "AEROREADY" in str(row.get("Name", "")) else
        "4D" if pd.isna(row.get("PIM - Technologies")) and "4D" in str(row.get("Name", "")) else
        "Boost" if pd.isna(row.get("PIM - Technologies")) and "Boost" in str(row.get("Name", "")) else
        "Bounce" if pd.isna(row.get("PIM - Technologies")) and "Bounce" in str(row.get("Name", "")) else
        "Dreamstrike" if pd.isna(row.get("PIM - Technologies")) and "Supernova" in str(row.get("Name", "")) else
        "Techfit" if pd.isna(row.get("PIM - Technologies")) and "Techfit" in str(row.get("Name", "")) else
        "WINTER.RDY" if pd.isna(row.get("PIM - Technologies")) and "WINTER.RDY" in str(row.get("Name", "")) else
        "CORDURA" if pd.isna(row.get("PIM - Technologies")) and "CORDURA" in str(row.get("Name", "")) else
        "PrimaLoft;EVA" if pd.isna(row.get("PIM - Technologies")) and "PUFFYLETTE" in str(row.get("Name", "")) else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "SL 72" in str(row.get("Name", "")) else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Ultraboost 5" in str(row.get("Name", "")) else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "Country" in str(row.get("Name", "")) else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Anthony Edwards" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "D.O.N" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Trae Young" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) else
        "Bounce" if pd.isna(row.get("PIM - Technologies")) and "Tech Response" in str(row.get("Name", "")) else
        "Torsion" if pd.isna(row.get("PIM - Technologies")) and "Avacourt" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Bounce;Torsion" if pd.isna(row.get("PIM - Technologies")) and "Courtjam Control" in str(row.get("Name", "")) else
        "Bounce;EVA" if pd.isna(row.get("PIM - Technologies")) and "GameCourt" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Torsion;Boost" if pd.isna(row.get("PIM - Technologies")) and "SoleMatch" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "Country Soft" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Cloudfoam" if pd.isna(row.get("PIM - Technologies")) and "RunFalcon" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "PrimaLoft" if pd.isna(row.get("PIM - Technologies")) and "PrimaLoft" in str(row.get("Name", "")) else
        row.get("PIM - Technologies")
    ), axis=1)
    df["Enriched Features"] = df.apply(lambda row: (
        "Lightweight;Cushioned" if pd.isna(row.get("PIM - Features")) and "SL 72" in str(row.get("Name", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Cushion" in str(row.get("Name", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Ozmillen" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Water-Repellent;Cushioned" if pd.isna(row.get("PIM - Features")) and "Puffylette" in str(row.get("Name", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "EVA" in str(row.get("PIM - Technologies", "")) else
        "Spikeless" if pd.isna(row.get("PIM - Features")) and "Spikeless" in str(row.get("Name", "")) else
        "Waterproof;Breathable" if pd.isna(row.get("PIM - Features")) and "GORE-TEX" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "LIGHTSTRIKE PRO" in str(row.get("PIM - Technologies", "")) else
        "Pleated" if pd.isna(row.get("PIM - Features")) and "Pleated" in str(row.get("Name", "")) else
        "Reversible" if pd.isna(row.get("PIM - Features")) and "Reversible" in str(row.get("Name", "")) else
        "Cushioned;Lightweight" if pd.isna(row.get("PIM - Features")) and "GameCourt" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Lo profile" in str(row.get("Name", "")) else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Taekwondo" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Japan OG" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Tokyo" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Lightstrike" if pd.isna(row.get("PIM - Features")) and "D.O.N" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Bounce" if pd.isna(row.get("PIM - Features")) and "Dame" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Boost;Lightstrike" if pd.isna(row.get("PIM - Features")) and "Harden" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Boost;Lightstrike" if pd.isna(row.get("PIM - Features")) and "Anthony Edwards" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "4D" in str(row.get("PIM - Technologies", "")) else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "AEROREADY" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Boost" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Bounce" in str(row.get("PIM - Technologies", "")) else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climachill" in str(row.get("PIM - Technologies", "")) else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climacool" in str(row.get("PIM - Technologies", "")) else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climacool " in str(row.get("PIM - Technologies", "")) else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climaheat" in str(row.get("PIM - Technologies", "")) else
        "Breathable;Windproof;Water-Repellent;Waterproof" if pd.isna(row.get("PIM - Features")) and "Climaproof" in str(row.get("PIM - Technologies", "")) else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climawarm" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Cloudfoam" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "CLOUDFOAM PLUS" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Dreamstrike" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Dreamstrike+" in str(row.get("PIM - Technologies", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and "Energyrods" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "EVA" in str(row.get("PIM - Technologies", "")) else
        "Period Proof" if pd.isna(row.get("PIM - Features")) and "Flow Shield" in str(row.get("PIM - Technologies", "")) else
        "Breathable;Compression" if pd.isna(row.get("PIM - Features")) and "Formotion" in str(row.get("PIM - Technologies", "")) else
        "Waterproof;Windproof;Breathable" if pd.isna(row.get("PIM - Features")) and "GORE-TEX" in str(row.get("PIM - Technologies", "")) else
        "Lightweight;Cushioned" if pd.isna(row.get("PIM - Features")) and "LIGHT BOOST" in str(row.get("PIM - Technologies", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Lightmotion" in str(row.get("PIM - Technologies", "")) else
        "Cushioned;Lightweight" if pd.isna(row.get("PIM - Features")) and "Lightstrike" in str(row.get("PIM - Technologies", "")) else
        "Cushioned;Lightweight;Stability" if pd.isna(row.get("PIM - Features")) and "LIGHTSTRIKEPRO" in str(row.get("PIM - Technologies", "")) else
        "Breathable" if pd.isna(row.get("PIM - Features")) and "Primeknit" in str(row.get("PIM - Technologies", "")) else
        "Waterproof" if pd.isna(row.get("PIM - Features")) and "RAIN.RDY" in str(row.get("PIM - Technologies", "")) else
        "Shock Absorption;Lightweight" if pd.isna(row.get("PIM - Features")) and "REPETITOR" in str(row.get("PIM - Technologies", "")) else
        "Shock Absorption;Lightweight" if pd.isna(row.get("PIM - Features")) and "REPETITOR+" in str(row.get("PIM - Technologies", "")) else
        "Grip;Stability" if pd.isna(row.get("PIM - Features")) and "Stealth C4" in str(row.get("PIM - Technologies", "")) else
        "Compression" if pd.isna(row.get("PIM - Features")) and "Techfit" in str(row.get("PIM - Technologies", "")) else
        "Grip;Stability" if pd.isna(row.get("PIM - Features")) and "Traxion" in str(row.get("PIM - Technologies", "")) else
        "Grip" if pd.isna(row.get("PIM - Features")) and "Anthony Edwards 1" in str(row.get("PIM - Product Family (productlinestyle)", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) else
        "Spikeless" if pd.isna(row.get("PIM - Features")) and "Golf" in str(row.get("PIM - Sport", "")) and "Spikeless" in str(row.get("Name", "")) else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Golf" in str(row.get("PIM - Sport", "")) and "Gazelle" in str(row.get("PIM - Product Line (sportsub)", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and "Football" in str(row.get("PIM - Sport", "")) and "adizero Electric" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport in str(row.get("PIM - Sport", "")) for sport in ["Softball", "Baseball"]) and "adizero Electric" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport in str(row.get("PIM - Sport", "")) for sport in ["Softball", "Baseball"]) and "adizero Impact" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport in str(row.get("PIM - Sport", "")) for sport in ["Softball", "Baseball"]) and "adizero Instinct" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        row.get("PIM - Features")
    ), axis=1)
    df["Enriched Closure"] = df.apply(lambda row: (
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "Country XLG" in str(row.get("Name", "")) else
        "Slip On" if pd.isna(row.get("PIM - Closure")) and "Slip On" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Laceless" if pd.isna(row.get("PIM - Closure")) and "Laceless" in str(row.get("Name", "")) and "Soccer" in str(row.get("PIM - Sport", "")) else
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "NMD 360" in str(row.get("Name", "")) else
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "Superstar 360" in str(row.get("Name", "")) else
        "Slip On" if pd.isna(row.get("PIM - Closure")) and "adilette 22" in str(row.get("PIM - Product Family (productlinestyle)", "")) else
        "BOA Laces" if pd.isna(row.get("PIM - Closure")) and "BOA" in str(row.get("Name", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) else
        row.get("PIM - Closure")
    ), axis=1)
    df["Enriched Best For"] = df.apply(lambda row: (
        'Race;Long Distance;Marathon' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "adizero" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "4D" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Comfort;Neutral' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Duramo" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Comfort;Everyday' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Supernova" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Comfort;Neutral' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Solar" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Neutral' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Response" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Everyday' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "Runfalcon" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Long Distance;Marathon' if pd.isna(row.get("PIM - Best For")) and "Running" in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers" in str(row.get("PIM adidas - Product Types", "")) and "adistar" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Speed;Agility;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "F50" in str(row.get("Name", "")) else 
        'Speed;Agility;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "F50" in str(row.get("Name", "")) else 
        'Speed;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Crazyfast" in str(row.get("Name", "")) else 
        'Speed;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "Crazyfast" in str(row.get("Name", "")) else 
        'Control;Inside;Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Copa" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Control;Outside;Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "Copa" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Agility;Accuracy;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" in str(row.get("PIM - Surface", "")) and "Predator" in str(row.get("PIM - Product Line (sportsub)", "")) else 
        'Agility;Accuracy;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer" in str(row.get("PIM - Sport", "")) and ("Cleats" in str(row.get("PIM adidas - Product Types", "")) or "Cleats - Turf" in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court" not in str(row.get("PIM - Surface", "")) and "Predator" in str(row.get("PIM - Product Line (sportsub)", "")) else 
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
        "On-Court" if pd.isna(row.get("PIM - Best For")) and any(name in str(row.get("Name", "")) for name in ["Anthony Edwards", "D.O.N", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8", "Dame 8", "Dame", "Trae", "Trae Unlimited"]) else 
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
    
