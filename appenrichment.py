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
    
