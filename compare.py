import sqlite3
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Comparisions',layout='wide')






st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)


db= sqlite3.connect("tennis.sqlite")
cur = db.cursor()


    
# creating dropbox for players
player_df = pd.read_sql_query("select DISTINCT winner_name from kagglematches ",db)
players=[]
for i in player_df['winner_name']:
    players.append(i)

players.insert(0,"⠀⠀⠀")


with st.container():
    left_column,middle_column,right_columns = st.columns(3)
    with left_column:
        option1 = st.selectbox(
        'Select player 1',
        (players),key=2)
    with middle_column:
        st.subheader("")
        st.subheader("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀V/S")
    with right_columns:
        option2 = st.selectbox(
        'Select player 2',
        (players),key=1)



href = 'http://localhost:8501/?select_box=%E2%A0%80%E2%A0%80%E2%A0%80'
target = '_self'
button_html = '<a href="{}" target="{}"><button>{}</button></a>'.format(href, target, "Clear the selections")
st.markdown(button_html, unsafe_allow_html=True)


if(option1!="⠀⠀⠀" and option2!="⠀⠀⠀"):

##############******************####################******************###############
#total titles

    df = pd.read_sql_query(f"select * from kagglematches where winner_name = '{option1}' and round='F'", db)
    total_titles1=len(df['tourney_name'])

    df = pd.read_sql_query(f"select * from kagglematches where winner_name = '{option2}' and round='F'", db)
    total_titles2=len(df['tourney_name'])

    # total wins
    df = pd.read_sql_query(f"select * from kagglematches where winner_name = '{option1}' and round='F'", db)
    sqlite_select_query = f"select count(winner_name) from kagglematches where winner_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        total_wins1=i

    df = pd.read_sql_query(f"select * from kagglematches where winner_name = '{option2}' and round='F'", db)
    sqlite_select_query = f"select count(winner_name) from kagglematches where winner_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        total_wins2=i

    # total losses
    sqlite_select_query = f"select count(loser_name) from kagglematches where loser_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        total_loss1=i

    sqlite_select_query = f"select count(loser_name) from kagglematches where loser_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        total_loss2=i

    # win percent
    win_percent1 = (total_wins1/(total_wins1+total_loss1))*100
    win_percent2 = (total_wins2/(total_wins2+total_loss2))*100

    #HARD COURT
     #wins
    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Hard' and winner_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        hard_wins1=i

    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Hard' and winner_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        hard_wins2=i

     #losses
    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Hard' and loser_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        hard_losses1=i

    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Hard' and loser_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        hard_losses2=i


    #GRASS COURT
     #wins
    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Grass' and winner_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        grass_wins1=i

    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Grass' and winner_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        grass_wins2=i


     #losses
    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Grass' and loser_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        grass_losses1=i

    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Grass' and loser_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        grass_losses2=i



    #CLAY COURT
     #wins
    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Clay' and winner_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        clay_wins1=i

    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Clay' and winner_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        clay_wins2=i

     #losses
    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Clay' and loser_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        clay_losses1=i

    sqlite_select_query = f"select count(winner_name) from kagglematches where surface='Clay' and loser_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        clay_losses2=i



    ######################********************#######################*********************





    ## HEAD - 2 - HEAD


    sqlite_select_query = f"select COUNT('{option1}') from kagglematches where winner_name='{option1}' and loser_name='{option2}' "
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        w1=i

    sqlite_select_query = f"select COUNT('{option2}') from kagglematches where winner_name='{option2}' and loser_name='{option1}' "
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        w2=i


    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt

    import streamlit as st
    import numpy as np
    import matplotlib.pyplot as plt

    # Generate some sample data
    players = [option1, option2]
    matches_won = [w1, w2]

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(players, matches_won, color=['red', 'blue'], width=0.5, edgecolor='black')

    # Add legend and title
    ax.set_title(f'No. Matches Won by {option1} and {option2}')

    # Add value inside the bars
    for i, v in enumerate(matches_won):
        ax.text(i, v/2, str(v), color='black', fontweight='bold', ha='center', va='center')









    st.write("----------")
    with st.container():
        left,middle,right=st.columns(3)
        with middle:
            st.write("")
            
            st.subheader("⠀⠀⠀⠀⠀⠀⠀⠀Head 2 Head")
            
            st.write("")
    st.write("----------")
    with st.container():
        left,middle,right=st.columns(3)
        with left:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("----------")
            st.markdown(f'<p class="big-font">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{option1}:⠀⠀{w1} times</p>', unsafe_allow_html=True)
            st.write("----------")
        with middle:
            st.pyplot(fig)
        with right:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("----------")
            st.markdown(f'<p class="big-font">{option2}:⠀⠀{w2} times</p>', unsafe_allow_html=True)
            st.write("----------")



    ###############$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^############


    # Create the data
    player_names = [f'{option1}', f'{option2}']
    surfaces = ['Hard', 'Grass', 'Clay']
    wins = [[hard_wins1, grass_wins1, clay_wins1], [hard_wins2, grass_wins2, clay_wins2]] # Hard, grass, clay wins for each player

    # Create a stacked bar chart
    fig, ax = plt.subplots()

    # Set bar width
    bar_width = 0.35

    # Create bars for each player and surface
    bottom = np.zeros(len(surfaces))
    for i, player in enumerate(player_names):
        ax.bar(surfaces, wins[i], bar_width, bottom=bottom, label=player)
        bottom += wins[i]

    # Add legend and labels
    ax.legend()
        
    ax.set_ylabel('Wins')
    ax.set_title('Number of macthes won by each player across surfaces')

    # Display the count on each stacked bar
    for i, patch in enumerate(ax.containers):
        for j, rect in enumerate(patch.patches):
            height = rect.get_height()
            if height > 0:
                ax.text(rect.get_x() + rect.get_width() / 2,
                        rect.get_y() + height / 2,
                        f'{int(height)}',
                        ha='center',
                        va='center')

    ###############$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^############







    st.write("----------")        
    with st.container():
        left,middle,right=st.columns(3)
        with middle:
            st.write("")
            
            st.subheader("⠀⠀⠀⠀⠀⠀⠀⠀Career Wins")
            st.write("")
    st.write("----------")
            

    with st.container():
        left,middle,right=st.columns(3)
        with middle:
            st.pyplot(fig)
        with left:
            labels = ['Hard Court', 'clay', 'Grass Court']
            values = [hard_wins1, clay_wins1, grass_wins1]

            # Create a pie chart
            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

            # Add title
            ax.set_title(f"{option1}'s total wins distribution across surfces")
            st.pyplot(fig)

        with right:
            labels = ['Hard Court', 'clay', 'Grass Court']
            values = [hard_wins2, clay_wins2, grass_wins2]

            # Create a pie chart
            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)

            # Add title
            ax.set_title(f"{option2}'s total wins distribution across surfces")
            st.pyplot(fig)


            ## Rankings

            ## player 1
    sqlite_select_query = f"select winner_id from kagglematches where winner_name = '{option1}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        player_id1=i
    
    final_data1 = pd.read_sql_query(f"select ranking_date, rank from atp_rankings_00s where player = {player_id1} ",db)

    final_data1['ranking_date'] = final_data1['ranking_date'].apply(str)

    for i in range(len(final_data1['ranking_date'])):
        final_data1['ranking_date'][i]=final_data1['ranking_date'][i][0:4]

    final_data1=final_data1.drop_duplicates(subset=["ranking_date"], keep='last')

    #final_data['ranking_date'] = final_data['ranking_date'].apply(int)

    final_data1=final_data1.sort_values(by=['ranking_date'])

    ## player 2
    sqlite_select_query = f"select winner_id from kagglematches where winner_name = '{option2}'"
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        player_id2=i
    
    final_data2 = pd.read_sql_query(f"select ranking_date, rank from atp_rankings_00s where player = {player_id2} ",db)

    final_data2['ranking_date'] = final_data2['ranking_date'].apply(str)

    for i in range(len(final_data2['ranking_date'])):
        final_data2['ranking_date'][i]=final_data2['ranking_date'][i][0:4]

    final_data2=final_data2.drop_duplicates(subset=["ranking_date"], keep='last')

    #final_data['ranking_date'] = final_data['ranking_date'].apply(int)

    final_data2=final_data2.sort_values(by=['ranking_date'])


        
    st.write("----------")        
    with st.container():
        left,middle,right=st.columns(3)
        with middle:
            st.write("")
            
            st.subheader("⠀⠀⠀⠀⠀⠀⠀⠀Ranking Comparison")
            st.write("")
    st.write("----------")
    with st.container():
        left,middle,right=st.columns(3)

        
        with left:
            m = final_data1.min(skipna = False)
            for i in m:
                min_rank1=i
            data = final_data1
            fig, ax = plt.subplots()
            ax.plot(data["ranking_date"], data["rank"], marker='o', color='blue')

            # Set labels and title
            ax.set_xlabel("Year")
            ax.set_ylabel("Ranking")
            ax.set_title(f"{option1}'s Ranking Over Years")
            ax.set_xticklabels(data["ranking_date"], rotation=90)

            for x, y in zip(data["ranking_date"], data["rank"]):
                ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 10),)
            st.pyplot(fig)

            
                    
        with right:
            m = final_data2.min(skipna = False)
            for i in m:
                min_rank2=i
            data = final_data2
            fig, ax = plt.subplots()
            ax.plot(data["ranking_date"], data["rank"], marker='o', color='blue')

           
            ax.set_xlabel("Year")
            ax.set_ylabel("Ranking")
            ax.set_title(f"{option2}'s Ranking Over Years")
            ax.set_xticklabels(data["ranking_date"], rotation=90)

            for x, y in zip(data["ranking_date"], data["rank"]):
                ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 10),)
            st.pyplot(fig)

        with middle:
            st.markdown(f'<p class="big-font">⠀⠀⠀⠀⠀⠀⠀⠀Best Rank Achieved</p>', unsafe_allow_html=True)
            st.write("")
            st.write("-----------")
            st.markdown(f'<p class="big-font">⠀⠀⠀⠀⠀⠀⠀⠀{option1}:⠀{min_rank1}</p>', unsafe_allow_html=True)
            st.write("-----------")
            st.markdown(f'<p class="big-font">⠀⠀⠀⠀⠀⠀⠀⠀{option2}:⠀{min_rank2}</p>', unsafe_allow_html=True)
            

###############################################################################################
    sqlite_select_query = f"select COUNT('w_ace') from kagglematches where winner_name='{option1}' "
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        a=i

    sqlite_select_query = f"select COUNT('w_ace') from kagglematches where loser_name='{option1}' "
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        b=i

    aces1=a+b



    sqlite_select_query = f"select COUNT('w_ace') from kagglematches where winner_name='{option2}' "
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        a=i

    sqlite_select_query = f"select COUNT('w_ace') from kagglematches where loser_name='{option2}' "
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for i in records[0]:
        b=i

    aces2=a+b 

    
    st.write("----------")        
    with st.container():
        left,middle,right=st.columns(3)
        with middle:
            st.write("")
            
            st.subheader("⠀⠀⠀⠀⠀⠀⠀⠀Number of Aces Hit")
            st.write("")
    st.write("----------")


    with st.container():
        left,middle,right=st.columns(3)
        with left:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("----------")
            st.markdown(f'<p class="big-font">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{option1}:⠀⠀{aces1} times</p>', unsafe_allow_html=True)
            st.write("----------")
        with middle:
            # Generate some sample data
            players = [option1, option2]
            matches_won = [aces1, aces2]

            # Create a bar chart
            fig, ax = plt.subplots()
            ax.bar(players, matches_won, color=['red', 'blue'], width=0.5, edgecolor='black')

            # Add legend and title
            ax.set_title(f'No. Aces Hit by {option1} and {option2}')

            # Add value inside the bars
            for i, v in enumerate(matches_won):
                ax.text(i, v/2, str(v), color='black', fontweight='bold', ha='center', va='center')

            st.pyplot(fig)
        with right:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("----------")
            st.markdown(f'<p class="big-font">{option2}:⠀⠀{aces2} times</p>', unsafe_allow_html=True)
            st.write("----------")


    st.write("----------")        
    with st.container():
        left,middle,right=st.columns(3)
        with middle:
            st.write("")
            
            st.subheader("⠀⠀⠀⠀⠀⠀⠀⠀Number Of Grand Slams")
            st.write("")
    st.write("----------")

    with st.container():
        left,middle,right=st.columns(3)

        with left:
            player_df = pd.read_sql_query(f"select count('winner_name') from kagglematches where round='F' and winner_name='{option1}' and  tourney_name IN ('Australian Open','Wimbledon','Roland Garros','US Open')",db)
            slam1=player_df["count('winner_name')"][0]
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("--------------")
            st.markdown(f'<p class="big-font">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{option1}:⠀⠀{slam1} </p>', unsafe_allow_html=True)
            st.write("--------------")
        with right:
            player_df = pd.read_sql_query(f"select count('winner_name') from kagglematches where round='F' and winner_name='{option2}' and  tourney_name IN ('Australian Open','Wimbledon','Roland Garros','US Open')",db)
            slam2=player_df["count('winner_name')"][0]
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("--------------")
            st.markdown(f'<p class="big-font">{option2}:⠀⠀{slam2} </p>', unsafe_allow_html=True)
            st.write("--------------")
        with middle:
            players = [option1, option2]
            matches_won = [slam1, slam2]

            # Create a bar chart
            fig, ax = plt.subplots()
            ax.bar(players, matches_won, color=['red', 'blue'], width=0.5, edgecolor='black')

            # Add legend and title
            ax.set_title(f'No. of Grand Slams Won by {option1} and {option2}')

            # Add value inside the bars
            for i, v in enumerate(matches_won):
                ax.text(i, v/2, str(v), color='black', fontweight='bold', ha='center', va='center')

            st.pyplot(fig)
            st.write("--------------")
            
