from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Cài đặt driver cho Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Bước 1: Mở trang web
urlRoot = 'https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats' 
goalKeepingUrl = 'https://fbref.com/en/comps/9/2023-2024/keepers/2023-2024-Premier-League-Stats'
shootingUrl = 'https://fbref.com/en/comps/9/2023-2024/shooting/2023-2024-Premier-League-Stats'
passingUrl = 'https://fbref.com/en/comps/9/2023-2024/passing/2023-2024-Premier-League-Stats'
passTypeUrl = 'https://fbref.com/en/comps/9/2023-2024/passing_types/2023-2024-Premier-League-Stats'
goalAndShotCreationUrl = 'https://fbref.com/en/comps/9/2023-2024/gca/2023-2024-Premier-League-Stats'
defensiveUrl = 'https://fbref.com/en/comps/9/2023-2024/defense/2023-2024-Premier-League-Stats'
possessionUrl = 'https://fbref.com/en/comps/9/2023-2024/possession/2023-2024-Premier-League-Stats'
playingTimeUrl = 'https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats'
miscellaneousUrl = 'https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats'






def openDriver(url):
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getFirtsName(s):
    tmp = s.split()
    return tmp[0]



def findInStats(texts, s):
    player = []
    td = texts.find_all('td', attrs = {"data-stat":s})
    for x in td:
        if len(str(x)) != 0:
            player.append(x.text.strip())
    return player

    
    
    


res = {}
soup = openDriver(urlRoot)
divs = soup.find('div', attrs={'id': 'div_stats_standard'})
texts = divs.find('table')

res['player'] = findInStats(texts, 'player')
res['nationality'] = findInStats(texts, 'nationality')
res['team'] = findInStats(texts, 'team')
res['position'] = findInStats(texts, 'position')
res['age'] = findInStats(texts, 'age')
res['games'] = findInStats(texts, 'games')
res['games_starts'] = findInStats(texts, 'games_starts')
res['minutes'] = findInStats(texts, 'minutes')
res['goals_pens'] = findInStats(texts, 'goals_pens')
res['pens_made'] = findInStats(texts, 'pens_made')
res['assists'] = findInStats(texts, 'assists')
res['cards_yellow'] = findInStats(texts, 'cards_yellow')
res['cards_red'] = findInStats(texts, 'cards_red')
res['xg'] = findInStats(texts, 'xg')
res['npxg'] = findInStats(texts, 'npxg')
res['xg_assist'] = findInStats(texts, 'xg_assist')
res['progressive_carries'] = findInStats(texts, 'progressive_carries')
res['progressive_passes'] = findInStats(texts, 'progressive_passes')
res['progressive_passes_received'] = findInStats(texts, 'progressive_passes_received')
res['goals_per90'] = findInStats(texts, 'goals_per90')
res['assists_per90'] = findInStats(texts, 'assists_per90')
res['goals_assists_per90'] = findInStats(texts, 'goals_assists_per90')
res['goals_pens_per90'] = findInStats(texts, 'goals_pens_per90')
res['goals_assists_pens_per90'] = findInStats(texts, 'goals_assists_pens_per90')
res['xg_per90'] = findInStats(texts, 'xg_per90')
res['xg_assist_per90'] = findInStats(texts, 'xg_assist_per90')
res['xg_xg_assist_per90'] = findInStats(texts, 'xg_xg_assist_per90')
res['npxg_per90'] = findInStats(texts, 'npxg_per90')
res['npxg_xg_assist_per90'] = findInStats(texts, 'npxg_xg_assist_per90')
#29




# stat goal keeper
res1 = {}
soupGoalKeeping = openDriver(goalKeepingUrl)
texts = soupGoalKeeping.find('table', attrs={'id':'stats_keeper'})
res1['player'] = findInStats(texts, 'player')
res1['team'] = findInStats(texts, 'team')
res1['gk_goals_against'] = findInStats(texts, 'gk_goals_against')
res1['gk_goals_against_per90'] = findInStats(texts, 'gk_goals_against_per90')
res1['gk_shots_on_target_against'] = findInStats(texts, 'gk_shots_on_target_against')
res1['gk_save_pct'] = findInStats(texts, 'gk_save_pct')
res1['gk_wins'] = findInStats(texts, 'gk_wins')
res1['gk_ties'] = findInStats(texts, 'gk_ties')
res1['gk_losses'] = findInStats(texts, 'gk_losses')
res1['gk_clean_sheets'] = findInStats(texts, 'gk_clean_sheets')
res1['gk_clean_sheets_pct'] = findInStats(texts, 'gk_clean_sheets_pct')
res1['gk_pens_att'] = findInStats(texts, 'gk_pens_att')
res1['gk_pens_allowed'] = findInStats(texts, 'gk_pens_allowed')
res1['gk_pens_saved'] = findInStats(texts, 'gk_pens_saved')
res1['gk_pens_missed'] = findInStats(texts, 'gk_pens_missed')
res1['gk_pens_save_pct'] = findInStats(texts, 'gk_pens_save_pct')
#14

# stat shooting
res2 = {}
soupShooting = openDriver(shootingUrl)
texts = soupShooting.find('table', attrs={'id':'stats_shooting'})
res2['player'] = findInStats(texts, 'player')
res2['team'] = findInStats(texts, 'team')
res2['goals'] = findInStats(texts, 'goals')
res2['shots'] = findInStats(texts, 'shots')
res2['shots_on_target'] = findInStats(texts, 'shots_on_target')
res2['shots_on_target_pct'] = findInStats(texts, 'shots_on_target_pct')
res2['shots_per90'] = findInStats(texts, 'shots_per90')
res2['shots_on_target_per90'] = findInStats(texts, 'shots_on_target_per90')
res2['goals_per_shot'] = findInStats(texts, 'goals_per_shot')
res2['shots'] = findInStats(texts, 'shots')
res2['average_shot_distance'] = findInStats(texts, 'average_shot_distance')
res2['shots_free_kicks'] = findInStats(texts, 'shots_free_kicks')
res2['pens_made'] = findInStats(texts, 'pens_made')
res2['pens_att'] = findInStats(texts, 'pens_att')
res2['xg'] = findInStats(texts, 'xg')
res2['npxg'] = findInStats(texts, 'npxg')
res2['npxg_per_shot'] = findInStats(texts, 'npxg_per_shot')     # cần xem lại------
res2['xg_net'] = findInStats(texts, 'xg_net')
res2['npxg_net'] = findInStats(texts, 'npxg_net')
#17


# stat passing
res3 = {}
soupPassing = openDriver(passingUrl)
texts = soupPassing.find('table', attrs={'id':'stats_passing'})
res3['player'] = findInStats(texts, 'player')
res3['team'] = findInStats(texts, 'team')
res3['passes_completed'] = findInStats(texts, 'passes_completed')
res3['passes'] = findInStats(texts, 'passes')
res3['passes_pct'] = findInStats(texts, 'passes_pct')
res3['passes_total_distance'] = findInStats(texts, 'passes_total_distance')
res3['passes_progressive_distance'] = findInStats(texts, 'passes_progressive_distance')
res3['passes_completed_short'] = findInStats(texts, 'passes_completed_short')
res3['passes_short'] = findInStats(texts, 'passes_short')
res3['passes_pct_short'] = findInStats(texts, 'passes_pct_short')
res3['passes_completed_medium'] = findInStats(texts, 'passes_completed_medium')
res3['passes_medium'] = findInStats(texts, 'passes_medium')
res3['passes_pct_medium'] = findInStats(texts, 'passes_pct_medium')
res3['passes_completed_long'] = findInStats(texts, 'passes_completed_long')
res3['passes_long'] = findInStats(texts, 'passes_long')
res3['passes_pct_long'] = findInStats(texts, 'passes_pct_long')
res3['assists'] = findInStats(texts, 'assists')
res3['xg_assist'] = findInStats(texts, 'xg_assist')
res3['pass_xa'] = findInStats(texts, 'pass_xa')
res3['xg_assist_net'] = findInStats(texts, 'xg_assist_net')
res3['assisted_shots'] = findInStats(texts, 'assisted_shots')
res3['passes_into_final_third'] = findInStats(texts, 'passes_into_final_third')
res3['passes_into_penalty_area'] = findInStats(texts, 'passes_into_penalty_area')
res3['crosses_into_penalty_area'] = findInStats(texts, 'crosses_into_penalty_area')
res3['progressive_passes'] = findInStats(texts, 'progressive_passes')
#23

# stat typePass
res4 = {}
soupPassTypes = openDriver(passTypeUrl)
texts = soupPassTypes.find('table', attrs={'id':'stats_passing_types'})
res4['player'] = findInStats(texts, 'player')
res4['team'] = findInStats(texts, 'team')
res4['passes_live'] = findInStats(texts, 'passes_live')
res4['passes_dead'] = findInStats(texts, 'passes_dead')
res4['passes_free_kicks'] = findInStats(texts, 'passes_free_kicks')
res4['through_balls'] = findInStats(texts, 'through_balls')
res4['passes_switches'] = findInStats(texts, 'passes_switches')
res4['crosses'] = findInStats(texts, 'crosses')
res4['throw_ins'] = findInStats(texts, 'throw_ins')
res4['corner_kicks'] = findInStats(texts, 'corner_kicks')
res4['corner_kicks_in'] = findInStats(texts, 'corner_kicks_in')
res4['corner_kicks_out'] = findInStats(texts, 'corner_kicks_out')
res4['corner_kicks_straight'] = findInStats(texts, 'corner_kicks_straight')
res4['passes_completed'] = findInStats(texts, 'passes_completed')
res4['passes_offsides'] = findInStats(texts, 'passes_offsides')
res4['passes_blocked'] = findInStats(texts, 'passes_blocked')
#14


# Stat goal and shot
res5 = {}
soupGCA = openDriver(goalAndShotCreationUrl)
texts = soupGCA.find('table', attrs={'id':'stats_gca'})
res5['player'] = findInStats(texts, 'player')
res5['team'] = findInStats(texts, 'team')
res5['sca'] = findInStats(texts, 'sca')
res5['sca_per90'] = findInStats(texts, 'sca_per90')
res5['sca_passes_live'] = findInStats(texts, 'sca_passes_live')
res5['sca_passes_dead'] = findInStats(texts, 'sca_passes_dead')
res5['sca_take_ons'] = findInStats(texts, 'sca_take_ons')
res5['sca_shots'] = findInStats(texts, 'sca_shots')
res5['sca_fouled'] = findInStats(texts, 'sca_fouled')
res5['sca_defense'] = findInStats(texts, 'sca_defense')
res5['gca'] = findInStats(texts, 'gca')
res5['gca_per90'] = findInStats(texts, 'gca_per90')
res5['gca_passes_live'] = findInStats(texts, 'gca_passes_live')
res5['gca_passes_dead'] = findInStats(texts, 'gca_passes_dead')
res5['gca_take_ons'] = findInStats(texts, 'gca_take_ons')
res5['gca_shots'] = findInStats(texts, 'gca_shots')
res5['gca_fouled'] = findInStats(texts, 'gca_fouled')
res5['gca_defense'] = findInStats(texts, 'gca_defense')
#16


# stat Defensive Actions
res6 = {}
soupDefensive = openDriver(defensiveUrl)
texts = soupDefensive.find('table', attrs={'id':'stats_defense'})
res6['player'] = findInStats(texts, 'player')
res6['team'] = findInStats(texts, 'team')
res6['tackles'] = findInStats(texts, 'tackles')
res6['tackles_won'] = findInStats(texts, 'tackles_won')
res6['tackles_def_3rd'] = findInStats(texts, 'tackles_def_3rd')
res6['tackles_mid_3rd'] = findInStats(texts, 'tackles_mid_3rd')
res6['tackles_att_3rd'] = findInStats(texts, 'tackles_att_3rd')
res6['challenge_tackles'] = findInStats(texts, 'challenge_tackles')
res6['challenges'] = findInStats(texts, 'challenges')
res6['challenge_tackles_pct'] = findInStats(texts, 'challenge_tackles_pct')
res6['challenges_lost'] = findInStats(texts, 'challenges_lost')
res6['blocks'] = findInStats(texts, 'blocks')
res6['blocked_shots'] = findInStats(texts, 'blocked_shots')
res6['blocked_passes'] = findInStats(texts, 'blocked_passes')
res6['interceptions'] = findInStats(texts, 'interceptions')
res6['tackles_interceptions'] = findInStats(texts, 'tackles_interceptions')
res6['clearances'] = findInStats(texts, 'clearances')
res6['errors'] = findInStats(texts, 'errors')
#16

# Possession 
res7 = {}
soupPossession = openDriver(possessionUrl)
texts = soupPossession.find('table', attrs={'id':'stats_possession'})
res7['player'] = findInStats(texts, 'player')
res7['team'] = findInStats(texts, 'team')
res7['touches'] = findInStats(texts, 'touches')
res7['touches_def_pen_area'] = findInStats(texts, 'touches_def_pen_area')
res7['touches_def_3rd'] = findInStats(texts, 'touches_def_3rd')
res7['touches_mid_3rd'] = findInStats(texts, 'touches_mid_3rd')
res7['touches_att_3rd'] = findInStats(texts, 'touches_att_3rd')
res7['touches_att_pen_area'] = findInStats(texts, 'touches_att_pen_area')
res7['touches_live_ball'] = findInStats(texts, 'touches_live_ball')
res7['take_ons'] = findInStats(texts, 'take_ons')
res7['take_ons_won'] = findInStats(texts, 'take_ons_won')
res7['take_ons_won_pct'] = findInStats(texts, 'take_ons_won_pct')
res7['take_ons_tackled'] = findInStats(texts, 'take_ons_tackled')
res7['take_ons_tackled_pct'] = findInStats(texts, 'take_ons_tackled_pct')
res7['carries'] = findInStats(texts, 'carries')
res7['carries_distance'] = findInStats(texts, 'carries_distance')
res7['carries_progressive_distance'] = findInStats(texts, 'carries_progressive_distance')
res7['progressive_carries'] = findInStats(texts, 'progressive_carries')
res7['carries_into_final_third'] = findInStats(texts, 'carries_into_final_third')
res7['carries_into_penalty_area'] = findInStats(texts, 'carries_into_penalty_area')
res7['miscontrols'] = findInStats(texts, 'miscontrols')
res7['dispossessed'] = findInStats(texts, 'dispossessed')
res7['passes_received'] = findInStats(texts, 'passes_received')
res7['progressive_passes_received'] = findInStats(texts, 'progressive_passes_received')
#22

# Playing Time Data Extraction
res8 = {}
soupPlayingTime = openDriver(playingTimeUrl)
texts = soupPlayingTime.find('table', attrs={'id':'stats_playing_time'})
res8['player'] = findInStats(texts, 'player')
res8['team'] = findInStats(texts, 'team')
res8['games_starts'] = findInStats(texts, 'games_starts')
res8['minutes_per_start'] = findInStats(texts, 'minutes_per_start')
res8['games_complete'] = findInStats(texts, 'games_complete')
res8['games_subs'] = findInStats(texts, 'games_subs')
res8['minutes_per_sub'] = findInStats(texts, 'minutes_per_sub')
res8['unused_subs'] = findInStats(texts, 'unused_subs')
res8['points_per_game'] = findInStats(texts, 'points_per_game')
res8['on_goals_for'] = findInStats(texts, 'on_goals_for')
res8['on_goals_against'] = findInStats(texts, 'on_goals_against')
res8['on_xg_for'] = findInStats(texts, 'on_xg_for')
res8['on_xg_against'] = findInStats(texts, 'on_xg_against')
#11
# Miscellaneous Stats Data Extraction
res9 = {}
soupMiscStats = openDriver(miscellaneousUrl)
texts = soupMiscStats.find('table', attrs={'id':'stats_misc'})
res9['player'] = findInStats(texts, 'player')
res9['team'] = findInStats(texts, 'team')
res9['fouls'] = findInStats(texts, 'fouls')
res9['fouled'] = findInStats(texts, 'fouled')
res9['offsides'] = findInStats(texts, 'offsides')
res9['crosses'] = findInStats(texts, 'crosses')
res9['own_goals'] = findInStats(texts, 'own_goals')
res9['ball_recoveries'] = findInStats(texts, 'ball_recoveries')
res9['aerials_won'] = findInStats(texts, 'aerials_won')
res9['aerials_lost'] = findInStats(texts, 'aerials_lost')
res9['aerials_won_pct'] = findInStats(texts, 'aerials_won_pct')



    


# gộp các res 
df_stats = pd.DataFrame(res)
df_goalKeeper = pd.DataFrame(res1)
df_shooting = pd.DataFrame(res2)
df_passing = pd.DataFrame(res3)
df_typePass = pd.DataFrame(res4)
df_goalAndShot = pd.DataFrame(res5)
df_defensive = pd.DataFrame(res6)
df_possession = pd.DataFrame(res7)
df_playingTime = pd.DataFrame(res8)
df_miscellaneous = pd.DataFrame(res9)

df_result = df_stats.merge(df_goalKeeper, on = ['player','team'], how='outer')
df_result =df_result.merge(df_shooting, on=['player','team'], how = 'outer')
df_result =df_result.merge(df_passing, on=['player','team'], how = 'outer')
df_result = df_result.merge( df_typePass, on=['player','team'], how = 'outer')
df_result = df_result.merge( df_goalAndShot, on=['player','team'], how = 'outer')
df_result = df_result.merge( df_defensive, on=['player','team'], how = 'outer')
df_result = df_result.merge( df_possession, on=['player','team'], how = 'outer')
df_result = df_result.merge(df_playingTime, on=['player','team'], how = 'outer')
df_result = df_result.merge( df_miscellaneous, on=['player','team'], how = 'outer')

# lọc ra các cầu thủ có số phút thi đấu lớn hơn hoặc bằng 90
df_result['minutes'] = df_result['minutes'].str.replace(',','')
df_result['minutes'] = pd.to_numeric(df_result['minutes'], errors='coerce')
df_result = df_result[df_result['minutes'] >= 90]

# nếu ô nào trống thì điền n/a
df_result.fillna('n/a', inplace=True)
df_result.replace('', 'n/a', inplace=True)

# Sắp xếp theo 'firstname' và sau đó theo 'age' giảm dần
df_result = df_result.sort_values(by=['player', 'age'], ascending=[True, False])

# Thêm cột STT tăng dần, bắt đầu từ 1
df_result.insert(0, 'STT', range(1, len(df_result) + 1))

df_result.to_csv('C:/Users/84976/Desktop/BTL_PTIT/PYTHON/btl/results.csv', index=False)







