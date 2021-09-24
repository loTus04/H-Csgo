import subprocess 
import requests 
import time 
import os
import pymem
import pymem.process
import keyboard
import time
import threading
import sys
from colorama import Fore, Style, Back
from pynput.keyboard import Listener
import json
import ctypes
import win32gui
import win32con


#time.sleep(2)
#print(cheat_hwnd)
#win32gui.SetWindowPos(pm.process_handle, win32con.HWND_TOPMOST, 100, 100, 900, 550, 0)

page_on_screen = "None"

def add_blank(key):
    blank = len(key)
    if blank > 9:
        key = "Key.Error  "
    else:
        add = 11 - blank
        for i in range(add):
            key = key + " "
        return key

def base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat):

    os.system("cls")
    print(banner)

    # just so its dosn;t get ugly
    if espH == True:
        so_w = Fore.GREEN
    else:
        so_w = Fore.RED

    if flashH == True:
        so_f = Fore.GREEN
    else:
        so_f = Fore.RED

    if radarH == True:
        so_r = Fore.GREEN
    else:
        so_r = Fore.RED

    if Trig_H == False:
        so_t = Fore.RED
    else:
        so_t = Fore.GREEN


    ESP_player_K = add_blank(ESP_player_K)
    AT_Flash_K = add_blank(AT_Flash_K)
    radar_K = add_blank(radar_K)
    rank_k = add_blank(rank_k)
    QUIT_K = add_blank(QUIT_K)
    FOV_K_1 = add_blank(FOV_K_1)
    FOV_K_2 = add_blank(FOV_K_2)
    Trig_k = add_blank(Trig_k)

    if Zoom_Power < 100:
        Zoom_Power = f"{Zoom_Power} "


    priconf = f"""

    ╔═════════════════════════╗        ╔═════════════════════════╗
    ║       Keyboard          ║        ║          Hacks          ║
    ║                         ║        ║                         ║
    ║ Wall Hack:   \033[36m{ESP_player_K}{Fore.RESET}║        ║ {so_w}Wall Hack{Fore.RESET}               ║                  
    ║ Anti Flash:  \033[36m{AT_Flash_K}{Fore.RESET}║        ║ {so_f}Anti Flash{Fore.RESET}              ║
    ║ Radar:       \033[36m{radar_K}{Fore.RESET}║        ║ {so_r}Radar{Fore.RESET}                   ║ 
    ║ Trigger Bot: \033[36m{Trig_k}{Fore.RESET}║        ║ {so_t}Trigger Bot [{Tr_stat}]{Fore.RESET}       ║
    ║                         ║        ║ {Fore.GREEN}Zoom {Zoom_Power}%{Fore.RESET}               ║
    ║ Zoom +:      \033[36m{FOV_K_1}{Fore.RESET}║        ╚═════════════════════════╝
    ║ Zoom -:      \033[36m{FOV_K_2}{Fore.RESET}║
    ║ Player Info: \033[36m{rank_k}{Fore.RESET}║
    ║ Exit:        \033[36m{QUIT_K}{Fore.RESET}║  
    ╚═════════════════════════╝

"""
    print(priconf)

def menu():
    global banner
    os.system("cls")
    print(banner)
    
    print(f'''

                                     ╔═══════════╗
    ╔════════════════════════════╗   ║    Menu   ║
    ║       H-Csgo Cheat         ║   ║           ║
    ║                            ║   ║ Main:  \033[36mF1{Fore.RESET} ║
    ║ Developer: {Fore.YELLOW}loTus04 & Hawks{Fore.RESET} ║   ║ Hacks: \033[36mF2{Fore.RESET} ║
    ║ Version:   {Fore.YELLOW}2.0{Fore.RESET}             ║   ║ Macro: \033[36mF3{Fore.RESET} ║
    ╚════════════════════════════╝   ║ Tools: \033[36mF4{Fore.RESET} ║
                                     ║ Help:  \033[36mF5{Fore.RESET} ║
                                     ╚═══════════╝

    ''')


def macro(anti_afk, B_Hop, AFK_H):
    global banner
    os.system("cls")
    print(banner)

    if AFK_H == True:
        wa = Fore.GREEN
    else:
        wa = Fore.RED

    print(f'''

    ╔═════════════════════════╗        ╔═════════════════════════╗
    ║       Keyboard          ║        ║          Macros         ║
    ║                         ║        ║                         ║
    ║ Anti AFK:  \033[36m{anti_afk}{Fore.RESET}            ║        ║ {wa}Anti AFK{Fore.RESET}                ║
    ║ Bonny Hop: \033[36m{B_Hop}{Fore.RESET}    ║        ║ {Fore.GREEN}Bonny Hop{Fore.RESET}               ║
    ╚═════════════════════════╝        ╚═════════════════════════╝

    ''')


def tools():
    global banner
    os.system("cls")
    print(banner)


def help():
    global banner
    os.system("cls")
    print(banner)


try:
    os.system('cls')
    os.system("title CSGO Hacks by Hawks and loTus04")
except:
    os.system("clear")

# configured keys
try:
    
    path_json = os.path.dirname(os.path.abspath(__file__))
    path_json_key = path_json + "\config\keys.json"
    f_key = open(path_json_key)
    key_json = json.load(f_key)

    radar_K = key_json["Radar_KEY"]
    ESP_player_K = key_json["Wall_Hack_KEY"]
    AT_Flash_K = key_json["Anti_flash_KEY"]
    B_Hop = key_json["B_Hop_KEY"]
    QUIT_K = key_json["Exit_KEY"]
    rank_k = key_json["Display_Rank"]
    FOV_K_1 = key_json["zoom_up"]
    FOV_K_2 = key_json["zoom_back"]
    anti_afk = key_json["Anti_AFK_KEY"]
    Trig_k = key_json["Triger_Bot_KEY_TOGGLE"]
    trig_tr = key_json["Triger_Bot_KEY_ACCTIVATE"]


except:
    print(f" {Fore.GREEN}[+]{Fore.RESET} Could not load keys")

# csgo item ids
try:
    offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
    response = requests.get( offsets ).json()
    dwEntityList = int(response["signatures"]["dwEntityList"])
    dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
    m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
    m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
    dwForceJump = int(response["signatures"]["dwForceJump"])
    dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
    m_fFlags = int(response["netvars"]["m_fFlags"])
    m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])
    m_bSpotted = int(response["netvars"]["m_bSpotted"])
    dwClientState = int(response["signatures"]["dwClientState"])
    dwClientState_PlayerInfo = int(response["signatures"]["dwClientState_PlayerInfo"])
    dwPlayerResource = int(response["signatures"]["dwPlayerResource"])
    m_iCompetitiveRanking = int(response["netvars"]["m_iCompetitiveRanking"])
    dwForceAttack = int(response["signatures"]["dwForceAttack"])
    m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
    dwClientState = int( response["signatures"]["dwClientState"] )
    m_hMyWeapons = int(response['netvars']['m_hMyWeapons'])
    m_iItemDefinitionIndex = int(response["netvars"]["m_iItemDefinitionIndex"])
    m_OriginalOwnerXuidLow = int(response["netvars"]["m_OriginalOwnerXuidLow"])
    m_iItemIDHigh = int(response["netvars"]["m_iItemIDHigh"])
    m_nFallbackPaintKit = int(response["netvars"]["m_nFallbackPaintKit"])
    m_iAccountID = int(response["netvars"]["m_iAccountID"])
    m_nFallbackStatTrak = int(response["netvars"]["m_nFallbackStatTrak"])
    m_nFallbackSeed = int(response["netvars"]["m_nFallbackSeed"])
    m_flFallbackWear = int(response["netvars"]["m_flFallbackWear"])
    m_iDefaultFOV = 0x332C
    print(f" {Fore.GREEN}[+]{Fore.RESET} Auto Updated Entities")
except:
    print(f" {Fore.GREEN}[+]{Fore.RESET} Could not Update Entities")


banner = f"""
        {Fore.RED}██{Fore.YELLOW}╗ {Fore.RED} ██{Fore.YELLOW}╗       {Fore.RED}██████{Fore.YELLOW}╗{Fore.RED}███████{Fore.YELLOW}╗ {Fore.RED}██████{Fore.YELLOW}╗  {Fore.RED}██████{Fore.YELLOW}╗ 
        {Fore.RED}██{Fore.YELLOW}║  {Fore.RED}██{Fore.YELLOW}║      {Fore.RED}██{Fore.YELLOW}╔════╝{Fore.RED}██{Fore.YELLOW}╔════╝{Fore.RED}██{Fore.YELLOW}╔════╝ {Fore.RED}██{Fore.YELLOW}╔═══{Fore.RED}██{Fore.YELLOW}╗
        {Fore.RED}███████{Fore.YELLOW}║{Fore.RED}█████{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}║     {Fore.RED}███████{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}║  {Fore.RED}███{Fore.YELLOW}╗{Fore.RED}██{Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}║
        {Fore.RED}██{Fore.YELLOW}╔══{Fore.RED}██{Fore.YELLOW}║╚════╝{Fore.RED}██{Fore.YELLOW}║     ╚════{Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}║{Fore.RED}██{Fore.YELLOW}║   {Fore.RED}██{Fore.YELLOW}║
        {Fore.RED}██{Fore.YELLOW}║  {Fore.RED}██{Fore.YELLOW}║      {Fore.YELLOW}╚{Fore.RED}██████{Fore.YELLOW}╗{Fore.RED}███████{Fore.YELLOW}║╚{Fore.RED}██████{Fore.YELLOW}╔╝╚{Fore.RED}██████{Fore.YELLOW}╔╝
        ╚═╝  ╚═╝       ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ {Fore.RESET}                              
        """

# cheat focntions 

espH = False
flashH = False
radarH = False
FOVH = False
AFK_H = False
Trig_H = False
Tr_stat = "OFF"
consolOn = True

Zoom_Power = 100

def glow():
    global espH
    while True:
        if espH == True:
            glow_manager = pm.read_int(client + dwGlowObjectManager)

            try:
                for i in range(0, 32):  # 1-32 = All players id | id 0 is only for workskop owner
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:

                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        Thatsme = pm.read_int(client + dwLocalPlayer)
                        my_team = pm.read_int(Thatsme + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)

                        if entity_team_id != my_team:  # Enemy in white
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

            except:
                pass
        else:
            break


def antiflash():
    while flashH == True:
        player = pm.read_int(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(0))
        time.sleep(1)

def radar():
    while radarH == True:
        try:
            for i in range(0, 32):  # Entities 1-32 are reserved for players. 0 = worrkshop host
                entity = pm.read_int(client + dwEntityList + i * 0x10)
                pm.write_int( entity + m_bSpotted, 1 )
        except:
            pass



def player_Info():

    base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)

    ranks = ["Unranked", "Silver I", "Silver II", "Silver III", "Silver IV", "Silver Elite", "Silver Elite Master", "Gold Nova I", "Gold Nova II", "Gold Nova III", "Gold Nova Master", "Master Guardian I", "Master Guardian II", "Master Guardian Elite", "Distinguished Master Guardian", "Legendary Eagle", "Legendary Eagle Master", "Supreme Master First Class", "Global Elite"]
    Friend = ""
    Enemy = ""
    for i in range(1, 32):

        entity = pm.read_int( client + dwEntityList + i * 0x10)
        try:
            entity_hp = pm.read_int( entity + 256) # health
            entity_team_id = pm.read_int( entity + m_iTeamNum )# team
            entity_dormant = pm.read_int( entity + 237) # dead
            wepond = pm.read_int( entity + 11768)
        except:
            pass


        if entity:
            try:
                entity_i = pm.read_int(client + dwLocalPlayer ) #me

                my_team = pm.read_int(entity_i + m_iTeamNum ) # My team
                player_info = pm.read_int((pm.read_int(engine + dwClientState )) + dwClientState_PlayerInfo)
                player_info_items = pm.read_int(pm.read_int( player_info + 0x40) + 0xC)
                info = pm.read_int(player_info_items + 0x28 + (i * 0x34)) # player
                playerres = pm.read_int(client + dwPlayerResource)
                rank = pm.read_int(playerres + m_iCompetitiveRanking + i * 4)
                name = pm.read_string(info + 0x10) # player name

                if pm.read_string( info + 0x10 ) != 'GOTV': # GOTV = spec

                    if entity_team_id != my_team:
                        #print(entity_team_id)
                        if entity_team_id == 2:
                            team = "Terrorist"
                            team_color = Fore.RED
                        elif entity_team_id == 3:
                            team = "Counter_Terrorist"
                            team_color = "\033[36m"

                        if entity_dormant < 100:
                            Status = "Alive"
                        elif entity_dormant > 100:
                            Status = "Dead"
                        
                        Enemy = Enemy + f"\n{team_color}Name: {name} | Team: {team} (Enemy) | Health: {entity_hp} | Status: {Status} | Rank: {ranks[rank]}"

                    else:
                        if entity_team_id == 2:
                            team = "Terrorist"
                            team_color = Fore.RED
                        elif entity_team_id == 3:
                            team = "Counter_Terrorist"
                            team_color = "\033[36m"
                        if entity_dormant < 100:
                            Status = "Alive"
                        elif entity_dormant > 100:
                            Status = "Dead"
                        
                        Friend = Friend + f"\n{team_color}Name: {name} | Team: {team} (Friend) | Health: {entity_hp} | Status: {Status} | Rank: {ranks[rank]}"

            except:
                pass

    print(Friend)
    print()
    print(Enemy)


def bhop():
    force_jump = client + dwForceJump
    player = pm.read_int(client + dwLocalPlayer)
    if player:
        on_ground = pm.read_int(player + m_fFlags)
        if on_ground and on_ground == 257:
            pm.write_int(force_jump, 5)
            time.sleep(0.08)
            pm.write_int(force_jump, 4)


def afk():

    # Found that on https://stackoverflow.com/questions/66274781/python-keyboard-input
    # Thx ;) 

    SendInput = ctypes.windll.user32.SendInput
    # C struct redefinitions
    PUL = ctypes.POINTER(ctypes.c_ulong)

    class KeyBdInput(ctypes.Structure):
        _fields_ = [("wVk", ctypes.c_ushort), ("wScan", ctypes.c_ushort), ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong), ("dwExtraInfo", PUL)]

    class HardwareInput(ctypes.Structure):
        _fields_ = [("uMsg", ctypes.c_ulong), ("wParamL", ctypes.c_short), ("wParamH", ctypes.c_ushort)]

    class MouseInput(ctypes.Structure):
        _fields_ = [("dx", ctypes.c_long),("dy", ctypes.c_long), ("mouseData", ctypes.c_ulong), ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong), ("dwExtraInfo", PUL)]

    class Input_I(ctypes.Union):
        _fields_ = [("ki", KeyBdInput), ("mi", MouseInput), ("hi", HardwareInput)]

    class Input(ctypes.Structure):
        _fields_ = [("type", ctypes.c_ulong), ("ii", Input_I)]

    def PressKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def ReleaseKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    time.sleep(5)
    while AFK_H == True:

        # W = 0x11 | A = 0x1E | S = 0x1F | D = 0x20 | UP = 0xC8 | LEFT = 0xCB | RIGHT = 0xCD | DOWN = 0xD0 | ENTER = 0x1C | ESC = 0x01 | TWO = 0x03
        # This will make the csgo-player walk in a small square
        PressKey(0x11)        
        time.sleep(0.5)
        ReleaseKey(0x11)

        PressKey(0x1E)
        time.sleep(0.5)
        ReleaseKey(0x1E)

        PressKey(0x1F)
        time.sleep(0.5)
        ReleaseKey(0x1F)

        PressKey(0x20)
        time.sleep(0.5)
        ReleaseKey(0x20)


def trigerBot(Tr_stat, trig_tr):
    print(trig_tr)
    print(Tr_stat)

    #while Trig_H == True:
        
    if Tr_stat == "ON ":
        while Trig_H == True:
            try:
                player = pm.read_int(client + dwLocalPlayer)
                entity_id = pm.read_int(player + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)
                entity_team = pm.read_int(entity + m_iTeamNum)
                player_team = pm.read_int(player + m_iTeamNum)
                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    pm.write_int(client + dwForceAttack, 6)
            except:
                pass

    elif Tr_stat == "KEY":
        while Trig_H == True:
            if not keyboard.is_pressed(trig_tr):
                time.sleep(0.1)
            if keyboard.is_pressed(trig_tr):
                try:
                    player = pm.read_int(client + dwLocalPlayer)
                    entity_id = pm.read_int(player + m_iCrosshairId)
                    entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)
                    entity_team = pm.read_int(entity + m_iTeamNum)
                    player_team = pm.read_int(player + m_iTeamNum)
                    if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                        pm.write_int(client + dwForceAttack, 6)
                except:
                    pass
    
def change_skin(skin_json):
    engine_state = pm.read_int(engine + dwClientState)
    while True:
        local_player = pm.read_int(client + dwLocalPlayer)
        if local_player == 0:
            continue
        for i in range( 0, 8 ):
            my_weapons = pm.read_int(local_player + m_hMyWeapons + (i - 1) * 0x4 ) & 0xFFF
            weapon_id = pm.read_int(client + dwEntityList + (my_weapons - 1) * 0x10)
            if weapon_id:
                weapon_id = pm.read_short(weapon_id + m_iItemDefinitionIndex)
                weapon_owner = pm.read_int(weapon_id + m_OriginalOwnerXuidLow)

                try:
                    weapon_id = str(weapon_id)
                    paintid = skin_json[weapon_id]

                    pm.write_int(weapon_id + m_iItemIDHigh, -1)
                    pm.write_int(weapon_id + m_nFallbackPaintKit, paintid)
                    pm.write_int(weapon_id + m_iAccountID, weapon_owner)
                    pm.write_int(weapon_id + m_nFallbackStatTrak, 1337)
                    pm.write_int(weapon_id + m_nFallbackSeed, 420)
                    pm.write_float(weapon_id + m_flFallbackWear, float(0.000001))
                except:
                    pass
        if keyboard.is_pressed("f9"):
            pm.write_int(engine_state + 0x174, -1)
        #else:
            #time.sleep(0.2)

'''
def fov():
    global Zoom_Power
    while FOVH == True:
        try:
            player = pm.read_int(client + dwEntityList)
            iFOV = pm.read_int(player + m_iDefaultFOV)
            pm.write_int(player + m_iDefaultFOV, Zoom_Power)
        except:
            pass
'''


# active cheats
#esp = threading.Thread(target=glow)
#flash = threading.Thread(target=antiflash)

# espH = False
# flashH = False

def on_press(key):
    global esp
    global flash
    global espH
    global flashH
    global radarH
    global FOVH
    global Zoom_Power
    global page_on_screen
    global AFK_H
    global Trig_H
    global Tr_stat

    key = str(key)
    key = key.replace("'", "")

    if key == ESP_player_K: # 1
        if page_on_screen == "hacks":
            if espH == True:
                espH = False
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)
            else:
                espH = True
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)
                esp = threading.Thread(target=glow)
                esp.start()

    elif key == AT_Flash_K: # 2
        if page_on_screen == "hacks":
            if flashH == True:
                flashH = False
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)
            else:
                flashH = True
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)
                flash = threading.Thread(target=antiflash)
                flash.start()

    
    elif key == B_Hop:
        bhop()

    elif key == FOV_K_1:
        if page_on_screen == "hacks":
            if Zoom_Power > 10:
                Zoom_Power = Zoom_Power - 10
                player = pm.read_int(client + dwEntityList)
                iFOV = pm.read_int(player + m_iDefaultFOV)
                pm.write_int(player + m_iDefaultFOV, Zoom_Power)
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)

    elif key == FOV_K_2:
        if page_on_screen == "hacks":
            if Zoom_Power < 170:
                Zoom_Power = Zoom_Power + 10
                player = pm.read_int(client + dwEntityList)
                iFOV = pm.read_int(player + m_iDefaultFOV)
                pm.write_int(player + m_iDefaultFOV, Zoom_Power)
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)

    elif key == radar_K: # 3
        if page_on_screen == "hacks":
            if radarH == True:
                radarH = False
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)
            else:
                radarH = True
                radarr = threading.Thread(target=radar)
                radarr.start()
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)


    if key == anti_afk: # 1
        if page_on_screen == "macro":
            if AFK_H == True:
                AFK_H = False
                macro(anti_afk, B_Hop, AFK_H)
            else:
                AFK_H = True
                afkkk = threading.Thread(target=afk)
                afkkk.start()
                macro(anti_afk, B_Hop, AFK_H)

    elif key == rank_k: #4
        if page_on_screen == "hacks":
            player_Info()

    elif key == Trig_k:
        if page_on_screen == "hacks":

            if Trig_H == False:
                Trig_H = True

                if Tr_stat == "KEY":
                    Tr_stat = "OFF"

                if Tr_stat == "ON ":
                    Tr_stat = "KEY"
                
                if Tr_stat == "OFF":
                    Tr_stat = "ON "


                trigg = threading.Thread(target=trigerBot, args=[Tr_stat, trig_tr])
                trigg.start()
                base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)

            elif Trig_H == True:
                if Tr_stat == "KEY": 
                    Trig_H = False
                    Tr_stat = "OFF"

                    base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)
                
                elif Tr_stat == "ON ":
                    Tr_stat = "KEY"
                    Trig_H = False # make other fuction stop
                    time.sleep(0.2) # make shure the other thread stops
                    Trig_H = True
                    trigg = threading.Thread(target=trigerBot, args=[Tr_stat, trig_tr])
                    trigg.start()
                    base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)



    #elif key == "aa ":
        #devConsol()


    elif key == "Key.f1":
        page_on_screen = "menu"
        menu()

    elif key == "Key.f2":
        page_on_screen = "hacks"
        base(espH, flashH, banner, B_Hop, radarH, FOVH, ESP_player_K, AT_Flash_K, QUIT_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, Trig_k, Trig_H, Tr_stat)

    elif key == "Key.f3":
        page_on_screen = "macro"
        macro(anti_afk, B_Hop, AFK_H)
    
    elif key == "Key.f4":
        page_on_screen = "tools"
        tools()

    elif key == "Key.f5":
        page_on_screen = "help"
        help()

    elif key == QUIT_K:
        print(f" {Fore.RED}[BYE] Exited the script{Fore.RESET}\n")
        quit()



# (had an hwid check here before)
result = "good"

if result == "good":
    no_scgo = True
    print(f" {Fore.RED}[?]{Fore.RESET} CSGO not Detected")
    while no_scgo == True:
        try:
            pm = pymem.Pymem("csgo.exe")
            client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
            engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
            no_scgo = False
            print(f" {Fore.GREEN}[!]{Fore.RESET} Injected CSGO")
            print(banner)
            time.sleep(0.3)

            # auto runing cheats
            
            path_json = os.path.dirname(os.path.abspath(__file__))
            path_json_key = path_json + "\config\skin.json"
            f_key = open(path_json_key)
            skin_json = json.load(f_key)
            skins = threading.Thread(target=change_skin, args=[skin_json])
            skins.start()

            page_on_screen = "menu"
            menu()

            #fovv = threading.Thread(target=fov)
            #fovv.start()

        except:
            pass

    if no_scgo == False:
        with Listener(on_press=on_press) as listener:
            listener.join()
