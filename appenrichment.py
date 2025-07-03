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
        "Agravic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "terrex agravic".lower() in str(row.get("Name", "")).lower() else
        "Samba;60s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "samba 62" in str(row.get("Name", "")).lower() else
        "Superstar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "superstar" in str(row.get("Name", "")).lower() else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten freerider" in str(row.get("Name", "")).lower() else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten aleon" in str(row.get("Name", "")).lower() else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten crawe" in str(row.get("Name", "")).lower() else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten hellcat" in str(row.get("Name", "")).lower() else
        "Hiangle" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten hiangle" in str(row.get("Name", "")).lower() else
        "Kestrel" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten kestrel" in str(row.get("Name", "")).lower() else
        "Kirigami" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten kirigami" in str(row.get("Name", "")).lower() else
        "NIAD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten niad" in str(row.get("Name", "")).lower() else
        "Sleuth" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten sleuth" in str(row.get("Name", "")).lower() else
        "Trailcross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "five ten trailcross" in str(row.get("Name", "")).lower() else
        "Adventure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Adventure", "Hyperturf", "Mocaturf", "Roverend", "Rovermule", "Superturf"]) else
        "Astir;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Astir".lower() in str(row.get("Name", "")).lower() else
        "Campus" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Campus".lower() in str(row.get("Name", "")).lower() else
        "Forum" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Forum".lower() in str(row.get("Name", "")).lower() else
        "Gazelle;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gazelle".lower() in str(row.get("Name", "")).lower() else
        "Nizza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Nizza".lower() in str(row.get("Name", "")).lower() else
        "NMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "NMD".lower() in str(row.get("Name", "")).lower() else
        "Oz;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Oz ".lower() in str(row.get("Name", "")).lower() else
        "Samba;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Samba".lower() in str(row.get("Name", "")).lower() and "Cycling" not in str(row.get("Name", "")).lower() else
        "Shmoofoil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Shmoofoil".lower() in str(row.get("Name", "")).lower() else
        "Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stan Smith".lower() in str(row.get("Name", "")).lower() else
        "Adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puffylette".lower() in str(row.get("Name", "")).lower() else
        "Adifom" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Supernova".lower() in str(row.get("Name", "")).lower() else
        "adilette" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adilette".lower() in str(row.get("Name", "")).lower() else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["adizero", "Jumpstar", "DistanceStar", "Ubersonic 4", "Sprintstar", "Throwstar"]) else
        "Aeroimpact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aeroimpact".lower() in str(row.get("Name", "")).lower() else
        "Alphaboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["alphaboost", "alphaboost V1"]) else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa".lower() in str(row.get("Name", "")).lower() else
        "Fast Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Fast Impact".lower() in str(row.get("Name", "")).lower() else
        "Optime" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Optime".lower() in str(row.get("Name", "")).lower() else
        "Own the Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["OTR", "Own the Run"]) else
        "Power Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Power Impact".lower() in str(row.get("Name", "")).lower() else
        "Powerreact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerreact".lower() in str(row.get("Name", "")).lower() else
        "Predator" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Predator".lower() in str(row.get("Name", "")).lower() else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tiro".lower() in str(row.get("Name", "")).lower() else
        "Purelounge" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Purelounge".lower() in str(row.get("Name", "")).lower() else
        "Solar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Solarboost", "Solarcontrol", "Solarglide", "Solarmotion"]) else
        "Supernova" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Supernova".lower() in str(row.get("Name", "")).lower() else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost".lower() in str(row.get("Name", "")).lower() else
        "4DFWD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "4DFWD".lower() in str(row.get("Name", "")).lower() else
        "Hellcat" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Hellcat".lower() in str(row.get("Name", "")).lower() else
        "Freerider" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Freerider".lower() in str(row.get("Name", "")).lower() else
        "Aleon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Aleon".lower() in str(row.get("Name", "")).lower() else
        "Crawe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Five Ten Crawe".lower() in str(row.get("Name", "")).lower() else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Agravic Speed Ultra".lower() in str(row.get("Name", "")).lower() else
        "AX4" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX AX4".lower() in str(row.get("Name", "")).lower() else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Eastrail".lower() in str(row.get("Name", "")).lower() else
        "Free Hiker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Free Hiker".lower() in str(row.get("Name", "")).lower() else
        "Skychaser" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Skychaser".lower() in str(row.get("Name", "")).lower() else
        "Swift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Swift".lower() in str(row.get("Name", "")).lower() else
        "Techrock" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Techrock".lower() in str(row.get("Name", "")).lower() else
        "Voyager" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Voyager".lower() in str(row.get("Name", "")).lower() else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xperior".lower() in str(row.get("Name", "")).lower() else
        "Xploric" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TERREX Xploric".lower() in str(row.get("Name", "")).lower() else
        "Coreflow" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Coreflow Studio".lower() in str(row.get("Name", "")).lower() or "Coreflow Luxe".lower() in str(row.get("Name", "")).lower()) else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cloudfoam Pure".lower() in str(row.get("Name", "")).lower() else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Codechaos".lower() in str(row.get("Name", "")).lower() else
        "Cross Em" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Cross Em".lower() in str(row.get("Name", "")).lower() else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["DON", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8"]) else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed for Training".lower() in str(row.get("Name", "")).lower() else
        "Exhibit" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Exhibit".lower() in str(row.get("Name", "")).lower() else
        "Go-To" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Go-To".lower() in str(row.get("Name", "")).lower() else
        "Impact FLX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Impact FLX".lower() in str(row.get("Name", "")).lower() else
        "Lillard;Dame" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Dame 8".lower() in str(row.get("Name", "")).lower() or "Dame".lower() in str(row.get("Name", "")).lower()) else
        "MC80" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC80".lower() in str(row.get("Name", "")).lower() else
        "MC87" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MC87".lower() in str(row.get("Name", "")).lower() else
        "Retrocross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retrocross".lower() in str(row.get("Name", "")).lower() else
        "S2G" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "S2G".lower() in str(row.get("Name", "")).lower() else
        "Soulstride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soulstride".lower() in str(row.get("Name", "")).lower() else
        "Swift Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Swift Run".lower() in str(row.get("Name", "")).lower() else
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
        "Trailmaker" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Trailmaker".lower() in str(row.get("Name", "")).lower() else
        "TrueCasuals" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TrueCasuals".lower() in str(row.get("Name", "")).lower() else
        "TruePace" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePace".lower() in str(row.get("Name", "")).lower() else
        "Ultimate365" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultimate365".lower() in str(row.get("Name", "")).lower() else
        "ZG" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("ZG23".lower() in str(row.get("Name", "")).lower() or "ZG21".lower() in str(row.get("Name", "")).lower()) else
        "Zoysia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Zoysia".lower() in str(row.get("Name", "")).lower() else
        "Trae" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Trae".lower() in str(row.get("Name", "")).lower() or "Trae Unlimited".lower() in str(row.get("Name", "")).lower()) else
        "Ultraboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultraboost light".lower() in str(row.get("Name", "")).lower() else
        "Tiro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TIRO24".lower() in str(row.get("Name", "")).lower() else
        "Copa" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Copa Gloro".lower() in str(row.get("Name", "")).lower() else
        "True Purpose" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TruePurpose".lower() in str(row.get("Name", "")).lower() else
        "Response" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Response".lower() in str(row.get("Name", "")).lower() else
        "Daily" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Daily".lower() in str(row.get("Name", "")).lower() else
        "Impact" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Five Ten Impact".lower() in str(row.get("Name", "")).lower() or "Five Ten".lower() in str(row.get("Name", "")).lower()) else
        "Futurecraft" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Futurecraft".lower() in str(row.get("Name", "")).lower() else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Run 80s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 80s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Earthlight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Earthlight".lower() in str(row.get("Name", "")).lower() else
        "Eastrail" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Eastrail".lower() in str(row.get("Name", "")).lower() else
        "VULCRAID3R" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VULCRAID3R".lower() in str(row.get("Name", "")).lower() else
        "Sport Pro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adidas x LEGO® Sport Pro Running Shoes".lower() in str(row.get("Name", "")).lower() else
        "Questar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Questar".lower() in str(row.get("Name", "")).lower() else
        "Tensaur" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tensaur".lower() in str(row.get("Name", "")).lower() else
        "Summervent" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Summervent".lower() in str(row.get("Name", "")).lower() else
        "Puig" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puig".lower() in str(row.get("Name", "")).lower() else
        "CourtJam" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "CourtJam".lower() in str(row.get("Name", "")).lower() else
        "Avacourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avacourt".lower() in str(row.get("Name", "")).lower() else
        "Tracefinder" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tracefinder".lower() in str(row.get("Name", "")).lower() else
        "QT Racer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "QT Racer".lower() in str(row.get("Name", "")).lower() else
        "Start Your Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Start Your Run".lower() in str(row.get("Name", "")).lower() else
        "Activeride" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Activeride 2.0".lower() in str(row.get("Name", "")).lower() else
        "ZNCHILL" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNCHILL".lower() in str(row.get("Name", "")).lower() else
        "Solarmotion" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solarmotion".lower() in str(row.get("Name", "")).lower() else
        "Kantana" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Kantana Shoes".lower() in str(row.get("Name", "")).lower() else
        "Midcity" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Midcity Low Shoes".lower() in str(row.get("Name", "")).lower() else
        "Winterplay" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Winterplay".lower() in str(row.get("Name", "")).lower() else
        "X" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "X League".lower() in str(row.get("Name", "")).lower() else
        "Retro" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Retro Graphic", "Retro Quarter"]) else
        "RDY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["COLD.RDY", "HEAT.RDY", "RAIN.RDY", "SUMMER.RDY", "WIND.RDY"]) else
        "Top Ten" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Top Ten".lower() in str(row.get("Name", "")).lower() else
        "Spezial;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and pd.notna(row.get("PIM - Label")) and "Originals".lower() in str(row.get("PIM - Label", "")).lower() and "Handball Spezial".lower() in str(row.get("Name", "")).lower() else
        "Tyshawn" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tyshawn".lower() in str(row.get("Name", "")).lower() else
        "adiFOM;Stan Smith" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Stan Smith".lower() in str(row.get("Name", "")).lower() else
        "adilette;adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adifom Adilette".lower() in str(row.get("Name", "")).lower() else
        "adiFOM" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adiFOM".lower() in str(row.get("Name", "")).lower() else
        "BYW Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BYW Select".lower() in str(row.get("Name", "")).lower() else
        "ADI2000" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADI2000".lower() in str(row.get("Name", "")).lower() else
        "Matchbreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak".lower() in str(row.get("Name", "")).lower() else
        "Crazy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy".lower() in str(row.get("Name", "")).lower() else
        "Crazyflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazyflight".lower() in str(row.get("Name", "")).lower() else
        "Adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adibreak".lower() in str(row.get("Name", "")).lower() else
        "Select" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Select".lower() in str(row.get("Name", "")).lower() else
        "All Me" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "All Me ".lower() in str(row.get("Name", "")).lower() else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["D4T", "Designed-for-Training"]) else
        "SL 72;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "SL 72".lower() in str(row.get("Name", "")).lower() else
        "Country;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Country".lower() in str(row.get("Name", "")).lower() else
        "Retropy;2000s;70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Retropy".lower() in str(row.get("Name", "")).lower() else
        "adicolor;Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Arsenal Beckenbauer", "Real Madrid Beckenbauer", "Juventus Beckenbauer", "Adicolor Classics Beckenbauer"
        ]) else
        "adicolor;VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor VRCT".lower() in str(row.get("Name", "")).lower() else
        "Beckenbauer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Beckenbauer".lower() in str(row.get("Name", "")).lower() else
        "3MC" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "3MC".lower() in str(row.get("Name", "")).lower() else
        "adicolor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adicolor".lower() in str(row.get("Name", "")).lower() else
        "Adimatic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adimatic".lower() in str(row.get("Name", "")).lower() else
        "Adipower" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adipower".lower() in str(row.get("Name", "")).lower() else
        "Adistar" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adistar".lower() in str(row.get("Name", "")).lower() else
        "Avaflash" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avaflash".lower() in str(row.get("Name", "")).lower() else
        "AVRYN" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Avryn_X".lower() in str(row.get("Name", "")).lower() else
        "Barricade" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Barricade".lower() in str(row.get("Name", "")).lower() else
        "Busenitz" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Busenitz".lower() in str(row.get("Name", "")).lower() else
        "Dropset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Dropset".lower() in str(row.get("Name", "")).lower() else
        "Galaxy" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Galaxy".lower() in str(row.get("Name", "")).lower() else
        "Harden" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Harden".lower() in str(row.get("Name", "")).lower() else
        "Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Hoops".lower() in str(row.get("Name", "")).lower() else
        "Icon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Icon".lower() in str(row.get("Name", "")).lower() else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Matchbreak Super".lower() in str(row.get("Name", "")).lower() else
        "MYSHELTER" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "MYSHELTER".lower() in str(row.get("Name", "")).lower() else
        "Powerlift" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Powerlift".lower() in str(row.get("Name", "")).lower() else
        "Pureboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pureboost".lower() in str(row.get("Name", "")).lower() else
        "Rapida" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "RapidaSport".lower() in str(row.get("Name", "")).lower() else
        "Rivalry" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rivalry".lower() in str(row.get("Name", "")).lower() else
        "Sereno" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Sereno".lower() in str(row.get("Name", "")).lower() else
        "Stabil" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stabil".lower() in str(row.get("Name", "")).lower() else
        "Tango" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tango".lower() in str(row.get("Name", "")).lower() else
        "Tour360" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tour360".lower() in str(row.get("Name", "")).lower() else
        "ZX" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZX".lower() in str(row.get("Name", "")).lower() else
        "adicross" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adicross".lower() in str(row.get("Name", "")).lower() else
        "ZPLAASH" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZPLAASH".lower() in str(row.get("Name", "")).lower() else
        "adibreak" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ADBRK".lower() in str(row.get("Name", "")).lower() else
        "Lacombe" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lacombe".lower() in str(row.get("Name", "")).lower() else
        "Hoop York City" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["HYC", "Hoop York City"]) else
        "X" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["X Crazyfast", "X Speedportal"]) else
        "4DFWD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "4DFWD".lower() in str(row.get("Name", "")).lower() else
        "Own the Run" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Own the Run".lower() in str(row.get("Name", "")).lower() else
        "Ultrabounce" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultrabounce".lower() in str(row.get("Name", "")).lower() else
        "ALL SZN" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ALL SZN".lower() in str(row.get("Name", "")).lower() else
        "Duramo" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Duramo".lower() in str(row.get("Name", "")).lower() else
        "XPLR" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["X_PLR", "XPLR"]) else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Z.N.E".lower() in str(row.get("Name", "")).lower() else
        "City Escape" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "City Escape".lower() in str(row.get("Name", "")).lower() else
        "FortaRun" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "FortaRun".lower() in str(row.get("Name", "")).lower() else
        "RunFalcon" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "RunFalcon".lower() in str(row.get("Name", "")).lower() else
        "Racer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Racer TR".lower() in str(row.get("Name", "")).lower() else
        "VL Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VL Court".lower() in str(row.get("Name", "")).lower() else
        "Front Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Front Court".lower() in str(row.get("Name", "")).lower() else
        "Ubounce" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ubounce".lower() in str(row.get("Name", "")).lower() else
        "Breaknet" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Breaknet".lower() in str(row.get("Name", "")).lower() else
        "Grand Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Grand Court".lower() in str(row.get("Name", "")).lower() else
        "Postmove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Postmove".lower() in str(row.get("Name", "")).lower() else
        "Alphaboost" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "alphaboost".lower() in str(row.get("Name", "")).lower() else
        "Puremotion" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Puremotion".lower() in str(row.get("Name", "")).lower() else
        "Kaptir" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Kaptir".lower() in str(row.get("Name", "")).lower() else
        "ZNSORED" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNSORED".lower() in str(row.get("Name", "")).lower() else
        "Future Icons" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Future Icons".lower() in str(row.get("Name", "")).lower() else
        "Lite Racer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lite Racer".lower() in str(row.get("Name", "")).lower() else
        "Grand Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["grand court alpha", "Grand Court"]) else
        "Alphabounce" if pd.isna(row.get("PIM - Product Line (sportsub)")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["alphabounce", "Alphabounce+"]) else
        "adicane" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adicane".lower() in str(row.get("Name", "")).lower() else
        "Advantage" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "advantage".lower() in str(row.get("Name", "")).lower() else
        "Courtblock" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "courtblock".lower() in str(row.get("Name", "")).lower() else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNE".lower() in str(row.get("Name", "")).lower() else
        "Koln" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Koln".lower() in str(row.get("Name", "")).lower() else
        "Munchen" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Munchen".lower() in str(row.get("Name", "")).lower() else
        "The Total" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "The Total".lower() in str(row.get("Name", "")).lower() else
        "Amplimove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Amplimove".lower() in str(row.get("Name", "")).lower() else
        "Velostan" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Velostan".lower() in str(row.get("Name", "")).lower() else
        "Novaflight" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Novaflight".lower() in str(row.get("Name", "")).lower() else
        "VRCT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "VRCT".lower() in str(row.get("Name", "")).lower() else
        "Gamemode" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamemode".lower() in str(row.get("Name", "")).lower() else
        "Goletto" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Goletto".lower() in str(row.get("Name", "")).lower() else
        "Anthony Edwards" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anthony Edwards".lower() in str(row.get("Name", "")).lower() else
        "D.O.N" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "D.O.N".lower() in str(row.get("Name", "")).lower() else
        "Megaride;2000s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Megaride".lower() in str(row.get("Name", "")).lower() else
        "Centennial" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Centennial".lower() in str(row.get("Name", "")).lower() else
        "Aloha Super" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aloha Super".lower() in str(row.get("Name", "")).lower() else
        "adizero" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Takumi Sen".lower() in str(row.get("Name", "")).lower() else
        "Helionic" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Helionic".lower() in str(row.get("Name", "")).lower() else
        "Alphaskin" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Alphaskin".lower() in str(row.get("Name", "")).lower() else
        "Anylander" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Anylander".lower() in str(row.get("Name", "")).lower() else
        "Xperior" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Xperior".lower() in str(row.get("Name", "")).lower() else
        "EQT" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("equipment".lower() in str(row.get("Name", "")).lower() or "eqt".lower() in str(row.get("Name", "")).lower()) else
        "Dugout" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Baseball".lower() in str(row.get("PIM - Sport", "")) or "Softball".lower() in str(row.get("PIM - Sport", ""))) else
        "Beyond the Course" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and "Beyond".lower() in str(row.get("Name", "")).lower() else
        "CodeChaos" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and "Codechaos".lower() in str(row.get("Name", "")).lower() else
        "Clima" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Clima".lower() in str(row.get("Name", "")).lower() else
        "Everyset" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Everyset".lower() in str(row.get("Name", "")).lower() else
        "Rapidmove" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Rapidmove".lower() in str(row.get("Name", "")).lower() else
        "Stella Court" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Stella McCartney Court".lower() in str(row.get("Name", "")).lower() else
        "GameCourt" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gamecourt".lower() in str(row.get("Name", "")).lower() else
        "Solematch" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Solematch".lower() in str(row.get("Name", "")).lower() else
        "TLDR" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "TLDR".lower() in str(row.get("Name", "")).lower() else
        "Coursecup" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Coursecup".lower() in str(row.get("Name", "")).lower() else
        "Gym+" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Gym+".lower() in str(row.get("Name", "")).lower() else
        "Pacer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Pacer".lower() in str(row.get("Name", "")).lower() else
        "Designed for Training" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Designed-for-Training".lower() in str(row.get("Name", "")).lower() else
        "Run 70s" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Run 70s".lower() in str(row.get("Name", "")).lower() else
        "Lightblaze " if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Lightblaze".lower() in str(row.get("Name", "")).lower() else
        "ZNSORY" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "ZNSORY".lower() in str(row.get("Name", "")).lower() else
        "Aspyre" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Aspyre".lower() in str(row.get("Name", "")).lower() else
        "BRMD" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "BRMD".lower() in str(row.get("Name", "")).lower() else
        "Ultradream" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ultradream".lower() in str(row.get("Name", "")).lower() else
        "ZNE" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and "Z.N.E".lower() in str(row.get("Name", "")).lower() else
        "Spezialist" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Spezialist".lower() in str(row.get("Name", "")).lower() else
        "Ligra" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ligra".lower() in str(row.get("Name", "")).lower() else
        "Essentials" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "essentials".lower() in str(row.get("Name", "")).lower() else
        "Worldwide Hoops" if pd.isna(row.get("PIM - Product Line (sportsub)")) and ("Worldwide Hoops".lower() in str(row.get("Name", "")).lower() or "WWH ".lower() in str(row.get("Name", "")).lower()) else
        "adilenium" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "adilenium".lower() in str(row.get("Name", "")).lower() else
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
        "Initiation" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Initiation".lower() in str(row.get("Name", "")).lower() else
        "BB Legends" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Basketball Legends".lower() in str(row.get("Name", "")).lower() else
        "Crazy Lite" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Crazy lite".lower() in str(row.get("Name", "")).lower() else
        "Ballerina" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ballerina".lower() in str(row.get("Name", "")).lower() else
        "Palos Hills" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Palos Hills".lower() in str(row.get("Name", "")).lower() else
        "Seeulater" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Seeulater".lower() in str(row.get("Name", "")).lower() else
        "Superskate" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Superskate".lower() in str(row.get("Name", "")).lower() else
        "Italia" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Italia".lower() in str(row.get("Name", "")).lower() else
        "Montreal" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Montreal".lower() in str(row.get("Name", "")).lower() else
        "Adiraptor" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Adiraptor".lower() in str(row.get("Name", "")).lower() else
        "Ghost Sprint" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Ghost Sprint".lower() in str(row.get("Name", "")).lower() else
        "Feroza" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport".lower() in str(row.get("PIM - Sport", "")).lower() and "Feroza".lower() in str(row.get("Name", "")).lower() else
        "Adiracer" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Motorsport".lower() in str(row.get("PIM - Sport", "")).lower() and "Adiracer".lower() in str(row.get("Name", "")).lower() else
        "Heritage" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis".lower() in str(row.get("PIM - Sport", "")).lower() and "Heritage".lower() in str(row.get("Name", "")).lower() else
        "Defiant Speed" if pd.isna(row.get("PIM - Product Line (sportsub)")) and "Tennis".lower() in str(row.get("PIM - Sport", "")).lower() and "Defiant".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Product Line (sportsub)")
    ), axis=1)
    
    df["Enriched Product Family"] = df.apply(lambda row: (
        "Hyperturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Hyperturf".lower() in str(row.get("Name", "")).lower() else
        "Sambae" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Sambae".lower() in str(row.get("Name", "")).lower() else
        "Mocaturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Mocaturf".lower() in str(row.get("Name", "")).lower() else
        "Roverend" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Roverend".lower() in str(row.get("Name", "")).lower() else
        "Rovermule" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rovermule".lower() in str(row.get("Name", "")).lower() else
        "Superturf" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superturf".lower() in str(row.get("Name", "")).lower() else
        "Campus 00" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 00".lower() in str(row.get("Name", "")).lower() else
        "Campus 80" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 80".lower() in str(row.get("Name", "")).lower() else
        "Forum High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Forum High".lower() in str(row.get("Name", "")).lower() or "Forum Hi".lower() in str(row.get("Name", "")).lower()) else
        "Forum Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Forum Low".lower() in str(row.get("Name", "")).lower() or "Forum Lo".lower() in str(row.get("Name", "")).lower()) else
        "Forum Mid" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum Mid".lower() in str(row.get("Name", "")).lower() else
        "Nizza High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza High".lower() in str(row.get("Name", "")).lower() else
        "Nizza Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza Low".lower() in str(row.get("Name", "")).lower() else
        "Nizza Mid" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Nizza Mid".lower() in str(row.get("Name", "")).lower() else
        "NMD 360" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD 360".lower() in str(row.get("Name", "")).lower() else
        "NMD_C2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_C2".lower() in str(row.get("Name", "")).lower() else
        "NMD_CS1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_CS1".lower() in str(row.get("Name", "")).lower() else
        "NMD_G1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_G1".lower() in str(row.get("Name", "")).lower() else
        "NMD_R1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1".lower() in str(row.get("Name", "")).lower() else
        "NMD_R1 V2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1 V2".lower() in str(row.get("Name", "")).lower() else
        "NMD_R1 V3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1 V3".lower() in str(row.get("Name", "")).lower() else
        "NMD_R1_PK" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R1_PK".lower() in str(row.get("Name", "")).lower() else
        "NMD_R2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_R2".lower() in str(row.get("Name", "")).lower() else
        "NMD_TR" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_TR".lower() in str(row.get("Name", "")).lower() else
        "NMD_TS1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_TS1".lower() in str(row.get("Name", "")).lower() else
        "NMD_V3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_V3".lower() in str(row.get("Name", "")).lower() else
        "NMD_W1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_W1".lower() in str(row.get("Name", "")).lower() else
        "NMD_XR1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "NMD_XR1".lower() in str(row.get("Name", "")).lower() else
        "Ozelia" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozelia".lower() in str(row.get("Name", "")).lower() else
        "Oznova" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Oznova".lower() in str(row.get("Name", "")).lower() else
        "Ozrah" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozrah".lower() in str(row.get("Name", "")).lower() else
        "Superstar 360" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar 360".lower() in str(row.get("Name", "")).lower() else
        "Superstar ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar ADV".lower() in str(row.get("Name", "")).lower() else
        "adizero Adios Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero adios".lower() in str(row.get("Name", "")).lower() else
        "adizero Afterburner" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Afterburner".lower() in str(row.get("Name", "")).lower() else
        "adizero Boston" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Boston".lower() in str(row.get("Name", "")).lower() else
        "adizero prime" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero prime".lower() in str(row.get("Name", "")).lower() else
        "adizero RC" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero RC".lower() in str(row.get("Name", "")).lower() else
        "adizero Select" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Select".lower() in str(row.get("Name", "")).lower() else
        "adizero SL" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero SL".lower() in str(row.get("Name", "")).lower() else
        "adizero takumi sen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero takumi sen".lower() in str(row.get("Name", "")).lower() else
        "adizero ubersonic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero ubersonic".lower() in str(row.get("Name", "")).lower() else
        "Copa Pure" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Pure".lower() in str(row.get("Name", "")).lower() else
        "Solarboost" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarboost".lower() in str(row.get("Name", "")).lower() else
        "Solarcontrol" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarcontrol".lower() in str(row.get("Name", "")).lower() else
        "Solar Glide" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarglide".lower() in str(row.get("Name", "")).lower() else
        "Solarmotion" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Solarmotion".lower() in str(row.get("Name", "")).lower() else
        "X Crazyfast" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X Crazyfast".lower() in str(row.get("Name", "")).lower() else
        "X Speedportal" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X Speedportal".lower() in str(row.get("Name", "")).lower() else
        "4DFWD Pulse" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "4DFWD Pulse".lower() in str(row.get("Name", "")).lower() else
        "Ultrabounce DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultrabounce DNA".lower() in str(row.get("Name", "")).lower() else
        "Duramo SL" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Duramo SL".lower() in str(row.get("Name", "")).lower() else
        "Duramo Speed" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Duramo Speed".lower() in str(row.get("Name", "")).lower() else
        "Ultraboost 1.0;Ultraboost DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 1.0".lower() in str(row.get("Name", "")).lower() else
        "xplrphase" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "x_plrphase".lower() in str(row.get("Name", "")).lower() else
        "Ubounce DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ubounce DNA".lower() in str(row.get("Name", "")).lower() else
        "Grand Court 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Grand Court 2.0".lower() in str(row.get("Name", "")).lower() else
        "adilette Aqua" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette aqua".lower() in str(row.get("Name", "")).lower() else
        "adilette Comfort" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette comfort".lower() in str(row.get("Name", "")).lower() else
        "adilette shower" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette shower".lower() in str(row.get("Name", "")).lower() else
        "Grand Court Alpha" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "grand court alpha".lower() in str(row.get("Name", "")).lower() else
        "adilette platform" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adilette platform".lower() in str(row.get("Name", "")).lower() else
        "Agravic Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Flow".lower() in str(row.get("Name", "")).lower() else
        "Agravic Speed Ultra" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Speed Ultra".lower() in str(row.get("Name", "")).lower() else
        "Agravic Speed" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Speed".lower() in str(row.get("Name", "")).lower() else
        "Agravic Ultra" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TERREX Agravic Ultra".lower() in str(row.get("Name", "")).lower() else
        "SL 72 RTN" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 RTN".lower() in str(row.get("Name", "")).lower() else
        "Anthony Edwards 1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Anthony Edwards 1".lower() in str(row.get("Name", "")).lower() else
        "3 Stripes" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("3 Stripes".lower() in str(row.get("Name", "")).lower() or "3-Stripes".lower() in str(row.get("Name", "")).lower()) else
        "F50 Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 Pro".lower() in str(row.get("Name", "")).lower() else
        "F50 Elite" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 Elite".lower() in str(row.get("Name", "")).lower() else
        "F50 League" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "F50 League".lower() in str(row.get("Name", "")).lower() else
        "Stan Smith Lux" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Stan Smith Lux".lower() in str(row.get("Name", "")).lower() else
        "Gazelle Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle Bold".lower() in str(row.get("Name", "")).lower() else
        "Predator Edge" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Edge".lower() in str(row.get("Name", "")).lower() else
        "Predator Club" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Club".lower() in str(row.get("Name", "")).lower() else
        "Predator Accuracy" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Accuracy".lower() in str(row.get("Name", "")).lower() else
        "Predator League" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator League".lower() in str(row.get("Name", "")).lower() else
        "Copa Sense" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Sense".lower() in str(row.get("Name", "")).lower() else
        "Copa Mundial" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Mundial".lower() in str(row.get("Name", "")).lower() else
        "adizero Instinct" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "adizero Instinct".lower() in str(row.get("Name", "")).lower() else
        "Free Hiker 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Free Hiker 2".lower() in str(row.get("Name", "")).lower() else
        "Exhibit Select" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Exhibit Select".lower() in str(row.get("Name", "")).lower() else
        "adizero Impact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Impact".lower() in str(row.get("Name", "")).lower() else
        "SL 72 OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 OG".lower() in str(row.get("Name", "")).lower() else
        "SL 72 RS" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 72 RS".lower() in str(row.get("Name", "")).lower() else
        "Predator Elite" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Predator Elite".lower() in str(row.get("Name", "")).lower() else
        "Forum Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum Bold".lower() in str(row.get("Name", "")).lower() else
        "VL Court 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "VL Court 3.0".lower() in str(row.get("Name", "")).lower() else
        "Ultraboost 20" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 20".lower() in str(row.get("Name", "")).lower() else
        "SL 76" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "SL 76".lower() in str(row.get("Name", "")).lower() else
        "Handball Spezial" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Originals".lower() in str(row.get("PIM - Label", "")).lower() and "Handball Spezial".lower() in str(row.get("Name", "")).lower() else
        "Response CL;2000s" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Response CL".lower() in str(row.get("Name", "")).lower() else
        "Rivalry Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Rivalry 86 Low".lower() in str(row.get("Name", "")).lower() or "Rivalry Summer Low".lower() in str(row.get("Name", "")).lower()) else
        "Rivalry High" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rivalry High".lower() in str(row.get("Name", "")).lower() else
        "Ozmillen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozmillen".lower() in str(row.get("Name", "")).lower() else
        "Lite Racer Adapt" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer Adapt".lower() in str(row.get("Name", "")).lower() else
        "Firebird" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Firebird".lower() in str(row.get("Name", "")).lower() else
        "adizero Electric" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Electric".lower() in str(row.get("Name", "")).lower() else
        "Adilette 22" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilette 22".lower() in str(row.get("Name", "")).lower() else
        "Superstar XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar XLG".lower() in str(row.get("Name", "")).lower() else
        "Country XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country XLG".lower() in str(row.get("Name", "")).lower() else
        "Samba XLG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba XLG".lower() in str(row.get("Name", "")).lower() else
        "Samba OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba OG".lower() in str(row.get("Name", "")).lower() else
        "Y-3 Classic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Y-3 Classic".lower() in str(row.get("Name", "")).lower() or "Y-3 CL".lower() in str(row.get("Name", "")).lower()) else
        "Retro Quarter" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Retro Quarter".lower() in str(row.get("Name", "")).lower() else
        "Retro Graphic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Retro Graphic".lower() in str(row.get("Name", "")).lower() else
        "Activeride 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Activeride 2.0".lower() in str(row.get("Name", "")).lower() else
        "QT Racer 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "QT Racer 3.0".lower() in str(row.get("Name", "")).lower() else
        "Eastrail 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Eastrail 2.0".lower() in str(row.get("Name", "")).lower() else
        "ZG21" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "ZG21".lower() in str(row.get("Name", "")).lower() else
        "ZG23" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "ZG23".lower() in str(row.get("Name", "")).lower() else
        "Daily 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Daily 3.0".lower() in str(row.get("Name", "")).lower() else
        "Copa Gloro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Copa Gloro".lower() in str(row.get("Name", "")).lower() else
        "Tiro 21" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 21".lower() in str(row.get("Name", "")).lower() or "TIRO21".lower() in str(row.get("Name", "")).lower()) else
        "Tiro 23" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 23".lower() in str(row.get("Name", "")).lower() or "TIRO23".lower() in str(row.get("Name", "")).lower()) else
        "Tiro 24" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("TIRO 24".lower() in str(row.get("Name", "")).lower() or "TIRO24".lower() in str(row.get("Name", "")).lower()) else
        "Ultraboost light" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost light".lower() in str(row.get("Name", "")).lower() else
        "Supernova Stride" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Stride".lower() in str(row.get("Name", "")).lower() else
        "Supernova Solution" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Solution".lower() in str(row.get("Name", "")).lower() else
        "Supernova Rise" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Rise".lower() in str(row.get("Name", "")).lower() else
        "Trae Young Unlimited" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Unlimited".lower() in str(row.get("Name", "")).lower() else
        "Trae Young 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 3".lower() in str(row.get("Name", "")).lower() else
        "Trae Young 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 2".lower() in str(row.get("Name", "")).lower() else
        "Dame Certified" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame Certified".lower() in str(row.get("Name", "")).lower() else
        "Dame 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame 8".lower() in str(row.get("Name", "")).lower() else
        "D.O.N Issue 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 8".lower() in str(row.get("Name", "")).lower() else
        "D.O.N Issue 7" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 7".lower() in str(row.get("Name", "")).lower() else
        "D.O.N Issue 6" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 6".lower() in str(row.get("Name", "")).lower() else
        "D.O.N Issue 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N Issue 5".lower() in str(row.get("Name", "")).lower() else
        "Barricade 13" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Barricade 13".lower() in str(row.get("Name", "")).lower() else
        "Crazy 8" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Crazy 8".lower() in str(row.get("Name", "")).lower() else
        "D.O.N Issue 6" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("D.O.N. ISSUE 6".lower() in str(row.get("Name", "")).lower() or "D.O.N ISSUE #6".lower() in str(row.get("Name", "")).lower()) else
        "D.O.N Issue 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "D.O.N. Issue #5".lower() in str(row.get("Name", "")).lower() else
        "Forum Hi" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "FORUM 84 HI".lower() in str(row.get("Name", "")).lower() else
        "Forum Low" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "FORUM 84 LOW".lower() in str(row.get("Name", "")).lower() else
        "Trae Young 4" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Trae Young 4".lower() in str(row.get("Name", "")).lower() else
        "Pureboost 5" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pureboost 5".lower() in str(row.get("Name", "")).lower() else
        "Alphaboost V1" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphaboost V1".lower() in str(row.get("Name", "")).lower() else
        "Alphaboost V2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphaboost V2".lower() in str(row.get("Name", "")).lower() else
        "Alphabounce+" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Alphabounce+".lower() in str(row.get("Name", "")).lower() else
        "Country OG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country OG".lower() in str(row.get("Name", "")).lower() else
        "Pro Shell ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Shell ADV".lower() in str(row.get("Name", "")).lower() else
        "Gazelle ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle ADV".lower() in str(row.get("Name", "")).lower() else
        "Centennial 85" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Centennial 85".lower() in str(row.get("Name", "")).lower() else
        "Cloudfoam Pure" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Cloudfoam Pure".lower() in str(row.get("Name", "")).lower() else
        "Supernova Prima" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Supernova Prima".lower() in str(row.get("Name", "")).lower() else
        "Ultraboost 5X" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultraboost 5X".lower() in str(row.get("Name", "")).lower() else
        "PowerImpact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "PowerImpact".lower() in str(row.get("Name", "")).lower() else
        "Run Pocket" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Run Pocket".lower() in str(row.get("Name", "")).lower() else
        "Soulstride Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Soulstride Flow".lower() in str(row.get("Name", "")).lower() else
        "TLRD Impact" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "TLRD Impact".lower() in str(row.get("Name", "")).lower() else
        "Campus Vulc" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus Vulc".lower() in str(row.get("Name", "")).lower() else
        "Campus ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus ADV".lower() in str(row.get("Name", "")).lower() else
        "Busenitz Vulc II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Busenitz Vulc II".lower() in str(row.get("Name", "")).lower() else
        "Busenitz Pro" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Busenitz Pro".lower() in str(row.get("Name", "")).lower() else
        "Matchbreak Super" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Matchbreak Super".lower() in str(row.get("Name", "")).lower() else
        "Ozweego" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozweego".lower() in str(row.get("Name", "")).lower() else
        "Samba ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba ADV".lower() in str(row.get("Name", "")).lower() else
        "Gazelle Indoor" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Gazelle Indoor".lower() in str(row.get("Name", "")).lower() else
        "Ozmorph" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ozmorph".lower() in str(row.get("Name", "")).lower() else
        "Samba Decon" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Samba Decon".lower() in str(row.get("Name", "")).lower() else
        "Samba Millenium" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and ("Samba MN".lower() in str(row.get("Name", "")).lower() or "Samba Millenium".lower() in str(row.get("Name", "")).lower()) else
        "Stan Smith Decon" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Stan Smith Decon".lower() in str(row.get("Name", "")).lower() else
        "Rivalry Mule" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Rivalry Mule".lower() in str(row.get("Name", "")).lower() else
        "Temper Run 2.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Temper Run 2.0".lower() in str(row.get("Name", "")).lower() else
        "Superstar II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar II".lower() in str(row.get("Name", "")).lower() else
        "Country II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Country II".lower() in str(row.get("Name", "")).lower() else
        "Harden Vol. 9" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Harden Vol. 9".lower() in str(row.get("Name", "")).lower() else
        "Crazy 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Crazy 2".lower() in str(row.get("Name", "")).lower() else
        "Tyshawn II" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tyshawn II".lower() in str(row.get("Name", "")).lower() else
        "adizero ZG" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and "Adizero ZG".lower() in str(row.get("Name", "")).lower() else
        "adizero Cybersonic" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tennis".lower() in str(row.get("PIM - Sport", "")).lower() and "Adizero Cybersonic".lower() in str(row.get("Name", "")).lower() else
        "Entrada 22" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and "Entrada 22".lower() in str(row.get("Name", "")).lower() else
        "Lite Racer 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer 3.0".lower() in str(row.get("Name", "")).lower() else
        "Swift Run 1.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Swift Run 1.0".lower() in str(row.get("Name", "")).lower() else
        "X_PLR Path" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "X_PLR Path".lower() in str(row.get("Name", "")).lower() else
        "Kaptir Flow" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Kaptir Flow".lower() in str(row.get("Name", "")).lower() else
        "Kaptir 3.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Kaptir 3.0".lower() in str(row.get("Name", "")).lower() else
        "Lite Racer 4.0" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Lite Racer 4.0".lower() in str(row.get("Name", "")).lower() else
        "VL Court Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "VL Court Bold".lower() in str(row.get("Name", "")).lower() else
        "Ultradream Bold" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultradream Bold".lower() in str(row.get("Name", "")).lower() else
        "Ultradream DNA" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Ultradream DNA".lower() in str(row.get("Name", "")).lower() else
        "Adilette Estrap" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilette Estrap".lower() in str(row.get("Name", "")).lower() else
        "Neuclassics" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Neuclassics".lower() in str(row.get("Name", "")).lower() else
        "Superstar 80s" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Superstar 82".lower() in str(row.get("Name", "")).lower() else
        "Adizero Aruku" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adizero Aruku".lower() in str(row.get("Name", "")).lower() else
        "iiinfinity" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "IIInfinity".lower() in str(row.get("Name", "")).lower() else
        "Adilenium Season 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Adilenium Season 3".lower() in str(row.get("Name", "")).lower() else
        "adizero takumi sen" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Takumi Sen".lower() in str(row.get("Name", "")).lower() else
        "Dame 9" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame 9".lower() in str(row.get("Name", "")).lower() else
        "Agravic 3" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Agravic 3".lower() in str(row.get("Name", "")).lower() else
        "Tracefinder 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Tracefinder 2".lower() in str(row.get("Name", "")).lower() else
        "Seeulater 2" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Seeulater 2".lower() in str(row.get("Name", "")).lower() else
        "Dame X" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Dame X".lower() in str(row.get("Name", "")).lower() else
        "Forum ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Forum ADV".lower() in str(row.get("Name", "")).lower() else
        "Pro Model ADV" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Model ADV".lower() in str(row.get("Name", "")).lower() else
        "Initiation" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Initiation".lower() in str(row.get("Name", "")).lower() else
        "Pro Model" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Pro Model".lower() in str(row.get("Name", "")).lower() else
        "Campus 00s Beta" if pd.isna(row.get("PIM - Product Family (productlinestyle)")) and "Campus 00s Beta".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Product Family (productlinestyle)")
    ), axis=1)

    df["Enriched Label"] = df.apply(lambda row: (
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "ALL SZN".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Duramo".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ultraboost 1.0".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "X_PLR".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "XPLR".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Z.N.E".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "City Escape".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "FortaRun".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "RunFalcon".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Runfalcon".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Racer TR".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "VL Court".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Front Court".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ownthegame".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Ubounce".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Breaknet".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Grand Court 2.0".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Postmove".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "alphaboost".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Alphaboost".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Puremotion".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Kaptir".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Spiritain".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "ZNSORED".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Future Icons".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Lite Racer".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette aqua".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette comfort".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette shower".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "grand court alpha".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "alphabounce".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Alphabounce".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adicane".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "adilette platform".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "advantage".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "courtblock".lower() in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y-3".lower() in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y3".lower() in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Y 3".lower() in str(row.get("Name", "")).lower() else
        "Five Ten" if pd.isna(row.get("PIM - Label")) and "Hellcat".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Run 70s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Sportswear" if pd.isna(row.get("PIM - Label")) and "Run 80s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "The Gravel Cycling".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ZG23".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ZG21".lower() in str(row.get("Name", "")).lower() else
        "adidas by Stella McCartney" if pd.isna(row.get("PIM - Label")) and "adidas by Stella McCartney".lower() in str(row.get("Name", "")).lower() else
        "adidas by Stella McCartney" if pd.isna(row.get("PIM - Label")) and "aSMC".lower() in str(row.get("Name", "")) else
        "TERREX" if pd.isna(row.get("PIM - Label")) and "Eastrail".lower() in str(row.get("Name", "")).lower() else
        "Impact" if pd.isna(row.get("PIM - Label")) and "Five Ten Impact".lower() in str(row.get("Name", "")).lower() else
        "Five Ten" if pd.isna(row.get("PIM - Label")) and "Five Ten".lower() in str(row.get("Name", "")).lower() else
        "Fear of God Athletics" if pd.isna(row.get("PIM - Label")) and "Fear of God Athletics".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Gazelle".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Samba Messi".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Sambae".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Samba".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Superstar".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Forum".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Stan Smith".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Ozelia".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "NMD".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "OZWEEGO".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "OZMILLEN".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Campus".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Adizero".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "ADIZERO".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Rivalry".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Falcon".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Craig Green".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Bad Bunny".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Originals".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Country OG".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Ozthemis".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adi2000".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Spezial".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Response CL".lower() in str(row.get("Name", "")).lower() else
        "Performance" if pd.isna(row.get("PIM - Label")) and "Response".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adifom".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "AdiFOM".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Wensley".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SPZL".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Moston Super".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL 72".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Pop Trading Co".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "NRTN".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SSTR N".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Wales Bonner".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL76".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SL 76".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "TMNT".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Centennial 85".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Civilist ZX".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Crazy".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Nizza".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Solid Crew".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Trefoil".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adibreak".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Korn".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adi Dassler".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Adicolor".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "100 Thieves".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Street Neuclassic".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "KSENIASCHNAIDER".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Premium".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Todmorden Smock".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Rossendale".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "SST".lower() in str(row.get("Name", "")).lower() else
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
        "TERREX" if pd.isna(row.get("PIM - Label")) and "Terrex".lower() in str(row.get("Name", "")).lower() else
        "Y-3" if pd.isna(row.get("PIM - Label")) and "Real Madrid 23/24".lower() in str(row.get("Name", "")).lower() else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and any(x.lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() for x in [
            "Gazelle", "Samba", "Stan Smith"
        ]) else
        "Originals" if pd.isna(row.get("PIM - Label")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and "Originals".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Label")
    ), axis=1)
    df["Enriched Sport"] = df.apply(lambda row: (   
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Freerider".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Aleon".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Crawe".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Hellcat".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Hiangle".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Kestrel".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Kirigami".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten NIAD".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Sleuth".lower() in str(row.get("Name", "")).lower() else
        "Outdoor" if pd.isna(row.get("PIM - Sport")) and "Five Ten Trailcross".lower() in str(row.get("Name", "")).lower() else
        "Basketball;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Forum".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Adifom Supernova".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero adios".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero adios pro".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero Boston".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero prime".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero RC".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero SL".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "adizero takumi sen".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarboost".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarcontrol".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Solarglide".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Ultrabounce".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ALL SZN".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "Duramo".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ultraboost 1.0".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "X_PLR".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "XPLR".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Z.N.E".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "City Escape".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "FortaRun".lower() in str(row.get("Name", "")).lower() else
        "Running" if pd.isna(row.get("PIM - Sport")) and "RunFalcon".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Racer TR".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "VL Court".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Front Court".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ownthegame".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Ubounce".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Breaknet".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Grand Court 2.0".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Postmove".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "alphaboost".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Puremotion".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Kaptir".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Spiritain".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ZNSORED".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Future Icons".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Lite Racer".lower() in str(row.get("Name", "")).lower() else
        "Swim; Yoga; Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette aqua".lower() in str(row.get("Name", "")).lower() else
        "Swim; Yoga; Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette comfort".lower() in str(row.get("Name", "")).lower() else
        "Swim; Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette shower".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "grand court alpha".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "alphabounce".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adicane".lower() in str(row.get("Name", "")).lower() else
        "Swim;Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "adilette platform".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "advantage".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "courtblock".lower() in str(row.get("Name", "")).lower() else
        "Swim;Yoga;Lifestyle" if pd.isna(row.get("PIM - Sport")) and pd.notna(row.get("PIM adidas - Product Types")) and "Slides" in row.get("PIM adidas - Product Types") else
        "Dance" if pd.isna(row.get("PIM - Sport")) and "Dance".lower() in str(row.get("Name", "")).lower() else
        "Golf" if pd.isna(row.get("PIM - Sport")) and "Golf".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "TrueCasuals".lower() in str(row.get("Name", "")).lower() else
        "Golf" if pd.isna(row.get("PIM - Sport")) and "Ultimate365".lower() in str(row.get("Name", "")).lower() else
        "Soccer" if pd.isna(row.get("PIM - Sport")) and "Copa Gloro".lower() in str(row.get("Name", "")).lower() else
        "Cycling" if pd.isna(row.get("PIM - Sport")) and "Bike Shoes".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "FARM".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Z.N.E.".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Run 70s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Run 80s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Cycling" if pd.isna(row.get("PIM - Sport")) and "The Gravel Cycling".lower() in str(row.get("Name", "")).lower() else
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
        "Lifestyle" if pd.isna(row.get("PIM - Sport")) and "ZNSORED High".lower() in str(row.get("Name", "")).lower() else
        "Training;Weightlifting" if pd.isna(row.get("PIM - Sport")) and "Dropset".lower() in str(row.get("Name", "")).lower() else
        "Weightlifting" if pd.isna(row.get("PIM - Sport")) and "The Total".lower() in str(row.get("Name", "")).lower() else
        "Basketball;Lifestyle" if pd.isna(row.get("PIM - Sport")) and "Fear of God Athletics".lower() in str(row.get("PIM - Label", "")).lower() else
        "Skateboarding;Lifestyle" if pd.isna(row.get("PIM - Sport")) and any(name.lower() in str(row.get("Name", "")).lower() for name in [
            "Samba ADV", "Superstar ADV", "Stan Smith ADV", "Centennial 85 Low ADV",
            "Gazelle ADV", "Pro Model 80 ADV", "Campus ADV"
        ]) else
        row.get("PIM - Sport")
    ), axis=1)
    df["Enriched Activity"] = df.apply(lambda row: (
        "Outdoor;Athletic" if "Hellcat".lower() in str(row.get("Name", "")).lower() else
        "Outdoor;Athletic" if "Terrex".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Y-3".lower() in str(row.get("PIM - Label", "")).lower() else
        "Premium" if "Fear of God Athletics".lower() in str(row.get("PIM - Label", "")).lower() else
        "Premium" if "adidas by Stella McCartney".lower() in str(row.get("PIM - Label", "")).lower() else
        "Premium" if "Y-3".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Fear of God".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "100 Thieves".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Avavav".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Sporty & Rich".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Dime".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Bape".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Song For The Mute".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Bad Bunny".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "SPZL".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Dingyun Zhang".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Edison Chen".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "SFTM".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "EQT".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Equipment".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Korn".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "JJJJound".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Wales Bonner".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Willy Chavarria".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Brain Dead".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Jabbar".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Pharrell".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "CP Company".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Minecraft".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Fortnite".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "BW Army".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Spongebob".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "NTS Radio".lower() in str(row.get("Name", "")).lower() else
        "Premium" if "Rolling Links".lower() in str(row.get("Name", "")).lower() else
        row.get("")
    ), axis=1)
    df["Enriched Pattern"] = df.apply(lambda row: (
        "All Over Print" if pd.isna(row.get("PIM - Pattern")) and "All Over Print".lower() in str(row.get("Name", "")).lower() else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Animal".lower() in str(row.get("Name", "")).lower() else
        "Camo" if pd.isna(row.get("PIM - Pattern")) and "Camo".lower() in str(row.get("Name", "")).lower() else
        "Camo" if pd.isna(row.get("PIM - Pattern")) and "Camouflage".lower() in str(row.get("Name", "")).lower() else
        "Graphic Print" if pd.isna(row.get("PIM - Pattern")) and "Graphic".lower() in str(row.get("Name", "")).lower() else
        "Floral" if pd.isna(row.get("PIM - Pattern")) and "Floral".lower() in str(row.get("Name", "")).lower() else
        "Floral" if pd.isna(row.get("PIM - Pattern")) and "Flower".lower() in str(row.get("Name", "")).lower() else
        "Polka Dots" if pd.isna(row.get("PIM - Pattern")) and "Dots".lower() in str(row.get("Name", "")).lower() else
        "Polka Dots" if pd.isna(row.get("PIM - Pattern")) and "Polka Dots".lower() in str(row.get("Name", "")).lower() else
        "Tie Dye" if pd.isna(row.get("PIM - Pattern")) and "Tie-Dye".lower() in str(row.get("Name", "")).lower() else
        "Tie Dye" if pd.isna(row.get("PIM - Pattern")) and "Tie Dye".lower() in str(row.get("Name", "")).lower() else
        "Metallic" if pd.isna(row.get("PIM - Pattern")) and "Metallic".lower() in str(row.get("Name", "")).lower() else
        "Flames" if pd.isna(row.get("PIM - Pattern")) and "Flame".lower() in str(row.get("Name", "")).lower() else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Leopard".lower() in str(row.get("Name", "")).lower() else
        "Animal" if pd.isna(row.get("PIM - Pattern")) and "Zebra".lower() in str(row.get("Name", "")).lower() else
        "Embroidery" if pd.isna(row.get("PIM - Pattern")) and "Embroidered".lower() in str(row.get("Name", "")).lower() else
        "Logo Print" if pd.isna(row.get("PIM - Pattern")) and "LOGO".lower() in str(row.get("Name", "")).lower() else
        "Glitter" if pd.isna(row.get("PIM - Pattern")) and "Glitter".lower() in str(row.get("Name", "")).lower() else
        "Glitter" if pd.isna(row.get("PIM - Pattern")) and "Rhinestones".lower() in str(row.get("Name", "")).lower() else
        "Logo Print" if pd.isna(row.get("PIM - Pattern")) and "Logo".lower() in str(row.get("Name", "")).lower() else
        "Crochet" if pd.isna(row.get("PIM - Pattern")) and "Crochet".lower() in str(row.get("Name", "")).lower() else
        "Colorblock" if pd.isna(row.get("PIM - Pattern")) and "Colorblock".lower() in str(row.get("Name", "")).lower() else
        "Color Block" if pd.isna(row.get("PIM - Pattern")) and "Color block".lower() in str(row.get("Name", "")).lower() else
        "Plaid" if pd.isna(row.get("PIM - Pattern")) and "Plaid".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Pattern")
    ), axis=1)
    df["Enriched Base Material"] = df.apply(lambda row: (
        "Fleece" if pd.isna(row.get("PIM - Base Material")) and "ALL SZN".lower() in str(row.get("Name", "")).lower() else
        "Nuganic" if pd.isna(row.get("PIM - Base Material")) and "Nuganic".lower() in str(row.get("Name", "")).lower() else
        "Denim" if pd.isna(row.get("PIM - Base Material")) and "Denim".lower() in str(row.get("Name", "")).lower() else
        "Satin" if pd.isna(row.get("PIM - Base Material")) and "Satin".lower() in str(row.get("Name", "")).lower() else
        "Velour;Velvet" if pd.isna(row.get("PIM - Base Material")) and (
            "Velour".lower() in str(row.get("Name", "")).lower() or "Velvet".lower() in str(row.get("Name", "")).lower()
        ) else
        "Piqué" if pd.isna(row.get("PIM - Base Material")) and "Pique".lower() in str(row.get("Name", "")).lower() else
        "Microfiber" if pd.isna(row.get("PIM - Base Material")) and "Microfiber".lower() in str(row.get("Name", "")).lower() else
        "Wool" if pd.isna(row.get("PIM - Base Material")) and "Wool".lower() in str(row.get("Name", "")).lower() else
        "Molded" if pd.isna(row.get("PIM - Base Material")) and "Molded".lower() in str(row.get("Name", "")).lower() else
        "Cashmere" if pd.isna(row.get("PIM - Base Material")) and "Cashmere".lower() in str(row.get("Name", "")).lower() else
        "Twistknit" if pd.isna(row.get("PIM - Base Material")) and "Twistknit".lower() in str(row.get("Name", "")).lower() else
        "Recycled Polyester" if pd.isna(row.get("PIM - Base Material")) and
        "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and (
                "Jerseys".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or
                "Jerseys - Long Sleeve".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or
                "Gloves - Goalkeeper".lower() in str(row.get("PIM adidas - Product Types", "")).lower()
            ) else
        "Cotton" if pd.isna(row.get("PIM - Base Material")) and
            "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and
            "Shorts".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and (
                "Tiro 24 Sweat Shorts".lower() in str(row.get("Name", "")).lower() or
                "Tiro 24 Shorts".lower() in str(row.get("Name", "")).lower()
            ) else
        "Cotton" if pd.isna(row.get("PIM - Base Material")) and
            "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and
            "T Shirts".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Twistweave" if pd.isna(row.get("PIM - Base Material")) and "Twistweave".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Base Material")
    ), axis=1)
    df["Enriched Partner"] = df.apply(lambda row: (
        "Disney" if pd.isna(row.get("PIM - Partner")) and "Disney".lower() in str(row.get("Name", "")).lower() else
        "Disney; Star Wars" if pd.isna(row.get("PIM - Partner")) and "Star Wars".lower() in str(row.get("Name", "")).lower() else
        "Disney;Mickey" if pd.isna(row.get("PIM - Partner")) and "Mickey".lower() in str(row.get("Name", "")).lower() else
        "Disney;Moana" if pd.isna(row.get("PIM - Partner")) and "Moana".lower() in str(row.get("Name", "")).lower() else
        "Farm" if pd.isna(row.get("PIM - Partner")) and "FARM".lower() in str(row.get("Name", "")).lower() else
        "UEFA Champions League;Club" if pd.isna(row.get("PIM - Partner")) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Juventus", "Manchester United", "Real Madrid", "AFC Ajax"
        ]) else
        "Stella McCartney" if pd.isna(row.get("PIM - Partner")) and "Stella McCartney".lower() in str(row.get("Name", "")).lower() else
        "LEGO" if pd.isna(row.get("PIM - Partner")) and "Lego".lower() in str(row.get("Name", "")).lower() else
        "Marimekko" if pd.isna(row.get("PIM - Partner")) and "Marimekko".lower() in str(row.get("Name", "")).lower() else
        "Disney;Marvel" if pd.isna(row.get("PIM - Partner")) and "Marvel".lower() in str(row.get("Name", "")).lower() else
        "Parley" if pd.isna(row.get("PIM - Partner")) and "Parley".lower() in str(row.get("Name", "")).lower() else
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
        "Club" if pd.isna(row["PIM - Partner"]) and "Benfica".lower() in str(row.get("Name", "")).lower() else
        "UEFA Champions League;Club" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "Celtic FC", "FC Bayern Munich", "Olympique Lyonnais", "Arsenal"
        ]) else
        "Club" if pd.isna(row["PIM - Partner"]) and "Newcastle United FC".lower() in str(row.get("Name", "")).lower() else
        "SPZL" if pd.isna(row["PIM - Partner"]) and "SPZL".lower() in str(row.get("Name", "")).lower() else
        "Andre Saravia" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["André Saraiva", "Andre Saraiva"]) else
        "Edison Chen" if pd.isna(row["PIM - Partner"]) and "Edison Chen".lower() in str(row.get("Name", "")).lower() else
        "Y 3" if pd.isna(row["PIM - Partner"]) and "Y-3".lower() in str(row.get("Name", "")).lower() else
        "Bad Bunny" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Bad Bunny", "Ballerina"]) else
        "KseniaSchnaider" if pd.isna(row["PIM - Partner"]) and "KSENIASCHNAIDER".lower() in str(row.get("Name", "")).lower() else
        "BAPE" if pd.isna(row["PIM - Partner"]) and "BAPE".lower() in str(row.get("Name", "")).lower() else
        "Pop Trading Company" if pd.isna(row["PIM - Partner"]) and "Pop Trading Co".lower() in str(row.get("Name", "")).lower() else
        "Wales Bonner" if pd.isna(row["PIM - Partner"]) and "Wales Bonner".lower() in str(row.get("Name", "")).lower() else
        "Pharrell" if pd.isna(row["PIM - Partner"]) and "Pharrell Williams".lower() in str(row.get("Name", "")).lower() else
        "100 Thieves" if pd.isna(row["PIM - Partner"]) and "100 Thieves".lower() in str(row.get("Name", "")).lower() else
        "Korn" if pd.isna(row["PIM - Partner"]) and "Korn".lower() in str(row.get("Name", "")).lower() else
        "UEFA Champions League" if pd.isna(row["PIM - Partner"]) and "UCL".lower() in str(row.get("Name", "")).lower() else
        "UEFA EURO" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Euro 24", "Fussballliebe"]) else
        "Deadpool;Marvel" if pd.isna(row["PIM - Partner"]) and "Deadpool".lower() in str(row.get("Name", "")).lower() else
        "Yeezy" if pd.isna(row["PIM - Partner"]) and "Yeezy".lower() in str(row.get("Name", "")).lower() else
        "Y3" if pd.isna(row["PIM - Partner"]) and "Y-3".lower() in str(row.get("Name", "")).lower() else
        "Avavav" if pd.isna(row["PIM - Partner"]) and "Avavav".lower() in str(row.get("Name", "")).lower() else
        "Club" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["AS Roma", "Boca Juniors"]) else
        "Lion King" if pd.isna(row["PIM - Partner"]) and "Lion King".lower() in str(row.get("Name", "")).lower() else
        "Fortnite" if pd.isna(row["PIM - Partner"]) and "Fortnite".lower() in str(row.get("Name", "")).lower() else
        "Teamgeist" if pd.isna(row["PIM - Partner"]) and "Teamgeist".lower() in str(row.get("Name", "")).lower() else
        "Willy Chavarria" if pd.isna(row["PIM - Partner"]) and "Willy Chavarria".lower() in str(row.get("Name", "")).lower() else
        "OG LA" if pd.isna(row["PIM - Partner"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["OG L.A", "OG LA"]) else
        "College" if pd.isna(row["PIM - Partner"]) and (
            "Collegiate".lower() in str(row.get("Name", "")).lower() or
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
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Hellcat".lower() in str(row.get("Name", "")).lower() else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Dame 8".lower() in str(row.get("Name", "")).lower() else
        "Pants" if pd.isna(row["PIM adidas - Product Types"]) and "Pants".lower() in str(row.get("Name", "")).lower() else
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Bike Shoes".lower() in str(row.get("Name", "")).lower() else
        "Bike Shoes" if pd.isna(row["PIM adidas - Product Types"]) and "Cycling".lower() in str(row.get("Name", "")).lower() else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Rivalry High".lower() in str(row.get("Name", "")).lower() else
        "High Tops; Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM adidas - Product Types"]) and "High Tops".lower() in str(row["PIM adidas - Product Types"]).lower() else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Run 70s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Run 80s Shoes".lower() in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Puig".lower() in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Samba".lower() in str(row["PIM - Product Line (sportsub)"]).lower() else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Gazelle".lower() in str(row["PIM - Product Line (sportsub)"]).lower() else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "SL 72".lower() in str(row["PIM - Product Line (sportsub)"]).lower() else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.notna(row["PIM - Product Line (sportsub)"]) and "Country".lower() in str(row["PIM - Product Line (sportsub)"]).lower() else
        "Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and pd.isna(row["PIM - Product Line (sportsub)"]) and "Originals".lower() in str(row["PIM - Label"]).lower() and "Handball Spezial".lower() in str(row.get("Name", "")).lower() else
        "Slides;Platform" if pd.isna(row["PIM adidas - Product Types"]) and "Platform".lower() in str(row.get("Name", "")).lower() and "Slides".lower() in str(row["PIM adidas - Product Types"]).lower() else
        "Boots" if pd.isna(row["PIM adidas - Product Types"]) and ("Boot".lower() in str(row.get("Name", "")).lower() or "Boots".lower() in str(row.get("Name", "")).lower()) else
        "Platform;Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Bold", "Platform", "XLG", "Sambae"]) else
        "Platform;Clogs" if pd.isna(row["PIM adidas - Product Types"]) and "Stan Smith Mule".lower() in str(row.get("Name", "")).lower() else
        "Balls" if pd.isna(row["PIM adidas - Product Types"]) and "Ball".lower() in str(row.get("Name", "")).lower() else
        "Vests" if pd.isna(row["PIM adidas - Product Types"]) and "Trail Running Vest".lower() in str(row.get("Name", "")).lower() else
        "Belts" if pd.isna(row["PIM adidas - Product Types"]) and "Belt".lower() in str(row.get("Name", "")).lower() else
        "Gloves;Gloves - Goalkeeper" if pd.isna(row["PIM adidas - Product Types"]) and "Goalkeeper Gloves".lower() in str(row.get("Name", "")).lower() else
        "Gloves" if pd.isna(row["PIM adidas - Product Types"]) and "Gloves".lower() in str(row.get("Name", "")).lower() else
        "Athletic & Sneakers;High Tops" if pd.isna(row["PIM adidas - Product Types"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["forum high", "forum hi", "Nizza high"]) else
        "Athletic & Sneakers;Athletic & Sneakers - T Toe" if pd.isna(row["PIM adidas - Product Types"]) and "Spezial".lower() in str(row.get("Name", "")).lower() else
        "Pants;Track Suits - Track Pants;Track Suits" if pd.isna(row["PIM adidas - Product Types"]) and "Track Pants".lower() in str(row.get("Name", "")).lower() else
        "Bags;Bags - Crossbody" if pd.isna(row["PIM adidas - Product Types"]) and "Crossbody Bag".lower() in str(row.get("Name", "")).lower() else
        "Bag" if pd.isna(row["PIM adidas - Product Types"]) and "Bag".lower() in str(row.get("Name", "")).lower() else
        "Bags;Bags - Duffle Bags" if pd.isna(row["PIM adidas - Product Types"]) and "Duffle Bag".lower() in str(row.get("Name", "")).lower() else
        "Bags;Bags - Tote" if pd.isna(row["PIM adidas - Product Types"]) and "Tote Bag".lower() in str(row.get("Name", "")).lower() else
        "Platform;Athletic & Sneakers" if pd.isna(row["PIM adidas - Product Types"]) and "Gazelle Stack".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM adidas - Product Types")
    ), axis=1)
    df["Enriched Surface"] = df.apply(lambda row: (
        "Multi Ground" if pd.isna(row["PIM - Surface"]) and "Multi ground".lower() in str(row.get("Name", "")).lower() else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "trail running".lower() in str(row["PIM - Sport"]).lower() else 
        "Gravel" if pd.isna(row["PIM - Surface"]) and "The Gravel Cycling".lower() in str(row.get("Name", "")).lower() else 
        "Indoor" if pd.isna(row["PIM - Surface"]) and "THE INDOOR CYCLING SHOE".lower() in str(row.get("Name", "")).lower() else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Originals".lower() in str(row["PIM - Label"]).lower() and (
            "Athletic & Sneakers".lower() in str(row["PIM adidas - Product Types"]).lower() or 
            "Athletic & Sneakers - T Toe".lower() in str(row["PIM adidas - Product Types"]).lower()) else 
        "Artificial Grass" if pd.isna(row["PIM - Surface"]) and "Artificial Grass".lower() in str(row.get("Name", "")).lower() else 
        "Clay Court" if pd.isna(row["PIM - Surface"]) and "Clay".lower() in str(row.get("Name", "")).lower() else 
        "Firm Ground" if pd.isna(row["PIM - Surface"]) and ("Firm Ground".lower() in str(row.get("Name", "")).lower() or "FG".lower() in str(row.get("Name", "")).lower()) else 
        "Soft Ground" if pd.isna(row["PIM - Surface"]) and "Soft Ground".lower() in str(row.get("Name", "")).lower() else 
        "Gravel" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["The Gravel", "Five Ten"]) else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "Trailcross".lower() in str(row.get("Name", "")).lower() else 
        "Turf" if pd.isna(row["PIM - Surface"]) and "Turf".lower() in str(row.get("Name", "")).lower() else 
        "Indoor-Court" if pd.isna(row["PIM - Surface"]) and "Indoor".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row["PIM - Sport"]).lower() else 
        "Road;Treadmill" if pd.isna(row["PIM - Surface"]) and "Running".lower() in str(row["PIM - Sport"]).lower() and 
            "Athletic & Sneakers".lower() in str(row["PIM adidas - Product Types"]).lower() and any(x.lower() in str(row.get("Name", "")).lower() for x in [
                "4DFWD", "adizero", "Duramo", "Pureboost", "RDY", "Puremotion", "Rapida", "Response", "RunFalcon", 
                "Solar", "speedmotion", "Supernova", "Switch FWD", "Ultrabounce", "Tensaur", "X9000"]) else 
        "Track" if pd.isna(row["PIM - Surface"]) and "Track & Field".lower() in str(row["PIM - Sport"]).lower() and "adizero".lower() in str(row.get("Name", "")).lower() else 
        "Trail" if pd.isna(row["PIM - Surface"]) and "Trail Running".lower() in str(row["PIM - Sport"]).lower() and "Agravic".lower() in str(row.get("Name", "")).lower() else 
        "Road" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Velosamba", "The Road", "Velostan Smith"]) else 
        "Hard Court" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row["PIM - Product Family (productlinestyle)"]).lower() for x in [
            "adizero Cybersonic", "adizero ubersonic"]) else 
        "Clay Court" if pd.isna(row["PIM - Surface"]) and "Tennis".lower() in str(row["PIM - Sport"]).lower() and "Clay".lower() in str(row.get("Name", "")).lower() else 
        "Hard Court" if pd.isna(row["PIM - Surface"]) and any(x.lower() in str(row["PIM - Product Line (sportsub)"]).lower() for x in [
            "Barricade", "CourtJam", "Avacourt", "GameCourt"]) else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Fear of God Athletics".lower() in str(row["PIM - Label"]).lower() and 
            "Athletic & Sneakers".lower() in str(row["PIM adidas - Product Types"]).lower() else 
        "Indoor-Court;Hard Court" if pd.isna(row["PIM - Surface"]) and "Cross Em".lower() in str(row.get("Name", "")).lower() else 
        "Street" if pd.isna(row["PIM - Surface"]) and "Running".lower() in str(row["PIM - Sport"]).lower() and 
            "Originals".lower() in str(row["PIM - Label"]) and "Athletic & Sneakers".lower() in str(row["PIM adidas - Product Types"]).lower() else 
        row.get("PIM - Surface")
    ), axis=1)
    df["Enriched Athletes"] = df.apply(lambda row: (
        "Ant Edwards" if pd.isna(row["PIM - Athletes"]) and "Anthony Edwards".lower() in str(row.get("Name", "")).lower() else 
        "Donovan Mitchell" if pd.isna(row["PIM - Athletes"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in [
            "D.O.N", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8", "D.O.N. Issue 5"]) else 
        "Damian Lillard" if pd.isna(row["PIM - Athletes"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Dame 8", "Dame"]) else 
        "Lionel Messi" if pd.isna(row["PIM - Athletes"]) and "Messi".lower() in str(row.get("Name", "")).lower() else 
        "Trae Young" if pd.isna(row["PIM - Athletes"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Trae", "Trae Young", "Trae Unlimited"]) else 
        "James Harden" if pd.isna(row["PIM - Athletes"]) and "Harden".lower() in str(row.get("Name", "")).lower() else 
        "Tyshawn Jones" if pd.isna(row["PIM - Athletes"]) and "Tyshawn".lower() in str(row.get("Name", "")).lower() else 
        "Dennis Busenitz" if pd.isna(row["PIM - Athletes"]) and "Busenitz".lower() in str(row.get("Name", "")).lower() else 
        "Lucas Puig" if pd.isna(row["PIM - Athletes"]) and "puig".lower() in str(row.get("Name", "")).lower() else 
        "Mark Gonzalez" if pd.isna(row["PIM - Athletes"]) and (
            "shmoofoil".lower() in str(row.get("Name", "")).lower() or "shmoofoil".lower() in str(row["PIM - Product Line (sportsub)"]).lower() or 
            "Gonz".lower() in str(row.get("Name", "")).lower() or "aloha Super".lower() in str(row.get("Name", "")).lower() or "aloha Super".lower() in str(row["PIM - Product Line (sportsub)"]).lower()) else 
        "Patrick Mahomes" if pd.isna(row["PIM - Athletes"]) and "Mahomes".lower() in str(row.get("Name", "")).lower() else 
        "Nora Vasconcellos" if pd.isna(row["PIM - Athletes"]) and "Nora ".lower() in str(row.get("Name", "")).lower() else 
        "Heitor Da Silva" if pd.isna(row["PIM - Athletes"]) and "Pro Shell ADV x Heitor".lower() in str(row.get("Name", "")).lower() else 
        "Kader Sylla" if pd.isna(row["PIM - Athletes"]) and "Kader".lower() in str(row.get("Name", "")).lower() else 
        "Henry Jones" if pd.isna(row["PIM - Athletes"]) and "Henry Jones".lower() in str(row.get("Name", "")).lower() else 
        "Jude Bellingham" if pd.isna(row["PIM - Athletes"]) and "Jude Bellingham".lower() in str(row.get("Name", "")).lower() else 
        "Lamine Yamal" if pd.isna(row["PIM - Athletes"]) and "Lamine".lower() in str(row.get("Name", "")).lower() else 
        "George Russell" if pd.isna(row["PIM - Athletes"]) and "George Russell".lower() in str(row.get("Name", "")).lower() else 
        "Kimi Antonelli" if pd.isna(row["PIM - Athletes"]) and "Kimi Antonelli".lower() in str(row.get("Name", "")).lower() else 
        row.get("PIM - Athletes")
    ), axis=1)
    df["Enriched Teams"] = df.apply(lambda row: (
        "Atlanta United" if pd.isna(row["PIM - Teams"]) and "Atlanta United".lower() in str(row.get("Name", "")).lower() else 
        "Austin FC" if pd.isna(row["PIM - Teams"]) and "Austin FC".lower() in str(row.get("Name", "")).lower() else 
        "CF Montreal" if pd.isna(row["PIM - Teams"]) and "CF Montreal".lower() in str(row.get("Name", "")).lower() else 
        "Charlotte FC" if pd.isna(row["PIM - Teams"]) and "Charlotte FC".lower() in str(row.get("Name", "")).lower() else 
        "Chicago Fire" if pd.isna(row["PIM - Teams"]) and "Chicago Fire".lower() in str(row.get("Name", "")).lower() else 
        "Colorado Rapids" if pd.isna(row["PIM - Teams"]) and "Colorado Rapids".lower() in str(row.get("Name", "")).lower() else 
        "Columbus Crew" if pd.isna(row["PIM - Teams"]) and "Columbus Crew".lower() in str(row.get("Name", "")).lower() else 
        "D.C. United" if pd.isna(row["PIM - Teams"]) and "D.C. United".lower() in str(row.get("Name", "")).lower() else 
        "Cincinnati FC" if pd.isna(row["PIM - Teams"]) and "FC Cincinnati".lower() in str(row.get("Name", "")).lower() else 
        "Dallas FC" if pd.isna(row["PIM - Teams"]) and "FC Dallas".lower() in str(row.get("Name", "")).lower() else 
        "Houston Dynamo" if pd.isna(row["PIM - Teams"]) and "Houston Dynamo".lower() in str(row.get("Name", "")).lower() else 
        "Inter Miami CF" if pd.isna(row["PIM - Teams"]) and "Inter Miami CF".lower() in str(row.get("Name", "")).lower() else 
        "Los Angeles Football Club" if pd.isna(row["PIM - Teams"]) and ("Los Angeles Football Club".lower() in str(row.get("Name", "")).lower() or "Los Angeles FC".lower() in str(row.get("Name", "")).lower()) else 
        "Manchester United" if pd.isna(row["PIM - Teams"]) and "Manchester United".lower() in str(row.get("Name", "")).lower() else 
        "Minnesota United" if pd.isna(row["PIM - Teams"]) and "Minnesota United".lower() in str(row.get("Name", "")).lower() else 
        "Nashville SC" if pd.isna(row["PIM - Teams"]) and "Nashville SC".lower() in str(row.get("Name", "")).lower() else 
        "New England Revolution" if pd.isna(row["PIM - Teams"]) and "New England Revolution".lower() in str(row.get("Name", "")).lower() else 
        "New York City FC" if pd.isna(row["PIM - Teams"]) and "New York City FC".lower() in str(row.get("Name", "")).lower() else 
        "New York Red Bulls" if pd.isna(row["PIM - Teams"]) and "New York Red Bulls".lower() in str(row.get("Name", "")).lower() else 
        "Orlando City SC" if pd.isna(row["PIM - Teams"]) and "Orlando City SC".lower() in str(row.get("Name", "")).lower() else 
        "Philadelphia Union" if pd.isna(row["PIM - Teams"]) and "Philadelphia Union".lower() in str(row.get("Name", "")).lower() else 
        "Real Madrid" if pd.isna(row["PIM - Teams"]) and "Real Madrid".lower() in str(row.get("Name", "")).lower() else 
        "Portland Timbers" if pd.isna(row["PIM - Teams"]) and "Portland Timbers".lower() in str(row.get("Name", "")).lower() else 
        "Real Salt Lake" if pd.isna(row["PIM - Teams"]) and "Real Salt Lake".lower() in str(row.get("Name", "")).lower() else 
        "San Jose Earthquakes" if pd.isna(row["PIM - Teams"]) and "San Jose Earthquakes".lower() in str(row.get("Name", "")).lower() else 
        "Seattle Sounders FC" if pd.isna(row["PIM - Teams"]) and "Seattle Sounders FC".lower() in str(row.get("Name", "")).lower() else 
        "Sporting Kansas City" if pd.isna(row["PIM - Teams"]) and "Sporting Kansas City".lower() in str(row.get("Name", "")).lower() else 
        "St Louis City SC" if pd.isna(row["PIM - Teams"]) and "St Louis CITY SC".lower() in str(row.get("Name", "")).lower() else 
        "Toronto FC" if pd.isna(row["PIM - Teams"]) and "Toronto FC".lower() in str(row.get("Name", "")).lower() else 
        "Vancouver Whitecaps" if pd.isna(row["PIM - Teams"]) and "Vancouver Whitecaps".lower() in str(row.get("Name", "")).lower() else 
        "Jamaica" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Jamaica Beckenbauer", "Jamaica OG", "Jamaica"]) else 
        "Tampa Bay Lightning" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Lightning Third", "Tampa Bay"]) else 
        "Arsenal" if pd.isna(row["PIM - Teams"]) and "Arsenal".lower() in str(row.get("Name", "")).lower() else 
        "Juventus" if pd.isna(row["PIM - Teams"]) and "Juventus".lower() in str(row.get("Name", "")).lower() else 
        "Argentina" if pd.isna(row["PIM - Teams"]) and "Argentina".lower() in str(row.get("Name", "")).lower() else 
        "Spain" if pd.isna(row["PIM - Teams"]) and "Spain".lower() in str(row.get("Name", "")).lower() else 
        "Schalke 04" if pd.isna(row["PIM - Teams"]) and "FC Schalke".lower() in str(row.get("Name", "")).lower() else 
        "Scotland" if pd.isna(row["PIM - Teams"]) and "Scotland 24".lower() in str(row.get("Name", "")).lower() else 
        "Italy" if pd.isna(row["PIM - Teams"]) and "Italy".lower() in str(row.get("Name", "")).lower() else 
        "Celtic FC" if pd.isna(row["PIM - Teams"]) and "Celtic FC".lower() in str(row.get("Name", "")).lower() else 
        "Sweden" if pd.isna(row["PIM - Teams"]) and "Sweden".lower() in str(row.get("Name", "")).lower() else 
        "Algeria" if pd.isna(row["PIM - Teams"]) and "Algeria 22".lower() in str(row.get("Name", "")).lower() else 
        "FC Girondins Bordeaux" if pd.isna(row["PIM - Teams"]) and "Girondins de Bordeaux".lower() in str(row.get("Name", "")).lower() else 
        "Hungary" if pd.isna(row["PIM - Teams"]) and "Hungary 24".lower() in str(row.get("Name", "")).lower() else 
        "Colombia" if pd.isna(row["PIM - Teams"]) and "Colombia 24".lower() in str(row.get("Name", "")).lower() else 
        "FC Nürnberg" if pd.isna(row["PIM - Teams"]) and "FC Nürnberg".lower() in str(row.get("Name", "")).lower() else 
        "Leeds United FC" if pd.isna(row["PIM - Teams"]) and "Leeds United FC".lower() in str(row.get("Name", "")).lower() else 
        "Black Ferns" if pd.isna(row["PIM - Teams"]) and "Black Ferns".lower() in str(row.get("Name", "")).lower() else 
        "Mexico" if pd.isna(row["PIM - Teams"]) and "Mexico".lower() in str(row.get("Name", "")).lower() else 
        "Fulham FC" if pd.isna(row["PIM - Teams"]) and "Fulham FC".lower() in str(row.get("Name", "")).lower() else 
        "Racing Club de Strasbourg" if pd.isna(row["PIM - Teams"]) and "RC Strasbourg".lower() in str(row.get("Name", "")).lower() else 
        "AS Roma" if pd.isna(row["PIM - Teams"]) and "AS Roma".lower() in str(row.get("Name", "")).lower() else 
        "Belgium" if pd.isna(row["PIM - Teams"]) and "Belgium".lower() in str(row.get("Name", "")).lower() else 
        "Wales" if pd.isna(row["PIM - Teams"]) and "Wales 24".lower() in str(row.get("Name", "")).lower() else 
        "All Blacks" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["All Blacks", "New Zealand Rugby"]) else 
        "FC Union Berlin" if pd.isna(row["PIM - Teams"]) and "FC Union Berlin".lower() in str(row.get("Name", "")).lower() else 
        "Hamburger SV" if pd.isna(row["PIM - Teams"]) and "Hamburger SV".lower() in str(row.get("Name", "")).lower() else 
        "Northern Ireland" if pd.isna(row["PIM - Teams"]) and "Northern Ireland".lower() in str(row.get("Name", "")).lower() else 
        "France" if pd.isna(row["PIM - Teams"]) and "France".lower() in str(row.get("Name", "")).lower() else 
        "Germany" if pd.isna(row["PIM - Teams"]) and "Germany".lower() in str(row.get("Name", "")).lower() else 
        "LA Galaxy" if pd.isna(row["PIM - Teams"]) and "LA Galaxy".lower() in str(row.get("Name", "")).lower() else 
        "Olympique Lyon" if pd.isna(row["PIM - Teams"]) and "Olympique Lyonnais".lower() in str(row.get("Name", "")).lower() else 
        "Chile" if pd.isna(row["PIM - Teams"]) and "Chile 24".lower() in str(row.get("Name", "")).lower() else 
        "Leicester City" if pd.isna(row["PIM - Teams"]) and "Leicester City FC".lower() in str(row.get("Name", "")).lower() else 
        "AFC Ajax" if pd.isna(row["PIM - Teams"]) and "Ajax".lower() in str(row.get("Name", "")).lower() else 
        "Boca Juniors" if pd.isna(row["PIM - Teams"]) and "Boca Juniors".lower() in str(row.get("Name", "")).lower() else 
        "FC Bayern Munich" if pd.isna(row["PIM - Teams"]) and "FC Bayern".lower() in str(row.get("Name", "")).lower() else 
        "San Diego FC" if pd.isna(row["PIM - Teams"]) and "San Diego FC".lower() in str(row.get("Name", "")).lower() else 
        "Tigres" if pd.isna(row["PIM - Teams"]) and "Tigres UANL".lower() in str(row.get("Name", "")).lower() else 
        "Arsenal FC" if pd.isna(row["PIM - Teams"]) and "AFC ".lower() in str(row.get("Name", "")).lower() else 
        "Louisville Cardinals" if pd.isna(row["PIM - Teams"]) and "University of Louisville".lower() in str(row.get("Name", "")).lower() else 
        "Texas A&M Aggies" if pd.isna(row["PIM - Teams"]) and "Texas A&M".lower() in str(row.get("Name", "")).lower() else 
        "Kansas Jayhawks" if pd.isna(row["PIM - Teams"]) and "University of Kansas".lower() in str(row.get("Name", "")).lower() else 
        "Miami Hurricanes" if pd.isna(row["PIM - Teams"]) and "University of Miami".lower() in str(row.get("Name", "")).lower() else 
        "Nebraska Cornhuskers" if pd.isna(row["PIM - Teams"]) and ("University of Nebraska".lower() in str(row.get("Name", "")).lower() or "Nebraska".lower() in str(row.get("Name", "")).lower()) else 
        "Mercedes AMG Petronas Formula One Team" if pd.isna(row["PIM - Teams"]) and "Motorsport".lower() in str(row["PIM - Sport"]).lower() and "Mercedes".lower() in str(row.get("Name", "")).lower() else 
        "NC State Wolfpack" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["North Carolina State University", "NC State"]) else 
        "Arizona State University" if pd.isna(row["PIM - Teams"]) and "Arizona State University".lower() in str(row.get("Name", "")).lower() else 
        "Grambling State Tigers" if pd.isna(row["PIM - Teams"]) and "Grambling State University".lower() in str(row.get("Name", "")).lower() else 
        "Indiana Hoosiers" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Indiana University", "Hoosiers"]) else 
        "Washington Huskies" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["University of Washington", "Huskies"]) else 
        "Georgia Tech" if pd.isna(row["PIM - Teams"]) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Yellow Jackets", "Georgia Tech"]) else 
        "Alcorn State Braves" if pd.isna(row["PIM - Teams"]) and "Alcorn State".lower() in str(row.get("Name", "")).lower() else 
        "Arkansas-Pine Bluff Golden Lions" if pd.isna(row["PIM - Teams"]) and "Arkansas Pine Bluff".lower() in str(row.get("Name", "")).lower() else 
        "Alabama State Hornets" if pd.isna(row["PIM - Teams"]) and "Alabama State".lower() in str(row.get("Name", "")).lower() else 
        "Georgia Tech" if pd.isna(row["PIM - Teams"]) and "Georgia Tech".lower() in str(row.get("Name", "")).lower() else 
        row.get("PIM - Teams")
    ), axis=1)
    df["Enriched Team Kits"] = df.apply(lambda row: (
        "Home Kit" if pd.isna(row.get("PIM - Team Kits")) and "Home".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Home Kit" if pd.isna(row.get("PIM - Team Kits")) and "Home".lower() in str(row.get("Name", "")).lower() and "Hockey".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit" if pd.isna(row.get("PIM - Team Kits")) and "Away".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit" if pd.isna(row.get("PIM - Team Kits")) and "Away".lower() in str(row.get("Name", "")).lower() and "Hockey".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third".lower() in str(row.get("Name", "")).lower() and "Hockey".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Pre-Match" if pd.isna(row.get("PIM - Team Kits")) and "Pre-Match".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Pre-Match" if pd.isna(row.get("PIM - Team Kits")) and "Pre-Match".lower() in str(row.get("Name", "")).lower() and "Hockey".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Home Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Authentic Home".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Authentic Away".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Home Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "AU Home".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Away Kit;Authentic" if pd.isna(row.get("PIM - Team Kits")) and "AU Away".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Fourth Kit" if pd.isna(row.get("PIM - Team Kits")) and "Fourth".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Fourth Kit" if pd.isna(row.get("PIM - Team Kits")) and "Fourth".lower() in str(row.get("Name", "")).lower() and "Lifestyle".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Third Kit" if pd.isna(row.get("PIM - Team Kits")) and "Third".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Driver" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport".lower() in str(row.get("PIM - Sport", "")).lower() and "Driver".lower() in str(row.get("Name", "")).lower() else
        "Mechanic" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport".lower() in str(row.get("PIM - Sport", "")).lower() and "mechanics".lower() in str(row.get("Name", "")).lower() else
        "Authentic" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport".lower() in str(row.get("PIM - Sport", "")).lower() and "authentic".lower() in str(row.get("Name", "")).lower() else
        "Replica" if pd.isna(row.get("PIM - Team Kits")) and "Motorsport".lower() in str(row.get("PIM - Sport", "")).lower() and "replica".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Team Kits")
    ), axis=1)
    df["Enriched Technologies"] = df.apply(lambda row: (
        "COLD.RDY" if pd.isna(row.get("PIM - Technologies")) and "COLD.RDY".lower() in str(row.get("Name", "")).lower() else
        "HEAT.RDY" if pd.isna(row.get("PIM - Technologies")) and "HEAT.RDY".lower() in str(row.get("Name", "")).lower() else
        "RAIN.RDY" if pd.isna(row.get("PIM - Technologies")) and "RAIN.RDY".lower() in str(row.get("Name", "")).lower() else
        "SUMMER.RDY" if pd.isna(row.get("PIM - Technologies")) and "SUMMER.RDY".lower() in str(row.get("Name", "")).lower() else
        "WIND.RDY" if pd.isna(row.get("PIM - Technologies")) and "WIND.RDY".lower() in str(row.get("Name", "")).lower() else
        "GORE-TEX" if pd.isna(row.get("PIM - Technologies")) and "Gore-tex".lower() in str(row.get("Name", "")).lower() else
        "GORE-TEX" if pd.isna(row.get("PIM - Technologies")) and "GTX".lower() in str(row.get("Name", "")).lower() else
        "AEROREADY" if pd.isna(row.get("PIM - Technologies")) and "AEROREADY".lower() in str(row.get("Name", "")).lower() else
        "4D" if pd.isna(row.get("PIM - Technologies")) and "4D".lower() in str(row.get("Name", "")).lower() else
        "Boost" if pd.isna(row.get("PIM - Technologies")) and "Boost".lower() in str(row.get("Name", "")).lower() else
        "Bounce" if pd.isna(row.get("PIM - Technologies")) and "Bounce".lower() in str(row.get("Name", "")).lower() else
        "Dreamstrike" if pd.isna(row.get("PIM - Technologies")) and "Supernova".lower() in str(row.get("Name", "")).lower() else
        "Techfit" if pd.isna(row.get("PIM - Technologies")) and "Techfit".lower() in str(row.get("Name", "")).lower() else
        "WINTER.RDY" if pd.isna(row.get("PIM - Technologies")) and "WINTER.RDY".lower() in str(row.get("Name", "")).lower() else
        "CORDURA" if pd.isna(row.get("PIM - Technologies")) and "CORDURA".lower() in str(row.get("Name", "")).lower() else
        "PrimaLoft;EVA" if pd.isna(row.get("PIM - Technologies")) and "PUFFYLETTE".lower() in str(row.get("Name", "")).lower() else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "SL 72".lower() in str(row.get("Name", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Ultraboost 5".lower() in str(row.get("Name", "")).lower() else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "Country".lower() in str(row.get("Name", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Anthony Edwards".lower() in str(row.get("Name", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "D.O.N".lower() in str(row.get("Name", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Lightboost;Boost" if pd.isna(row.get("PIM - Technologies")) and "Trae Young".lower() in str(row.get("Name", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Bounce" if pd.isna(row.get("PIM - Technologies")) and "Tech Response".lower() in str(row.get("Name", "")).lower() else
        "Torsion" if pd.isna(row.get("PIM - Technologies")) and "Avacourt".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Bounce;Torsion" if pd.isna(row.get("PIM - Technologies")) and "Courtjam Control".lower() in str(row.get("Name", "")).lower() else
        "Bounce;EVA" if pd.isna(row.get("PIM - Technologies")) and "GameCourt".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Torsion;Boost" if pd.isna(row.get("PIM - Technologies")) and "SoleMatch".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "EVA" if pd.isna(row.get("PIM - Technologies")) and "Country Soft".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Cloudfoam" if pd.isna(row.get("PIM - Technologies")) and "RunFalcon".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "PrimaLoft" if pd.isna(row.get("PIM - Technologies")) and "PrimaLoft".lower() in str(row.get("Name", "")).lower() else
        row.get("PIM - Technologies")
    ), axis=1)
    df["Enriched Features"] = df.apply(lambda row: (
        "Lightweight;Cushioned" if pd.isna(row.get("PIM - Features")) and "SL 72".lower() in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Cushion".lower() in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Ozmillen".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Water-Repellent;Cushioned" if pd.isna(row.get("PIM - Features")) and "Puffylette".lower() in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "EVA".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Spikeless" if pd.isna(row.get("PIM - Features")) and "Spikeless".lower() in str(row.get("Name", "")).lower() else
        "Waterproof;Breathable" if pd.isna(row.get("PIM - Features")) and "GORE-TEX".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "LIGHTSTRIKE PRO".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Pleated" if pd.isna(row.get("PIM - Features")) and "Pleated".lower() in str(row.get("Name", "")).lower() else
        "Reversible" if pd.isna(row.get("PIM - Features")) and "Reversible".lower() in str(row.get("Name", "")).lower() else
        "Cushioned;Lightweight" if pd.isna(row.get("PIM - Features")) and "GameCourt".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Lo profile".lower() in str(row.get("Name", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Taekwondo".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Japan OG".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Low Profile" if pd.isna(row.get("PIM - Features")) and "Tokyo".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Lightstrike" if pd.isna(row.get("PIM - Features")) and "D.O.N".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Bounce" if pd.isna(row.get("PIM - Features")) and "Dame".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Boost;Lightstrike" if pd.isna(row.get("PIM - Features")) and "Harden".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Boost;Lightstrike" if pd.isna(row.get("PIM - Features")) and "Anthony Edwards".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "4D".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "AEROREADY".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Boost".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Bounce".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climachill".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climacool".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climacool ".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climaheat".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Breathable;Windproof;Water-Repellent;Waterproof" if pd.isna(row.get("PIM - Features")) and "Climaproof".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Moisture Wicking;Quick Dry" if pd.isna(row.get("PIM - Features")) and "Climawarm".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Cloudfoam".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "CLOUDFOAM PLUS".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Dreamstrike".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Dreamstrike+".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and "Energyrods".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "EVA".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Period Proof" if pd.isna(row.get("PIM - Features")) and "Flow Shield".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Breathable;Compression" if pd.isna(row.get("PIM - Features")) and "Formotion".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Waterproof;Windproof;Breathable" if pd.isna(row.get("PIM - Features")) and "GORE-TEX".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Lightweight;Cushioned" if pd.isna(row.get("PIM - Features")) and "LIGHT BOOST".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Lightmotion".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned;Lightweight" if pd.isna(row.get("PIM - Features")) and "Lightstrike".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Cushioned;Lightweight;Stability" if pd.isna(row.get("PIM - Features")) and "LIGHTSTRIKEPRO".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Breathable" if pd.isna(row.get("PIM - Features")) and "Primeknit".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Waterproof" if pd.isna(row.get("PIM - Features")) and "RAIN.RDY".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Shock Absorption;Lightweight" if pd.isna(row.get("PIM - Features")) and "REPETITOR".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Shock Absorption;Lightweight" if pd.isna(row.get("PIM - Features")) and "REPETITOR+".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Grip;Stability" if pd.isna(row.get("PIM - Features")) and "Stealth C4".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Compression" if pd.isna(row.get("PIM - Features")) and "Techfit".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Grip;Stability" if pd.isna(row.get("PIM - Features")) and "Traxion".lower() in str(row.get("PIM - Technologies", "")).lower() else
        "Grip" if pd.isna(row.get("PIM - Features")) and "Anthony Edwards 1".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")) and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else
        "Spikeless" if pd.isna(row.get("PIM - Features")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and "Spikeless".lower() in str(row.get("Name", "")).lower() else
        "Cushioned" if pd.isna(row.get("PIM - Features")) and "Golf".lower() in str(row.get("PIM - Sport", "")).lower() and "Gazelle".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and "Football".lower() in str(row.get("PIM - Sport", "")).lower() and "adizero Electric".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport.lower() in str(row.get("PIM - Sport", "")).lower() for sport in ["Softball", "Baseball"]) and "adizero Electric".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport.lower() in str(row.get("PIM - Sport", "")).lower() for sport in ["Softball", "Baseball"]) and "adizero Impact".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Lightweight" if pd.isna(row.get("PIM - Features")) and any(sport.lower() in str(row.get("PIM - Sport", "")).lower() for sport in ["Softball", "Baseball"]) and "adizero Instinct".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        row.get("PIM - Features")
    ), axis=1)
    df["Enriched Closure"] = df.apply(lambda row: (
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "Country XLG".lower() in str(row.get("Name", "")).lower() else
        "Slip On" if pd.isna(row.get("PIM - Closure")) and "Slip On".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Laceless" if pd.isna(row.get("PIM - Closure")) and "Laceless".lower() in str(row.get("Name", "")).lower() and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() else
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "NMD 360".lower() in str(row.get("Name", "")).lower() else
        "Slip On;Laceless" if pd.isna(row.get("PIM - Closure")) and "Superstar 360".lower() in str(row.get("Name", "")).lower() else
        "Slip On" if pd.isna(row.get("PIM - Closure")) and "adilette 22".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "BOA Laces" if pd.isna(row.get("PIM - Closure")) and "BOA".lower() in str(row.get("Name", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else
        row.get("PIM - Closure")
    ), axis=1)
    df["Enriched Best For"] = df.apply(lambda row: (
        'Race;Long Distance;Marathon' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "adizero".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "4D".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort;Neutral' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "Duramo".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort;Everyday' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "Supernova".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Comfort;Neutral' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "Solar".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Neutral' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "Response".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Everyday' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")) and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "Runfalcon".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Long Distance;Marathon' if pd.isna(row.get("PIM - Best For")) and "Running".lower() in str(row.get("PIM - Sport", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() and "adistar".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Speed;Agility;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court".lower() in str(row.get("PIM - Surface", "")).lower() and "F50".lower() in str(row.get("Name", "")).lower() else 
        'Speed;Agility;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court".lower() not in str(row.get("PIM - Surface", "")).lower() and "F50".lower() in str(row.get("Name", "")).lower() else 
        'Speed;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court".lower() in str(row.get("PIM - Surface", "")).lower() and "Crazyfast".lower() in str(row.get("Name", "")).lower() else 
        'Speed;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", ""))) and "Indoor-Court".lower() not in str(row.get("PIM - Surface", "")).lower() and "Crazyfast".lower() in str(row.get("Name", "")).lower() else 
        'Control;Inside;Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", "")).lower()) and "Indoor-Court".lower() in str(row.get("PIM - Surface", "")).lower() and "Copa".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Control;Outside;Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", "")).lower()) and "Indoor-Court" not in str(row.get("PIM - Surface", "")).lower() and "Copa".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Agility;Accuracy;Inside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", "")).lower()) and "Indoor-Court".lower() in str(row.get("PIM - Surface", "")).lower() and "Predator".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Agility;Accuracy;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", "")).lower()) and "Indoor-Court".lower() not in str(row.get("PIM - Surface", "")).lower() and "Predator".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Agility;Outside' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and ("Cleats".lower() in str(row.get("PIM adidas - Product Types", "")).lower() or "Cleats - Turf".lower() in str(row.get("PIM adidas - Product Types", "")).lower()) and "Indoor-Court".lower() in str(row.get("PIM - Surface", "")).lower() and "Nemeziz".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        'Speed;Agility;Comfort' if pd.isna(row.get("PIM - Best For")) and ("Baseball".lower() in str(row.get("PIM - Sport", "")).lower() or "Softball".lower() in str(row.get("PIM - Sport", "")).lower()) and "adizero Electric".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else 
        'Speed;Agility;Comfort;Stability' if pd.isna(row.get("PIM - Best For")) and ("Baseball".lower() in str(row.get("PIM - Sport", "")).lower() or "Softball".lower() in str(row.get("PIM - Sport", "")).lower()) and "adizero Impact".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else 
        'Speed; Agility;Comfort' if pd.isna(row.get("PIM - Best For")) and ("Baseball".lower() in str(row.get("PIM - Sport", "")).lower() or "Softball".lower() in str(row.get("PIM - Sport", "")).lower()) and "adizero Instinct".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else 
        'Agility' if pd.isna(row.get("PIM - Best For")) and ("adizero Cybersonic".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() or "adizero Ubersonic".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower()) else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Comfy".lower() in str(row.get("Name", "")).lower() else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "adilette".lower() in str(row.get("Name", "")).lower() else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "Soccer".lower() in str(row.get("PIM - Sport", "")).lower() and "T Shirts".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "Basketball Legends".lower() in str(row.get("Name", "")) else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "We Ball Together Badge of Sport".lower() in str(row.get("Name", "")).lower() else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "Badge of Sport".lower() in str(row.get("Name", "")).lower() else 
        'On-Court' if pd.isna(row.get("PIM - Best For")) and "We Ball Together".lower() in str(row.get("Name", "")).lower() else 
        'Off-Court' if pd.isna(row.get("PIM - Best For")) and "Fear of God Athletics".lower() in str(row.get("PIM - Label", "")).lower() and "Athletic & Sneakers".lower() in str(row.get("PIM adidas - Product Types", "")).lower() else 
        'Speed' if pd.isna(row.get("PIM - Best For")) and "adizero Electric".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else 
        'Comfort' if pd.isna(row.get("PIM - Best For")) and "4D".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        'Speed' if pd.isna(row.get("PIM - Best For")) and "adizero Impact".lower() in str(row.get("PIM - Product Family (productlinestyle)", "")).lower() else
        "Staying Cool;Comfort" if pd.isna(row.get("PIM - Best For")) and "AEROREADY".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Boost".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Bounce".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry;Staying Cool" if pd.isna(row.get("PIM - Best For")) and "Climachill".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry;Staying Cool" if pd.isna(row.get("PIM - Best For")) and "Climacool".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry;Staying Warm" if pd.isna(row.get("PIM - Best For")) and "Climaheat".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "Climalite".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "Climaproof".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry;Staying Warm" if pd.isna(row.get("PIM - Best For")) and "Climawarm".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort;Everyday" if pd.isna(row.get("PIM - Best For")) and "Cloudfoam".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "CLOUDFOAM PLUS".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry;Staying Warm" if pd.isna(row.get("PIM - Best For")) and "COLD.RDY".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Dreamstrike".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "Dreamstrike+".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "EVA".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "Flow Shield".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort" if pd.isna(row.get("PIM - Best For")) and "LIGHT BOOST".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort;Speed" if pd.isna(row.get("PIM - Best For")) and "Lightmotion".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort;Speed" if pd.isna(row.get("PIM - Best For")) and "Lightstrike".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Comfort;Speed" if pd.isna(row.get("PIM - Best For")) and "LIGHTSTRIKEPRO".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Versatility;Comfort" if pd.isna(row.get("PIM - Best For")) and "Primeknit".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "WIND.RDY".lower() in str(row.get("PIM - Technologies", "")).lower() else 
        "Day Hiking" if pd.isna(row.get("PIM - Best For")) and "Skychaser".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        "Day Hiking" if pd.isna(row.get("PIM - Best For")) and "Anylander".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        "Day Hiking" if pd.isna(row.get("PIM - Best For")) and "Trailmaker".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        "Moderate" if pd.isna(row.get("PIM - Best For")) and "Kirigami".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        "Moderate" if pd.isna(row.get("PIM - Best For")) and "Hiangle".lower() in str(row.get("PIM - Product Line (sportsub)", "")).lower() else 
        "On-Court" if pd.isna(row.get("PIM - Best For")) and any(name.lower() in str(row.get("Name", "")).lower() for name in ["Anthony Edwards", "D.O.N", "D.O.N Issue 5", "D.O.N Issue 6", "D.O.N Issue 7", "D.O.N Issue 8", "Dame 8", "Dame", "Trae", "Trae Unlimited"]) else 
        "On-Court" if pd.isna(row.get("PIM - Best For")) and "Basketball".lower() in str(row.get("PIM - Sport", "")).lower() and "Performance".lower() in str(row.get("PIM - Label", "")).lower() else 
        "Off-Court" if pd.isna(row.get("PIM - Best For")) and "Basketball".lower() in str(row.get("PIM - Sport", "")).lower() and "Performance".lower() not in str(row.get("PIM - Label", "")).lower() else 
        "All Mountain" if pd.isna(row.get("PIM - Best For")) and "Five Ten".lower() in str(row.get("Name", "")).lower() and any(label.lower() in str(row.get("PIM - Label", "")).lower() for label in ["Mountain Bike", "Lifestyle"]) else 
        "Staying Dry" if pd.isna(row.get("PIM - Best For")) and "RAIN.RDY".lower() in str(row.get("Name", "")).lower() else 
        "Long Distance" if pd.isna(row.get("PIM - Best For")) and "Adistar".lower() in str(row.get("Name", "")).lower() else 
        "Staying Cool;Staying Dry" if pd.isna(row.get("PIM - Best For")) and "HEAT.RDY".lower() in str(row.get("Name", "")).lower() else 
        "Staying Warm" if pd.isna(row.get("PIM - Best For")) and "COLD.RDY".lower() in str(row.get("Name", "")).lower() else 
        "Train" if pd.isna(row.get("PIM - Best For")) and "Training".lower() in str(row.get("PIM - Sport", "")).lower() else 
        "Strength Training" if pd.isna(row.get("PIM - Best For")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Power", "Optime", "Techfit"]) else 
        "Commute;Cycle" if pd.isna(row.get("PIM - Best For")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["Velosamba", "Velostan Smith"]) else 
        "Cycle" if pd.isna(row.get("PIM - Best For")) and any(x.lower() in str(row.get("Name", "")).lower() for x in ["The Road", "The Gravel", "The Indoor", "Velocade"]) else
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
    
