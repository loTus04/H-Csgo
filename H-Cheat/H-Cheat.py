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
import re
from math import *
from Import.Vector3 import Vec3

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

def base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH):

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

    if ChamsH == True:
        so_c = Fore.GREEN
    else:
        so_c = Fore.RED


    ESP_player_K = add_blank(ESP_player_K)
    AT_Flash_K = add_blank(AT_Flash_K)
    radar_K = add_blank(radar_K)
    rank_k = add_blank(rank_k)
    #QUIT_K = add_blank(QUIT_K)
    FOV_K_1 = add_blank(FOV_K_1)
    FOV_K_2 = add_blank(FOV_K_2)
    #Trig_k = add_blank(Trig_k)

    if Zoom_Power < 100:
        Zoom_Power = f"{Zoom_Power} "

    priconf = f"""

    ╔═════════════════════════╗        ╔════════════╗
    ║       Keyboard          ║        ║   Visuals  ║
    ║                         ║        ║            ║
    ║ Wall Hack:   \033[36m{ESP_player_K}{Fore.RESET}║        ║ {so_w}Wall Hack{Fore.RESET}  ║                  
    ║ Anti Flash:  \033[36m{AT_Flash_K}{Fore.RESET}║        ║ {so_f}Anti Flash{Fore.RESET} ║
    ║ Radar:       \033[36m{radar_K}{Fore.RESET}║        ║ {so_r}Radar{Fore.RESET}      ║ 
    ║ Player Info: \033[36m{rank_k}{Fore.RESET}║        ║ {Fore.GREEN}Zoom {Zoom_Power}%{Fore.RESET}  ║
    ║ Chams        \033[36m6{Fore.RESET}          ║        ║ {so_c}Chams{Fore.RESET}      ║
    ║                         ║        ╚════════════╝
    ║ Zoom +:      \033[36m{FOV_K_1}{Fore.RESET}║        
    ║ Zoom -:      \033[36m{FOV_K_2}{Fore.RESET}║
    ╚═════════════════════════╝"""

    print(priconf)

def menu():
    global banner
    os.system("cls")
    print(banner)
    
    print(f'''

                                     ╔══════════════╗
    ╔════════════════════════════╗   ║     Menu     ║
    ║       H-Csgo Cheat         ║   ║              ║
    ║                            ║   ║ Visuals:  \033[36mF2{Fore.RESET} ║
    ║ Developer: {Fore.YELLOW}loTus04 & Hawks{Fore.RESET} ║   ║ Aim:      \033[36mF3{Fore.RESET} ║
    ║ Version:   {Fore.YELLOW}2.1{Fore.RESET}             ║   ║ Movement: \033[36mF4{Fore.RESET} ║
    ╚════════════════════════════╝   ║ Misc:     \033[36mF6{Fore.RESET} ║
                                     ╚══════════════╝


    ''')

def aim(Trig_H, Tr_stat):
    global banner
    os.system("cls")
    print(banner)

    if Trig_H == False:
        so_t = Fore.RED
    else:
        so_t = Fore.GREEN

    print(f'''

    ╔════════════════╗        ╔═════════════════════╗
    ║   Keyboard     ║        ║         Aim         ║
    ║                ║        ║                     ║
    ║ Trigger Bot: \033[36m{Trig_k}{Fore.RESET} ║        ║ {so_t}Trigger Bot [{Tr_stat}]{Fore.RESET}   ║
    ╚════════════════╝        ╚═════════════════════╝

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


def misc(moneyH, whH):
    global banner
    os.system("cls")
    print(banner)

    if moneyH == True: wa = Fore.GREEN
    else: wa = Fore.RED

    if whH == True: we = Fore.GREEN
    else: we = Fore.RED

    print(f'''

    ╔═════════════════════════╗        ╔═════════════════════════╗
    ║         Keyboard        ║        ║           Misc          ║
    ║                         ║        ║                         ║
    ║ Money Hack: \033[36m1{Fore.RESET}           ║        ║ {wa}Money Hack{Fore.RESET}              ║
    ║ Wall Hack:  \033[36m2{Fore.RESET}           ║        ║ {we}Wall Hack{Fore.RESET}               ║
    ╚═════════════════════════╝        ╚═════════════════════════╝

    ''')


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
    offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
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
    m_iHealth = int(response["netvars"]["m_iHealth"])
    m_iObserverMode = int(response["netvars"]["m_iObserverMode"])
    m_iFOV = int(response["netvars"]["m_iFOV"])
    dwClientState_ViewAngles = int(response["signatures"]["dwClientState_ViewAngles"])
    m_aimPunchAngle = int(response["netvars"]["m_aimPunchAngle"])
    m_vecOrigin = int(response["netvars"]["m_vecOrigin"])
    m_vecViewOffset = int(response["netvars"]["m_vecViewOffset"])
    m_dwBoneMatrix = int(response["netvars"]["m_dwBoneMatrix"])
    m_bSpottedByMask = int(response["netvars"]["m_bSpottedByMask"])
    dwClientState_GetLocalPlayer = int(response["signatures"]["dwClientState_GetLocalPlayer"])
    m_bDormant = int(response["signatures"]["m_bDormant"])
    dwbSendPackets = int(response["signatures"]["dwbSendPackets"])
    dwInput = int(response["signatures"]["dwInput"])
    clientstate_last_outgoing_command = int(response["signatures"]["clientstate_last_outgoing_command"])
    clientstate_net_channel = int(response["signatures"]["clientstate_net_channel"])
    m_iShotsFired = int(response["netvars"]["m_iShotsFired"])
    print(f" {Fore.GREEN}[+]{Fore.RESET} Auto Updated Entities")
except:
    print(f" {Fore.GREEN}[+]{Fore.RESET} Could not Update Entities")
    exit()


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
ThirdH = False
whH = False
moneyH = False
ChamsH = False

Zoom_Power = 100

def chanms():
    global ChamsH
    while True:

        for i in range(0, 64):
            entity = pm.read_uint(client + dwEntityList + i * 0x10)
            if entity:
                entity_hp = pm.read_uint(entity + m_iHealth)

                if ChamsH == True:
                    if entity_hp >= 75: # 100-75 GREEN
                        r, g, b = 0, 255, 0
                    elif entity_hp >= 50 and entity_hp < 100: # 75-50 YELLOW
                        r, g, b = 255,255,0
                    elif entity_hp >= 25 and entity_hp < 50: # 50-25 ORANGE
                        r, g, b = 255, 165, 0
                    elif entity_hp > 5 and entity_hp < 25: # 25-6 RED
                        r, g, b = 255,0,0
                    elif entity_hp < 6: # 5-0 PURPLE
                        r, g, b = 255,0,255
                else:
                    r, g, b = 255,255,255

                pm.write_uchar(entity + 112, r)
                pm.write_uchar(entity + 113, g)
                pm.write_uchar(entity + 114, b)


def glow():
    global espH
    while True:
        if espH == True:
            glow_manager = pm.read_uint(client + dwGlowObjectManager)

            #while Tru
            #try:
            for i in range(0, 64):  # Entities 1-32 are reserved for players. 0 = worrkshop host
                entity = pm.read_uint(client + dwEntityList + i * 0x10)
                # if entity != 0:
                #     print(entity)

                if entity:
                    #pm.write_int( entity + m_bSpotted, 1 ) # radar hack

                    # glow team
                    entity_team_id = pm.read_uint( entity + m_iTeamNum )# team
                    entity_i = pm.read_uint( client + dwLocalPlayer ) #me
                    my_team = pm.read_uint(entity_i + m_iTeamNum) # My team
                    entity_glow = pm.read_uint(entity + m_iGlowIndex)
                    entity_hp = pm.read_uint(entity + m_iHealth)

                    if entity_hp >= 75: # 100-75 GREEN
                        r, g, b = 0, 255, 0
                        #print("green")
                    elif entity_hp >= 50 and entity_hp < 100: # 75-50 YELLOW
                        r, g, b = 255,255,0
                        #print("yellow")
                    elif entity_hp >= 25 and entity_hp < 50: # 50-25 ORANGE
                        r, g, b = 255, 165, 0
                        #print("orange")
                    elif entity_hp > 5 and entity_hp < 25: # 25-6 RED
                        r, g, b = 255,0,0
                        #print("red")
                    elif entity_hp < 6: # 5-0 PURPLE
                        r, g, b = 255,0,255
                        #print("purple")
                    #print(r, g, b)

                    if entity_team_id != my_team:  # Enemy in white
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))   # R 
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))   # G
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))   # B
                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # Alpha
                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                    #else: 
                        #pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))   # R
                        #pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # G
                        #pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # B
                        #pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                        #pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow
            # except:
            #     pass
        else:
            break

def antiflash():
    while flashH == True:
        player = pm.read_uint(client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(0))
        time.sleep(1)

def radar():
    while radarH == True:
        try:
            for i in range(0, 32):  # Entities 1-32 are reserved for players. 0 = worrkshop host
                entity = pm.read_uint(client + dwEntityList + i * 0x10)
                pm.write_int( entity + m_bSpotted, 1 )
        except:
            pass



def player_Info():

    global money

    base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)

    
    ranks = ["Unranked", "Silver I", "Silver II", "Silver III", "Silver IV", "Silver Elite", "Silver Elite Master", "Gold Nova I", "Gold Nova II", "Gold Nova III", "Gold Nova Master", "Master Guardian I", "Master Guardian II", "Master Guardian Elite", "Distinguished Master Guardian", "Legendary Eagle", "Legendary Eagle Master", "Supreme Master First Class", "Global Elite"]
    Friend = ""
    Enemy = ""
    for i in range( 1, 32 ):

        entity = pm.read_uint( client + dwEntityList + i * 0x10 )
        try:
            entity_hp = pm.read_uint( entity + 256) # health
            entity_team_id = pm.read_uint( entity + m_iTeamNum )# team
            entity_dormant = pm.read_uint( entity + 237 ) # dead
            wep = pm.read_uint( entity + 11768 )
        except:
            pass


        if entity:
            try:
                entity_i = pm.read_uint( client + dwLocalPlayer ) #me

                #pm.write_uchar(money, 0xEB if pm.read_uchar(money) == 0x75 else 0x75)

                #if entity_team_id != pm.read_uint( entity_i + m_iTeamNum )
                my_team = pm.read_uint( entity_i + m_iTeamNum ) # My team
                player_info = pm.read_uint((pm.read_uint(engine + dwClientState )) + dwClientState_PlayerInfo )
                player_info_items = pm.read_uint( pm.read_uint( player_info + 0x40 ) + 0xC )
                info = pm.read_uint( player_info_items + 0x28 + (i * 0x34) ) # player
                playerres = pm.read_uint( client + dwPlayerResource )
                rank = pm.read_uint( playerres + m_iCompetitiveRanking + i * 4 )
                name = pm.read_string(info + 0x10) # player name

                if pm.read_string( info + 0x10 ) != 'GOTV':
                    #print(entity_team_id)
                    #print(my_team)

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
    player = pm.read_uint(client + dwLocalPlayer)
    if player:
        on_ground = pm.read_uint(player + m_fFlags)
        if on_ground and on_ground == 257 or on_ground == 263:
            #pm.write_int(force_jump, 5)
            #time.sleep(0.08)
            pm.write_int(force_jump, 6)


def afk():
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
    #print(trig_tr)
    #print(Tr_stat)
    #while Trig_H == True:
    
    if Tr_stat == "ON ":
        while Trig_H == True:
            #print("sadad")
            # try:
            try:
                player = pm.read_uint(client + dwLocalPlayer)
                entity_id = pm.read_uint(player + m_iCrosshairId)
                entity = pm.read_uint(client + dwEntityList + (entity_id - 1) * 0x10)
                entity_team = pm.read_uint(entity + m_iTeamNum)
                player_team = pm.read_uint(player + m_iTeamNum)
                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    pm.write_int(client + dwForceAttack, 6)
            except:
                pass
                    #pm.write_int(client + dwForceAttack, 6)
                    
                    # except:
                    #     pass

    elif Tr_stat == "KEY":
        while Trig_H == True:
            if not keyboard.is_pressed(trig_tr):
                time.sleep(0.1)
            if keyboard.is_pressed(trig_tr):
                try:
                    player = pm.read_uint(client + dwLocalPlayer)
                    entity_id = pm.read_uint(player + m_iCrosshairId)
                    entity = pm.read_uint(client + dwEntityList + (entity_id - 1) * 0x10)
                    entity_team = pm.read_uint(entity + m_iTeamNum)
                    player_team = pm.read_uint(player + m_iTeamNum)
                    if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                        pm.write_int(client + dwForceAttack, 6)
                except:
                    pass

# def change_skin(skin_json):   Dead
#     engine_state = pm.read_int(engine + dwClientState)
#     #engine_state = pm.read_int(engine + dwClientState)
#     pm.write_int(engine_state + 0x174, -1)
#     while True:
#         print("asdasdsddd")
#         local_player = pm.read_int(client + dwLocalPlayer)
#         if local_player == 0:
#             continue
#         for i in range( 0, 8 ):
#             print("sadasd")
#             my_weapons = pm.read_int(local_player + m_hMyWeapons + (i - 1) * 0x4 ) & 0xFFF
#             weapon_id = pm.read_int(client + dwEntityList + (my_weapons - 1) * 0x10)
#             if weapon_id:
#                 weapon_id = pm.read_short(weapon_id + m_iItemDefinitionIndex)
#                 weapon_owner = pm.read_int(weapon_id + m_OriginalOwnerXuidLow)

#                 #
#                 weapon_id = str(weapon_id)
#                 paintid = skin_json[weapon_id]

#                 pm.write_int(weapon_id + m_iItemIDHigh, -1)
#                 pm.write_int(weapon_id + m_nFallbackPaintKit, paintid)
#                 pm.write_int(weapon_id + m_iAccountID, weapon_owner)
#                 pm.write_int(weapon_id + m_nFallbackStatTrak, 1337)
#                 pm.write_int(weapon_id + m_nFallbackSeed, 420)
#                 pm.write_float(weapon_id + m_flFallbackWear, float(0.000001))
#                 #
#         # if keyboard.is_pressed("f9"):
#         #     print("sadasd9999999999")
#         #     pm.write_int(engine_state + 0x174, -1)
#         #else:
#             #time.sleep(0.2)


def fovF():
    global Zoom_Power
    FOVH = True
    while FOVH == True:
        try:
            # player = pm.read_uint(client + dwEntityList)
            # iFOV = pm.read_uint(player + m_iDefaultFOV)
            # pm.write_int(player + m_iDefaultFOV, Zoom_Power)
            lcbase = pm.read_int(client + dwLocalPlayer)
            fov = lcbase + m_iFOV
            pm.write_int(fov, Zoom_Power)
            if Zoom_Power == 100:
                break
        except:
            pass
        #time.sleep(0.1)


def on_press(key):
    global esp, flash, espH, flashH, radarH, FOVH, Zoom_Power, page_on_screen, AFK_H, Trig_H, Tr_stat, consolOn, ThirdH, whH, moneyH, ChamsH

    key = str(key)
    key = key.replace("'", "")

    if key == ESP_player_K: # 1
        if page_on_screen == "hacks":
            if espH == True:
                espH = False
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)
            else:
                espH = True
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)
                esp = threading.Thread(target=glow)
                esp.start()

    if key == AT_Flash_K: # 2
        if page_on_screen == "hacks":
            if flashH == True:
                flashH = False
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)
            else:
                flashH = True
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)
                flash = threading.Thread(target=antiflash)
                flash.start()

    
    if key == B_Hop:
        bhop()

    if key == FOV_K_1:
        if page_on_screen == "hacks":
            if Zoom_Power > 10:
                Zoom_Power = Zoom_Power - 10
                fovv = threading.Thread(target=fovF)
                fovv.start()
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)

    if key == FOV_K_2:
        if page_on_screen == "hacks":
            if Zoom_Power < 170:
                Zoom_Power = Zoom_Power + 10
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)

    if key == radar_K: # 3
        if page_on_screen == "hacks":
            if radarH == True:
                radarH = False
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)
            else:
                radarH = True
                radarr = threading.Thread(target=radar)
                radarr.start()
                base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)


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

    if key == rank_k: #4
        if page_on_screen == "hacks":
            player_Info()

    if key == "5": #5
        if page_on_screen == "hacks":
            if ThirdH == True:
                ThirdH = False
                lcbase = pm.read_int(client + dwLocalPlayer)
                pm.write_int(lcbase + m_iObserverMode, 0)
                #fov = lcbase + m_iFOV
                #pm.write_int(fov, 160)
            else:
                ThirdH = True
                lcbase = pm.read_int(client + dwLocalPlayer)
                pm.write_int(lcbase + m_iObserverMode, 1)
                #player = pm.read_uint(client + dwEntityList)
                #iFOV = pm.read_uint(player + m_iDefaultFOV)
                #pm.write_int(player + m_iDefaultFOV, 160)
                #fov = lcbase + m_iFOV
                #pm.write_int(fov, 120)
    
    if key == "2":
        if page_on_screen == "misc": 
            global wall
            #pm.write_uchar(wall, 2 if pm.read_uchar(wall) == 1 else 1)
            if whH == True:
                whH = False
                truc = 2
            else:
                whH = True
                truc = 1
            misc(moneyH, whH)
            pm.write_uchar(wall, truc)

    
    if key == "1":
        if page_on_screen == "misc": 
            global money

            #pm.write_uchar(money, 0xEB if pm.read_uchar(money) == 0x75 else 0x75)

            if moneyH == True:
                moneyH = False
                truc = 0x75
            else:
                moneyH = True
                truc = 0xEB
            misc(moneyH, whH)
            pm.write_uchar(money, truc)

    if key == "6":
        if page_on_screen == "hacks":

            if ChamsH == True:
                ChamsH = False
            else:
                ChamsH = True
                chama = threading.Thread(target=chanms)
                chama.start()
            base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)



    if key == Trig_k:
        if page_on_screen == "aim":

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
                aim(Trig_H, Tr_stat)

            elif Trig_H == True:
                if Tr_stat == "KEY": 
                    Trig_H = False
                    Tr_stat = "OFF"

                    aim(Trig_H, Tr_stat)
                
                elif Tr_stat == "ON ":
                    Tr_stat = "KEY"
                    Trig_H = False # make other fuction stop
                    time.sleep(0.2) # make shure the other thread stops
                    Trig_H = True
                    trigg = threading.Thread(target=trigerBot, args=[Tr_stat, trig_tr])
                    trigg.start()
                    aim(Trig_H, Tr_stat)



    #elif key == "aa ":
        #devConsol()


    elif key == "Key.f1":
        page_on_screen = "menu"
        menu()

    elif key == "Key.f2":
        page_on_screen = "hacks"
        base(espH, flashH, banner, radarH, ESP_player_K, AT_Flash_K, radar_K, rank_k, FOV_K_1, FOV_K_2, Zoom_Power, ChamsH)

    elif key == "Key.f3":
        page_on_screen = "aim"
        aim(Trig_H, Tr_stat)
    elif key == "Key.f4":
        page_on_screen = "macro"
        macro(anti_afk, B_Hop, AFK_H)

    elif key == "Key.f6":
        page_on_screen = "misc"
        misc(moneyH, whH)
    
    # elif key == "Key.f9":
    #     engine_state = pm.read_int(engine + dwClientState)
    #     pm.write_int(engine_state + 0x174, -1)

    elif key == "Key.delete":
        cheat_hwnd = win32gui.FindWindow(None, "CSGO Hacks by Hawks and loTus04")
        if consolOn == False:
            consolOn = True
            win32gui.ShowWindow(cheat_hwnd, win32con.SW_SHOW)
        else:
            consolOn = False
            win32gui.ShowWindow(cheat_hwnd, win32con.SW_HIDE)
        
        # time.sleep(1)
        # cheat_hwnd = win32gui.FindWindow(None, "CSGO Hacks by Hawks and loTus04")

        # win32gui.ShowWindow(cheat_hwnd, win32con.SW_HIDE)
        # time.sleep(5)
        # win32gui.ShowWindow(cheat_hwnd, win32con.SW_SHOW)
        # input()
        # quit()

    elif key == QUIT_K:
        print(f" {Fore.RED}[BYE] Exited the script{Fore.RESET}\n")
        quit()



def check_hwid():
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    print(f" [~] HWID: {hwid}")

    try:
        r = requests.get(f'https://hcheat-shop.mtxserv.com/api/api_traitement.php?hwid={hwid}')
    except:
        print(f' {Fore.RED}[ERROR]{Fore.RESET} Failed to connect to database')
        input()
        exit()

    result = str(r.text)

    if len(result) > 8:
        r_res = result.split(",")
        createdDate = r_res[0]
        keyTime = r_res[1]

        day_left = (int(createdDate) + int(keyTime)) - int(time.time())
        day_left = day_left/24/60/60
        day_left = round(day_left)
        print(f" [~] Time Left: {day_left} Days")
        if int(createdDate) + int(keyTime) > int(time.time()): 
            result = "good"
            return result
        
        else:
            print(f" {Fore.RED}[ERROR]{Fore.RESET} KEY Explired")
            input()
            exit()

    else:
        print(banner)
        print(f' {Fore.RED}[ERROR]{Fore.RESET} HWID Not in Database')
        print(f' [?] HWID: \33[4m{hwid}{Style.RESET_ALL}') 
        input()
        exit()

# on start

#result = check_hwid()
result = "good"
if result == "good":
    no_scgo = True
    print(f" {Fore.RED}[?]{Fore.RESET} CSGO not Detected")
    while no_scgo == True:
        try:
            pm = pymem.Pymem("csgo.exe")
            client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
            engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
            client2 = pymem.process.module_from_name(pm.process_handle, "client.dll")
            no_scgo = False
            print(f" {Fore.GREEN}[!]{Fore.RESET} Injected CSGO")
            print(banner)
            time.sleep(0.3)
            #print(pm.read_bytes(client, client2.SizeOfImage))
            #print("ff")
            m_drawOtherModels = re.search(rb"\x83\xF8.\x8B\x45\x08\x0F", pm.read_bytes(client, client2.SizeOfImage)).start() + 2
            wall = client + m_drawOtherModels
            m_money = re.search(rb".\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF", pm.read_bytes(client, client2.SizeOfImage)).start()
            money = client + m_money

            # path_json = os.path.dirname(os.path.abspath(__file__))
            # path_json_key = path_json + "\config\skin.json"
            # f_key = open(path_json_key)
            # skin_json = json.load(f_key)
            # skins = threading.Thread(target=change_skin, args=[skin_json])
            # skins.start()
            page_on_screen = "menu"
            menu()

            #fovv = threading.Thread(target=fov)
            #fovv.start()

        except:
            pass

    if no_scgo == False:
        with Listener(on_press=on_press) as listener:
            listener.join()
